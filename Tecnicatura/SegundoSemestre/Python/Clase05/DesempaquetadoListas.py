#Desempaquetado de listas o list Unpacking
def show(name, lastname):
    print(name + ' ' + lastname)
person = ['Abelardo', 'Marlene']
show(person[0], person[1]) #Pasamos uno por uno los datos de la lista a la función
show(*person) #esto es lo mismo q lo anterior pero le pasamos todo junto

#desempaquetamos a través de una tupla
person2 = ("Miguel", "Gritar")
# el uso de * (uno), es para desempaquetar una secuencia como una lista o tupla
show(*person2)

#desempaquetamos a través de un diccionario
person3 = {"LastName": "Barco", "name": "Eliana"}
#el uso de **(dos) es para desempaquetar diccionarios; pasa sus pares clave-valor como argumentos a la función show
show(**person3)#como necesitamos que muestre clave y valor agregamos dos asteriscos