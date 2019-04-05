import sys
def func(w):
	depth = 0
	for i in w:
		if i=='(':
			depth+=1
		elif i==')':
			depth-=1
		if depth<0:
			return 'NO'
	if depth==0:
		return 'YES'
	else:
		return 'NO'
T = int(input())
for i in range(T):
	word = sys.stdin.readline()
	print(func(word))
