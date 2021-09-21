import SomeModules as m
import my_input
THEM_DANH_BA = 1
SUA_DANH_BA = 2
XOA_DANH_BA = 3
HIEN_THI_TOAN_BO_DANH_BA = 4
TIM_KIEM_DANH_BA_THEO_TEN = 5
HIEN_THI_DANH_BA_THEO_TAG = 6
THOAT_CHUONG_TRINH = 7

contact_fields = {}
contacts = {
    'Chu Van Tuyet': {
        'name': 'Chu Van Tuyet',
        'phone': ['080', '070'],
        'email': ['vantuyet@gmail.com'],
        'address': 'Vung Tau',
        'note': 'lop E1',
        'tags': ['hoc vien', 'ban be']
    }
}
def show_menu():
    print('''
Hãy chọn tính năng muốn thực hiện:
1. Thêm danh bạ
2. Sửa danh bạ
3. Xóa danh bạ
4. Hiển thị toàn bộ danh bạ
5. Tìm kiếm danh bạ theo tên
6. Hiển thị danh bạ theo tag
7. Thoát chương trình

    ''')

def get_choice():
    return m.nhapSo("Lựa chọn của bạn")

def input_contact():
    return my_input.get_input_by_field(contact_fields)

def get_updated_contact_value():
    for field in contact_fields:
        print(field["name"])
    inputed_field = input("Ban muon sua thong tin gi")

    update_field = {}
    for field in contact_fields:
        if inputed_field == field["name"]:
            update_field = field

    values = my_input.get_input_by_field(update_field)
    return inputed_field, values

def edit_contact(name, field, values):
    contacts[name][field] = values


while True:
    show_menu()
    user_choice = get_choice()
    print(f"Bạn đã chọn {user_choice}")
    if user_choice == THOAT_CHUONG_TRINH:
        print("Kết thúc chương trình")
        break
    elif user_choice == THEM_DANH_BA:
        contact = input_contact()
        contacts.update({contact["name"]: contact})
    elif user_choice == SUA_DANH_BA:
        name = input("Nhap ten danh ba muon sua: ")
        if name in contacts.keys():
            print("Bat dau sua danh ba")
            input("Ban muon sua thong tin gi?")
            edit_contact(name, field, values)
            edit_contact()
        else:
            print("Khong tim thay ten vua nhap trong danh ba")
    elif user_choice == XOA_DANH_BA:
        name = input("Nhap ten danh ba muon xoa: ")
        if name in contacts.keys():
            del contacts[name]
            print("Da xoa ban co ten la" + name)
        else:
            print("Khong tim thay ten vua nhap trong danh ba")
    elif user_choice == HIEN_THI_TOAN_BO_DANH_BA:
        pass
    elif user_choice == TIM_KIEM_DANH_BA_THEO_TEN:
        name = input("Nhap ten danh ba muon tim: ")
        if name in contacts.keys():
            print(contacts[name])
        else:
            print("Khong tim thay ten vua nhap trong danh ba")
    elif user_choice == HIEN_THI_DANH_BA_THEO_TAG:
        tag = input("Nhap tag danh ba muon hien thi: ")
        contacts_list = contacts.values()
        for contact in contacts_list:
            if tag in contact["tags"]:
                print(contact)
    else:
        print("Chon sai chuc nang")

    choice_again = input("Ban co muon thuc hien tiep ? (y/n):")
    if choice_again == 'n':
        break


