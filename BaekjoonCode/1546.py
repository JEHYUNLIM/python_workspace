N = int(input())
score = list(map(int,input().split()))
score.sort()
max = score[N-1]
aver = 0;
for i in range(0, N):
	aver+=score[i]/max*100
print(aver/N)
