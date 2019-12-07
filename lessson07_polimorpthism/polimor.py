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


# /////////////////////////////////////
sh = Shape()

