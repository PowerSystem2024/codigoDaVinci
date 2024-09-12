#las tuplas son inmutables , no se pueden modificar
#las listas sí se pueden modificar.. esa es la gran diferencia

#definimos tuplas
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)

#saber el largo o cantidad de elementos que tiene una tupla
print("utilizamos función len para ver la cantidad de elementos - longitud de la tupla: ")
print(len(cocina))

#acceder a un elemento, para esto utilizamos corchetes no paréntesis
print(cocina[0])

#mostramos la manera inversa
print(cocina[-1]) #nos mostrará el último elemento

#cómo acceder a un rango
print(cocina[0:1]) #rango de 0 a 1 muestra hasta el último rango incluído -1
print(cocina[0:2])

#ESTO NO ES UNA TUPLA, ES UN STRING, LA TUPLA NECESITA UN ELEMENTO AL MENOS Y LA COMA ('PAPA',)
verduras = ('papa')

