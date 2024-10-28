class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f"persona: {self.nombre} {self.apellido} {self.edad}")


persona1 = Persona("Santiago", "Torres", "18")
print(f"El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")
persona2 = Persona("Jonas", "Ponzio", "22")
print(f"El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}")


persona1.nombre = "Graciela"
persona1.apellido = "Ferrari"
persona1.edad = "49"
print(f"El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")

persona1.mostrar_detalle()
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1)
persona1.telefono = "12324124"
print(f"Este es el telefono de: {persona1.nombre} {persona1.telefono}")

#print(persona2.telefono) el objeto persona2 no tiene este atributo, da error

