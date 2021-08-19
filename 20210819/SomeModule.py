# Nhap gia tri tu ban phim

def nhapSo(sideName):
    inputErrorMsg = "Hay nhap so tu nhien lon hon 0"
    while True:
        num: str = input(f"Nhap {sideName} : ")
        if num.isdigit():
            break
        else:
            print(inputErrorMsg)

    return num
