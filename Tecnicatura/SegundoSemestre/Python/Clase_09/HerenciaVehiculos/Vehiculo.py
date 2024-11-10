'''
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas
Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos:

Vehiculo (clase padre)
-Atributos (color, ruedas)
-Métodes(_ init(color, ruedas) y __str_())

Auto(clase hija de Vehiculo)
-Atributos(velocidad (km/hr))
-Métodos(_init_ (color, ruedas, velocidad) y _str_())

Bicicleta(clase hija de Vehiculo)
-Atributos(tipo(urbana/montaña/etc.)
-Métodos(_init_ (color, ruedas, tipo) y _str_()

Crear un obieto de cada clase
'''
class Vehiculo:

    def __init__(self, color,ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return 'Color: '+ self.color + ', Ruedas: '+ str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color,ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+', Velocidad(km/hr): '+ str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+', Tipo: '+self.tipo

# Primer objeto de la clase padre vehiculo
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)

# Segundo objeto, de la clase auto
auto = Auto ('Amarillo',4,120)
print(auto)

# Tercer objeto, bicicleta
bici = Bicicleta('Azul', 2, 'Urbana')
print(bici)