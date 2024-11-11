#Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = [] #creamos la lista vacía
#creamos diccionarios
P= {'Nombre' : 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dúnadan del Norte'}
personajes.append(P)#AGREGAMOS A LA LISTA UN PERSONAJE
P= {'Nombre' : 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)
P= {'Nombre' : 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P)
P = {'Nombre': 'Frodo', 'Clase': 'Portador del Anillo', 'Raza': 'Hobbit'}
personajes.append(P)
P = {'Nombre': 'Gimli', 'Clase': 'Guerrero', 'Raza': 'Enano'}
personajes.append(P)
P = {'Nombre': 'Boromir', 'Clase': 'Guerrero', 'Raza': 'Hombre de Gondor'}
personajes.append(P)
print(personajes)