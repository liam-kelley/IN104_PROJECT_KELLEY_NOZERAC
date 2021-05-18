import aiarena
# changer l'import ci-dessous pour changer la version de minimax utilisée
from .minimax.limited_time import minimax
from .evaluation_functions import connect4c, checkers

import sys
import signal
import time

# definition d'un dictionaire qui associe à chaque jeu une fonction d'évaluation
evaluations_functions = {
    aiarena.checkers: checkers.evaluate,
    aiarena.connect4: connect4c.evaluate
}


def handler(a,b):
    raise NameError()

class MinimaxIterDeepBrain:

    def __init__(self, gameclass, gameclass_arguments={}):
        self.depth = 1      # Set the exploration depth here
        self.get_children = gameclass.GameState.findNextStates
        self.evaluate = evaluations_functions[gameclass]
        print("Please enter AI name")
        self.name = sys.stdin.readline()[0:-1]
        self.alwaysSeeAsWhite = True


    def play(self, gameState, timeLimit):
        possibleMoves=gameState.findPossibleMoves()
        children=self.get_children(gameState)
        possibleScore=[0,0,0,0,0,0,0]
        availableScore=[]
        signal.signal(signal.SIGALRM, handler)
        signal.setitimer(signal.ITIMER_REAL, timeLimit-0.1, 0.0)
        if timeLimit>=10:
            self.depth=5
        elif timeLimit>=5:
            self.depth=4
        elif timeLimit>=2:
            self.depth=3
        elif timeLimit>=1:
            self.depth=2
        print(self.depth)
        for i in children:
            availableScore.append(minimax(i, False, self.get_children, self.evaluate, 1, float('-inf'), float('inf')))

        for j in range(len(children)):
            possibleScore[j]=availableScore[j] #à voir si True/f
        try:
            k=0
            while True:
                for i in range(len(children)):
                    availableScore[i]=minimax(children[i], False, self.get_children, self.evaluate, self.depth+k, float('-inf'), float('inf'))
                for j in range(len(children)):
                    possibleScore[j]=availableScore[j]
                k+=1  #à voir si True/false maximize
            
            signal.setitimer(signal.ITIMER_REAL, 0.00001, 0.0)
            # bestScore=possibleScore[0]
            # bestScoreIndex=0
            # for i in range(len(children)):
            #     if possibleScore[i]>bestScore:
            #         bestScore=possibleScore[i]
            #         bestScoreIndex=i
            # #time.sleep(0.1)
            # return possibleMoves[bestScoreIndex]
            while True:
                c=1
        except NameError:
            bestScore=possibleScore[0]
            bestScoreIndex=0
            for i in range(len(children)):
                if possibleScore[i]>bestScore:
                    bestScore=possibleScore[i]
                    bestScoreIndex=i
            #time.sleep(0.1)
            return possibleMoves[bestScoreIndex]


    def __str__(self):
        return "MiniMax_Player"


