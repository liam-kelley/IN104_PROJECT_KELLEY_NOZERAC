def minimax(state, maximize, get_children, evaluate, max_depth, alpha, beta, random_tab):
	if max_depth==0:
		return evaluate(state, random_tab)
	else:
		children=get_children(state)
		score_array=[]
		if maximize==True:
			score=float('-inf')
			for i in children:

				score_array.append(minimax(i,False, get_children, evaluate, max_depth-1, alpha, beta, random_tab))
				alpha=max(alpha, max(score_array))

				if alpha>=beta:
					break
			
			if score_array==[]:
				return evaluate(state, random_tab)

			return max(score_array)

		else:
			score=float('inf')
			for i in children:

				score_array.append(minimax(i,True, get_children, evaluate, max_depth-1, alpha, beta, random_tab))
				beta=min(beta, min(score_array))

				if beta<=alpha:
					break

			if score_array==[]:
					return evaluate(state, random_tab)

			return min(score_array)