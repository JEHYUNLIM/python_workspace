N = 10000
r = [0]*(N+1)
for i in range(N+1):
        r[i] += i
r[1] = 0
for i in range(2,N+1):
        if r[i] == 0:
                continue
        for j in range(i+i,N+1,i):
                r[j] = 0
n = int(input())
for i in range(n):
	a = int(input())
	for j in range(int(a/2),0,-1):
		if r[j]!=0:
			if r[a-j]!=0:
				print(str(j)+" "+str(a-j))
				break
	
