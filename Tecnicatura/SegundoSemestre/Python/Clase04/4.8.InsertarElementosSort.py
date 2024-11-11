#Ejercicio 3: insertar elementos y ordenarlos
#pedir números y meterlos en una lista , cuando el usaurio
#introduzca un número 0 , el programa debe dejar de insertar
#por último, mostrar los números ordenados de menor a mayor

lista = []
salir = False

while not salir:
    numero = int(input('Digite un número: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()
print(f'\nLista ordenada: \n{lista}')