# Ejercicio 1
lista = [1, 2, 3, 4, 5, 6, 7, 8]

def impares(lista):
    res = []
    for elemento in lista:
        if elemento % 2 != 0:
            res.append(elemento)
    return res

print(f"resultado: {impares(lista)}")
print(f"resultado2: {impares(list(range(1, 100, 7)))}")

# Ejercicio 2
texto = "Esto es un texto largo farmacia. banana"

for palabra in texto.split():
    if len(palabra) >= 5 and len(palabra) % 2 != 0:
        print(palabra)

# ejercicio 3
import math

lista = [4, 9, 16, 25, 30]

for i in range(len(lista)):
    lista[i] = math.sqrt(lista[i])

print(lista)

# Listas

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print(lista1 == lista2)

texto = 'hola mundo'
texto2 = 'hola mundo'
print(texto is texto2)



lista1 = [1, 2, 3]
lista2 = lista1
lista3 = lista1[:]

print(lista1 is lista2)

lista1[0] = 100
lista2[1] = 300

print(lista1)
print(lista2)
print(lista3)


lista = [1, 2, 3, 4, 5]

def tail(lista):
    return lista[1:]

_tail = tail(lista)

print(lista)
print(_tail)

# Ejercicio 5

numeros = [1, 2, 2, 3, 4, 35]

def esta_ordenada(lista):
    lista_ordenada = lista[:]
    lista_ordenada.sort()
    return lista == lista_ordenada

print(esta_ordenada(numeros))
print(numeros)

