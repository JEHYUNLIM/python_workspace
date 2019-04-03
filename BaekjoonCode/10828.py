import sys
N = int(input())
r = []
for i in range(N):
	word = sys.stdin.readline().split()
	if word[0]=="push":
		r.append(word[1])
	elif word[0]=="top":
		if len(r)==0:
			print(-1)
		else:
			print(r[len(r)-1])
	elif word[0]=="size":
		print(len(r))
	elif word[0]=="empty":
		if len(r)==0:
			print(1)
		else:
			print(0)
	elif word[0]=="pop":
		if len(r)==0:
			print(-1)
		else:
			print(r.pop())
