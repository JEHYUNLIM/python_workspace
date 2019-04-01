def func(n):
        c = 0
        if n==1:
                return 0
        for i in range(2,n):
                if n%i == 0:
                        return 0
        return 1

M = int(input())
N = int(input())
r = [M]*(N-M+1)
ans = 0
cnt = 0
for i in range(0, N-M+1):
	r[i] += i
r.reverse()
for x in r:
	if func(x) == 1:
		ans += x
		cnt = x
if ans ==0:
	print(-1)
else:
	print(ans)
	print(cnt)
