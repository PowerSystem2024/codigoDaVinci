from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        #super.__init__(lado) no sabria de que clase padre lo traeria
        FiguraGeometrica.__init__(self, lado,lado)
        Color.__init__(self, color)


    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'