# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.human_vs_AI
import aiarena
from ..minimaxBrain import MinimaxBrain
from ..minimaxAlphaBetaBrain import MinimaxAlphaBetaBrain
from ..minimaxBrainSmart import MinimaxBrainSmart
from ..minimaxIterDeepBrain import MinimaxIterDeepBrain
from .randomBrain import RandomBrain

# Lancer une partie entre votre IA MinimaxBrain et un humain sur le puissance4 ou aux dames

brain2 = RandomBrain()
#brain2 = MinimaxIterDeepBrain(aiarena.connect4)
brain1 = MinimaxBrainSmart(aiarena.checkers)
timeLimit = 20
brain1.depth=5
game = aiarena.Game(aiarena.checkers, brain1, timeLimit, brain2, timeLimit)
game.displayLevel=1
game.start()
print(game.pgn) # display the game summary