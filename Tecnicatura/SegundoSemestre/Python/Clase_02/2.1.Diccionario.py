#Un diccionario está compuesto por dos elemenos : una llave y un valor
#dict(key,value)
diccionario = {
    'IDE': 'Integrated Development Environmet',
    'POO': 'Programación orientada a objetos',
    'SABD':'Sistema de administración de base de datos'
}

print(diccionario)
#Verifico la cantidad de elemtnos del diccionario
print(len(diccionario))
print(diccionario)

## Acceder a un diccionario con la llave(Key)
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))

##Un diccionario puede modificarse
#Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Clase 2.2

#cómo recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)

#Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): #Estamos usando una función
    print(termino) # muestra solo las llaves

for valor in diccionario.values(): #usamos una función para acceder al valor
    print(valor)

# Comprobar la existencia de algún elemento
print('IDE' in diccionario) #devuelve un booleano

#Agregamos un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario - se borra el dicionario
#lo comento para que no de error la ejecución de otros ejercicios
#del diccionario