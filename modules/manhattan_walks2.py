def iterate(successes, trials, input_string=None):
	border=trials-successes
	if input_string==None:
		input_string='1'*successes+'0'*border
	count_1, count_0=successes, border
	input_string
	for letter_number, letter in enumerate(input_string[::-1]):
		if letter=='1':
			count_1-=1
		elif letter=='0':
			count_0-=1
#		print count_0, count_1, letter
		if count_1<successes and count_0<border and letter=='1':
			new_str=input_string[:-(letter_number+1)]+'0'
#			print new_str
			count_0+=1
			break

	while count_0<border or count_1<successes:
		if count_1<successes:
			try:
				new_str=new_str+'1'
				count_1+=1
			except UnboundLocalError:
				return 'done'
				break
		else:
			new_str=new_str+'0'
			count_0+=1
	return new_str

new_str='11111111111111111111000000000000'
counter=0
while new_str!='done':
	if counter%1000000==0:
		print counter/225792840.0
	print new_str
	new_str=iterate(20,32, new_str)
	counter+=1
