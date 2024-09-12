#Genero una lista
monedas = ['Peso', 'Sol', 'Peso Chileno', 'Dólar']
#preguntamos cuantos elementos tiene la lista
print(len(monedas)) #le pasamos como parametro la lista

#agregamos un elemento
monedas.append('Euro')
print(monedas)

#insertamos un elemento en un índice en específico
monedas.insert(1,'Dólar mexicano')#el elemento existente en la posición uno se mueve uno a la derecha para ingresar el nuevo valor
print(monedas)
monedas.insert(3, 'Libra esterlina')
print(monedas)

#Eliminamos un elemento
monedas.remove('Dólar')
print(monedas)

#Eliminar el último elemento de la lista
monedas.pop() # pop por default sin parámetros elimina el último de la lista
print(monedas)

#Eliminar un índice específico
del monedas[2] #del significa delete (eliminar)
print(monedas)

#Eliminar, borrar o limpiar todos los elementos
monedas.clear()
print(monedas)

#Eliminar la lista
del monedas
print(monedas)