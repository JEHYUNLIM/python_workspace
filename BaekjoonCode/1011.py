T = int(input())

for i in range(0,T):
	i1, i2 = input().split()
	d = int(i2)-int(i1)
	ans = 1
	cnt = 0
	while ans<d:
		ans+=(cnt+2)
		cnt+=2
	if ans==d:
		print(cnt+1)
	else:
		if d<ans-int(cnt/2):
			print(cnt-1)
		else:
			print(cnt)
