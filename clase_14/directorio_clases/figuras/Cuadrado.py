from .FiguraGeometrica import FiguraGeometrica


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