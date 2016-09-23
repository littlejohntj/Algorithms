"""
8-3 b. You are given an array of srings, where different strings
may have different numbers of characers, but the total number of 
characters over all the strings is n. Show how to sort the strings
in O(n) time. (Note that the desired order here is the standard 
alphabetical order; for example a < ab < b.) 
"""

# 26 0s
def zeros(): 
	return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def r_sort(a):
	a_list = []
	a_dict = {}

	max_word_len = 0 

	for word in a:

		word_len = len(word)
		a_list_len = len(a_list)

		# find the word with the most letters
		if word_len > max_word_len:
			max_word_len = word_len

		# if the key word_len is in the dictionary already, we append
		# word to the list inside of a_list. We get the index from the 
		# dictionary a_dict with the key being the length of word. if it is
		# not, then we create the dictionary entry of the index for words
		# of that size and then add the new list to a_list
		if word_len in a_dict:
			a_list[a_dict[word_len]].append(word)
		else:
			a_dict[word_len] = a_list_len
			a_list.append([word])

	a = []

	for i in reversed(range(max_word_len)):

		# zero out c for the next itteration
		c = zeros()

		if i + 1 in a_dict:
			sub_list = a_list[a_dict[i + 1]] + a
		else:
			sub_list = a

		b = [None] * len(sub_list)

		for s in sub_list:
			c[ ord(s[i]) - 97 ] = c[ ord(s[i]) - 97 ] + 1

		for n in range(26):
			if n >= 1:
				c[n] = c[n] + c[n - 1]

		for j in reversed(sub_list):
			b[c[ ord(j[i]) - 97 ] -1] = j
			c[ ord(j[i]) - 97 ] = c[ord(j[i]) - 97] - 1

		a = b

	return a 

a = ["b", "a","ab"]
b = r_sort(a)
print b