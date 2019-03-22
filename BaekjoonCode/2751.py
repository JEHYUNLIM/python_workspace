import sys
N = int(input())
r = [0]*1000001
for i in range(0,N):
        n = int(sys.stdin.readline())
        if n>0:
                r[n] = 1
        elif n<0:
                r[n*(-1)] += 2
        else:
                r[n] = 1
for i in range(1000000,-1,-1):
        if r[i]==2 or r[i]==3:
                print(i*(-1))
for i in range(0,1000001):
        if r[i]==1 or r[i]==3:
                print(i)
