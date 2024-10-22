'''
Ejercicio 2: Funcion con * args para multiplicar
Crear una funcion para multiplicar los valores recibidos
de tipo numerico, utilizando argumentos variables *args
como parametro de la funcion y regresar conmo resultado
la multiplicacion de todos los valores pasados como argumento
'''
# Defino la funcion
def multiplicarNumeros(*args):
    producto = 1
    for num in args:
        producto *= num
    return producto 

# Llamamos a la funcion
print(multiplicarNumeros(4,3,2))