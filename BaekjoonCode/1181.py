import sys
N = int(input())
l = [[0,[]] for i in range(51)]
for i in range(N):
	word = str(sys.stdin.readline().rstrip())
	l[len(word)][0] +=1
	l[len(word)][1].append(word)
for i in l:
	if i[0]>0:
		if i[0]>1:
			ret = list(set(i[1]))
			ret.sort()
			for j in ret:
				print(j)
		else:
			print(i[1][0])
