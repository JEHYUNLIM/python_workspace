import sys
word = input()
ans = [-1]*(int(ord('z'))-int(ord('a'))+1)
for i in range(len(word)-1,-1,-1):
	ans[int(ord(word[i]))-int(ord('a'))] = i
for i in range(0,len(ans)):
	sys.stdout.write(str(ans[i]))
	if i!=25:
		sys.stdout.write(' ')
print()
