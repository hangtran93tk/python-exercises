import SomeModule as modul
chuoi = modul.nhapChuoi("chuoi bat ky")
for i in range(1,len(chuoi) // 2 + 1):
    loopLen = len(chuoi[:i])
    loopCount = chuoi.count(chuoi[:i], 0, len(chuoi))
    if len(chuoi) // loopLen == loopCount and len(chuoi) % loopLen == 0:
        print(f"{chuoi} la chuoi lap")
        break
else:
    print(f"{chuoi} khong phai chuoi lap")

