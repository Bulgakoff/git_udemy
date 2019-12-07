class Shape:

    def __init__(self):
        print('Shape created')

    def draw(self):
        print('Deawing the shape')

    def area(self):
        print('calc area')

    def perimetr(self):
        print('calc perimetr')


class Rectangle(Shape):
    def __init__(self, width, height):
        Shape.__init__(self)
        self.width = width
        self.height = height
        print('rectagle draw')
        Shape.area(self)  # леголеголеголеголеголеголего

    def area(self):  # переорпределяем метод
        return self.width * self.height

    def perimetr(self):
        return 2 * (self.width + self.height)

    def draw(self):
        print(f'Drawing rectangle with width =  {self.width} and higth = {self.height}')


# /////////////////////////////////////
sh = Shape()
rect = Rectangle(12, 45)
print(rect.draw())