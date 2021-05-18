import aiarena
from aiarena.checkers import cell

def evaluate(gameState):
	board = aiarena.checkers.GameState()
	nbBlack=0
	nbWhite=0
	nbRows=8
	nbWhiteFree=0
	nbBlackFree=0
	nbCells=(nbRows**2)/2

	for i in range(int(nbCells)):
		currentCell=board.cells[i]
		if currentCell.type!=aiarena.checkers.cell.NONE:

			if currentCell.isWhite==True:
				nbWhite+=1

				if i%nbRows==nbRows/2:
					nextCellR=board.cells[int(i-nbRows/2)]

				elif i%nbRows==(nbRows/2)-1:
					nextCellL=board.cells[int(i-(nbRows/2)-1)]

				elif i>nbRows/2:
					nextCellR=board.cells[int(i-nbRows/2)]
					nextCellL=board.cells[int(i-(nbRows/2)-1)]

				if nextCellL.type==aiarena.checkers.cell.NONE:
					nbWhiteFree+=1

				if nextCellR.type==aiarena.checkers.cell.NONE:
					nbWhiteFree+=1


			else:
				nbBlack+=1

				if i%nbRows==nbRows/2:
					nextCellL=board.cells[int(i+nbRows/2)]

				elif i%nbRows==(nbRows/2)-1:
					nextCellR=board.cells[int(i+(nbRows/2)+1)]

				elif i<nbCells-nbRows/2:
					nextCellR=board.cells[int(i+nbRows/2)]
					nextCellL=board.cells[int(i+(nbRows/2)+1)]

				if nextCellL.type==aiarena.checkers.cell.NONE:
					nbBlackFree+=1

				if nextCellR.type==aiarena.checkers.cell.NONE:
					nbBlackFree+=1





	return ((nbWhite-nbBlack)+(nbWhiteFree-nbBlackFree)*2)
    