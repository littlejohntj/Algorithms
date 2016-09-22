n = 5

a = 0
b = 1
c = 0

for i in range(n + 1):
	if i >= 2:
		c = a + b
		a = b
		b = c

if c == 0:
	print n
else:
	print c
