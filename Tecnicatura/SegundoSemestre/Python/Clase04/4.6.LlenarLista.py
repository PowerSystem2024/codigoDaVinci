#LLenar una lista con los números del 1 al 50, luego mostrarla
#con el bucle for, los elementos deben mostrarse
#de la siguiente forma:
# 1-2-3-4-5....-50

lista = []
i = 1
while i < 50:
    lista.append(i)
    i += 1
    print(i , end='-')


listaConRango = list(range(1, 51)) #Algoritmo eficaz
for i in listaConRango:
    print(i, end='-')
