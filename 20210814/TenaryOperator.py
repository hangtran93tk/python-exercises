num_check = int(input("Nhập vào số tự nhiên bất kỳ : "))

# USING TERNARY OPERATOR
msg = "{} Là số chẵn".format(num_check) if num_check %2 == 0 else "{} Là số lẻ".format(num_check)
print(msg)