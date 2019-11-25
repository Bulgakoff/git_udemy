import json

# ПРЕВОД СЛОЖНОГО ОБЪЕКТА В СТРОКУ
friends = [dict(name='Max', age=23, phone=[123, 654]), dict(name='Leo', age=33)]
# смтрим тип объекта
print(friends)
print(type(friends))  # <class 'list'>
# щткрываем файл
with open('friends.jon', 'w') as f:
    json_friends = json.dump(friends, f)
    print(f'{json_friends}//////////////////')
    print(type(json_friends))
with open('friends.jon', 'r') as f:
    json_friends = json.load(f)
    print(json_friends)
    print(type(json_friends))
