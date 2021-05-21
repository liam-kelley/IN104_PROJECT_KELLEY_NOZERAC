import aiarena
import math
from aiarena.checkers import cell

def evaluate(gameState): #Think about King/Queen rules (rules['Kings can fly'])
	# board = aiarena.checkers.GameState()
	# how to read game rules ?

	nbRows=8
	nbColumns=8

	nbRows=gameState.nRows				
	nbColumns=gameState.nRows


	kValue=1.95 #It's better to have two simples than a king

	kingRules=False

	if kingRules==False:
		kValue=1.95
	else:
		kValue=5

	# if 'kings can fly'==False:
	# 	kValue=1.95
	# else:
	# 	kValue=5

	v1=math.ceil(nbColumns/4)
	v2=math.floor(nbColumns/2)
	v3=math.ceil(nbRows/4)
	v4=math.floor(nbRows/2)

	wCount=0
	wKCount=0		#Utilité d'utiliser deux counts positifs au lieu d'un count relatif: pouvoir déterminer l'état du jeu
	bCount=0
	bKCount=0
	mobility=0
	mValue=0
	endmodifier=0
	advancement=0
	wThreatened=0
	bThreatened=0

#   ,----------------,    ,----------------,
# 0 |   *   *   *   *|    |   0   1   2   3|
# 1 | *   *   *   *  |    | 4   5   6   7  |
# 2 |   *   *   *   *|    |   8   9  10  11|
# 3 |                |    |12  13  14  15  |
# 4 |                |    |  16  17  18  19|
# 5 | o   o   o   o  |    |20  21  22  23  |
# 6 |   o   o   o   o|    |  24  25  26  27|
# 7 | o   o   o   o  |    |28  29  30  31  |
#   '----------------'    '----------------'
#     0 1 2 3 4 5 6 7
	
	#COUNTING

	for h in range(nbColumns):
		for v in range(nbRows):
			if (h+v)%2==1:	#if we are in a existing cell ( could we make shorter for loops? negligeable)

				currentCell=gameState.getCell(h,v)

				if currentCell.type!=aiarena.checkers.cell.NONE:
					if currentCell.isWhite==True: ########################################White Section########################################
						
						#W-COUNTING
						if currentCell.type==aiarena.checkers.cell.MAN:
							wCount+=1
							advancement+=((nbRows-v)/nbRows)**0.5			#valorise avancement sur la board --> incite a avancer les pions les plus en arriere, mais cest tres marginal
						elif currentCell.type==aiarena.checkers.cell.KING:	
							wCount+=1
							wKCount+=1

						#W-MIDDLE VALUING
						if h>=v1 and h<=v1+v2 and v>=v3 and v<= v3+v4:
							mValue+=0.5

						#W-MOBILITY and #W-THREATENED									
						if h>0 and v>0:#coin devant gauche				
							nextCell=gameState.getCell(h-1,v-1)
							if nextCell.type==aiarena.checkers.cell.NONE:
								mobility+=1

								if h-1>0 and v-1>0:#LOOKING EVEN FURTHEER for blocked mobility (does this work?) [acronyme : LEF]
									nextCell=gameState.getCell(h-2,v-2)
									if nextCell.type!=aiarena.checkers.cell.NONE:
										if nextCell.isWhite==False:
											mobility-=2		

							elif nextCell.isWhite==False: #W-THREATENED	si qqch au coin devant gauche
								wThreatened+=1
								# BUT threat only if nothing behing him in opposite corner OR wall!
								if h<nbColumns-1 and v<nbRows-1:
									nextCell=gameState.getCell(h+1,v+1)
									if nextCell.type!=aiarena.checkers.cell.NONE:
										wThreatened-=1
								else:
									wThreatened-=1

						if h<nbColumns-1 and v>0:
							nextCell=gameState.getCell(h+1,v-1)
							if nextCell.type==aiarena.checkers.cell.NONE:
								mobility+=1

								if h+1<nbColumns-1 and v-1>0:#LEF
									nextCell=gameState.getCell(h+2,v-2)
									if nextCell.type!=aiarena.checkers.cell.NONE:
										if nextCell.isWhite==False:
											mobility-=2

							elif nextCell.isWhite==False: #W-THREATENED	si qqch au coin devant droite
								wThreatened+=1
								# BUT threat only if nothing behing him in opposite corner OR wall!
								if h>0 and v<nbRows-1:
									nextCell=gameState.getCell(h-1,v+1)
									if nextCell.type!=aiarena.checkers.cell.NONE:
										wThreatened-=1
								else:
									wThreatened-=1

						if currentCell.type==aiarena.checkers.cell.KING:		#King mobility
							if h>0 and v<nbRows-1:
								nextCell=gameState.getCell(h-1,v+1)
								if nextCell.type==aiarena.checkers.cell.NONE:
									mobility+=1


							if h<nbRows-1 and v<nbRows-1:
								nextCell=gameState.getCell(h+1,v+1)
								if nextCell.type==aiarena.checkers.cell.NONE:
									mobility+=1



					
					else:########################################Black Section########################################

						#B-COUNTING
						if currentCell.type==aiarena.checkers.cell.MAN:	
							bCount+=1
							# advancement-=(nbRows-v)/(10*nbRows)    		#Not counting advancement of enemy will stop back line from opening up for an "advantageous trade" when it really isnt
						elif currentCell.type==aiarena.checkers.cell.KING:	
							bCount+=1
							bKCount+=1
							#if rules['Kings can fly']==True:	
							#	bCount+=3

						#B-MIDDLE VALUING
						if h>=v1 and h<=v1+v2 and v>=v3 and v<= v3+v4:
							mValue-=0.5

						#B-MOBILITY and B-THREATENED
						if h>0 and v<nbRows-1:			
							nextCell=gameState.getCell(h-1,v+1)
							if nextCell.type==aiarena.checkers.cell.NONE:#B-MOBILITY
								mobility-=1

								if h-1>0 and v+1<nbRows-1:#LOOKING EVEN FURTHEER
									nextCell=gameState.getCell(h-2,v+2)
									if nextCell.type!=aiarena.checkers.cell.NONE:
										if nextCell.isWhite==True:
											mobility+=2

							elif nextCell.isWhite==True: #B-THREATENED	si qqch au coin derriere gauche
								bThreatened+=1
								# BUT threat only if nothing behing him in opposite corner OR wall!
								if h<nbColumns-1 and v>0:
									nextCell=gameState.getCell(h+1,v-1)
									if nextCell.type!=aiarena.checkers.cell.NONE:
										bThreatened-=1
								else:
									bThreatened-=1

						if h<nbRows-1 and v<nbRows-1:
							nextCell=gameState.getCell(h+1,v+1)
							if nextCell.type==aiarena.checkers.cell.NONE:#B-MOBILITY
								mobility-=1

								if h+1<nbRows-1 and v+1<nbRows-1:#LOOKING EVEN FURTHEER
									nextCell=gameState.getCell(h+2,v+2)
									if nextCell.type!=aiarena.checkers.cell.NONE:
										if nextCell.isWhite==True:
											mobility+=2

							elif nextCell.isWhite==True: #B-THREATENED	si qqch au coin derriere droite
								bThreatened+=1
								# BUT threat only if nothing behing him in opposite corner OR wall!
								if h>0 and v>0:
									nextCell=gameState.getCell(h-1,v-1)
									if nextCell.type!=aiarena.checkers.cell.NONE:
										bThreatened-=1
								else:
									bThreatened-=1

						if currentCell.type==aiarena.checkers.cell.KING:		#King mobility
							if h>0 and v>0:
								nextCell=gameState.getCell(h-1,v-1)
								if nextCell.type==aiarena.checkers.cell.NONE:
									mobility-=1
							if h<nbRows-1 and v>0:
								nextCell=gameState.getCell(h+1,v-1)
								if nextCell.type==aiarena.checkers.cell.NONE:
									mobility-=1													

	# Midlle Valuing Nerf (valoriser au maximum 2 pieces au milieu)
	mValue=max(min(mValue,1),-1)

	# # OPENING STRATEGY
	# if wCount + bCount >= 23:
	# 	mValue=mValue*2

	# # ENDGAME STRATEGY
	# if wCount + bCount <= 12:
	# 	mValue=0.5
	# 	wKCount=wKCount*(1+0.1*(12-wCount + bCount))
	# 	advancement=advancement*(12-wCount + bCount)

	# if wCount + bCount <= 12:
	# 	mValue=0.5 # stop counting mValues
	# 	wKCount=wKCount*1.1 # kings are more important at the end
	# 	bKCount=bKCount*1.1	
	# 	advancement=advancement*4 # moving up pieces becomes very important at the end
	# # 	#xxx valuing trades at the end

	# Win detect
	if bCount == 0:
		endmodifier=10000

	return ((wCount+wKCount*(kValue-1)-bCount-bKCount*(kValue-1))*4	+advancement/(10*nbRows*nbRows)	+mobility	+endmodifier	+mValue*4	-wThreatened)
    