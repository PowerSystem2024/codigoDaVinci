#Genero una lista
nombres  = ['Pedro', 'Amanda', 'Mabel', 'Karin']
print(nombres)
#imprime el indice 0, 1 pero no el índice 2
print(nombres[0:2])
#ir del incio de la lista al indice (sin incluirlo)
print(nombres[ :3])#dejo un espacio entre los dos puntos y el número final
# Desde el índice indicado hasta el final
print(nombres[1: ])#indice 1 hasta el final
#modificamos un valor de la lista
nombres[3] = 'Liliana'
nombres[0] = 'Juan'
print(nombres)
#iteramos la lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print('se acabaron los elementos de la lista')