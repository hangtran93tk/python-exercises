inputErrorMsg = "Hay nhap so tu nhien lon hon 0"

def nhapSo(sideName):
    while True:
        num = input(f"Nhap {sideName} : ")
        if num.isdigit():
            break
        else:
            print(inputErrorMsg)

    return num

chieudai = int(nhapSo("chieu dai"))
chieurong = int(nhapSo("chieu rong"))
char = "*"
for i in range(1,chieurong + 1):
    print_str = ''
    for j in range(1,chieudai + 1):
        if i == 1 or i == chieurong:
            print_str += char
        else:
            if j == 1 or j == chieudai:
                print_str += char
            else:
                print_str += ' '
    print(print_str)