import turtle
t = turtle.Turtle()
canh = 100
goc = 90
t.fillcolor("green")
t.begin_fill()
for i in range(4):
    t.right(goc)
    t.forward(canh)
t.end_fill()
t.speed(10)

t.left(goc)
t.fd(canh/2)
t.left(goc)
t.forward(canh)
t.left(goc)
t.fd(canh/2)

t.fillcolor("red")
t.begin_fill()
t.rt(-goc)
t.fd(canh/4)
t.left(goc)
t.backward(canh)
t.end_fill()

t.fillcolor("orange")
t.begin_fill()
t.rt(goc)
t.fd(canh/4)
t.left(goc)
t.fd(canh)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
t.rt(goc)
t.fd(canh/4)
t.left(goc)
t.backward(canh)
t.end_fill()

t.fillcolor("orange")
t.begin_fill()
t.rt(goc)
t.fd(canh/4)
t.left(goc)
t.fd(canh)
t.end_fill()

t.left(goc)
t.fd(10)
t.right(goc)
t.fd(40)
t.left(90)
t.fd(80)
t.left(90)
t.fd(40)