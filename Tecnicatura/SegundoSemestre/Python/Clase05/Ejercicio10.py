#Ejercicio 10: No repetir caracteres
#Hacer un programa que pida una cadena por teclado, luego
#meter los caracteres en una lista sin repetir caracteres

cadena = input("Digite una cadena") #pido al usuario que ingrese una cadena de texto
lista = [] #genero una lista vacía
for i in cadena: #voy a recorrer cada posición de la cadena
    if i not in lista: #si el caracter aún no está en la lista
        lista.append(i) #Lo agregamos a la lista
print(f'\nLista de caracteres sin repetir ninguno: \n {lista}')