def func(x):
	if x<100:
		return True
	elif x>99:
		nums = []
		while True:
			if x==0:
				break
			nums.append(x%10)
			x = int(x/10)
		dif = nums[0] - nums[1]
		for i in range(1, len(nums)-1):
			if (nums[i]-nums[i+1])!=dif:
				return False
		return True

X = int(input())
cnt = 0
for i in range(1,X+1):
	if func(i)==True:
		cnt+=1
print(cnt)
