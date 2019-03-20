import math
words = input()
for i in range(0,math.ceil(len(words)/10)):
	print(words[i*10:(i+1)*10])
	
