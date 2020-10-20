
# Ejercicio 1

archivo = open('data/mbox-short.txt')
d = dict()

for linea in archivo:
    linea = linea.rstrip()
    palabras = linea.split()
    if (linea.startswith('From ')):
        correo = palabras[1]
        d[correo] = d.get(correo, 0) + 1

lista = list()

for correo, valor in list(d.items()):
    lista.append( (valor, correo) )

lista.sort(reverse=True)

for valor, correo in lista:
    print(correo, valor)


# Ejercicio 2

archivo = open('data/mbox-short.txt')
d = dict()

for linea in archivo:
    linea = linea.rstrip()
    palabras = linea.split()
    if (linea.startswith('From ')):
        hora = palabras[5].split(':')[0]
        d[hora] = d.get(hora, 0) + 1

print(d)

lista = list()

for hora, valor in list(d.items()):
    lista.append( (valor, hora) )

lista.sort(reverse=True)

for valor, hora in lista:
    print(hora, valor)


# Ejercicio 3

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
  
# Programación Funcional

def sumar_uno(x):
    return x + 1

print(sumar_uno(1))
print((lambda x: x + 1)(1))

sumar_uno_func = lambda x: x + 1

print(sumar_uno_func(2))

sumar = lambda x, y: x + y
print(sumar(1, 3))

def foo(f, x, y):
    return f(x, y)

print(foo(sumar, 10, 50))
print(foo(lambda x, y: x ** y, 10, 3))

def funcionPadre(x):
    def funcionHijo(y):
        return y + 1 + x
    return funcionHijo(x*10)

print(funcionPadre(3))

# Funciones Filter, Map, Reduce

lista = [
    {"nombre": "Juan", "apellido": "Perez", "ci": "786432134", "departamento": "Cochabamba", 'edad': 20},
    {"nombre": "Pedro", "apellido": "Ramirez", "ci": "986232134", "departamento": "Cochabamba", 'edad': 26},
    {"nombre": "Marco", "apellido": "Zurita", "ci": "686452134", "departamento": "Oruro", 'edad': 30},
    {"nombre": "Lucas", "apellido": "Mendez", "ci": "586462134", "departamento": "Oruro", 'edad': 30},
    {"nombre": "Mateo", "apellido": "Ballarta", "ci": "487432134", "departamento": "La Paz", 'edad': 45},
]

# filter
print(list(filter(lambda d: d['departamento'] == "Oruro", lista)))

# Map
numeros = list(range(1, 11))
print(numeros)
print(list(map(lambda x: x ** 2, numeros)))

from functools import reduce
# Reduce
print(reduce(lambda res, x: res + ' - ' + x['nombre'] if res != '' else x['nombre'], lista, ''))


# Ejercicio 2

def actualizar_persona(d):
    d['email'] = f"{d['nombre'].lower()}.{d['apellido'].lower()}.{d['ci'][:3]}@gmail.com"
    return d

nueva_lista = list(map(actualizar_persona, lista))
print(nueva_lista)