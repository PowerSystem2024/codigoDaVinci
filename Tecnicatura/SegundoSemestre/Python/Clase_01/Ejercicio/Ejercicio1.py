#Ejercicio 1: iterar un rango de 0 a 10 e imprimir números divisibles
#entre 3  , ej de ejecución: 0, 3, 6, 9

#Genero lista
numeros = [0,1,2,3,4,5,6,7,8,9,10]
print("Rango de 0 a 10 con números divisibles entre 3")
for numero in numeros:
    if numero % 3 == 0:
        print(numero)