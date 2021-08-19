import  SomeModule as m

number = m.nhapSo("Nhap so tu nhien lon hon 0")
len = len(number)
number = int(number)

for i in range(len):
    x = number % 10
    number = int(number / 10)
    print(x, end="")
