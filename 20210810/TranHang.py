import turtle
import  turtle as pen

#Tran Thu Hang
for i in range(2):
    pen.fillcolor("purple")
    pen.begin_fill()
    pen.forward(150)
    pen.right(90)
    pen.forward(180)
    pen.right(90)
    pen.end_fill()

pen.fillcolor("purple")
pen.begin_fill()
pen.left(240)
pen.forward(60)
pen.left(30)
pen.forward(145)
pen.left(120)
pen.forward(35)
pen.end_fill()

pen.right(30)
pen.forward(150)
pen.right(120)
pen.forward(25)
pen.right(60)
pen.forward(175)

pen.penup()
pen.goto(360,0)
pen.pendown()

#Thanh Nguyen
pen.pensize(3)
pen.pencolor("red")
pen.circle(100)
pen.penup()
pen.pencolor("blue")
pen.goto(360,-32)
pen.pendown()
pen.circle(70)

pen.penup()
pen.goto(-180,0)
pen.pendown()

#LongVu
canh = 100
goc = 90
pen.fillcolor("green")
pen.begin_fill()
for i in range(4):
    pen.right(goc)
    pen.forward(canh)
pen.end_fill()
pen.speed(10)

pen.left(goc)
pen.fd(canh/2)
pen.left(goc)
pen.forward(canh)
pen.left(goc)
pen.fd(canh/2)

pen.fillcolor("red")
pen.begin_fill()
pen.rt(-goc)
pen.fd(canh/4)
pen.left(goc)
pen.backward(canh)
pen.end_fill()

pen.fillcolor("orange")
pen.begin_fill()
pen.rt(goc)
pen.fd(canh/4)
pen.left(goc)
pen.fd(canh)
pen.end_fill()

pen.fillcolor("red")
pen.begin_fill()
pen.rt(goc)
pen.fd(canh/4)
pen.left(goc)
pen.backward(canh)
pen.end_fill()

pen.fillcolor("orange")
pen.begin_fill()
pen.rt(goc)
pen.fd(canh/4)
pen.left(goc)
pen.fd(canh)
pen.end_fill()

pen.left(goc)
pen.fd(10)
pen.right(goc)
pen.fd(40)
pen.left(90)
pen.fd(80)
pen.left(90)
pen.fd(40)

pen.penup()
pen.goto(-180,-180)
pen.pendown()

#Tran Duy Luan
pen.circle(100)

pen.penup()
pen.goto(-320,-180)
pen.pendown()
pen.dot(20)

pen.penup()
# pen.goto(-70,160)
pen.goto(-360,-160)
pen.pendown()
pen.goto(-310,-150)

pen.penup()
# pen.goto(50,140)
pen.goto(-240,-180)
pen.pendown()
pen.dot(20)

pen.penup()
pen.goto(-250,-150)
pen.pendown()
pen.goto(-200,-160)

pen.penup()
pen.goto(-290,-220)
pen.pendown()
pen.dot(5)

pen.penup()
pen.goto(-260,-220)
pen.pendown()
pen.dot(5)

pen.penup()
pen.goto(-320,-250)
pen.pendown()
pen.goto(-240,-250)

turtle.done()