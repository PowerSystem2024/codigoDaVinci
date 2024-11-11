#   CLASE 11 Parte 1
#   VIDEO 8
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __add__(self, other): # other = otro
        return f'{self.nombre} {other.nombre}'
    
    #   VIDEO 9
    def __sub__(self, otro):
        return self.edad - otro.edad
    
persona1 = Persona('Ariel', 40)
persona2 = Persona('Betancud', 5)

#persona1.__add__(persona2) # Sintaxis interna y automatica
print(persona1 + persona2) # Sintaxis normal

#   VIDEO 9
print(persona1 - persona2)