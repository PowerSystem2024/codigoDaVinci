'''
Ejercicio 01: Crear una funcion para sumar los valores recibidos de tipo
numericos, utilizando argumentos variables *args como parametro de la
Funcion y agregar como resultado la suma de todos los valores pasados
como argumentos
'''
# Definimos la funcion
def sumarNumeros(*args):
    suma = 0
    for numeros in args:
        suma += numeros
    return suma

# Llamamos a la funcion
resultado = sumarNumeros(5,4,6)
print(f'La suma de los numeros es: {resultado}')
