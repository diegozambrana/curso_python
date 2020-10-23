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

    def __del__(self):
        print('se esta eliminando el Cuadrado')


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


class Triangulo(FiguraGeometrica):
    h = 0
    b = 0

    def __init__(self, x, y, h, b):
        FiguraGeometrica.__init__(Triangulo, x, y)
        self.h = h
        self.b = b

    def area(self):
        return (self.h * self.b) / 2

    def __str__(self):
        return f"Triangulo: esta en la posicion({self.x}, {self.y}) tiene " + \
               f"una base de {self.b}, una altura de {self.h} y un area de {self.area()}"


rectangulo = Cuadrado(3, 4, 10, 20)
print(rectangulo)
print(rectangulo.x)
print(rectangulo.y)
print(rectangulo.ancho)
print(rectangulo.alto)
print(rectangulo.area())

rectangulo2 = Cuadrado(4, 4, 3, 5)
print(rectangulo2.area())
rectangulo2.ancho = 10
print(rectangulo2.area())
print(rectangulo2.posicion())
print(rectangulo2.distancia())


print('------ circulo -------')
circulo = Circulo(10, 10, 5)
print(circulo.distancia())
print(circulo.area())
print(circulo)

triangulo = Triangulo(1, 2, 4, 3)
print(triangulo)
print(triangulo.area())