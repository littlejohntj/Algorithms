"""
8-3: You are given an array of integers, where different integers
may have different number of characters, but the total number of 
characters over all the strings is. Show how to sort the array in 
O(n) time. 
"""

def zeros():
	return [0,0,0,0,0,0,0,0,0,0]

# radix sort 
def r_sort(a): 

	a_list = []
	a_dict = {}

	max_number_len = 0

	for e in a:

		e_len = len(str(e))
		a_list_len = len(a_list)

		# find the number with most digits 
		if e_len > max_number_len:
			max_number_len = e_len

		# if the key e_len is in the dictionary already, we append
		# e to the list inside of a_list. We get the index from the 
		# dictionary a_dict with the key being the size of e. if it is
		# not, then we create the dictionary entry of the index for ints
		# of that size and then add the new list to a_list
		if e_len in a_dict:
			a_list[a_dict[e_len]].append(e)
		else:
			a_dict[e_len] = a_list_len
			a_list.append([e])

	c = zeros()

	# enumerate through each sublist. Each sublist 
	# contains all the numbers of equal digit lengths 
	for p, sub_list in enumerate(a_list):

		# set b to be an empty list the same size as this sublist 
		b = [None] * len(sub_list)

		# itterate from len(elements in this sublist) to 0
		# to be able to access numbers from the least significant
		# to the most significant
		for d in reversed(range(len(str(sub_list[0])))):

			# for this digit index d, we count all occurances
			# of the numbers 0-9. at the end of this loop, c[i] will 
			# contain the number of elements in sub_list that have 
			# i as the digit at this index d.  
			for s in sub_list:
				c[ int(str(s)[d]) ] = c[ int(str(s)[d]) ] + 1

			# here we incrementally sum all of the counts from left 
			# to right so at the end of the loop, c[i] will be the number of 
			# elements in the sub_list that at digit d, are less than or equal to i
			for i in range(10):
				if i >= 1:
					c[i] = c[i] + c[i - 1]

			# for each itteration we look at the d index of the number j.
			# we look at this number as the index of c. this gives us the
			# to spot to place it in b. also we decrement c at this index at c.
			# this will cause the next value equal to this j to be placed directly
			# before it in the list b.
			for j in reversed(sub_list):
				b[c[int(str(j)[d])] - 1] = j
				c[int(str(j)[d])] = c[int(str(j)[d])] - 1

			# zero out c for the next itteration
			c = zeros()

		# replace this sublist with the newly sorted list b
		a_list[p] = b

	# from 0...max_number_len check if this number is a key in the a_dict. 
	# the value will be the index of a_list. mergeing in this manner is 
	# insuring that that numbers with more digits will be placed after 
	# numbers with less digits.
	final_list = []		
	for k in range(max_number_len + 1):
		if k in a_dict:
			final_list += a_list[a_dict[k]]

	return final_list

a = [1, 11, 111, 2, 22, 222, 3, 321, 33, 333, 54, 4, 44, 444, 5, 55, 555]

l = r_sort(a)
print l






























