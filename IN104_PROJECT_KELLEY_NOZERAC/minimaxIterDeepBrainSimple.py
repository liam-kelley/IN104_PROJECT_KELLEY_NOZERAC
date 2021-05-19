import aiarena
# changer l'import ci-dessous pour changer la version de minimax utilisée
from .minimax.limited_time import minimax
from .evaluation_functions import connect4c, checkers2simple

import sys
import signal
import copy
import time

# definition d'un dictionaire qui associe à chaque jeu une fonction d'évaluation
evaluations_functions = {
    aiarena.checkers: checkers2simple.evaluate,
    aiarena.connect4: connect4c.evaluate
}


def handler(a,b):
    raise NameError()

class MinimaxIterDeepBrainSimple:

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
        possibleScore=[]
        availableScore=[]
        signal.signal(signal.SIGALRM, handler)
        signal.setitimer(signal.ITIMER_REAL, timeLimit-0.05, 0.0) #0.1 seconds de marge
        
        # if timeLimit>=10:
        #     self.depth=5
        # elif timeLimit>=5:
        #     self.depth=4
        # elif timeLimit>=2:
        #     self.depth=3
        # elif timeLimit>=1:
        #     self.depth=2
        
        #Initial Run Through, just in case initial depth too high
        for i in children:      
            availableScore.append(minimax(i, False, self.get_children, self.evaluate, 1, float('-inf'), float('inf')))
        possibleScore=copy.deepcopy(availableScore)

        try:
            k=0
            while True:
                print(self.depth+k)
                availableScore=[]
                for i in range(len(children)):
                    availableScore.append(minimax(children[i], False, self.get_children, self.evaluate, self.depth+k, float('-inf'), float('inf')))
                possibleScore=copy.deepcopy(availableScore)
                k+=1

            signal.setitimer(signal.ITIMER_REAL, 0.00001, 0.0)

            while True:
                c=1
        except NameError:
            bestScore=possibleScore[0]
            bestScoreIndex=0
            for i in range(len(children)):
                if possibleScore[i]>bestScore:
                    bestScore=possibleScore[i]
                    bestScoreIndex=i
            #time.sleep(0.8)
            return possibleMoves[bestScoreIndex]


    def __str__(self):
        return "MiniMax_Player"


