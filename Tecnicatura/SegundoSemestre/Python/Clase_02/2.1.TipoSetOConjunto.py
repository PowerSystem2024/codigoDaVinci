#tipo set - también conocidos como conjuntos
planetas = {'Marte', 'Júpiter', 'Venus'} #no mantiene indice, se ejecute en orden aleatorio
print(planetas)

#funciones a utilizar con tipo set
print(len(planetas))#usamos la función len = length significa largo

#revisar si un elemento existe dentro del set
print('Júpiter' in planetas)# retorna un valor booleano
print('Júpiter' not in planetas)# uso la negación- Júpiter no está en planetas? false

#agregar un elemento
planetas.add('Tierra')#add es una función
#no se puede agregar elementos duplicados, por más que repitamos n veces solo agrega una
planetas.add('Tierra')#add es una función
planetas.add('Tierra')#add es una función

#Eliminar elementos , puede arrojar un error si el elemento no existe
planetas.remove('Júpiter')#Esta función ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard('tierra')#Esta función no nmos presenta ningún error
print(planetas)

#limpiar set
planetas.clear()
print(planetas)

#Eliminar set, se ejecuta la función del
 #del planetas