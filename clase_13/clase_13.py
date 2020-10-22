# Ejercicio 1
import re

texto = "pedro tiene 10 manzanas, Juan tiene 20 manzanas y carlos tiene 30 manzanas"
lista = re.findall('\d+', texto)
print(lista)
print(sum(map(lambda x: int(x), lista)))

# Ejercicio 2

import re

texto = input('ingrese Hora: ')
match = re.match('\d{2}:\d{2}:\d{2}', texto)
print(match)
if match is not None:
    h = match.group()
    h = h.split(':')
    print(f"son las {h[0]} horas, con {h[1]} minutos y {h[2]} segundos.")
else:
    print("No es una hora válida.")


# Ejercicio 3

import re

texto = input('ingrese texto: ')
palabras = re.findall('[a-zA-Z]*[aA]+[a-zA-Z]*', texto)
print(palabras)


# POO

class Contador:
    x = 0
    nombre = ''

    def __init__(self, nombre):
        self.nombre = nombre

    def imprimirEstado(self):
        print('El', self.nombre, 'esta en', self.x)

    def agregar(self):
        self.x += 1
        self.imprimirEstado()

    def __str__(self):
        return f"Contador: nombre='{self.nombre}', x={self.x}"

    def __del__(self):
        print('Este', self.nombre, 'esta siendo destruido')


contador_1 = Contador('Contador 1')
contador_1.agregar()
contador_1.imprimirEstado()
print(contador_1)
del contador_1

contador_2 = Contador('Contador 2')
contador_2.agregar()
Contador.agregar(contador_2)
contador_2.imprimirEstado()


string_contador2 = str(contador_2)
print(string_contador2)
print(contador_2)
contador_2 = 12

# herencia

import math

class FiguraGeometrica:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def posicion(self):
        return (self.x, self.y)

    def distancia(self):
        return (self.x ** 2 + self.y ** 2) ** (1/2)


class Cuadrado(FiguraGeometrica):
    alto = 0
    ancho = 0

    def __init__(self, x, y, alto, ancho):
        FiguraGeometrica.__init__(Cuadrado, x, y)
        self.alto = alto
        self.ancho = ancho

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"Cuadrado: esta en la posicion({self.x}, {self.y}) tiene" + \
               f"un alto de {self.alto} y ancho de {self.ancho} y un area de {self.area()}"

class Circulo(FiguraGeometrica):
    radio = 0

    def __init__(self, x, y, radio):
        FiguraGeometrica.__init__(Circulo, x, y)
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def __str__(self):
        return f"Circulo: esta en la posicion({self.x}, {self.y}) tiene" + \
               f"un radio de {self.radio} y un area de {self.area()}"


rectangulo = Cuadrado(3, 4, 10, 20)
print(rectangulo.posicion())
print(rectangulo.x)
print(rectangulo.y)
print(rectangulo.area())
print(rectangulo.distancia())
print(rectangulo)

print('------ circulo -------')
circulo = Circulo(10, 10, 10)
print(circulo.distancia())
print(circulo.area())
print(circulo)