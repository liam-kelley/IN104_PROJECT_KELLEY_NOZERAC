import aiarena
from aiarena.connect4 import cell
import random

def evaluate(gameState):


	board = aiarena.connect4.GameState()
	scoreWhite=0
	scoreBlack=0
	for h in range(6):
		for w in range(7):
			currentCell=gameState.getCell(h,w)
			weight=[0,0,0,0]



			if h<5:

				if w>0: 
					nextCell=gameState.getCell(h+1,w-1)  #haut gauche
					if nextCell.color==currentCell.color:
						weight[0]=weight[0]+1
					elif nextCell.color!=aiarena.connect4.cell.NONE:
						weight[0]=weight[0]+16

				if w<6:
					nextCell=gameState.getCell(h+1,w+1) #haut droite
					if nextCell.color==currentCell.color:
						weight[2]=weight[2]+1
					elif nextCell.color!=aiarena.connect4.cell.NONE:
						weight[2]=weight[2]+16

				nextCell=gameState.getCell(h+1,w) #haut
				if nextCell.color==currentCell.color:
					weight[1]=weight[1]+1
				elif nextCell.color!=aiarena.connect4.cell.NONE:
					weight[1]=weight[1]+16


			if h>0:

				if w>0: 
					nextCell=gameState.getCell(h-1,w-1)  #bas gauche
					if nextCell.color==currentCell.color:
						weight[2]=weight[2]+2
					elif nextCell.color!=aiarena.connect4.cell.NONE:
						weight[2]=weight[2]+32

				if w<6:
					nextCell=gameState.getCell(h-1,w+1) #bas droite
					if nextCell.color==currentCell.color:
						weight[0]=weight[0]+2
					elif nextCell.color!=aiarena.connect4.cell.NONE:
						weight[0]=weight[0]+32

				nextCell=gameState.getCell(h-1,w) #bas
				if nextCell.color==currentCell.color:
					weight[1]=weight[1]+2
				elif nextCell.color!=aiarena.connect4.cell.NONE:
					weight[1]=weight[1]+32


			if w>0:
				nextCell=gameState.getCell(h,w-1)  #gauche
				if nextCell.color==currentCell.color:
					weight[3]=weight[3]+1
				elif nextCell.color!=aiarena.connect4.cell.NONE:
					weight[3]=weight[3]+16

			if w<6:
				nextCell=gameState.getCell(h,w+1)  #droite
				if nextCell.color==currentCell.color:
					weight[3]=weight[3]+2
				elif nextCell.color!=aiarena.connect4.cell.NONE:
					weight[3]=weight[3]+32



