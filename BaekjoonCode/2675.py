T = int(input())
for i in range(0,T):
	ans = ""
	i1, i2 = input().split()
	n = int(i1)
	for x in i2:
		for i in range(0,n):
			ans+=x
	print(ans)
