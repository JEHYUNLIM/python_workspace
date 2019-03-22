N = int(input())
r = [0]*2001
for i in range(0,N):
        n = int(input())
        r[n+1000] = 1
for i in range(0,2001):
        if r[i]==1:
                print(i-1000)r = [0]*1000001
