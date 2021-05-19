import aiarena
from aiarena.checkers import cell
import time

def evaluate(gameState):
	board = aiarena.checkers.GameState()
	nbBlack=0
	nbWhite=0
	for h in range(8):
		for v in range(8):
			if (h+v)%2==1:
				currentCell=gameState.getCell(h,v)
				if currentCell.type!=aiarena.checkers.cell.NONE:
					if currentCell.isWhite==True:
						nbWhite+=1
					else:
						nbBlack+=1

	return nbWhite-nbBlack
    