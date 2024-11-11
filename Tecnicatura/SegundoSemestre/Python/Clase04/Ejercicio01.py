#Ejercicio 1: Eliminar duplicados de una lista
#crear una lista y eliminar los elementos repetidos , mostrar la lista

lista = [1,2,1,2,2,3,4,4,5,5]
listaSinElementosDuplicados = [] #genero una lista vacía
for numero in lista:
    if numero not in listaSinElementosDuplicados:
        listaSinElementosDuplicados.append(numero)

print(listaSinElementosDuplicados)

#Otro método de resolver
lista2 = [2, 3,4, "Amazon", "Netflix", "Alberto", 1, 2]
lista2 = list(set(lista)) #convertimos el conjunto en una lista
print(lista2)