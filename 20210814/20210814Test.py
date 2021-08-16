#20210814
# discount program
# money = int(input("Bạn đã chi bao nhiêu tiền : "))
#
# if money >= 150:
#     print("Bạn được giảm 50$")
#     money -= 50
# elif money >= 100:
#     print("Bạn được giảm 25$")
#     money -= 25
# elif money >= 75:
#     print("Bạn được giảm 15$")
#     money -= 15
#
# print(f"Số tiền phải thanh toán: {money}")

#BMI program
w = float(input("Nhập cân nặng : "))
t = float(input("Nhập chiều cao (m) : "))
bmi = w / (t * 2)
if bmi < 16:
    print("Gầy cấp độ III")
elif bmi < 17:
    print("Gầy cấp độ II")
elif bmi < 18.5:
    print("Gầy cấp độ I")
elif bmi < 25:
    print("Binh thường")
elif bmi < 30:
    print("Thừa cân")
elif bmi < 35:
    print("Béo phì cấp độ I")
elif bmi < 40:
    print("Béo phì cấp độ II")
else:
    print("Béo phì cấp độ III")