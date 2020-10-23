import math
from .FiguraGeometrica import FiguraGeometrica


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