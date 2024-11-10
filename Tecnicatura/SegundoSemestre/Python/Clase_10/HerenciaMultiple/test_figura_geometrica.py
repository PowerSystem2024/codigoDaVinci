from Cuadrado import Cuadrado
from HerenciaMultiple.FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creacion de objeto clase cuadrado'.center(50, '_'))
cuadrado1 = Cuadrado(8,'Azul')
cuadrado1.alto = 7
cuadrado1.ancho = 7
#print(cuadrado1.ancho)
#print(cuadrado1.alto)
print(f'Calculo del area del cuadrado:  {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
print(Cuadrado.mro())

print(cuadrado1)

print('Creacion de objeto clase rectangulo'.center(50, '_'))
rectangulo1 =Rectangulo(2,6,'Rojo')
rectangulo1.ancho = 15
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

#figura1 = FiguraGeometrica() No se puede instanciar una clase abstracta
print(Cuadrado.mro())
