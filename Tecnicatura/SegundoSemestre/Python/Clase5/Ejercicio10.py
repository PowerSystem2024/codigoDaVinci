'''
Ejercicio 10: No repetir caracteres
Hacer un programa que pida una cadena por teclado, luego 
meter los caracteres en una lista sin repetir caracteres
'''
palabra = str(input("Ingrese un texto:\n."))
palabra = list(set(palabra))
print(palabra)