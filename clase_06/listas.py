lista = [10, 20, 30, 40]
lenguajes = ['python', 'Java', 'PHP']
lista2 = ['texto', 1, 2.3, True, [1, 2, 3]]
vacia = []
l = list('Hola Mundo!')

print(lista)
print(lenguajes)
print(lista2)
print(vacia)
print(l)

lista[2] = 100
print(lista)


lista = [1, 2, 3, 4]
print(lista[0])
print(lista[-3])
print(lista[-1])
print(lista[-5])

lista = ['python', 'PHP', 'Java']

print('python' in lista)

for elemento in lista:
    print(elemento)


lista = [1, 2, 3, 5, 8, 13, 21]

for i in range(len(lista)):
    lista[i] = lista[i] ** 2

print(lista)

for i in []:
    print('no se imprime')

for elemento in [1, 2, [3, 4]]:
    print(elemento)

# operaciones

a = [1, 2, 3]
b = [4, 5]
print(a + b)

print(a * 2)
print(b * 3)

# slices

lista = ['a', 'b', 'c', 'd', 'e']

print(lista[1:3])
print(lista[:2])
print(lista[2:])
print(lista[:])

lista[1:3] = ['x', 'y', 'z']
print(lista)

# metodos

lista = [1, 2, 3]
lista.append(4)
print(lista)

lista = [1, 2, 3]
lista2 = [4, 5]
lista.extend(lista2)

print(lista)

lista = ['a', 'c', 'b', 'e', 'd']
lista.sort()

print(lista)

lista = [1, 2, 3, 4]
x = lista.pop(1)
y = lista.pop()

print(lista)
print(x)
print(y)

lista = [1, 2, 3, 4]
del lista[0]
print(lista)

lista = ['a', 'b', 'c']
lista.remove('b')
print(lista)

lista = [1, 2, 3, 4, 5]
del lista[1:4]
print(lista)

numeros = [1, 2, 3, 5, 8, 13, 21]

print(len(numeros))
print(max(numeros))
print(min(numeros))
print(sum(numeros))

lista = [10, 60, 20, 5, 10, 5]
c = 0

promedio = sum(lista) / len(lista)
print ('El Promedio de los elementos de la lista es {}'.format(promedio))

archivo = open('data/mbox-short.txt')
for linea in archivo:
    linea = linea.rstrip()
    if not linea.startswith('From'): continue
    palabras = linea.split()
    print(palabras[1])


# texto = input('ingrese')
# lista = texto.split(',')

lista = []
while(True):
    texto = input('ingrese elemento: ')
    if texto == 'fin': break
    lista.append(int(texto))

def medio(lista):
    return lista[1:len(lista) - 1]

print(medio(lista))