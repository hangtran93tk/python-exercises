import turtle
import PartOfHouse as p

t = turtle.Turtle()

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
p.part1(t)
t.end_fill()

# for top of
# the house
t.fillcolor('brown')
t.begin_fill()
p.part2(t)
t.end_fill()

# for door and
# windows
t.right(90)
t.forward(400)

t.left(90)
t.forward(50)

t.left(90)
t.forward(150)

t.right(90)
t.forward(200)

t.right(180)
t.forward(200)
p.part3(t)

t.right(90)
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(75)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)
p.part4(t)

turtle.done()