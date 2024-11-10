# Colecciones en python
# Las listas se conoce en otros lenguajes como arreglos o vectores

nombres = ['Jonathan', 'Carmina', 'Pedro']
nombres.append('René')# agrego un elemento a la lista
nombres.append(True) # agrego un valor booleano
nombres.append(10.5) # agrego un valor tipo float
nombres.append([4,5]) # agrego una lista interna
print(nombres)

#concatenamos listas
lista1 = [1,1,2,3]
lista2 = [4,5,6, 1]
lista3 = lista1 +lista2 #concatenamos
print(lista3)

lista3.extend([7,8,9]) #Función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(2)) #Función para u bicar en qué indice está el valor ingresado

#cómo saber cuántos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuandos valores iguales hay dentro de la lista

#para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

#Métodos de ordenamiento
lista3.sort() #Ordena los elementos de forma ascendente
print(lista3)

#Muestra la lista en orden inverso , descendente
lista3.sort(reverse=True) # Ordena descendentemente
print(lista3)