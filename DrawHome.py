import turtle
import math

screen = turtle.Screen()
screen.bgcolor("skyblue")

george = turtle.Turtle()
george.color("black")

def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()

def drawParallelogram(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.left(30)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(120)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(90)
    t.end_fill()

def drawFourRays(t, length, radius):
    for i in range(4):
        t.penup()
        t.forward(radius)
        t.pendown()
        t.forward(length)
        t.penup()
        t.backward(length + radius)
        t.left(90)


# Draw and fill the front of the house
george.penup()
george.goto(-150, -120)
george.pendown()
drawRectangle(george, 100, 110, "blue")

# Draw and fill the front door
george.penup()
george.goto(-120, -120)
george.pendown()
drawRectangle(george, 40, 60, "lightgreen")

# Front roof
george.penup()
george.goto(-150, -10)
george.pendown()
drawTriangle(george, 100, "magenta")

# Side of the house
george.penup()
george.goto(-50, -120)
george.pendown()
drawParallelogram(george, 60, 110, "yellow")

# Window
george.penup()
george.goto(-30, -60)
george.pendown()
drawParallelogram(george, 20, 30, "brown")

# Side roof
george.penup()
george.goto(-50, -10)
george.pendown()
george.fillcolor("orange")
george.begin_fill()
george.left(30)
george.forward(60)
george.left(105)
george.forward(100 / math.sqrt(2))
george.left(75)
george.forward(60)
george.left(105)
george.forward(100 / math.sqrt(2))
george.left(45)
george.end_fill()

# Tree base
george.penup()
george.goto(100, -130)
george.pendown()
drawRectangle(george, 20, 40, "brown")

# Tree top
george.penup()
george.goto(65, -90)
george.pendown()
drawTriangle(george, 90, "lightgreen")
george.penup()
george.goto(70, -45)
george.pendown()
drawTriangle(george, 80, "lightgreen")
george.penup()
george.goto(75, -5)
george.pendown()
drawTriangle(george, 70, "lightgreen")

# Sun
george.penup()
george.goto(55, 110)
george.fillcolor("yellow")
george.pendown()
george.begin_fill()
george.circle(24)
george.end_fill()

# Sun rays
george.penup()
george.goto(55, 134)
george.pendown()
drawFourRays(george, 25, 24)
george.right(45)
drawFourRays(george, 15, 24)
george.left(45)

george.penup()
george.goto(-100, -150)
george.left(90)

turtle.done()