#   CLASE 11 Parte 2
#   VIDEO 2
class Empleado: # No hereda sino solo de la clase object
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
        
    def __str__(self) -> str:
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'
    
    def mostrar_detalles(self):
        return self.__str__()