# Ejercicio 2

archivo = open('data/mbox-short.txt')
d = dict()

for linea in archivo:
    linea = linea.rstrip()
    palabras = linea.split()
    if (linea.startswith('From ')):
        d[palabras[2]] = d.get(palabras[2], 0) + 1

print(d)


# 
d = {'d': 1, 'b': 2, 'c': 3, 'a': 1,}

for llave in d:
    print(llave, d[llave])

print('------ ')
llaves = list(d.keys())
llaves.sort()

for llave in llaves:
    print(llave, d[llave])


import string
archivo = open('data/cuento.txt')
d = dict()
print(string.punctuation)

for linea in archivo:
    linea = linea.rstrip()
    linea = linea.lower()
    linea = linea.replace('—', '')
    linea = linea.translate(linea.maketrans('', '', string.punctuation))
    palabras = linea.split()
    for palabra in palabras:
        d[palabra] = d.get(palabra, 0) + 1

print(d)

# Ejercicio 5
archivo = open('data/mbox-short.txt')
d = dict()

for linea in archivo:
    linea = linea.rstrip()
    palabras = linea.split()
    if (linea.startswith('From ')):
        correo = palabras[1]
        dominio = correo[correo.find('@') + 1:]
        d[dominio] = d.get(dominio, 0) + 1

print(d)


maxLlave = max(d, key=d.get)
minLlave = min(d, key=d.get)

print(f'Dominio que mas emails envia: {maxLlave}')
print(f'Dominio que menos emails envia: {minLlave}')