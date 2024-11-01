class Persona:  #Creamos una clase

    def __init__(self, nombre, apellido, edad):  #las variables q vienen x parametro
        self.nombre = nombre  #atributo = variable
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(
            f'Persona: {self.nombre} {self.apellido} {self.edad}')  #para poder llamar a otro metodo dentro de la clase se usa el self


persona1 = Persona('Sammy', 'Diebeste', 15)  #necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Kima', 'Diebeste', 10)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}, su edad es: {persona2.edad} años')
#Tarea hacer la interpolacion con el objeto 1
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, su edad es: {persona1.edad} años')

#Se pueden modificar los atributos de un objeto? Sip
persona1.nombre = 'Tigresa'
persona1.apellido = "Gil"
persona1.edad = '8'
print(
    f'El Objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}, su edad es: {persona1.edad} años')

#Los atributos son las caracteristicas para nuestros objetos = ADJETIVOS
#Los metodos son el comportamiento que van a tener los objetos (acciones) = VERBOS. El metodo esta asociado a una clase y la funcion es propia de si misma
persona1.mostrar_detalle()
persona2.mostrar_detalle()