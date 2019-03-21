inp = input()
ret = 0
for x in inp:
	if x<='C':
		ret += 3
	elif x>='D' and x<='F':
		ret += 4
	elif x>='G' and x<='I':
		ret += 5
	elif x>='J' and x<='L':
		ret += 6
	elif x>='M' and x<='O':
		ret += 7
	elif x>='P' and x<='S':
		ret += 8
	elif x>='T' and x<='V':
		ret += 9
	elif x>='W' and x<='Z':
		ret += 10
print(ret)
