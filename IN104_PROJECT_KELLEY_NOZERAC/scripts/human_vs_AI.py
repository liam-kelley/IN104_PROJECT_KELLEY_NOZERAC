# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.human_vs_AI
import aiarena
from ..minimaxBrain import MinimaxBrain
from ..minimaxAlphaBetaBrain import MinimaxAlphaBetaBrain
from ..minimaxBrainSmart import MinimaxBrainSmart

# Lancer une partie entre votre IA MinimaxBrain et un humain sur le puissance4 ou aux dames

brain1 = aiarena.ManualBrain()
brain2 = MinimaxAlphaBetaBrain(aiarena.connect4)
brain2.depth=3
timeLimit = 30
game = aiarena.Game(aiarena.connect4, brain2, timeLimit, brain1, timeLimit)
game.displayLevel=1
game.start()
print(game.pgn) # display the game summary