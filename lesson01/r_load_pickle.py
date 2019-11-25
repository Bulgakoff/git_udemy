import pickle

with open('ph2.txt', 'rb') as f:
    # читаем объект из файла сразу с помощью pickle
    result = pickle.load(f)
print(result)