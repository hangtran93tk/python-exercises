class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def get_perimater(self):
        return ((self.width + self.height) * 2 )

    def draw_rectangle(self, pen):
        for i in range (2):
            pen.forward(self.width)
            pen.left(90)
            pen.forward(self.height)
            pen.left(90)
        pen.done()
