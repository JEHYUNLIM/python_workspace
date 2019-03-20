N = int(input())
for i in range(N,-1,-1):
	if N-5*i>=0 and (N-5*i)%3 == 0:
		j = (N-5*i)/3
		print(int(i+j))
		break
	else:
		if i == 0:
			print("-1")
