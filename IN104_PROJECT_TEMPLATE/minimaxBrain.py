import aiarena
# changer l'import ci-dessous pour changer la version de minimax utilisée
from .minimax.limited_depth import minimax
from .evaluation_functions import connect4, checkers

# definition d'un dictionaire qui associe à chaque jeu une fonction d'évaluation
evaluations_functions = {
    aiarena.checkers: checkers.evaluate,
    aiarena.connect4: connect4.evaluate
}

class MinimaxBrain:

    def __init__(self, gameclass, gameclass_arguments={}):
        self.depth = 5  # Set the exploration depth here
        self.get_children = gameclass.GameState.findNextStates
        self.evaluate = evaluations_functions[gameclass]

    def play(self, gameState, timeLimit):
        raise NotImplementedError()

    def __str__(self):
        return "MiniMax_Player"
