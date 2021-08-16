import turtle
import PartOfHouse as p

t = turtle.Turtle()
corner = 90
# for background
screen = turtle.Screen()
screen.bgcolor("yellow")

#color and speed
# of turtle
# creating the house
t.color("black")
t.speed(10)

# for creating base of
# the house
t.fillcolor('cyan')
t.begin_fill()
p.part1(t,corner)
t.end_fill()

# for top of
# the house
t.fillcolor('brown')
t.begin_fill()
p.part2(t, corner)
t.end_fill()

# for door and
# windows
t.right(corner)
t.forward(400)
t.left(corner)
t.forward(50)
t.left(corner)
t.forward(150)
t.right(corner)
t.forward(200)
t.right(180)
t.forward(200)
p.part3(t,corner)

t.right(corner)
t.forward(100)
t.right(corner)
t.forward(150)
t.right(corner)
t.forward(100)
t.right(corner)
t.forward(75)
t.right(corner)
t.forward(200)
t.right(180)
t.forward(200)
p.part4(t,corner)

turtle.done()