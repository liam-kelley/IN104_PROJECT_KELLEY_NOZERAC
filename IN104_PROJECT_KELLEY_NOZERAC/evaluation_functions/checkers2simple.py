import aiarena
import math
from aiarena.checkers import cell

def evaluate(gameState): #Think about King/Queen rules (rules['Kings can fly'])
	board = aiarena.checkers.GameState()
	nbRows=8
	nbColumns=8
	nbCells=(nbRows*nbColumns)/2
	endmodifier=0

	wCount=0		#Utilité d'utiliser deux counts positifs au lieu d'un count relatif: pouvoir déterminer l'état du jeu
	bCount=0
	mobility=0
	
	#COUNTING

	for h in range(nbColumns):
		for v in range(nbRows):
			if (h+v)%2==1:	#if we are in a existing cell ( could we make shorter for loops? )

				currentCell=gameState.getCell(h,v)

				if currentCell.type!=aiarena.checkers.cell.NONE:									#Ifs redondants pour l'instant, pas grave

					if currentCell.isWhite==True and currentCell.type==aiarena.checkers.cell.MAN:
						wCount+=1#+((v/(10*nbRows))**0.5)/5				#valorise avancement sur la board, surtout arriere--> incite a avancer
					elif currentCell.isWhite==True and currentCell.type==aiarena.checkers.cell.KING:	
						wCount+=2
					elif currentCell.isWhite==False and currentCell.type==aiarena.checkers.cell.MAN:	
						bCount+=1#+(((nbRows-v)/(10*nbRows))**0.5)/5
					elif currentCell.isWhite==False and currentCell.type==aiarena.checkers.cell.KING:	
						bCount+=2
					#SI REGLE "rules['Kings can fly']==True" ALORS
					#elif currentCell.isWhite==True and currentCell.type!=aiarena.checkers.cell.KING:	
					#	wCount+=5
					#elif currentCell.isWhite==False and currentCell.type!=aiarena.checkers.cell.KING:	
					#	bCount+=5														


	#SWITCH MODE FOR OPENING, ENDGAME, BASED ON COUNT
	#
	#

	#MOBILITY

	# for h in range(nbColumns):
	# 	for v in range(nbRows):
	# 		if (h+v)%2==1:

	# 			currentCell=gameState.getCell(h,v)
	# 			nextCell=gameState.getCell(h,v)			

	# 			if currentCell.type!=aiarena.checkers.cell.NONE:
	# 				if currentCell.isWhite==True:		#This test can only work if its not NONE type

	# 					if h>0 and v>0:									#W-MOBILITY
	# 						nextCell=gameState.getCell(h-1,v-1)
	# 						if nextCell.type==aiarena.checkers.cell.NONE:
	# 							mobility+=1
	# 					if h<nbRows-1 and v>0:
	# 						nextCell=gameState.getCell(h+1,v-1)
	# 						if nextCell.type==aiarena.checkers.cell.NONE:
	# 							mobility+=1

	# 				else:
	# 					if h>0 and v<nbRows-1:							#B-MOBILITY
	# 						nextCell=gameState.getCell(h-1,v+1)
	# 						if nextCell.type==aiarena.checkers.cell.NONE:
	# 							mobility-=1
	# 					if h<nbRows-1 and v<nbRows-1:
	# 						nextCell=gameState.getCell(h+1,v+1)
	# 						if nextCell.type==aiarena.checkers.cell.NONE:
	# 							mobility-=1


	#MIDDLE VALUING

	# if wCount+bCount > 12: #No middle valuing in late game
	# 	for h in range(math.floor(nbColumns/2)):		#50% du milieu horizontal important
	# 		for v in range(math.floor(nbRows/4)+1):		#25% du milieu vertical important
	# 			if (h+v)%2==1:
	# 				currentCell=gameState.getCell(h+math.ceil(nbColumns/4),v+math.ceil(nbRows/4))	
	# 				if currentCell.type!=aiarena.checkers.cell.NONE:
	# 					if currentCell.isWhite==True:
	# 						wCount+=0.5
	# 					else:
	# 						bCount+=0.5


	#COUNTING TRADES

	# for h in range(nbColumns):
	# 	for v in range(nbRows):
	# 		if (h+v)%2==1:

	# 			currentCell=gameState.getCell(h,v)
	# 			nextCellR=gameState.getCell(h,v)
	# 			nextCellL=gameState.getCell(h,v)

	# 			if currentCell.type!=aiarena.checkers.cell.NONE:

	# 				if currentCell.isWhite==True:

	# 					if h>0 and v>0:									#W-MOBILITY
	# 						nextCellL=gameState.getCell(h-1,v-1)
	# 						if nextCellL.type==aiarena.checkers.cell.NONE:
	# 							mobility+=1
	# 					if h<nbRows-1 and v>0:
	# 						nextCellR=gameState.getCell(h+1,v-1)
	# 						if nextCellR.type==aiarena.checkers.cell.NONE:
	# 							mobility+=1

	# 				else:
	# 					if h>0 and v<nbRows-1:							#B-MOBILITY
	# 						nextCellL=gameState.getCell(h-1,v+1)
	# 						if nextCellL.type==aiarena.checkers.cell.NONE:
	# 							mobility-=1
	# 					if h<nbRows-1 and v<nbRows-1:
	# 						nextCellR=gameState.getCell(h+1,v+1)
	# 						if nextCellR.type==aiarena.checkers.cell.NONE:
	# 							mobility-=1

	# ENDGAME STRATEGY
	if bCount == 0:
		endmodifier=10000

	# return ((wCount-bCount)*3+mobility)
	return wCount-bCount + endmodifier