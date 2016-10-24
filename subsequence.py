def is_subsequence(X,Y):
	c = 0
	for i in X:
		if i == Y[c]:
			c += 1
		if c == len(Y):
			return True
	return False

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
b = ['b', 'd', 'f', 'h']

print is_subsequence(X=a, Y=b)