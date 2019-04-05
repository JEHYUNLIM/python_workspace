import sys
r = []
ans = []
count = 1
tf = True
N = int(input())
for i in range(N):
	num = int(sys.stdin.readline())
	while count <=num:
		r.append(count)
		ans.append('+')
		count+=1
	if r[-1] == num:
		r.pop()
		ans.append('-')
	else:
		tf = False

if tf ==False:
	print('NO')
else:
	for j in ans:
		print(j)
