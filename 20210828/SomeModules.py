# Nhap so tu ban phim

def nhapSo(sideName):
    inputErrorMsg = "Hãy nhập số tự nhiên lớn hơn 0"
    while True:
        num: str = input(f"{sideName} : ")
        if num.isdigit():
            break
        else:
            print(inputErrorMsg)

    return num
# Nhap chuoi

def nhapChuoi(tenChuoi):
    while True:
        chuoi = input(f"{tenChuoi}: ")
        if len(chuoi) < 1 or len(chuoi) > 1000:
            print("Độ dài chuỗi phải lớn hơn 1 hoặc nhỏ hơn 1000")
        else:
            break

    return chuoi