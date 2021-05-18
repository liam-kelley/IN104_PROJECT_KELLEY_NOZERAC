import random
# import sys
# import subprocess as sp
# from .misc import smart_display

class RandomBrain:
    def __init__(self):
        print("Please enter AI name")
        self.name = sys.stdin.readline()[0:-1]
        self.alwaysSeeAsWhite = False

    def play(self, gameState, timeLimit):
        possibleMoves = gameState.findPossibleMoves()
        # sp.check_call('clear')
        # affichage
        # gameState.display(showBoard=True)
        # print("Authorized moves : ")
        # pdn_list = [str(m) for m in possibleMoves]
        # smart_display(pdn_list, count=True)

        rand_int=random.randint(0,len(possibleMoves))
        return possibleMoves[rand_int]



    def __str__(self):
        return "Random_Player"
