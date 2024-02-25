'''
Collection of functions to calculate point densities for a scatter plot
'''

def make_point_dict(x_values, y_values, bin_size):
	'''
	returns the number of points present for each coordinate pair in a graph.
	Points are binned for greater search efficiency in the density calculation
	'''
	point_dict={}
	for value_number, x_value in enumerate(x_values):
		point=(x_value, y_values[value_number])
		bin_number=int(x_value/bin_size)
		if bin_number not in point_dict:
			point_dict[bin_number]={}
		if point not in point_dict[bin_number]:
			point_dict[bin_number][point]=0
		point_dict[bin_number][point]+=1
	return point_dict

def calculate_distance(first_point, second_point):
	x_distance=abs(first_point[0]-second_point[0])
	y_distance=abs(first_point[1]-second_point[1])
	return (x_distance**2+y_distance**2)**0.5

def calculate_density(first_point, points, threshold_distance):
	'''
	returns the number of points within distance units of first_point given a dictionary of points
	'''
	count=0
	current_bin=int(first_point[0]/threshold_distance)
	for bin_number in range(current_bin-2, current_bin+3):
		if bin_number in points:
			for second_point in sorted(points[bin_number]):
#				print second_point
				if abs((second_point[1]-first_point[1]))<threshold_distance and abs((second_point[1]-first_point[1]))<threshold_distance:
					observed_distance=calculate_distance(first_point, second_point)
					if observed_distance<threshold_distance:
						count+=points[bin_number][second_point]
	return count

def main(x_list, y_list, density_distance):
	import math
	point_dict=make_point_dict(x_list, y_list, density_distance)
	count_list=[]
	for x_number, x in enumerate(x_list):
		if x_number%100==0:
			print x_number/float(len(x_list))
		y=y_list[x_number]
		count=calculate_density((x,y), point_dict, density_distance)
#		print count
#		print math.log(count, 2)
		count_list.append(math.log(count, 2)+1)
	return count_list
