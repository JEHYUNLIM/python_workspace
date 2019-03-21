def d(n):
	num = n
	while True:
		if n==0:
                        break
		num+=n%10
		n = int(n/10)
	return num

self = [False]*10001
for i in range(1,10000):
	ret = d(i)
	if ret<=10000:
		self[ret] = True
for i in range(1,10001):
	if self[i]==False:
		print(i)
