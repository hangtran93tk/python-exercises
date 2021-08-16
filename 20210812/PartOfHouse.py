def part1(t,corner) :
    t.right(corner)
    t.forward(250)
    t.left(corner)
    t.forward(400)
    t.left(corner)
    t.forward(250)
    t.left(corner)
    t.forward(400)
    t.right(corner)

def part2(t,corner):
    t.right(45)
    t.forward(200)
    t.right(corner)
    t.forward(200)
    t.left(180)
    t.forward(200)
    t.right(135)
    t.forward(259)
    t.right(corner)
    t.forward(142)

def part3(t,corner):
    for i in range(2):
        t.right(corner)
        t.forward(200)
        t.right(corner)
        t.forward(150)

def part4(t,corner):
    t.right(corner)
    t.forward(75)
    t.left(corner)
    t.forward(15)
    t.left(corner)
    t.forward(200)
    t.right(corner)
    t.forward(15)
    t.right(corner)
    t.forward(75)