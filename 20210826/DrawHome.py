import turtle
import turtle as t

def setup_turtle(size, color):
    t.shapesize(size)
    t.color(color)

def draw_rectangle(t, colorName, corner, width, height):
    t.begin_fill()
    t.fillcolor(colorName)
    for i in range(2):
        t.forward(width)
        t.left(corner)
        t.forward(height)
        t.left(corner)
    t.end_fill()

setup_turtle(3, "aqua")
draw_rectangle(t,"green", 90, 200, 100)
turtle.done()
