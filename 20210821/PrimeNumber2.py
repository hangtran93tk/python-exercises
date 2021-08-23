
num = int(input("Hay nhap mot so tu nhien lon hon 0: "))

for i in range(2,num + 1,1):
    if i == 2:
        print(i, end=", ")
    else:
        a = i // 2 + 1
        for j in (2,a, 1):
            if i % j == 0:
                break
            else:
                print(i, end=", ")
                break