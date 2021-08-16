a = float(input("Nhập vào số bất kỳ : "))
msg = ""
if a % 2 == 0:
    msg = "{} là số chẵn"
elif a % 2 == 1:
    msg = "{} là số lẻ"
else:
    msg = "{} không phải là số tự nhiên"

print(msg.format(a))