# Выведите все элементы, которые меньше 5.
a = [3, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def out_p(aa):
    new = []
    for p in a:
        if p < 5:
            new.append(p)
    print(new)


out_p(a)
print('/////////////Задача 2////////////////////////')
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
a = [1, 1, 2, 3, 5, 555, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 555, 7, 8, 9, 10, 11, 12, 13]


def new_list(aa, bb):
    return [p for p in a if p in b]


c = new_list(a, b)
print(c)
# ///////////////map////////////////

a = [1, 1, 2, 3, 5, 555, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 555, 7, 8, 9, 10, 11, 12, 13]
c = list(map(lambda aa: aa in a, b))
print(c)
print('/////////////filter(....)///////////////////////')
c = list(filter(lambda p: p in a, b))
print(f'++++++++>>>>>>>{c}')
print('/////////////классика ///////////////////////')
ff = []
for qwe in a:
    if qwe in b:
        ff.append(qwe)
print(f'.....>>>>>...>>{ff}')
print('/////////////set()///////////////////////')

c = list(set(b) & set(a))
d = list(set(a).intersection(set(b)))
print(c)
print(d)
print('/////////////Задача 3///////////////////////')
# Отсортируйте словарь по значению в порядке возрастания и убывания.
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
my_dict1 = sorted(my_dict.values())
print(my_dict1)
my_dict1 = reversed(my_dict.values())
print(list(my_dict1))
my_dict2 = sorted(my_dict.keys())
print(f'---------key  {my_dict2}')

print('/////////////Задача 4///////////////////////')
# Напишите программу для слияния нескольких словарей в один.
y = {'ddd': 10, 'ccc': 11}
x = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
print('/////////////1///.copy().copy().copy().copy()////.update(x).update(x).update(x).update(x).update(x)')
copy_y = y.copy()  # {'b': 10, 'c': 11}
print(f'копировали y в  copy_y---------->{copy_y}')
copy_y.update(x)
print(f'модифицировали х в  copy_y---------->{copy_y}')

print('/////////////2//x.items()x.items()x.items()x.items()x.items()x.items()/////////////////////')
qwe = (list(x.items()) + list(y.items()))
print(qwe)
print(x)
print(y)

print('///////////Задача 5/////////////////////')
# Найдите три ключа с самыми высокими значениями в словаре
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
qw = list(sorted(my_dict.values())) # [20, 400, 500, 560, 5874, 5874]
qwer =qw[-3:]
qwerty = [k for k, v in my_dict.items() if v in qwer]
print(qwerty)
# result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(f'00000000-------.>{result}')
print('/////////////4///////////////////////')
