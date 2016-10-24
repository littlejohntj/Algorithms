def find_change(n, C):
	global c_set, a_set
	t = []
	for i in C:
		t.append(0)
	coin(t=t, n=n, C=C)
	print len(c_set)
	print " "
	while not len(c_set) == 0:
		print c_set.pop()
def coin(t,n,C):
	global c_set, a_set
	if tuple(t) in a_set or n < 0:
		return 
	elif n == 0:
		c_set.add(tuple(t))
		return
	a_set.add(tuple(t))
	for p,d in enumerate(C):
		tp = t[:]
		tp[p] = tp[p] + 1
		coin(tp, n - d, C)
c_set = set([])
a_set = set([])
C = [100, 50, 25, 10,5, 1]
n = 100
find_change(n=n, C=C)