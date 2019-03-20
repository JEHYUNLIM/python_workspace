i1, i2 = input().split()
month = int(i1)
day = int(i2)

getMonth = 0;
for i in range(1, month):
	if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
		getMonth+=31
	elif i==2:
		getMonth+=28
	else:
		getMonth+=30
getMonth = getMonth+day-1
if getMonth%7==0:
	print("MON")
elif getMonth%7==1:
	print("TUE")
elif getMonth%7==2:
	print("WED")
elif getMonth%7==3:
        print("THU")
elif getMonth%7==4:
        print("FRI")
elif getMonth%7==5:
        print("SAT")
elif getMonth%7==6:
        print("SUN")
