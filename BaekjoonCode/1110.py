N = int(input())
mod = N
cnt = 0;
while True:
	mod = mod%10*10 + (int(mod/10) + mod%10)%10
	cnt+=1;
	if mod == N:
		print(cnt)
		break
