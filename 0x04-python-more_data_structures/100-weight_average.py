#!/usr/bin/python3
def weight_average(my_list=[]):
	if my_list and len(my_list):
		above=0
		under=0
		for t in my_list:
			above+=t[0]*t[1]
			under+=t[1]
		return above/under
	else:
		return 0
