num_check = int(input("Nhập vào số tự nhiên bất kỳ : "))

# USING TERNARY OPERATOR
msg = "{} Là số chẵn" if num_check %2 == 0 else "{} Là số lẻ"
print(msg.format(num_check))