class Persona:  #Esta clase hereda de la clase Objetct
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self): # Override return
        return f'Persona: [ Nombre: {self._nombre}, Edad {self._edad}]'

class Empleado(Persona):  #Esta clase es la hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super ().__init__(nombre, edad)
        self.sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Sueldo: {self._sueldo}] {super().__str__()}'

empleado1 = Empleado('Sammy', 13,8888888)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
# Tarea: encapsular los atributos y agregar los metodos getter and setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

empledo2 = Empleado('Santiago', 22, 300000)
print(empledo2.nombre)
print(empledo2.edad)
print(empledo2.sueldo)
empledo2.nombre ='Pilar'
empledo2.edad = 28
empledo2.sueldo = 715000
print(empledo2.nombre)
print(empledo2.edad)
print(empledo2.sueldo)