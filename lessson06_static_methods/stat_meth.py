class Static_test:
    x = 1


t1 = Static_test()

print(f'from instance class  {t1.x}')
print(f'from Static_test class {Static_test.x}')

t1.x = 3
print(f'from instance class  {t1.x}')
print(f'from Static_test class {Static_test.x}')
t1.x = 4
print(f'from instance class  {t1.x}')
print(f'from Static_test class {Static_test.x}')

Static_test.x = 10
print(f'from instance class  {t1.x}')
print(f'from Static_test class {Static_test.x}')


class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return f'{self.month} -- {self.day} --{self.year}'

    @classmethod
    def millenium_c(cls, month, day):# cls - вызывет конструктор def __init__(self, month, day, year):
        return cls(month, day, 2000)# решает вопрос разных конструкторов

    @staticmethod
    def millenium_s(mo, da):
        return Date(mo, da, 5000)

#,,,\\\\\\\\\\\\\\\\\\\\\\\\rликлиент
#,,,\\\\\\\\\\\\\\\\\\\\\\\\rликлиент
#,,,\\\\\\\\\\\\\\\\\\\\\\\\rликлиент

print()
print(type(Date.millenium_c(6, 9)))
d1 = Date.millenium_c(6, 9)
print(type(d1))
print(f'--->{d1.millenium_c(6, 9)}')
d2 = Date.millenium_s(6, 9)

print(d1.display())
print(d2.display())
class DataTime(Date): #унаследовались
    def display(self):
        return f'{self.month} -- {self.day} --{self.year} 00:00:00 PM'

dt1 = DataTime(10,2,1111)
dt2 = DataTime.millenium_s(20,20)
print(isinstance(dt1,DataTime))
print(f'------------------на прямую --------------------->{dt1.display()}')
print(isinstance(dt2,DataTime))
print(f'==========================================>{dt1.display()}')