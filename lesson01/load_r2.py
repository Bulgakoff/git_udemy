with open('ph2.txt', 'rb') as f:
    result_list = f.readlines()
    print(result_list)
    print(type(result_list))
#     теперь надо возсоздать объект и надо точно вспомнить порядок записи элементов!!!
pers = dict()  # пустой!!
# далее записываем в него первый элемент---> name
pers['namee'] = result_list[0].decode('utf-8').replace('\n', '')
# далее записываем в него второй элемент---> номера numbers
phones = []
for res in result_list[1:3]:
    phones.append(res.decode('utf-8').replace('\n', ''))
pers['phoneeee'] = phones
# далее записываем в него (в pers = dict()) третий элемент---> номера ДМС dms
dms = []
for med in result_list[3:]:
    dms.append(med.decode('utf-8').replace('\n', ''))
pers['dmssssss'] = dms
print(pers)

print('all read')
