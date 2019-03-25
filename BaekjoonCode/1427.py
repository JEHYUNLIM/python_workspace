N = str(input())
r = [""]*len(N)
i=0
for a in N:
	r[i] = a
	i+=1
r.sort()
r.reverse()
print(''.join(r))
