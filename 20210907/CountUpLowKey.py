import  SomeModules as m

def count(s):
    lowkey = 0
    upperkey = 0
    for i in range(len(string)):
        if string[i].islower():
            lowkey += 1
            continue
        if string[i].isupper():
            upperkey += 1
            continue
    return lowkey, upperkey

string = m.nhapChuoi("Nhập chuỗi cần đếm")

lowkey, upperkey = count(string)
print(f"Số chữ cái viết thường: {lowkey}")
print(f"Số chữ cái viết hoa: {upperkey}")