from .FiguraGeometrica import FiguraGeometrica


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