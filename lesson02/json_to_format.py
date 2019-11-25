import json

# ПРЕВОД СЛОЖНОГО ОБЪЕКТА В СТРОКУ
friends = [dict(name='Max', age=23, phone=[123, 654]), dict(name='Leo', age=33)]
# смтрим тип объекта
print(friends)
print(type(friends))  # <class 'list'>
# упреобразуем --->dumps список друзей в json формат
json_friends = json.dumps(friends)

print(json_friends)
# проверим тип
print(type(json_friends))  # <class 'str'>
# ОБРАТНО В СЛОЖНЫЙ ОБЪЕКТ
friends = json.loads(json_friends)
print(friends)
print(type(friends))
