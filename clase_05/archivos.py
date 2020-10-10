file = open('data/01_ejemplo.txt')

total = ""

for linea in file:
    linea = linea.rstrip()
    salida = salida + '\n' + linea.replace('a', 'A').replace('u', '5')
    # print(linea)

resultado = open('data/salida.txt', 'w')
resultado.write(salida)

# ejemplo

file = open('data/01_ejemplo.txt')
total = 0
c = 0

for linea in file:
    total = total + len(linea.split())
    c = c + 1

print('promedio: {}'.format(total/c))