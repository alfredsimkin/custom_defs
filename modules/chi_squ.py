'''
A program (probably destined to become a module) to estimate chi-square values
given a list of observed values and a set of ratios. Rearranges data points to
minimize reported chi-square
'''
import space_walks2
import sys
import scipy.stats
#original_values=map(float, sys.argv[1].split(','))
#expected_ratio=map(float, sys.argv[2].split(','))

def get_chi_square(obs_values, exp_values):
	chi_square=0.0
	for obs_number, obs in enumerate(obs_values):
		exp=exp_values[obs_number]
		chi_square+=((obs-exp)**2)/exp
	return chi_square

def calculate_expected(observed_values, expected_ratios):
	expected=[]
	observed_sum=sum(observed_values)
	expected_sum=sum(expected_ratios)
	for ratio in expected_ratios:
		expected.append(float(observed_sum)/expected_sum*ratio)
	return expected

def do_it(original_values, expected_ratios):
	starting_string=range(len(original_values))
	starting_string=''.join(map(str, starting_string))
#	print starting_string
	permutations=space_walks2.main_function(starting_string)
	best_chi='a'
	for permutation in permutations:
		observed_values=[original_values[int(number)] for number in permutation]
		exp_values=calculate_expected(observed_values, expected_ratios)
		chi_square=get_chi_square(observed_values, exp_values)
#		print permutation
#		print exp_values
#		print observed_values
#		print chi_square, '\n\n'
		if chi_square<best_chi:
			best_values=observed_values
			best_chi=chi_square
	print best_values, best_chi
	best_exp=calculate_expected(best_values, expected_ratios)
#	best_vsum, rsum=sum(best_values), sum(expected_ratios)
#	value_fracs=[float(value)/best_vsum for value in best_values]
#	ratio_fracs=[float(value)/rsum for value in expected_ratios]
	chisquare, p=scipy.stats.chisquare(best_values, best_exp)
	print 'official_chi=', chisquare, 'official_p=', p
#main_func(original_values, expected_ratios)
