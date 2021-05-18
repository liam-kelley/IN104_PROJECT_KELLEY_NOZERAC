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
						scoreWhite=scoreWhite+200
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+200

				if weight[k]==3 or weight[k]==10 or weight[k]==5:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+800
						if k==3:
							scoreWhite=scoreWhite+800
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+800
						if k==3:
							scoreBlack=scoreBlack+800

				if weight[k]==7 or weight[k]==11:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+10000
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+10000


				if weight[k]==160:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+150
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+150

				if weight[k]==33 or weight[k]==130:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+300
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+300

				if weight[k]==16 or weight[k]==52 or weight[k]==56:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreBlack=scoreBlack+50
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreWhite=scoreWhite+50


				if weight[k]==65 or weight[k]==18:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreBlack=scoreBlack+250
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreWhite=scoreWhite+250


				if weight[k]==32:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+10
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+10


				if weight[k]==112 or weight[k]==176:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreBlack=scoreBlack+1000
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreWhite=scoreWhite+1000

				if weight[k]==67 or weight[k]==26 or weight[k]==37 or weight[k]==134:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreBlack=scoreBlack+1100
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreWhite=scoreWhite+1100

				if weight[k]==40 or weight[k]==20:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreBlack=scoreBlack+500
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreWhite=scoreWhite+500


				if weight[k]==6 or weight[k]==9:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+150
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+150

				if weight[k]==4 or weight[k]==8:
					if currentCell.color==aiarena.connect4.cell.WHITE:
						scoreWhite=scoreWhite+25
					elif currentCell.color==aiarena.connect4.cell.BLACK:
						scoreBlack=scoreBlack+25


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








	return random.randint(scoreWhite-scoreBlack-5,scoreWhite-scoreBlack+5)
