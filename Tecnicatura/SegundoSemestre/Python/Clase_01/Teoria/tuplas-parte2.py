#recorremos elementos de la tupla
verduras = ('papa', 'Berenjena', 'Cebolla')
for verdura in verduras:
    print(verdura)#print imprime saltos de línea porque usa \n

print("Imprimo sin saltos de línea: ")
for verdura in verduras:
    print(verdura, end=' ')  # agrego espacios en lugar de saltos de línea


#ÚNICA FORMA DE MODIFICAR UNA TUPLA: PARSEARLA A LISTA
 #NO es una buena práctica
print(' ')
print("Convierto la tupla en lista y la vuelvo a pasar a tupla: ")
verdurasLista = list(verduras)
verdurasLista[0] = 'Tomate'
verduras = tuple(verdurasLista)
print(verduras)
print('\n', verduras)#vuelve atrás el print modificado con espacios agregados end= ' '

#En tuplas no se usan funciones como append , insert, etc.

#Eliminamos la tupla
# con esta función : del verduras
