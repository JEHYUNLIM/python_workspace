import sys
N = int(input())
r = [0] * 10001

for i in range(N):
    a = int(sys.stdin.readline())
    r[a] = r[a] + 1

for b in range(len(r)):
    if r[b] !=0:
        for c in range(r[b]):
            print(b)i
