# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.human_vs_AI
import aiarena
from ..minimaxBrain import MinimaxBrain
from ..minimaxBrainLiam import MinimaxBrainLiam
from ..minimaxAlphaBetaBrain import MinimaxAlphaBetaBrain
from .randomBrain import RandomBrain
from ..minimaxBrainSmart import MinimaxBrainSmart
from ..minimaxIterDeepBrain import MinimaxIterDeepBrain
from ..minimaxBrainDeepGenetic import MinimaxBrainDeepGenetic
from ..minimaxBrainGenetic import MinimaxBrainGenetic

import time
import random

# Lancer une partie entre votre IA MinimaxBrain et un humain sur le puissance4 ou aux dames

brain1 = MinimaxBrainSmart(aiarena.connect4)
brain1.depth=2
ajustValue=2.5
#brain2 = MinimaxBrain(aiarena.connect4)
#brain2.depth=2


convergence=0
global valueSlot # Indice du tableau des valeurs
global random_pattern # Tableau des valeurs aléatoires autour d'un certain point
global final_pattern # Tableau des nouvelles valeurs

modele_pattern=[350,2000,50,50,500,200,50,200,500,225,300,500,2500,300,2500,200,2500,150,2500,150,100,50,250,9000,50,9000,50,50]
final_pattern=[350,2000,50,50,500,200,50,200,500,225,300,500,2500,300,2500,200,2500,150,2500,150,100,50,250,9000,50,9000,50,50]
random_pattern=[75,500,20,20,75,50,20,50,100,75,75,100,500,100,500,100,500,50,500,50,25,20,50,1000,20,1000,20,20]
valueSlot=0

def generatorRandom(numberRandom,ajustValue):

    coeff=random.gauss(0,ajustValue) # Trouve un coefficient aléatoire sur une gaussienne de range ajustValue
    mainValue=random_pattern[valueSlot]
    final_pattern[valueSlot]=modele_pattern[valueSlot]+mainValue*coeff # Mutation d'un coefficient
    fichier = open("data.txt", "a")
    fichier.write(str(numberRandom))
    fichier.write(": ")

    for i in final_pattern: # On note la modification dans le fichier data.txt
            fichier.write(str(i))
            fichier.write(" ; ")
    fichier.close()
    print("Random generated")
    time.sleep(1)
    return final_pattern


## On va effectuer plusieurs matchs

for i in range(140):
	final_pattern=generatorRandom(i,ajustValue)
	brain2 = MinimaxBrainGenetic(aiarena.connect4,final_pattern) # Le Brain prend en compte les nouveaux coefficients aléatoires
	brain2.depth=2
	timeLimit=500
	game = aiarena.Game(aiarena.connect4, brain1, timeLimit, brain2, timeLimit)
	game.displayLevel=1
	game.start()
	print(game.pgn) # display the game summary
	print("Game over")
	fichier = open("data.txt", "a")
	convergence+=1
	if "0-1" in game.pgn: # Si la nouvelle AI a gagné, alors l'AI est considérée comme "meilleure" (ici se situe une erreur de raisonnement)
		fichier.write("victory")
		brain1 = MinimaxBrainGenetic(aiarena.connect4,final_pattern) # elle devient la nouvelle AI (la faire devenir le nouveau modèle fausse l'algorithme génétique)
		brain1.depth=2
		ajustValue=ajustValue*0.7 # on rétrécit le range de l'aléatoire pour cibler une valeur
		modele_pattern[valueSlot]=final_pattern[valueSlot]

	elif "1-0" in game.pgn:
		fichier.write("lost")
	else:
		fichier.write("draw")

	if convergence>4: # au bout de 4 matchs, on passe à la valeur suivante en conservant la meilleure
		final_pattern[valueSlot]=modele_pattern[valueSlot]
		convergence=0
		valueSlot+=1
		ajustValue=2.5

	fichier.write("\n\n")
	fichier.close()
	time.sleep(1)