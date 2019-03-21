def erase(table, l, x, y):
	if l==3:
		table[y][x] = ' '
	else:
		for i in range(0, int(l/2)):
			for j in range(i, l-i-1):
				table[y+i][x+j] = ' '
		if l==6:
			erase(table, int(l/2), x+int(int(l/2)/2)+1, y-int(int(l/2)/2)-1)
		else:
			erase(table, int(l/2), x+int(int(l/2)/2), y-int(int(l/2)/2))
		erase(table, int(l/2), x-int(int(l/2)/2), y+int(int(l/2)/2))
		erase(table, int(l/2), x-int(int(l/2)/2)+l, y+int(int(l/2)/2))

def draw(table, n, x, y):
	if n==3:
		table[y][x] = '*'
		table[y+1][x-1] = '*'
		table[y+1][x+1] = '*'
		table[y+2][x-2] = '*'
		table[y+2][x-1] = '*'
		table[y+2][x] = '*'
		table[y+2][x+1] = '*'
		table[y+2][x+2] = '*'
	else:
		draw(table, int(n/2), x, y)
		draw(table, int(n/2), x-int(n/2), y+int(n/2))
		draw(table, int(n/2), x+int(n/2), y+int(n/2))


N = int(input())
star = [[' ']*((5*int(N/3))+(int(N/3)-1)) for i in range(N)]
'''
for i in range(0, N):
	for j in range(N-i-1,N+i):
		star[i][j] = '*'
if N==3:
	erase(star,N,2,1)
else:
	erase(star, N, int(N/2), int(N/2))
'''
draw(star,N,N-1,0)
for i in range(0,N):
	print(''.join(star[i]))
