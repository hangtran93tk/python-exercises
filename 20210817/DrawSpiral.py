import turtle
import  turtle as t
num = int(input("Nhập vào khoảng cách tùy ý (Bội của 10) : "))
size = 10
corner1 = 180

while True:
    if size <= num:
        t.circle(size, corner1)
        size += 10
    else:
        break

turtle.done()