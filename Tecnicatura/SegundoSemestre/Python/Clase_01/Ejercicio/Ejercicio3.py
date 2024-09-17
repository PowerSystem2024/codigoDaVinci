#ejercicio3 Crear un rango de 3 a 10 pero con un incremento de 2 en 2 , ejemplo de ejecución 3, 5, 7, 9

rango = range(3,10)
print('Rango con valores de inicio = 3 y fin = 10 , incremento = 2')
for numero in rango:
    if numero % 2 != 0:
        print(numero)
        print(" ")

#Otra forma de resolverlo
for i in range(3,11,2):
    print(i)