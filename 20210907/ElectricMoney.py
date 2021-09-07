import SomeModules as m

def cal_money(mount):
    unit_price = [1678,1734,2014,2536,2834,2927]
    level = [50,50,100,100,100]
    total_price = 0
    for i in range(len(level)):
        if mount > level[i]:
            total_price += unit_price[i] * level[i]
        elif mount > 0:
            total_price += unit_price[i] * mount
        else:
            break
        mount -= level[i]
    if mount > 0:
        total_price += unit_price[len(unit_price) - 1] * mount
    return total_price

def tax(money):
    return int(money * 0.1)

luongDienTieuThu = int(m.nhapSo("Tổng điện năng tiêu thụ trong tháng là"))
print("Số tiền phải trả sẽ được tính như sau: ")

total_price = cal_money(luongDienTieuThu)
tax = tax(total_price)
total_price_with_tax = int(total_price * 1.1)

print(f"Tiền điện trước thuế: {total_price}")
print(f"Tiền thuế (10%) : {tax}")
print(f"Tiền điện sau thuế : {total_price_with_tax}")

