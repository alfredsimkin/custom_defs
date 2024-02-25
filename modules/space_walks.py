#input_str='00111'
import sys
input_str=sys.argv[1]
#input_str='00000000000011111111111111111111'
def fill_in_rest(prefix, chars, count_dict, border_dict):
	while sum(count_dict.values())<sum(border_dict.values()):
		for char_number, char in enumerate(chars):
			while count_dict[char]<border_dict[char]:
				prefix=prefix+char
				count_dict[char]+=1
	return prefix

def get_borders(input_str):
	border_dict={}
	for char_number, char in enumerate(input_str):
		if char not in border_dict:
			border_dict[char]=0
		border_dict[char]+=1
	chars=sorted(border_dict.keys())
	return chars, border_dict

def get_counts(chars, input_str):
	count_dict={}
	for letter in chars:
		count_dict[letter]=0
	for letter in input_str:
		count_dict[letter]+=1	
	return count_dict

def make_prefix(chars, border_dict, input_str, counter):
	count_dict={}
	for letter in chars:
		count_dict[letter]=0
	putative_prefix=None
	for letter_number, letter in enumerate(input_str):
		count_dict[letter]+=1
		current_index=chars.index(letter)
		index_counter=0
		found_one=None
		while found_one==None:
			index_counter+=1
			try:
				next_letter=chars[current_index+index_counter]
			except IndexError:
				break
			if count_dict[next_letter]<border_dict[next_letter]:
				found_one=True
				putative_last=letter_number
				putative_prefix=input_str[:putative_last]+next_letter
	if putative_prefix==None:
		print counter
		exit()
	else:
		print 'was not none'
	prefix, count_dict=putative_prefix, get_counts(chars, putative_prefix)
	return prefix, count_dict
	
chars, border_dict=get_borders(input_str)
pattern_list=[]
pattern_list.append(input_str)
#print input_str
counter=1
new_value=None
while input_str!=new_value:
#	if counter%1000000==0:
#		print counter/225792840.0
	prefix, count_dict=make_prefix(chars, border_dict, input_str, counter)
	input_str=fill_in_rest(prefix, chars, count_dict, border_dict)
#	print input_str
	pattern_list.append(input_str)
	counter+=1

#extra bit added on for supplemental thesis figure
import transliterate
for pattern in pattern_list:
#	pass
	print transliterate.trans(input_str)
