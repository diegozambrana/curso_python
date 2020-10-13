print('Ejercicio 5')

file = open('data/ejemplo.txt')
total = 0
articulos = ['el', 'la', 'los', 'las', 'en']

for linea in file:
    palabras = linea.split()
    for palabra in palabras:
        if palabra in articulos:
            total = total + 1

print(f'total de articulos: {total}')