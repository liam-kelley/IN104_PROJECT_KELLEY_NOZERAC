import aiarena
import random
from aiarena.connect4 import cell

def evaluate(gameState):
	TotalCount=0
	for h in range(6):
		for w in range(7):
			currentCell=gameState.getCell(h,w)
			if currentCell.color == aiarena.connect4.cell.WHITE:
				for Ri in [-1,0,1]:
					for Up in [-1,0,1]:
						if Ri !=0 and Up != 0:
							posy=h+Ri
							posx=w+Up
							counter=0
							wrong = False
							while posy<6 and posy>=0 and posx<7 and posx >=0 and wrong == False:
								nextCell=gameState.getCell(h+Ri,w+Up)
								if nextCell.color == aiarena.connect4.cell.WHITE :
									counter+=1
								else:
									wrong = True
								posx+=Ri
								posy+=Up
							if counter >=3 :
								return(10000000)
							TotalCount+=10**counter
			if currentCell.color == aiarena.connect4.cell.BLACK:
				for Ri in [-1,0,1]:
					for Up in [-1,0,1]:
						if Ri !=0 and Up != 0:
							posy=h+Ri
							posx=w+Up
							counter=0
							wrong = False
							while posy<6 and posy>=0 and posx<7 and posx >=0 and wrong == False:
								nextCell=gameState.getCell(h+Ri,w+Up)
								if nextCell.color == aiarena.connect4.cell.BLACK :
									counter+=1
								else:
									wrong = True
								posx+=Ri
								posy+=Up
							if counter >=3 :
								return(-10000000)
							TotalCount-=11**counter
	return TotalCount + random.randrange(9)