can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh','Mậu','Kỷ']
chi = ['Thân', 'Dậu', 'Tuất', 'Hợi','Tí','Sửu','Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi']
msg = ""
# Input year
while True:
    year = input("Nhập vào năm dương : ")
    if year.isdigit():
        break
    else:
        msg = "Đây không phải số"
        print(msg)

# Check Lunar Year
a = int(year) % 10
b = int(year) % 12
print(can[a] + " " + chi[b])
