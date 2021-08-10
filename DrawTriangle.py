import turtle
import  turtle as pen

pen.color("blue")

size = 100
double_size = size * 2
corner = 90

pen.left(90)

for i in range(5):
    pen.forward(size)
    pen.right(corner)
    for j in range(3):
        pen.forward(double_size)
        pen.right(corner)
    pen.forward(size)
    pen.right(72)

turtle.done()

