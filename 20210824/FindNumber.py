import SomeModule as module

num_in = int(module.nhapSo("Số thứ tự"))
count = 0
num_list = ["0"]
last_num = "0"
default_num = "0123456789"
last_num_len = len(last_num)
while count < num_in:
    default_num = "0123456789"
    for i in range(last_num_len):
        index = default_num.find(last_num[i])
        if index >= 0:
            default_num = default_num.replace(last_num[i],"")
    print(f"DEBUG1 : default_num {default_num}")

    if last_num[0] == '9':
        print("Start")
        last_num = "1" + last_num[1:] + "0"
        last_num_len += 1
        print(f"DEBUG2 : last_num {last_num}")

    else:
        for i in range(len(default_num)):
            if last_num[0] < default_num[i]:
                last_num = default_num[i] + last_num[1:]
                break
        print(f"DEBUG3 : last_num {last_num}")

    for i in range(1,last_num_len):
        print(last_num_len)
        if i == last_num_len - 1:
            last_num = last_num[:i] + default_num[0]
        else:
            last_num = last_num[:i] + default_num[0] + last_num[i + 1:]

    num_list.append(last_num)
    count += 1

print(f"DEBUG4 : num_list : {num_list}")
print(f"DEBUG5 : So thu tu {num_in} la {num_list[num_in]}")
print("DEBUG6 : finish")

