# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.human_vs_AI
import aiarena
from ..minimaxBrain import MinimaxBrain
from ..minimaxAlphaBetaBrain import MinimaxAlphaBetaBrain
from ..minimaxBrainSmart import MinimaxBrainSmart
from ..minimaxIterDeepBrain import MinimaxIterDeepBrain
from .randomBrain import RandomBrain

# Lancer une partie entre votre IA MinimaxBrain et un humain sur le puissance4 ou aux dames

brain2 = aiarena.ManualBrain()
#brain2 = MinimaxIterDeepBrain(aiarena.connect4)
brain1 = MinimaxIterDeepBrain(aiarena.connect4)
timeLimit = 5
brain1.depth=3
game = aiarena.Game(aiarena.connect4, brain1, timeLimit, brain2, 10000)


#1.3 0 2.2 0 3.0 0 4.1 4 5.1 1 6.3 2 7.3 3 8.4 4 9.6 5 10.5 6 11.5 2 12.2 5 13.1 1 14.2 4 15.2 4 16.4 5 17.5 0 18.0 1 19.6 6  0-1 *

game.displayLevel=1
game.start()
print(game.pgn) # display the game summary