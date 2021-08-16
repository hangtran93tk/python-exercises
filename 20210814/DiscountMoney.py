
money = int(input("Bạn đã chi bao nhiêu tiền : "))

if money >= 150:
    print("Bạn được giảm 50$")
    money -= 50
elif money >= 100:
    print("Bạn được giảm 25$")
    money -= 25
elif money >= 75:
    print("Bạn được giảm 15$")
    money -= 15

print(f"Số tiền phải thanh toán: {money}")