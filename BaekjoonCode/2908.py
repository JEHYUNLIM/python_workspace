def func(a):
	ret = a[2]+a[1]+a[0]
	return ret
i1, i2 = input().split()
for i in range(2,-1,-1):
	if i2[i]>i1[i]:
		print(func(i2))
		break
	elif i2[i]<i1[i]:
		print(func(i1))
		break
