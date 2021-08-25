import  SomeModule as m
import random

def encode(string):
    chuoi = m.nhapChuoi(string)
    # khoa = int(m.nhapSo("khoa K"))
    khoa = random.randint(0, len(chuoi))
    print(chuoi)
    print(f"Khoa : {khoa}")
    print(f"Chuoi ma hoa la {chuoi[:khoa][::-1] + chuoi[khoa:][::-1]}")

while True:
    num = int(m.nhapSo("chuc nang (0: Ket thuc, 1: Ma hoa, 2: Giai ma)"))
    if num == 0:
        print("Ket thuc chuong trinh")
        break
    elif num == 1:
        encode("van ban S")
    elif num == 2:
        encode("chuoi ma hoa Q")
    else:
        print("Hay chon so 1 hoac 2 hoac 3")