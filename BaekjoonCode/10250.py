T = int(input())
for i in range(0,T):
	i1,i2,i3 = input().split()
	H = int(i1)
	W = int(i2)
	N = int(i3)
	if N%H==0:
		ans = str(H)
		if int(N/H)<10:
			ans = ans + "0"+ str(int(N/H))
		else:
			ans = ans+str(int(N/H))
	else:
		ans = str(N%H)
		if int(N/H)<9:
			ans = ans + "0"+ str(int(N/H)+1)
		else:
			ans = ans+str(int(N/H)+1)
	print(ans)
