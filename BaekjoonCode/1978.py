def func(n):
	c = 0
	if n==1:
		return 0
	for i in range(2,n):
		if n%i == 0:
			return 0
	return 1

N = int(input())
r = [0]*N
r = list(map(int, input().split()))
cnt = 0
for x in r:
	cnt+=func(x)
print(cnt)
