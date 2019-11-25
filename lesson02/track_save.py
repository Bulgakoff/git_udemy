import json

favourite_tracks = [dict(name='Вечная любовь', artist='Агата Кристи'),
                    dict(name='Angel', artist='Massive Attack'),
                    dict(name='Jamming', artist='Bob Marley')]
with open('tracks.json', 'w', encoding='utf-8') as f:
    json_tr = json.dump(f'{favourite_tracks}', f)
# with open('tracks.sh', 'w') as f:
print("Готова запись")
with open('tracks.txt', 'r', encoding='utf-8') as f:
    json_tr = json.load(f)
    print(json_tr)
