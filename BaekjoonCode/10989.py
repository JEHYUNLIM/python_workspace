import sys
N = int(input())
r = [0]*10001
p = [0]*(N+1)
q = [0]*(N+1)
for i in range(1,N+1):
	a = int(sys.stdin.readline())
	r[a]+=1
	p[i] = a
for i in range(1,10001):
	r[i] += r[i-1]
for i in range(1,N+1):
	q[r[p[i]]] = p[i]
	r[p[i]] -= 1
for i in range(1,N+1):
	print(q[i])
