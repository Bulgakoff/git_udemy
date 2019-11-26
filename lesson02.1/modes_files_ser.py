person = dict(name='Eva', phones=[444444, 888], dms=[555, 222, 7777])

with open('ph3.txt', 'wb') as f:
    # заносим каждый ключ
    nam = person['name']  # туттуттуттуттуттуттут
    f.write(f'{nam}\n'.encode('utf-8'))
    ph = person['phones']  # туттуттуттуттуттуттут
    for p in ph:
        f.write(f'{p}\n'.encode('utf-8'))
    med = person['dms']  # туттуттуттуттуттуттут
    for m in med:
        f.write(f'{m}\n'.encode('utf-8'))
print('all right сериализовали')
# /////////////// добавление новых записей 'a'
with open('ph3.txt', 'ab') as f:
    f.write('give me many manager, все'.encode('utf-8'))
    print('добавили запись сериализовали')
# /////////////// и чтение и добавление  записей 'r+'
with open('ph3.txt', 'r+', encoding='utf-8') as f:
    # вначале ставим курсор в конец дока
    f.seek(0, 2)
    f.write('\nчто то - 5555')
    f.seek(0)
    r = f.read()

    print(f'----r+-->\n{r}')

# /////////////// переазпись существующего и создание новго  записей 'w+'
with open('phNew.txt', 'w+', encoding='utf-8') as f:
    f.write('new info- по русски')
    f.seek(0)  # что бы прочитать весь докум ставим курсор на начало дока
    read_result = f.read()
    print(read_result)
