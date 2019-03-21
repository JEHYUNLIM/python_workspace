N = int(input())
cnt = 1
ans = 1
while ans<N:
	ans+=cnt
	cnt+=1
if ans==N:
	if cnt%2==1:
		print(str(cnt)+"/1")
	else:
		print("1/"+str(cnt))
else:
	if cnt%2==1:
		print(str(N-ans+cnt)+"/"+str(ans-N))
	else:
		print(str(ans-N)+"/"+str(N-ans+cnt))
