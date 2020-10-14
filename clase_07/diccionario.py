dic = {'a': 1, 'b': 'esto es texto', 'c': True}

print(dic['a'])
print(dic['b'])
print(len(dic))
print('d' in dic)
print(list(dic.values()))
print(list(dic.keys()))

file = open('data/ejemplo.txt')
dic = dict()

for linea in file:
    palabras = linea.split()
    for palabra in palabras:
        if palabra in dic:
            dic[palabra] = dic[palabra] + 1
        else:
            dic[palabra] = 1
        # dic[palabra] = dic.get(palabra, 0) + 1

print(dic)