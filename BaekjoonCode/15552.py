import sys
T = int(input())
for i in range(0,T):
	i1,i2 = sys.stdin.readline().rstrip().split()
	print(int(i1)+int(i2))
