
num = int(input("Hay nhap mot so tu nhien lon hon 0: "))

count = 0
n = 1
while count < num:
    n += 1
    for i in  range(2, n // 2 + 1):
        if n % i == 0:
            break
    else:
        print(n, end=" ")
        count += 1
