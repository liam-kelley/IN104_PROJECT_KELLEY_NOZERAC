# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.human_vs_AI
import aiarena
from ..minimaxBrain import MinimaxBrain
from ..minimaxBrainLiam import MinimaxBrainLiam
from ..minimaxAlphaBetaBrain import MinimaxAlphaBetaBrain
from .randomBrain import RandomBrain
from ..minimaxBrainSmart import MinimaxBrainSmart
from ..minimaxBrainSmart2 import MinimaxBrainSmart2
from ..minimaxIterDeepBrain import MinimaxIterDeepBrain
from ..minimaxIterDeepBrainSimple import MinimaxIterDeepBrainSimple


# Lancer une partie entre votre IA MinimaxBrain et un humain sur le puissance4 ou aux dames

brain1 = RandomBrain()
# brain1.depth=5
#brain2 = MinimaxBrain(aiarena.connect4)
#brain2.depth=2
brain2 = MinimaxIterDeepBrain(aiarena.checkers)
brain2.depth=1
timeLimit=2
game = aiarena.Game(aiarena.checkers, brain2, timeLimit, brain1, timeLimit)
game.displayLevel=1
game.start()
print(game.pgn) # display the game summary