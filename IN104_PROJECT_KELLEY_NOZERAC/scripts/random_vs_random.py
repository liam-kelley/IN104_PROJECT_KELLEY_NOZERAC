# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.random_vs_random
import aiarena
from .randomBrain import RandomBrain

# TODO: Instantier ICI des IA de type RandomBrain
brain1 = RandomBrain()
brain2 = RandomBrain()
ai_time = 1 #the AI will only have 1 sec to play

for module in [aiarena.abalone, aiarena.chess, aiarena.checkers, aiarena.connect4]:
    # TODO: ajouter le code pour lancer une partie et afficher son déroulement
    # afficher le PGN en fin de partie
    input('press enter to continue')

    game = aiarena.Game(module, brain1, ai_time, brain2, ai_time)
    # game.displayLevel = 1   # this prints the board after each move
    game.start()
    print(game.pgn) #print the summary of the game. 