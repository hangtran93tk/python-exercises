count = 0
msg = ""
try:
    num1 = float(input("Nhập số đo cạnh 1 (số tự nhiên lớn hơn 0) : "))
    num2 = float(input("Nhập số đo cạnh 2 (số tự nhiên lớn hơn 0) : "))
    num3 = float(input("Nhập số đo cạnh 3 (số tự nhiên lớn hơn 0) : "))

    if (num1 > 0) & (num2 > 0) & (num3 > 0):
        if (num1 + num2 > num3) & (num1 + num3 > num2) & (num2 + num3 > num1):
            if (num1 == num2) & (num2 == num3):
                msg = "Đây là tam giác đều"
            elif (num1 == num2) | (num2 == num3) | (num3 == num1):
                msg = "Đây là tam giác cân"
            elif (num1 * num1 == num2 * num2 + num3 * num3) | (num2 * num2 == num1 * num1 + num3 * num3) | (
                    num3 * num3 == num1 * num1 + num2 * num2):
                msg = "Đây là tam giác vuông"
            elif (num1 * num1 > num2 * num2 + num3 * num3) | (num2 * num2 > num1 * num1 + num3 * num3) | (
                        num3 * num3 > num1 * num1 + num2 * num2):
                msg = "Đây là tam giác tù"
            else:
                msg = "Đây là tam giác nhọn"
        else:
            msg = "Đây không phải ba cạnh tam giác"
    else:
        msg = "Số nhập vào không hợp lệ"
except ValueError:
    msg = "Đây không phải số"
print(msg)
