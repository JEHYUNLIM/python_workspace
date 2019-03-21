aver = 0
for i in range(0,5):
	a = int(input())
	if a<40:
		aver+=40
	else:
		aver+=a
print(int(aver/5))
