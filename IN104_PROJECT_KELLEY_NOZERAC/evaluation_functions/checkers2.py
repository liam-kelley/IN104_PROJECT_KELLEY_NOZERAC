import aiarena
import math
from aiarena.checkers import cell

def evaluate(gameState): #Think about King/Queen rules (rules['Kings can fly'])
	board = aiarena.checkers.GameState()
	nbRows=8
	nbColumns=8

	v1=math.ceil(nbColumns/4)
	v2=math.floor(nbColumns/2)
	v3=math.ceil(nbRows/4)
	v4=math.floor(nbRows/2)

	wCount=0		#Utilité d'utiliser deux counts positifs au lieu d'un count relatif: pouvoir déterminer l'état du jeu
	bCount=0
	mobility=0
	endmodifier=0
	advancement=0
	
	#COUNTING

	for h in range(nbColumns):
		for v in range(nbRows):
			if (h+v)%2==1:	#if we are in a existing cell ( could we make shorter for loops? negligeable)

				currentCell=gameState.getCell(h,v)

				if currentCell.type!=aiarena.checkers.cell.NONE:
					if currentCell.isWhite==True:
						
						#W-COUNTING
						if currentCell.type==aiarena.checkers.cell.MAN:
							wCount+=1
							advancement+=v/(10*nbRows)			#valorise avancement sur la board --> incite a avancer les pions
						elif currentCell.type==aiarena.checkers.cell.KING:	
							wCount+=1.95									#It's better to have two simples than a king
							#if rules['Kings can fly']==True:	
							#	wCount+=3

						#W-MIDDLE VALUING
						if h>=v1 and h<=v1+v2 and v>=v3 and v<= v3+v4:
							wCount+=0.5

						#W-MOBILITY											
						if h>0 and v>0:										#it seems important to take into account blocked mobility
							nextCell=gameState.getCell(h-1,v-1)
							if nextCell.type==aiarena.checkers.cell.NONE:
								mobility+=1

								if h-1>0 and v-1>0:#LOOKING EVEN FURTHEER
									nextCell=gameState.getCell(h-2,v-2)
									if nextCell.type!=aiarena.checkers.cell.NONE:
										if nextCell.isWhite==False:
											mobility-=0.5

						if h<nbRows-1 and v>0:
							nextCell=gameState.getCell(h+1,v-1)
							if nextCell.type==aiarena.checkers.cell.NONE:
								mobility+=1

								if h+1<nbRows-1 and v-1>0:#LOOKING EVEN FURTHEER
									nextCell=gameState.getCell(h+2,v-2)
									if nextCell.type!=aiarena.checkers.cell.NONE:
										if nextCell.isWhite==False:
											mobility-=0.5

						if currentCell.type==aiarena.checkers.cell.KING:		#King mobility
							if h>0 and v<nbRows-1:
								nextCell=gameState.getCell(h-1,v+1)
								if nextCell.type==aiarena.checkers.cell.NONE:
									mobility+=1


							if h<nbRows-1 and v<nbRows-1:
								nextCell=gameState.getCell(h+1,v+1)
								if nextCell.type==aiarena.checkers.cell.NONE:
									mobility+=1
					
					else:

						#B-COUNTING
						if currentCell.type==aiarena.checkers.cell.MAN:	
							bCount+=1
							advancement-=(nbRows-v)/(10*nbRows)
						elif currentCell.type==aiarena.checkers.cell.KING:	
							bCount+=1.95
							#if rules['Kings can fly']==True:	
							#	bCount+=3

						#B-MIDDLE VALUING
						if h>=v1 and h<=v1+v2 and v>=v3 and v<= v3+v4:
							bCount+=0.5

						#B-MOBILITY
						if h>0 and v<nbRows-1:			
							nextCell=gameState.getCell(h-1,v+1)
							if nextCell.type==aiarena.checkers.cell.NONE:
								mobility-=1

								if h-1>0 and v+1<nbRows-1:#LOOKING EVEN FURTHEER
									nextCell=gameState.getCell(h-2,v+2)
									if nextCell.type!=aiarena.checkers.cell.NONE:
										if nextCell.isWhite==True:
											mobility+=0.5

						if h<nbRows-1 and v<nbRows-1:
							nextCell=gameState.getCell(h+1,v+1)
							if nextCell.type==aiarena.checkers.cell.NONE:
								mobility-=1

								if h+1<nbRows-1 and v+1<nbRows-1:#LOOKING EVEN FURTHEER
									nextCell=gameState.getCell(h+2,v+2)
									if nextCell.type!=aiarena.checkers.cell.NONE:
										if nextCell.isWhite==True:
											mobility+=0.5

						if currentCell.type==aiarena.checkers.cell.KING:		#King mobility
							if h>0 and v>0:
								nextCell=gameState.getCell(h-1,v-1)
								if nextCell.type==aiarena.checkers.cell.NONE:
									mobility-=1
							if h<nbRows-1 and v>0:
								nextCell=gameState.getCell(h+1,v-1)
								if nextCell.type==aiarena.checkers.cell.NONE:
									mobility-=1													
	
	# ENDGAME STRATEGY
	if bCount == 0:
		endmodifier=10000


	#Opening strategy was "perfect" at some point

	return ((wCount-bCount)*3+advancement+mobility+endmodifier)
    