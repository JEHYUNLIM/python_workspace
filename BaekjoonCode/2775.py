import sys
def func(x,y):
	global r
	if y==1:
		return y
	else:
		if x==0:
			return y
		else:
			a = func(x,y-1)+func(x-1,y)
			r[x][y] = a
			return a
T = int(sys.stdin.readline().rstrip())
r = [[0 for i in range(15)] for j in range(15)]
for i in range(15):
	r[i][1] = 1
	r[0][i] = i
'''
for i in range(1,15):
	for j in range(1,15):
		r[i][j] = r[i][j-1]+r[i-1][j]
'''
max = func(14,14)
for i in range(0,T):
	k = int(sys.stdin.readline().rstrip())
	n = int(sys.stdin.readline().rstrip())
##	print(func(k,n))
	print(r[k][n])
	
