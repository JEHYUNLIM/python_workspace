nums = list(map(int, input().split()))
dif = nums[0]-nums[1]
for i in range(1,7):
	if nums[i]-nums[i+1] != dif:
		print("mixed")
		break;
	if i==6:
		if dif<0:
			print("ascending")
		else:
			print("descending")
