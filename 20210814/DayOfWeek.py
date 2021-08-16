num = int(input("Nhập số tùy ý (Từ 1 tới 7): "))
msg = ""
if num == 1:
	msg = "Monday"
elif num == 2:
	msg = "Tuesday"
elif num == 3:
	msg = "Wednesday"
elif num == 4:
	msg = "Thursday"
elif num == 5:
	msg = "Friday"
elif num == 6:
	msg  = "Saturday"
elif num == 7:
	msg = "Sunday"
else:
	msg = "Error, out of range"

print(msg)