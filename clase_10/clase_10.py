file1 = open('data/primer.txt')
file2 = open('data/segundo.txt')

res1 = list()
res2 = list()

for linea in file1:
    palabras1 = linea.split()
    res1 = res1 + palabras1
for linea in file2:
    palabras2 = linea.split()
    res2 = res2 + palabras2

print('las palabras en comun son: {}'.format(set(res1) & set(res2)))
print('palabras que existen en el primer archivo: {}'.format(set(res1) - set(res2)))
print('palabtas que existen solo en el segundo archivo: {}'.format(set(res2) - set(res1)))


# TUPLA

tupla = (1, 2, 3, 4, 5, 6)
tupla2 = 1, 2, 3, 4, 5, 6
tupla3 = tuple([1, 2, 3])
tupla4 = (1, )
tupla5 = tuple('hola')

print(type(tupla))
print(tupla)
print(tupla2)
print(tupla3)
print(tupla4)
print(tupla5)
#print(tupla[10])
print(tupla[2:4])

# tupla[0] = 3
tupla = (3, ) + tupla[1:]
print(tupla)

a = 1
b = 2

# aux = a
# a = b
# b = aux


a, b = b, a
print(a)
print(b)

lista = ['a', 'b', True, {1, 2, 3, 4}]
a, b, c, d = lista
print(a)
print(b)
print(c)
print(d)

# a, b = (1, )

usuario, dominio = "Juan@gmail.com".split('@')
print(usuario)
print(dominio)


d = {'c': 0, 'a': 1, 'b': 2}
t = list(d.items())
t.sort()
print(t)

for llave, valor in list(d.items()):
    print(llave, valor)


lista = ['a', 'b', 'c']

for index, valor in enumerate(lista):
    print(index, valor)

d = {'a': 10, 'b': 9, 'c': 7}
l = list()

for llave, valor in list(d.items()):
    l.append( (valor, llave) )

print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)


# Ejercicio: Tupla

import string
archivo = open('data/cuento.txt')
diccionario = dict()

for linea in archivo:
    linea = linea.translate(str.maketrans('', '', string.punctuation))
    linea = linea.lower()
    linea = linea.replace('—', '').replace('¡', '').replace('¿', '')
    linea = linea.translate(str.maketrans('áéíóú', 'aeiou'))
    palabras = linea.split()
    for palabra in palabras:
        diccionario[palabra] = diccionario.get(palabra, 0) + 1

print(diccionario)

lista = list()

for llave, valor in list(diccionario.items()):
    lista.append((valor, llave))

lista.sort(reverse=True)

for valor, llave in lista[:10]:
    print(llave, valor)


# Ejercicio

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

print(list(enumerate(lista2)))

for index, val in enumerate(lista1):
    if index % 2 != 0:
        lista1[index], lista2[index] = lista2[index], lista1[index]

print(lista1)
print(lista2)

# Ejercicio:

texto1 = input('texto1: ')
texto2 = input('texto2: ')

lista1 = texto1.split()
lista2 = texto2.split()

for index, val in enumerate(lista1 if len(lista2) > len(lista1) else lista2):
    if index % 2 != 0:
        lista1[index], lista2[index] = lista2[index], lista1[index]

print(" ".join(lista1))
print(" ".join(lista2))