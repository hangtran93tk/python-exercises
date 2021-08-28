import turtle
import turtle as t

def setup_turtle(size, color):
    t.shapesize(size)
    t.color(color)

def draw_rectangle(t):
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(200)
        t.left(90)

def draw_color_rectangle(t, colorName):
    t.begin_fill()
    t.fillcolor(colorName)
    draw_rectangle(t)
    t.end_fill()

setup_turtle(3, "aqua")
draw_rectangle(t)

draw_color_rectangle(t,"green")
turtle.done()
