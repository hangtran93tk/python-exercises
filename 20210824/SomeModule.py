# Nhap so tu ban phim

def nhapSo(sideName):
    inputErrorMsg = "Hay nhap so tu nhien lon hon 0"
    while True:
        num: str = input(f"Nhap {sideName} : ")
        if num.isdigit():
            break
        else:
            print(inputErrorMsg)

    return num
# Nhap chuoi

def nhapChuoi(tenChuoi):
    while True:
        chuoi = input(f"Nhap {tenChuoi}: ")
        if len(chuoi) < 1 or len(chuoi) > 1000:
            print("Do dai chuoi phai lon hon 1 hoac nho hon 1000")
        else:
            break

    return chuoi