N = input()
r = [0]*10
for x in N:
	r[int(x)] += 1
max = 0
r[6] += r[9]
r[6] = int(r[6]/2)+r[6]%2
r[9] = 0
for i in range(0,10):
	if r[i]>max:
		max = r[i]
print(max)
