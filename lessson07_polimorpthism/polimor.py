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
        Shape.__init__(self)# вызывается конструктор базового и передаем туда себя
        self.width = width
        self.height = height
        print('rectagle draw')
        # Shape.area(self)  # леголеголеголеголеголеголего для преопределения вызываю area передаю туда себя
        # Shape.perimetr(self) #вызов из конструкотора
        # Shape.draw(self) #вызов из конструкотора

    def area(self):  # переорпределяем метод
        return self.width * self.height

    def perimetr(self):
        return 2 * (self.width + self.height)

    def draw(self):
        print(f'Drawing rectangle with width =  {self.width} and higth = {self.height}')


# /////////////////////////////////////
sh = Shape()
rect = Rectangle(12, 10)
print(rect.draw())
print(f'-------------area---===========>{rect.area()} sm')
print(f'--------------perimetr--===========>{rect.perimetr()} sm')