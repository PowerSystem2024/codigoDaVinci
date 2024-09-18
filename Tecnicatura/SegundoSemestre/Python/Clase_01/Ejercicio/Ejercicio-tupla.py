#Dada la siguiente tupla
tupla = (13 , 1, 8, 3, 2, 5, 8)
#crear una lista que solo incluya los números menores a 5

listaTupla = []
#filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        listaTupla.append(elemento)
print('Imprimimos la lista resultante')
print(listaTupla)
#Utilizando compresión de listas
#con compresión de lista
lista = [num for num in tupla if num < 5]
print(lista)
