import sys
import math
N = int(input())
sum = 0
r = [0]*8001
count = 0
max = 0
ret = 0
cnt = 0
for i in range(N):
	a = int(sys.stdin.readline())
	sum += a
	r[a+4000]+=1
n = 9000
for b in range(len(r)):
	if r[b]==max:
		cnt+=1
	if r[b]>max:
		cnt = 1
		max = r[b]
		ret = b-4000
	if r[b]>0 and n == 9000:
		n = b-4000
	for c in range(r[b]):
		count+=1
		if count==int(N/2)+1:
			print(round(sum/N))
			print(b-4000)
		if count==N:
			m = b-4000
if cnt == 1:
	print(ret)
else:
	ret = 0
	for d in range(len(r)):
		if max==r[d]:
			if ret==1:
				print(d-4000)
				break
			ret+=1
print(m-n)

