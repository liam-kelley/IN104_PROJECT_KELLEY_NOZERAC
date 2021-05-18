import aiarena
from aiarena.checkers import cell

def evaluate(gameState):
	board = aiarena.checkers.GameState()
	nbBlack=0
	nbWhite=0
	for i in range(32):
		currentCell=board.cells[i]
		if currentCell.type!=aiarena.checkers.cell.NONE:
			if currentCell.isWhite==True:
				nbWhite+=1
			else:
				nbBlack+=1
	return nbWhite-nbBlack
    