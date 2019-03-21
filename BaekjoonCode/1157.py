inp = input()
word = inp.upper()
a = {}
ret = ""
max = 0
for x in word:
	if a.get(x)==None:
		a[x] = 1
	else:
		a[x] = a[x]+1
for y in a.keys():
	if max<a[y]:
		max = a[y]
for y in a.keys():
	if a[y]==max:
		ret+=y
if len(ret)>1:
	print('?')
else:
	print(ret)
