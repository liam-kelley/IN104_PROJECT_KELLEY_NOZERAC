# class StateNode:

#     def __init__(self, int dep):
#         self.depth = dep    # Set the exploration depth here
#         # self.get_children = gameclass.GameState.findNextStates
#         # self.evaluate = evaluations_functions[gameclass]
#         self.parent = None
#         self.value = None
#         self.visited = False

#     def get_children

#     def evaluate



import random


def minimax(state, maximize, get_children, evaluate, max_depth):
	if max_depth==0:
		return evaluate(state)
	else:
		children=get_children(state)
		score_array=[]
		for i in children:
			score_array.append(minimax(i,(maximize+1)%2, get_children, evaluate, max_depth-1))
		if score_array==[]:
			return evaluate(state)
		if maximize==1:
			return max(score_array)
		else:
			return min(score_array)



#minimax(i,(maximize+1)%2, get_children, evaluate, max_depth-1)



    

