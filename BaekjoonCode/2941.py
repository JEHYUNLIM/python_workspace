word = input()
cnt = 0
i = 0
while i<len(word):
	if word[i]=='c':
		if i<len(word)-1:
			if word[i+1]=='=' or word[i+1]=='-':
				i=i+1
		cnt+=1
	elif word[i]=='d':
		if i<len(word)-2:
			if word[i+1]=='z' and word[i+2]=='=':
				i=i+2
		if i<len(word)-1:
			if word[i+1]=='-':
				i=i+1
		cnt+=1
	elif word[i]=='l':
		if i<len(word)-1:
			if word[i+1]=='j':
				i=i+1
		cnt+=1
	elif word[i]=='n':
		if i<len(word)-1:
			if word[i+1]=='j':
				i=i+1
		cnt+=1
	elif word[i]=='s':
		if i<len(word)-1:
			if word[i+1]=='=':
				i=i+1
		cnt+=1
	elif word[i]=='z':
		if i<len(word)-1:
			if word[i+1]=='=':
				i=i+1
		cnt+=1
	else:
		cnt+=1
	i+=1
print(cnt)
