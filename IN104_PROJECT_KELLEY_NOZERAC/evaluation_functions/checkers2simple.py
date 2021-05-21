import aiarena
import math
import random
from aiarena.checkers import cell

def evaluate(gameState): #Think about King/Queen rules (rules['Kings can fly'])
	board = aiarena.checkers.GameState()
	nbRows=8
	nbColumns=8
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

	# ENDGAME STRATEGY
	if bCount == 0:
		endmodifier=10000

	# return ((wCount-bCount)*3+mobility)
	return wCount-bCount + endmodifier + random.gauss(0,0.5)