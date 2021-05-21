import aiarena
import math
from aiarena.checkers import cell

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


def evaluate(gameState): #Think about King/Queen rules (rules['Kings can fly'])
	# board = aiarena.checkers.GameState()
	# how to read game rules ?
	nbRows=8				
	nbColumns=8
	kValue=1.95 
	# if 'kings can fly'==False:
	# 	kValue=2
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

	# INITIALISE BOARDS
	cBoard=[]
	tBoard=[]

	for h in range(nbColumns):
		cL=[]
		tL=[]
		for v in range(nbRows):
			if (h+v)%2==1:	#if we are in a existing cell ( could we make shorter for loops? negligeable)
				currentCell=gameState.getCell(h,v)
				if currentCell.type!=aiarena.checkers.cell.NONE:
					if currentCell.isWhite==True:
						cL.append(1) 	#ColorBoard==1 = white
					else:				#ColorBoard==0 = empty
						cL.append(-1) 	#ColorBoard==-1 = black
					if currentCell.type==aiarena.checkers.cell.MAN:
						tL.append(1)	#TypeBoard==1 = man
					else:				#TypeBoard==0 = empty
						tL.append(2)	#TypeBoard==2 = king
				else:
					cL.append(0)
					tL.append(0)
			else:
				cL.append(0)
				tL.append(0)
		cBoard.append(cL)
		tBoard.append(tL)

	# EVALUATE
	for h in range(nbColumns):
		for v in range(nbRows):
			if (h+v)%2==1:	#if we are in a existing cell ( could we make shorter for loops? negligeable)
				if tBoard[h][v]!=0:
					if tBoard[h][v]==1: ########################################White Section########################################
						
						#W-COUNTING
						if tBoard[h][v]==1:
							wCount+=1
							advancement+=(((nbRows-v)/nbRows)**0.5)/(10*nbRows*nbRows)			#valorise avancement sur la board --> incite a avancer les pions les plus en arriere, mais cest tres marginal, vraiment pour prioritiser a choix egals
						elif tBoard[h][v]==2:	
							wCount+=1
							wKCount+=1									#It's better to have two simples than a king

						#W-MIDDLE VALUING
						if h>=v1 and h<=v1+v2 and v>=v3 and v<= v3+v4:
							mValue+=0.4

						#W-MOBILITY and #W-THREATENED									
						if h>0 and v>0:#coin devant gauche				
							# nextCell=gameState.getCell(h-1,v-1)
							if tBoard[h-1][v-1]==0:
								mobility+=1

								if h-1>0 and v-1>0:#LOOKING EVEN FURTHEER for blocked mobility (does this work?) [acronyme : LEF]
									# nextCell=gameState.getCell(h-2,v-2)
									if tBoard[h-2][v-2]!=0:
										if cBoard[h-2][v-2]==-1:
											mobility-=0.5

							elif cBoard[h-1][v-1]==-1: #W-THREATENED	si qqch au coin devant gauche
								wThreatened+=1
								# BUT threat only if nothing behing him in opposite corner OR wall!
								if h<nbColumns-1 and v<nbRows-1:
									# nextCell=gameState.getCell(h+1,v+1)
									if tBoard[h+1][v+1]!=0:
										wThreatened-=1
								else:
									wThreatened-=1

						if h<nbColumns-1 and v>0:
							# nextCell=gameState.getCell(h+1,v-1)
							if tBoard[h+1][v-1]==0:
								mobility+=1

								if h+1<nbColumns-1 and v-1>0:#LEF
									# nextCell=gameState.getCell(h+2,v-2)
									if tBoard[h+2][v-2]!=0:
										if cBoard[h+2][v-2]==-1:
											mobility-=0.5

							elif cBoard[h+1][v-1]==-1: #W-THREATENED	si qqch au coin devant droite
								wThreatened+=1
								# BUT threat only if nothing behing him in opposite corner OR wall!
								if h>0 and v<nbRows-1:
									# nextCell=gameState.getCell(h-1,v+1)
									if tBoard[h-1][v+1]!=0:
										wThreatened-=1
								else:
									wThreatened-=1

						if tBoard[h][v]==2:		#King mobility
							if h>0 and v<nbRows-1:
								# nextCell=gameState.getCell(h-1,v+1)
								if tBoard[h-1][v+1]==0:
									mobility+=1
									# Not looking further here

							if h<nbRows-1 and v<nbRows-1:
								# nextCell=gameState.getCell(h+1,v+1)
								if tBoard[h+1][v+1]==0:
									mobility+=1
									# Not looking further here


					
					else:########################################Black Section########################################

						#B-COUNTING
						if tBoard[h][v]==1:	
							bCount+=1
							# advancement-=(nbRows-v)/(100*nbRows)    		#Not counting advancement of enemy will stop back line from opening up for an "advantageous trade" when it really isnt
						elif tBoard[h][v]==2:	
							bCount+=1
							bKCount+=1

						#B-MIDDLE VALUING
						if h>=v1 and h<=v1+v2 and v>=v3 and v<= v3+v4:
							mValue-=0.4

						#B-MOBILITY and B-THREATENED
						if h>0 and v<nbRows-1:			
							# nextCell=gameState.getCell(h-1,v+1)
							if tBoard[h-1][v+1]==0:#B-MOBILITY
								mobility-=1

								if h-1>0 and v+1<nbRows-1:#LOOKING EVEN FURTHER
									# nextCell=gameState.getCell(h-2,v+2)
									if tBoard[h-2][v+2]!=0:
										if cBoard[h-2][v+2]==1:
											mobility+=0.7		#stopping enemy mobility is valued higher!

							elif tBoard[h-1][v+1]==1: #B-THREATENED	si qqch au coin derriere gauche
								bThreatened+=1
								# BUT threat only if nothing behing him in opposite corner OR wall!
								if h<nbColumns-1 and v>0:
									# nextCell=gameState.getCell(h+1,v-1)
									if tBoard[h+1][v-1]!=0:
										bThreatened-=1
								else:
									bThreatened-=1

						if h<nbRows-1 and v<nbRows-1:
							# nextCell=gameState.getCell(h+1,v+1)
							if tBoard[h+1][v+1]==0:#B-MOBILITY
								mobility-=1

								if h+1<nbRows-1 and v+1<nbRows-1:#LER
									# nextCell=gameState.getCell(h+2,v+2)
									if tBoard[h+2][v+2]!=0:
										if cBoard[h+2][v+2]==1:
											mobility+=0.7

							elif cBoard[h+1][v+1]==1: #B-THREATENED	si qqch au coin derriere droite
								bThreatened+=1
								# BUT threat only if nothing behing him in opposite corner OR wall!
								if h>0 and v>0:
									# nextCell=gameState.getCell(h-1,v-1)
									if tBoard[h-1][v-1]!=0:
										bThreatened-=1
								else:
									bThreatened-=1

						if tBoard[h][v]==2:		#King mobility
							if h>0 and v>0:
								# nextCell=gameState.getCell(h-1,v-1)
								if tBoard[h-1][v-1]==0:
									mobility-=1

							if h<nbRows-1 and v>0:
								# nextCell=gameState.getCell(h+1,v-1)
								if tBoard[h+1][v-1]==0:
									mobility-=1													
	
	# Midlle Valuing Nerf (valoriser au maximum 2 pieces au milieu)
	mValue=max(min(mValue,1),-1)

	# ENDGAME STRATEGY
	if wCount + bCount < 12:
		mValue=0.4 # stop counting mValues
		#xxx valuing trades at the end

	# Win detect
	if bCount == 0:
		endmodifier=10000

	return     ((wCount+wKCount*(kValue-1)-bCount-bKCount*(kValue-1))*4+advancement+mobility+endmodifier+mValue*3+(bThreatened-wThreatened)    )