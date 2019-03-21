N = int(input())
cnt = 0
for i in range(0,N):
	word = input()
	l = []
	for i in range(0, len(word)):
		if i == 0:
			l.append(word[i])
		elif word[i] != word[i-1]:
			l.append(word[i])
	for i in range(0, len(l)):
		if l.count(l[i]) != 1:
			break
		if i==len(l)-1:
			cnt+=1
print(cnt)
			
		
