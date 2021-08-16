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