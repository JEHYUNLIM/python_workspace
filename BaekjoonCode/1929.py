m, n = input().split()
M = int(m)
N = int(n)
r = [0]*(N+1)
for i in range(N+1):
        r[i] += i
r[1] = 0
for i in range(2,N+1):
	if r[i] == 0:
		continue
	for j in range(i+i,N+1,i):
		r[j] = 0

for i in range(M, N+1):
	if r[i]!=0:
		print(r[i])
