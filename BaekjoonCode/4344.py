C = int(input())
for i in range(0,C):
	nums = list(map(int,input().split()))
	aver = 0;
	for j in range(1,nums[0]+1):
		aver+=nums[j]
	aver = aver/nums[0]
	cnt = 0;
	for j in range(1,nums[0]+1):
		if nums[j]>aver:
			cnt+=1;
	print("{0:0.3f}%".format(round(cnt/nums[0]*100,3)))
