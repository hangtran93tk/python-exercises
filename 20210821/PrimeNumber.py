num = int(input("Hay nhap mot so tu nhien lon hon 2: "))

for i in range(2,(num // 2) + 1):
    if num % i == 0:
        print(f"{num} khong phai so nguyen to")
        break
else:
    print(f"{num} la so nguyen to")