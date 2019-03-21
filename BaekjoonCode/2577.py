A = int(input())
B = int(input())
C = int(input())
num = str(A*B*C)
res = [0]*10
for i in range(0, len(num)):
	res[int(num[i])]+=1
for i in range(0,10):
	print(res[i])
