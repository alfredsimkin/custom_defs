
def iterate(successes, trials):
	counter=0
	border=trials-successes
	count_1, count_0, current_pos, current_str=0,0,0,''
	stop=False
	def chew_back(current_pos, current_str):
		while current_str[-1]!='1':
			current_str=current_str[:-1]
			current_pos-=1
		return current_pos-1

	while stop==False:
		if count_1>0 and count_0==border:
			one_pos=chew_back(current_pos, current_str)
			next_count_1=count_1-1
		elif count_0==border and count_1==0:
			stop=True
		while count_1<successes or count_0<border:
			if count_1<successes:
				if count_0<border:
					one_pos=current_pos
					next_count_1=count_1
				current_str+='1'
				count_1+=1
			elif count_0<border:
				current_str+='0'
				count_0+=1
			current_pos+=1
#		print current_str
		counter+=1
		if counter%1000000==0:
			print counter/225792840.0
		current_str, count_1=current_str[:one_pos]+'0', next_count_1
		count_0, current_pos=len(current_str)-count_1, len(current_str)
	print counter
iterate(20, 32)
