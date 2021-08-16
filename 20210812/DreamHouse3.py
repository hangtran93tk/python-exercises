import turtle
import math
corner = 90
side = 200
half_side = int(side / 2)
double_side = side * 2
t = turtle.Turtle()
# for background
screen = turtle.Screen()
#color and speed
# of turtle
# creating the house
t.color("lightblue")
t.pensize(3)
t.speed(10)

def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(corner)
    t.forward(height)
    t.left(corner)
    t.forward(width)
    t.left(corner)
    t.forward(height)
    t.left(corner)
    t.end_fill()

def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(corner)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()

# for creating base of
# the house
t.right(corner)
t.forward(250)
t.left(corner)
t.forward(double_side)
t.left(corner)
t.forward(250)
t.left(corner)
t.forward(double_side)
t.right(corner)

# for top of
# the house
t.right(45)
t.forward(side)
t.right(corner)
t.forward(side)
t.left(180)
t.forward(70)
t.right(45)
t.forward(70)
t.left(90)
t.forward(20)
t.left(90)
t.forward(50)

t.penup()
t.goto(230,200)
t.pendown()
t.forward(60)

t.penup()
t.goto(210,180)
t.pendown()
t.forward(30)

t.penup()
t.goto(150,-100)
t.pendown()
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)


# Tree base
t.penup()
t.goto(-100, -260)
t.pendown()
drawRectangle(t, 20, 40, "gray")

# Tree top
t.color("lightgreen")
t.penup()
t.goto(-165, -260)
t.pendown()
t.left(180)
drawTriangle(t, 110, "darkgreen")
t.penup()
t.goto(-150, -205)
t.pendown()
drawTriangle(t, 80, "green")
t.penup()
t.goto(-145, -165)
t.pendown()
drawTriangle(t, 70, "lightgreen")

# Tree base
t.penup()
t.goto(500, -360)
t.pendown()
drawRectangle(t, 40,60, "gray")

# Tree top
t.color("lightgreen")
t.penup()
t.goto(423, -300)
t.pendown()
drawTriangle(t, 200, "darkgreen")
t.penup()
t.goto(450, -200)
t.pendown()
drawTriangle(t, 140, "green")
t.penup()
t.goto(470, -130)
t.pendown()
drawTriangle(t, 100, "lightgreen")

turtle.done()