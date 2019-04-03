N = 123456*2
r = [0]*(N+1)
for i in range(N+1):
        r[i] += i
r[1] = 0
for i in range(2,N+1):
        if r[i] == 0:
                continue
        for j in range(i+i,N+1,i):
                r[j] = 0
for i in range(2,N+1):
	if r[i]!=0:
		r[i] = r[i-1]+1
	else:
		r[i] = r[i-1]

while True:
	n = int(input())
	if n == 0:
		break
	else:
		print(r[2*n]-r[n])
