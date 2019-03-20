i1, i2, i3 = input().split()
a = int(i1)
b = int(i2)
c = int(i3)

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
