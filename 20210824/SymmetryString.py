import SomeModule as module

chuoi = module.nhapChuoi("chuoi bat ky")
tail = len(chuoi) - 1

for i in range(len(chuoi)//2):
    if chuoi[i] != chuoi[tail]:
        print(f"{chuoi} khong phai chuoi doi xung")
        break
    tail -= 1
else:
    print(f"{chuoi} la chuoi doi xung")
