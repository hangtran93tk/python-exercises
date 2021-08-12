#20210812
import turtle

color = input("Nhập màu hoặc mã màu: ")
w = float(input("Nhập chiều dài hình chữ nhật: "))
h = float(input("Nhập chiều rộng hình chữ nhật: "))
corner = 90
t = turtle.Turtle()
t.hideturtle()

# Thiết lập màu tô
t.color(color)
t.begin_fill()

# Vẽ cạnh trên chiều dài
t.forward(w)
t.right(corner)

# Vẽ cạnh bên phải chiều rộng
t.forward(h)
t.right(corner)

# Vẽ cạnh dưới chiều dài
t.forward(w)
t.right(corner)

# Vẽ cạnh bên trái chiều rộng
t.forward(h)
t.end_fill()
turtle.done()

c = 2 * (w + h)
s = w * h

print("Chu vi của hình chữ nhật (dài = {w}, rộng = {h}) là {c}".format(w=w, h=h, c=c))
print("Diện tích của hình chữ nhật (dài = {w}, rộng = {h}) là {s}".format(w=w, h=h, s=s))