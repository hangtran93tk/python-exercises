import SomeModule as module

num_in = int(module.nhapSo("Số thứ tự"))
count = 0
num_list = ["0"]
last_num = "0"
last_num_len = len(last_num)

while count < num_in:
    default_num = "0123456789"

    # Tìm và loại bỏ số đã tồn tại
    for i in range(last_num_len):
        index = default_num.find(last_num[i])
        if index >= 0:
            default_num = default_num.replace(last_num[i],"")
    # print(f"DEBUG1 : default_num {default_num}")

    # Thiết lập chữ số đầu tiên cho số
    if last_num[0] == '9':
        last_num = "1" + last_num[1:] + "0"
        last_num_len += 1
        # print(f"DEBUG2 : last_num {last_num}")
    else:
        for i in range(len(default_num)):
            if last_num[0] < default_num[i]:
                last_num = default_num[i] + last_num[1:]
                break
        # print(f"DEBUG3 : last_num {last_num}")

    # Thiết lập các chữ số tiếp theo cho số
    for i in range(1,last_num_len):
        if i == last_num_len - 1:
            last_num = last_num[:i] + default_num[0]
        else:
            last_num = last_num[:i] + default_num[0] + last_num[i + 1:]

    # Thêm số vào chuỗi
    num_list.append(last_num)
    count += 1

# print(f"DEBUG4 : num_list : {num_list}")
print(f"Số ở vị trí {num_in} là {num_list[num_in]}")

