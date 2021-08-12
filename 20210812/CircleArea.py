#20210812
import turtle
import math

r = int(input("Enter the radius: "))

t = turtle.Turtle()
t.hideturtle()
t.pensize(1)
t.color("red")
t.circle(r)
turtle.done()

c = 2 * math.pi * r
s = math.pi * r * r

print("Chu vi của hình tròn có bán kính = {} là {:.2f}".format(r, c))
print("Diện tích của hình tròn có bán kính = {} là {:.2f}".format(r, s))