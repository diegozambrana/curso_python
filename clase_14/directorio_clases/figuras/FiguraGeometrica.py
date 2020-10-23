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