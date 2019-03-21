import sys
T = int(input())
for i in range(0,T):
	i1,i2,i3,i4 = sys.stdin.readline().rstrip().split()
	M = int(i1)
	N = int(i2)
	x = int(i3)
	y = int(i4)
	if M==N:
		if x==y:
			print(x)
		else:
			print("-1")
	elif M-N>0:
		d = M-N
		r = {}
		a = N
		b = 1
		while a>0:
			r[a] = b
			if M-a<N:
				r[a-M] = b
			b+=1
			a = (a+N)%M
		if x==y:
			print(x)
		else:
			if r.get(x-y)==None:
				print("-1")
			else:
				ret = 0
				ret = y+N*r.get(x-y)
				print(ret)
	elif M-N<0:
		d = N-M
		r = {}
		a = M
		b = 1
		while a>0:
			r[a] = b
			if N-a<M:
				r[a-N] = b
			b+=1
			a = (a+M)%N
		if x==y:
			print(x)
		else:
			if r.get(y-x)==None:
				print("-1")
			else:
				ret = 0
				ret = x+M*r.get(y-x)
				print(ret)
