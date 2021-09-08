import SomeModules as module
import turtle as t
import  sys
def draw_circle(t, radius, number):
    for i in range(number):
        t.circle(radius)
        t.left(360 // number)

def draw_square(t, width, number):
    for i in range(number):
        for j in range(4):
            t.forward(width)
            t.left(90)
        t.left(360 //number)

def draw_rectangle(t, width, height, number):
    for i in range(number):
        for j in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.left(360 // number)

def draw_pentagon(t, width, number):
    for i in range(number):
        for j in range(5):
            t.forward(width)
            t.right(360 // 5)
        t.left(360 // number)

def draw_equilateral_triangle(t, width, number):
    for i in range(number):
        t.forward(width)
        t.left(120)
        t.forward(width)
        t.left(120)
        t.forward(width)
        t.right(360 // number)

def draw_oval(t, number):
    for i in range(number):
        for i in range(2):
            t.circle(100, 90)
            t.circle(50, 90)
        t.right(360 // number)

def draw_heart(t, number, color):
    for i in range(4):
        draw_circle(t,50,1)
        t.circle(50,135)
        t.left(90)
        draw_circle(t, 50, 1)
        draw_square(t,100,1)

        t.left(45)
        t.forward(140)
        t.left(90)
        t.forward(100)
        t.right(90)

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
    number = int(module.nhapSo("Nhập số hình muốn vẽ"))
    color_number = module.nhapSo("Nhập màu muốn ve bằng số̃ (1.green 2.blue 3.red 4.yellow 5.purple)")
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
            color += "purple"
            break
        else:
            print("Hãy nhập trong phạm vi 1 tới 5 !")
            color_number = module.nhapSo("Nhập màu muốn ve bằng số̃ (1.green 2.blue 3.red 4.yellow 5.red)")
    return number,color

#main program
try:
    t.speed(20)
    show_menu()
    while True:
        show_menu()
        user_pick = get_pick()
        t.clear()
        if user_pick == "8":
            print("Kết thúc chương trình")
            break
        else:
            number, color = get_information()
            t.pencolor(color)
            if user_pick == "1":
                radius = int(module.nhapSo("Nhập bán kính"))
                draw_circle(t, radius, number)
            elif user_pick == "2":
                width = int(module.nhapSo("Nhập chiều dài 1 cạnh"))
                draw_square(t, width, number)
            elif user_pick == "3":
                width = int(module.nhapSo("Nhập chiều dài"))
                height = int(module.nhapSo("Nhập chiều rộng"))
                draw_rectangle(t, width, height, number)
            elif user_pick == "4":
                width = int(module.nhapSo("Nhập chiều dài 1 cạnh"))
                draw_pentagon(t, width, number)
            elif user_pick == "5":
                width = int(module.nhapSo("Nhập chiều dài 1 cạnh"))
                draw_equilateral_triangle(t, width, number)
            elif user_pick == "6":
                draw_oval(t, number)
            elif user_pick == "7":
                draw_heart(t, number, color)
except:
    print("Bạn đã đóng cửa sổ vẽ con rùa =.= ")
    sys.exit()
