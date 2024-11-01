'''
Ejercicio 3: Funcion Recursiva
Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
Puede ser cualquier valor positivo, por ejermplo, si pasamos el valor
de 5, debe imprimir:
5
4
3
2
1
En caso de ser el numero 3 debe imprimir:
3
2
1
Si se ingresan numeros negativos no imprime nada
'''
# Definimos la funcion
def imprimirNumeros(numero):
    if numero == 1:
        print(numero) 
    else:
        print(numero)
        imprimirNumeros(numero-1)

# Pedimos un numero y llamamos a la funcion
num = int(input('Digite un numero: '))
imprimirNumeros(num)