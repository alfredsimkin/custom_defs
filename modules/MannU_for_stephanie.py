def make_ranks(x, y):
	'''
	takes paired x and y values and returns ranks, with correct tie handling
	'''
	import scipy.stats
	x=scipy.stats.stats.rankdata(x)
	y=scipy.stats.stats.rankdata(y)
	return x, y

def MannU(x_values, y_values):
	'''
	takes some x_values and y_values, ranks them together, and outputs which
	has a lower sum of ranks, and a P-value
	'''
	import scipy.stats
	merged_values=x_values+y_values	
	ranks, junk=make_ranks(merged_values, y_values)
	x_ranks=ranks[:len(x_values)]
	rank_sum=sum(x_ranks)
	rank_count=len(x_ranks)
	x_U=rank_sum-((rank_count*(rank_count+1))/2)
	y_U=len(x_values)*len(y_values)-x_U
	smaller_U, p=scipy.stats.mannwhitneyu(x_values, y_values)
	if x_U<y_U:
		statement='x_smaller'
	if y_U<x_U:
		statement='y_smaller'
	if y_U==x_U:
		statement='equal'
	return statement, smaller_U, p

