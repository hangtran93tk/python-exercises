import turtle
import math
corner = 90
side = 200
half_side = int(side / 2)
double_side = side * 2
t = turtle.Turtle()
# for background
screen = turtle.Screen()
screen.bgcolor("yellow")

#color and speed
# of turtle
# creating the house
t.color("black")
t.shape("turtle")
t.speed(10)

# for creating base of
# the house
t.fillcolor('cyan')
t.begin_fill()
t.right(corner)
t.forward(250)
t.left(corner)
t.forward(double_side)
t.left(corner)
t.forward(250)
t.left(corner)
t.forward(double_side)
t.right(corner)
t.end_fill()

# for top of
# the house
t.fillcolor('brown')
t.begin_fill()
t.right(45)
t.forward(side)
t.right(corner)
t.forward(side)
t.left(180)
t.forward(side)
t.right(135)
t.forward(259)
t.right(corner)
t.forward(142)
t.end_fill()

# for door and
# windows
t.right(corner)
t.forward(double_side)
t.left(corner)
t.forward(50)
t.left(corner)
t.forward(150)
t.right(corner)
t.forward(side)
t.right(180)
t.forward(side)
t.right(corner)
t.forward(side)
t.right(corner)
t.forward(150)
t.right(corner)
t.forward(side)
t.right(corner)
t.forward(150)
t.right(corner)
t.forward(half_side)
t.right(corner)
t.forward(150)
t.right(corner)
t.forward(half_side)
t.right(corner)
t.forward(75)
t.right(corner)
t.forward(side)
t.right(180)
t.forward(side)
t.right(corner)
t.forward(75)
t.left(corner)
t.forward(15)
t.left(corner)
t.forward(side)
t.right(corner)
t.forward(15)
t.right(corner)
t.forward(75)

turtle.done()