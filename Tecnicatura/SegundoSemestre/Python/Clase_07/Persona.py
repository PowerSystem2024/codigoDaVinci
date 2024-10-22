class Persona:
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs ): #Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #atributo encapsulado
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f"La clase persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la dirrecion es: {self.args}, los datos importantes son: {self.kwargs}")


persona1 = Persona("Santiago", "Torres", 47268869, 18)
print(f"El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")
persona2 = Persona("Jonas", "Ponzio", 40654873, 22)
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
persona3 = Persona("Santino", "Torresi", 45239957, 19, "Telefono", "2617876220", "Calle Gainza", 456, "Piso", 3, "Departamento", "B", Altura=1.97, Peso=82, CFavorito="Rojo", Auto="Renault", Modelo=2017)
persona3.mostrar_detalle()
#print(persona3._dni) esto no se debe utilizar(esta encapsulado)
#persona3.__nombre  esta totalmente encapsulado