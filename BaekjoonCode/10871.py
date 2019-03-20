import sys
i1, i2 = input().split()
N = int(i1)
X = int(i2)
cnt = 0;
nums = []
nums = input().split()
for i in range(0,N):
	if int(nums[i])<X:
		if cnt!=0:
			sys.stdout.write(' ')
		sys.stdout.write(nums[i])
		cnt+=1;