### RANG 2

			if h<4:

				if w>1: 
					nextCell=gameState.getCell(h+2,w-2)  #haut gauche
					if nextCell.color==currentCell.color:
						weight[0]=weight[0]+4
					elif nextCell.color!=aiarena.connect4.cell.NONE:
						weight[0]=weight[0]+64

				if w<5:
					nextCell=gameState.getCell(h+2,w+2) #haut droite
					if nextCell.color==currentCell.color:
						weight[2]=weight[2]+4
					elif nextCell.color!=aiarena.connect4.cell.NONE:
						weight[2]=weight[2]+64

				nextCell=gameState.getCell(h+2,w) #haut
				if nextCell.color==currentCell.color:
					weight[1]=weight[1]+4
				elif nextCell.color!=aiarena.connect4.cell.NONE:
					weight[1]=weight[1]+64


			if h>1:

				if w>1: 
					nextCell=gameState.getCell(h-2,w-2)  #bas gauche
					if nextCell.color==currentCell.color:
						weight[2]=weight[2]+8
					elif nextCell.color!=aiarena.connect4.cell.NONE:
						weight[2]=weight[2]+128

				if w<5:
					nextCell=gameState.getCell(h-2,w+2) #bas droite
					if nextCell.color==currentCell.color:
						weight[0]=weight[0]+8
					elif nextCell.color!=aiarena.connect4.cell.NONE:
						weight[0]=weight[0]+128

				nextCell=gameState.getCell(h-2,w) #bas
				if nextCell.color==currentCell.color:
					weight[1]=weight[1]+8
				elif nextCell.color!=aiarena.connect4.cell.NONE:
					weight[1]=weight[1]+128


			if w>1:
				nextCell=gameState.getCell(h,w-2)  #gauche
				if nextCell.color==currentCell.color:
					weight[3]=weight[3]+4
				elif nextCell.color!=aiarena.connect4.cell.NONE:
					weight[3]=weight[3]+64

			if w<5:
				nextCell=gameState.getCell(h,w+2)  #droite
				if nextCell.color==currentCell.color:
					weight[3]=weight[3]+8
				elif nextCell.color!=aiarena.connect4.cell.NONE:
					weight[3]=weight[3]+128



			#Convertir poids en score : AVEC UN SWITCH CASE

			for k in [3,1,0,2]:

				if weight[k]==1 or weight[k]==2:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+350
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+350

				elif weight[k]==3 or weight[k]==10 or weight[k]==5:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+2000
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+2000

				elif weight[k]==7 or weight[k]==11:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+100000
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+100000

				elif weight[k]==32:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+50
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+50

				elif weight[k]==16:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-50
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-50

				elif weight[k]==160:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+500
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+500

				elif weight[k]==33 or weight[k]==130:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+175
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+175

				elif weight[k]==48:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+50
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+50


				elif weight[k]==65 or weight[k]==18:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-200
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-200

				elif weight[k]==80:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-100
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-100

				elif weight[k]==4 or weight[k]==8:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-300
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-150

				elif weight[k]==20 or weight[k]==40:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-300
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-300

				elif weight[k]==26 or weight[k]==30 or weight[k]==90 or weight[k]==67:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-3000
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-3000

				elif weight[k]==22 or weight[k]==130 or weight[k]==150:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-2500
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-2500

				elif weight[k]==82 or weight[k]==90 or weight[k]==210:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-300
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-300

				elif weight[k]==134 or weight[k]==6:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+2500
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+2500

				elif weight[k]==66:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-200
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-200

				elif weight[k]==41:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-2500
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-2500

				elif weight[k]==56:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+150
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+150

				elif weight[k]==9 or weight[k]==13 or weight[k]==73:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+2500
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+2500

				elif weight[k]==24:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+150
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+150

				elif weight[k]==37 or weight[k]==131:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+100
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+100

				elif weight[k]==52 or weight[k]==180 or weight[k]==60:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-50
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-50

				elif weight[k]==193 or weight[k]==195 or weight[k]==321 or weight[k]==146 or weight[k]==150 or weight[k]==210:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-250
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-250

				elif weight[k]==112:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+9000
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+9000

				elif weight[k]==36 or weight[k]==164 or weight[k]==44:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+50
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+50

				elif weight[k]==176:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+9000
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+9000

				elif weight[k]==129:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+50
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+50

				elif weight[k]==64 or weight[k]==128:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite-10
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack-10


			if w==3:
				if currentCell.color==aiarena.connect4.cell.WHITE:
					scoreWhite=scoreWhite+15
					if h==0:
						scoreWhite=scoreWhite+500
				elif currentCell.color==aiarena.connect4.cell.BLACK:
					scoreBlack=scoreBlack+15
					if h==0:
						scoreBlack=scoreBlack+500
			if w==2 or w==4:
				if currentCell.color==aiarena.connect4.cell.WHITE:
					scoreWhite=scoreWhite+10
				elif currentCell.color==aiarena.connect4.cell.BLACK: 
					scoreBlack=scoreBlack+10


			if (weight==[0,16,0,2] or weight==[0, 80, 16, 2] or weight==[0, 16, 16, 2] or weight==[0, 80, 0, 2]) and h==0:
				if currentCell.color==aiarena.connect4.cell.WHITE:
					scoreWhite=scoreWhite+5000
				elif currentCell.color==aiarena.connect4.cell.BLACK: 
					scoreBlack=scoreBlack+5000

			elif ((weight[0]==0 or weight[0]==16) and (weight[1]==16 or weight[1]==80) and (weight[2]==0 or weight[2]==16) and (weight[3]==3)) and h==0:
				if currentCell.color==aiarena.connect4.cell.WHITE:
					scoreWhite=scoreWhite+8000
				elif currentCell.color==aiarena.connect4.cell.BLACK: 
					scoreBlack=scoreBlack+8000


			elif ((weight[0]==0 or weight[0]==16) and (weight[1]==16 or weight[1]==80) and (weight[2]==0) and (weight[2]==1)) and h==0:
				if currentCell.color==aiarena.connect4.cell.WHITE:
					scoreWhite=scoreWhite+5000
				elif currentCell.color==aiarena.connect4.cell.BLACK: 
					scoreBlack=scoreBlack+5000

			elif (weight==[1,32,2,16] and w<5) or (weight==[2,32,1,32] and w>1):
				if currentCell.color==aiarena.connect4.cell.WHITE:
					scoreWhite=scoreWhite+2000
				elif currentCell.color==aiarena.connect4.cell.BLACK: 
					scoreBlack=scoreBlack+2000

			elif (weight==[33,33,2,16] and w<5) or (weight==[2,33,33,32] and w>1):
				if currentCell.color==aiarena.connect4.cell.WHITE:
					scoreWhite=scoreWhite+5000
				elif currentCell.color==aiarena.connect4.cell.BLACK: 
					scoreBlack=scoreBlack+5000

			elif ((weight==[1,146,32,1] or weight==[1,146,8,1] or weight==[32,146,160,1]) and w<5) or ((weight==[32,146,1,2] or weight==[160,146,1,2] or weight==[8,146,1,2]) and w>1):
				if currentCell.color==aiarena.connect4.cell.WHITE:
					scoreWhite=scoreWhite+1000
				elif currentCell.color==aiarena.connect4.cell.BLACK: 
					scoreBlack=scoreBlack+1000

			elif ((weight==[33,146,32,3] or weight==[33,146,8,3] or weight==[33,146,160,3]) and w<5) or ((weight==[32,146,33,3] or weight==[160,146,33,3] or weight==[8,146,33,3]) and w>1):
				if currentCell.color==aiarena.connect4.cell.WHITE:
					scoreWhite=scoreWhite+10000
				elif currentCell.color==aiarena.connect4.cell.BLACK: 
					scoreBlack=scoreBlack+10000






	return scoreWhite-scoreBlack
