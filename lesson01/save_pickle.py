
import pickle

person = dict(name='Eva', phones=[5648992, 56489001], dms=[123, 89, 234], age = 20)
# открываем объект на запись в виде байт ----->'wb'
with open('ph2.txt', 'wb') as f:
    pickle.dump(person,f)
print('объект записан')