a = int(input("Nhap vao so nguyen a: "))
b = int(input("Nhap vao so nguyen b: "))
sum = 0

for i in  range (a, b + 1):
    sum += i

print(f"Tong tu {a} toi {b} la {sum}")