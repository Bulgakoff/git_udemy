class InvalidTrapezoidError(Exception):
    """Raised then trapezoid has invalid sides"""

def sqr_trapezoid(a, b, h):
    if a <= 0 or b <= 0 or h <= 0 or b == None:
        raise InvalidTrapezoidError(f'тут')

    sqr = (a + b) * h / 2
    return sqr


try:
    result = sqr_trapezoid(10, -20, 30)# кастомно создали ИС
except InvalidTrapezoidError as a:
    print(f'ошибка ввода данных -->{a}')
else:
    print(result)
