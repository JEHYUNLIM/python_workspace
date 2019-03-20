import sys
N = int(input())
for i in range(N,0,-1):
        for k in range(1, i+1):
                sys.stdout.write('*')
        print()
