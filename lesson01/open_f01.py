# dic = dict(, , )
s1 = 'john=1234 '
s2 = 'Bob=5678 '
s3 = ' Alise=9432'

with open('sample.txt', 'w') as f:
    f.write(s1)
    f.write(s2)
    f.write(s3)

with open('sample.txt', 'r', encoding='cp1251') as f:
    data = f.read()
    print(type(data))
    print(data)
    f.seek(2)  # 2 эт с какого  байта идет курсор read()
    print(f.read())
    f.seek(0)
    lines = f.readlines()
    print(lines)  # ['john=1234 Bob=5678  Alise=9432']
    print(type(lines))
