import  turtle as t

colors = ["pink","blue","green","yellow","orange", "red"]
turn = 0
loop = 0
t.speed(20)
while loop < 6:
    for i in range(6):
        t.color(colors[i])
        while turn < 2:
            t.circle(100,90)
            t.circle(50,90)
            turn += 1
        turn = 0
        t.right(10)
    loop += 1

t.done()