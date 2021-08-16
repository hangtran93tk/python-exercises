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
turtle.done()

