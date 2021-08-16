year = int(input("Nhập số năm : "))

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print("{} là năm nhuận".format(year))
else:
    print("{} không phải năm nhuận".format(year))