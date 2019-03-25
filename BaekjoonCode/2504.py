import sys
def func(p,d):
	a = p.pop()
	ans = 1
	l = []
	if a[0] ==')' or a[0] ==']':
		while True:
			b = p.pop()
			if b[1]==a[1]:
##				if b[1]==d:
				if len(l)==0:
					if b[0]=='(' and a[0]==')':
						return 2
					elif b[0]=='[' and a[0]==']':
						return 3
					else:
						print("0")
						sys.exit(1)
				if b[0] == '(' and a[0] ==')':
					l.reverse()
					ans = 2*func(l,d+1)
					return ans
				elif b[0] =='[' and a[0] ==']':
					l.reverse()
					ans = 3*func(l,d+1)
					return ans
				else:
					l.append(b)
			else:
				l.append(b)
	else:
		print("0")
		sys.exit(1)
word = input()
depth = 0
r = []
for i in word:
	if i=='(' or i=='[':
		depth+=1
		r.append([i,depth])
	elif i==')'or i==']':
		r.append([i,depth])
		depth-=1
a = func(r,1)
print(a)
