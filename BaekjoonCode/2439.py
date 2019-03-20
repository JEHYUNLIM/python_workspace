import sys
N = int(input())
for i in range(1,N+1):
	for j in range(1, N-i+1):
		sys.stdout.write(' ')
	for k in range(1, i+1):
		sys.stdout.write('*')
	print()

