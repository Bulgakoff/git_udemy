class Shape:

    def __init__(self):
        print('Shape created in Shape')

    def draw(self):
        print('Deawing the shape  in Shape')

    def area(self):
        print('calc area  in Shape')

    def perimetr(self):
        print('calc perimetr  in Shape')


class Rectangle(Shape):
    def __init__(self, width, height):
        Shape.__init__(self)  # вызывается конструктор базового и передаем туда себя
        self.width = width
        self.height = height
        print('rectagle draw in Rectangle')
        # Shape.area(self)  # леголеголеголеголеголеголего для преопределения вызываю area передаю туда себя
        # Shape.perimetr(self) #вызов из конструкотора
        # Shape.draw(self) #вызов из конструкотора

    def area(self):  # переорпределяем метод
        return self.width * self.height

    def perimetr(self):
        return 2 * (self.width + self.height)

    def draw(self):
        print(f'Drawing rectangle with width =  {self.width} and higth = {self.height} in Rectangle')


import math


class Triangle(Shape):
    def __init__(self, a, b, c):
        Shape.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        print('Triangle craeted in Triangle')

    def draw(self):
        print(f'Drawing triangle in sides= {self.a}, {self.b}, {self.c}')

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimetr(self):
        p = self.a + self.b + self.c
        return p

    @classmethod
    def draw_next(cls, aa, bb, cc):
        return cls(aa, bb, cc)



tri = Triangle(2, 6, 10)
print(f'-------perimetr--------> {tri.perimetr()}')
tri.draw()
print('# /////////////////////////////////////')
tri1 = Triangle.draw_next(11, 22, 33)
tri1.draw()
print('# /////////////////////////////////////')
sh = Shape()
rect = Rectangle(12, 10)
rect.draw()
print(f'----------rect---area---===========>{rect.area()} sm')
print(f'-----------rect---perimetr--===========>{rect.perimetr()} sm')
print('# //////////////////так работает полиморфизм ///////////////////')
for sha in [rect, tri, tri1, sh]:
    sha.draw()
