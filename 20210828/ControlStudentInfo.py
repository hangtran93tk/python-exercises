import SomeModules as m
import pandas as pd

student_list = []

def show_title():
    info = "{:18} {:18} {:18} {:18} {:18} {:18}"
    print(info.format("Mã số", "Họ tên", "Giới tính", "Tỉnh/thành phố", "Điểm thi lý thuyết", "Điểm thi thực hành"))

def add_student():
    path = input("Nhap path cua file excel (Ex: C:\\Users\\..) : ")
    # df = pd.read_excel('C:\\Users\\81805\\Downloads\\Students.xlsx', engine="openpyxl")
    df = pd.read_excel(f'{path}', engine="openpyxl")
    dn = df.to_numpy()
    for i in range(len(dn)):
        student_list.append(dn[i])
    print("Thêm danh sách học sinh thành công")

def edit_student():
    student_id = m.nhapChuoi("Nhập mã số học sinh")
    index = find_index(student_id)
    while True:
        if index is None:
            print("Mã số học sinh không chính xác. Vui lòng nhập lại ! ")
            student_id = m.nhapChuoi("Nhập mã số học sinh: ")
            index = find_index(student_id)
        else:
            break

    #Display student info you want edit
    for i in range(len(student_list[index])):
        info = "{:18}"
        print(info.format(student_list[index][i]), end=" ")
    print("\n")

    student_list[index][1] = m.nhapChuoi("Họ tên")
    student_list[index][2] = m.nhapChuoi("Giới tính")
    student_list[index][3] = m.nhapChuoi("Tỉnh/thành phố")
    student_list[index][4] = m.nhapSo("Điểm thi lý thuyết")
    student_list[index][5] = m.nhapSo("Điểm thi thực hành")
    print("Thay đổi thông tin học sinh hoàn thành.")

    for i in range(len(student_list[index])):
        info = "{:18}"
        print(info.format(student_list[index][i]), end=" ")
    print("\n")

def show_student_list():
    show_title()
    info = "{:18}"
    for i in range(len(student_list)):
        for j in  range(len(student_list[i])):
            print(info.format(student_list[i][j]), end=" ")
        print("\n")

def get_average_score(*num):
    total = 0
    for i in range(len(num)):
        total += num[i]
    return total // len(num)

def show_passed_students():
    print("Danh sách học viên thi đỗ")
    show_title()
    for i in range (len(student_list)):
        average = get_average_score(student_list[i][4],student_list[i][5])
        if average >= 75:
            for j in range(len(student_list[i])):
                info = "{:18}"
                print(info.format(student_list[i][j]), end=" ")
            print("\n")

def show_failed_students():
    print("Danh sách học viên thi trượt")
    show_title()
    for i in range (len(student_list)):
        average = get_average_score(student_list[i][4],student_list[i][5])
        if average < 75:
            for j in range(len(student_list[i])):
                info = "{:18}"
                print(info.format(student_list[i][j]), end=" ")
            print("\n")

def  remove_student():
    student_id = m.nhapChuoi("Nhập mã số học sinh")
    del_index = find_index(student_id)
    while True:
        if del_index is None:
            print("Mã số học sinh không chính xác. Vui lòng nhập lại ! ")
            student_id = m.nhapChuoi("Nhập mã số học sinh: ")
            del_index = find_index(student_id)
        else:
            break
    del_confirm = m.nhapChuoi(f"Bạn có chắc chắn muốn xóa học sinh số {student_id} không ? Y/N : ")
    if del_confirm == "Y":
        del student_list[del_index]
        print(f"Đã xóa học sinh số {student_id}")
def find_index(student_id):
    del_index = None
    for i in range(len(student_list)):
        if student_id == student_list[i][0]:
            del_index = i
            break
    return del_index
def show_menu():
    print('''
Hãy chọn tính năng muốn thực hiện:
1. Thêm thông tin học viên vào bộ nhớ
2. Cập nhật thông tin học viên
3. Hiển thị danh sách tất cả học viên
4. Hiển thị danh sách học viên thi đỗ (Điểm trung bình >= 75)
5. Hiển thị danh sách học viên thi trượt (Điểm trung bình < 75)
6. Xóa thông tin của học viên
7. Thoát chương trình

    ''')

def get_choice():
    return m.nhapSo("Lựa chọn của bạn")

while True:
    show_menu()
    user_choice = get_choice()
    print(f"Bạn đã chọn {user_choice}")
    if user_choice == "7":
        print("Kết thúc chương trình")
        break
    elif user_choice == "1":
        add_student()
    elif user_choice == "2":
        edit_student()
    elif user_choice == "3":
        show_student_list()
    elif user_choice == "4":
        show_passed_students()
    elif user_choice == "5":
        show_failed_students()
    elif user_choice == "6":
        remove_student()

