import SomeModule as m

chieudai = int(m.nhapSo("chieu dai"))
chieurong = int(m.nhapSo("chieu rong"))
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