import aiarena
# changer l'import ci-dessous pour changer la version de minimax utilisée
from .minimax.limited_depth_alpha import minimax
from .evaluation_functions import connect4c, checkers2

import sys
import time

# definition d'un dictionaire qui associe à chaque jeu une fonction d'évaluation
evaluations_functions = {
    aiarena.checkers: checkers2.evaluate,
    aiarena.connect4: connect4c.evaluate
}

class MinimaxBrainSmart:

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
        for i in children:
            possibleScore.append(minimax(i, False, self.get_children, self.evaluate, self.depth, float('-inf'), float('inf'))) #à voir si True/false maximize
        bestScore=possibleScore[0]
        bestScoreIndex=0
        for i in range(len(children)):
            if possibleScore[i]>bestScore:
                bestScore=possibleScore[i]
                bestScoreIndex=i
        time.sleep(1)
        return possibleMoves[bestScoreIndex]


    def __str__(self):
        return "MiniMax_Smart"
