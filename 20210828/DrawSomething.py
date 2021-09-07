import SomeModules as module
import turtle as t

def draw_circle():
    radius = int(module.nhapSo("Nhập bán kính"))
    number, color = get_information()
    for i in range(number):
        t.pencolor(color)
        t.circle(radius)
        t.left(360 // number)

def draw_square():
    pass
def draw_rectangle():
    pass
def draw_pentagon():
    pass
def draw_equilateral_triangle():
    pass
def draw_oval():
    pass
def draw_heart():
    pass
def show_menu():
    print('''
Hãy chọn hình muốn vẽ:
1. Hình tròn
2. Hình vuông
3. Hình chữ nhật
4. Ngũ giác
5. Tam giác đều
6. Oval
7. Trái tim
8. Thoát chương trình
    ''')

def get_pick():
    return module.nhapSo("Lựa chọn của bạn")

def get_information():
    number = module.nhapSo("Nhập số hình muốn vẽ")
    color_number = module.nhapSo("Nhập màu muốn ve bằng số̃ (1.green 2.blue 3.red 4.yellow 5.pink)")
    color = ""
    while True:
        if color_number == "1":
            color += "green"
            break
        elif color_number == "2":
            color += "blue"
            break
        elif color_number == "3":
            color += "red"
            break
        elif color_number == "4":
            color += "yellow"
            break
        elif color_number == "5":
            color += "pink"
            break
        else:
            print("Hãy nhập trong phạm vi 1 tới 5 !")
            color_number = module.nhapSo("Nhập màu muốn ve bằng số̃ (1.green 2.blue 3.red 4.yellow 5.pink)")
    return number,color

#main program
show_menu()
while True:
    show_menu()
    user_pick = get_pick()
    print(f"Bạn đã chọn {user_pick}")
    if user_pick == "8":
        print("Kết thúc chương trình")
        break
    elif user_pick == "1":
        draw_circle()
    elif user_pick == "2":
        draw_square()
    elif user_pick == "3":
        draw_rectangle()
    elif user_pick == "4":
        draw_pentagon()
    elif user_pick == "5":
        draw_equilateral_triangle()
    elif user_pick == "6":
        draw_oval()
    elif user_pick == "7":
        draw_heart()