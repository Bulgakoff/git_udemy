person = dict(name='Eva', phones=[5648992, 56489001], dms=[123, 89, 234])

with open('ph2.txt', 'wb') as f:
    # заносим каждый ключ
    nam = person['name']#туттуттуттуттуттуттут
    f.write(f'{nam}\n'.encode('utf-8'))
    ph = person['phones']#туттуттуттуттуттуттут
    for p in ph:
        f.write(f'{p}\n'.encode('utf-8'))
    med = person['dms']#туттуттуттуттуттуттут
    for m in med:
        f.write(f'{m}\n'.encode('utf-8'))
print('all right')