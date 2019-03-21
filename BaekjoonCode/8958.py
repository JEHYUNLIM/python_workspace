def func(a):
	ret = 0;
	while a>0:
		ret+=a
		a-=1
	return ret
n = int(input())
for i in range(0,n):
	score = 0
	scores = input().split('X')
	for x in scores:
		if len(x)>0:
			score+=func(len(x))
	print(score)
