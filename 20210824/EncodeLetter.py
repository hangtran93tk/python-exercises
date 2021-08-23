import  SomeModule as m
while True:
    num = int(m.nhapSo("chuc nang (0: Ket thuc, 1: Ma hoa, 2: Giai ma)"))
    if num == 0:
        print("Ket thuc chuong trinh")
        break
    elif num == 1:
        chuoi = m.nhapChuoi("van ban S")
        khoa = int(m.nhapSo("khoa K"))
        print(chuoi)
        print(f"Chuoi ma hoa la {chuoi[:khoa][::-1]+chuoi[khoa:][::-1]}")
    elif num == 2:
        chuoi = m.nhapChuoi("chuoi ma hoa Q")
        khoa = int(m.nhapSo("khoa K"))
        print(chuoi)
        print(f"Chuoi ma hoa la {chuoi[:khoa][::-1] + chuoi[khoa:][::-1]}")
    else:
        print("Hay chon so 1 hoac 2 hoac 3")