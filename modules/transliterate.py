def trans(input_string):
	start_values='012345'
	begin=0
	start_dict={}
	for char in input_string:
		if char not in start_dict:
			start_dict[char]=start_values[begin]
			begin+=1
	output_string=''
	for char in input_string:
		output_string+=start_dict[char]
	return output_string
