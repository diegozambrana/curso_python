# Ejercicio 4

texto = "hola como estas mundo palabra"
lista = texto.split()

lista_cantidad_caracteres = list(map(lambda s: len(s), filter(lambda s: len(s) >= 5, lista)))
print('el promedio es', sum(lista_cantidad_caracteres)/len(lista_cantidad_caracteres))


#5.- Dada una lista de numeros devolver la suma de todos los nuemeros que sean multiplos de un valor N dado
from functools import reduce

n = int(input('ingrese el numero N'))
lista = list(range(1, 51))
lista2 = (list(filter(lambda x: x % n == 0, lista)))

print(lista2)
print(reduce(lambda res, x: res + x, lista2, 0)/len(lista2))

# ejercicio 6
n = [1, 2, 9, 10]

for index, val in enumerate(n):
    if index % 2 != 0:
        n[index] = n[index] ** 2
    else:
        n[index] = n[index] ** (1/2)

print(n)

#Ejercicio 6
lista = [1, 2, 9, 10]  # list(range(1,11))
print(lista)
print(list(map(lambda x: x**2 if x % 2 == 0 else x**(1/2), lista)))

# Regular expresion
import re

texto = "hola mundo, mundo mundo"
match = re.match('mundo', texto)
print(match)

match2 = re.search('mundo', texto)
print(match2)

lista = re.findall('mundo', texto)
print(lista)


import re

archivo = open('data/mbox-short.txt')
#Sat, 05 Jan 2008 09:14:16
regex = '([\w]{3}),\s[\d]{2}\s[\w]{3}\s[\d]{4}\s(\d{2}:\d{2}:\d{2})'

for linea in archivo:
    linea = linea.rstrip()
    match = re.search(regex, linea)
    if match is not None:
        print(match.group())
        print(match.group(1))
        print(match.group(2))