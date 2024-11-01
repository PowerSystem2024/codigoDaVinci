#   PARTE 1
#   VIDEO 3 (lista)
# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ['Ariel', 'Betancud']
show(person[0],person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person)   # Esto es lo mismo que lo anterior pero pasamos todo junto
person2 = ('Osvaldo', 'Giordanini') # desempaquetamos a traves de una tupla
show(*person2)
person3 = {'lastName': 'Lucero','name': 'Natalia'} 
show(**person3)    # para que esto funcione, los argumentos deben tener exactamente los mismo nombres que los parametros

#   VIDEO 4 (lista)
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
else:
    print("Esto se termino")

# Manera para que no se muestre el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termino")
    
#   VIDEO 5 (listas y diccionarios)
# List comprehesion, lista de compresion
names = ['Paolo', 'Rodrigo', 'Lupe', 'Pepe']
alongP = [p for p in names if p[0] == 'P']  # Esto regresa una nueva lista
print(alongP)
bottleC = [{'name': 'Quilmes','country':'Arg'},
           {'name': 'Corona','country':'Mx'},
           {'name': 'Stella Artois','country':'Belgium'}
           ]
Arg = [b for b in bottleC if b['country'] == 'Arg'] # Recorremos en singular elemento por elemento todo el diccionario
#                                                     'bottleC', luego una condicion que pregunta si el elemento que estamos
#                                                      recorriendo dentro de 'country' es igual a Arg se guarda
print(Arg)
print(bottleC)

#   VIDEO 6 (funciones)
# Paso de Argumentos
def mi_funcion2(name,lastName):
    print('Saludos a todos lo que ven a traves del canal de YouTube')
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Jorge','Lucero')
mi_funcion2('Analia','Pedrosa')
mi_funcion2('Alberto','Bustos')

#   VIDEO 7 (funciones)
# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a,b):
    return a + b
resultado = sumar(78,22)
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55,55)}')

#   VIDEO 8 (funciones)
def sumar2(a = 0,b = 0): # Estos iguales al lado de los parametros, son valores por default
    return a + b
resultado = sumar2()                        # Si no proporcionamos argumentos
print(f'Resultado de la suma: {resultado}') # Actuan los valores por default
print(f'Resultado de la suma: {sumar(22,66)}')  # Pero si ingresamos valores se utilizaran dichos valores

#   VIDEO 9 (funciones)
# Argumentos, variables en funciones
def listarNombres(*nombres): # Con esta sintaxis pueden variar los argumentos. Normalmento se utiliza: *args
    for nombre in nombres:  # Se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas','Jose','Claudia','Rosa','Maria')
print("")
listarNombres('Marcos','Daniel','Romina','Pepe','Marcela','Carlos')

#   PARTE 2
#   VIDEO 2 (diccionario)
def listarTerminos(**terminos): #esta sintaxis es para recibir un diccionario como argumento
    for llave, valor in terminos.items():   # Lo mas utilizado es **kwargs para recibir los argumentos
        print(f'{llave} : {valor}')         # kwargs significa: key word argument
        
listarTerminos()    # No recibe nada, nada va a mostrar
listarTerminos(IDE = 'Integrated Development Enviroment', PK='Primary Key')
#listarTerminos(10='Leonel Messi') # No toma como key un numero
listarTerminos(Nombre='Leonel Messi')

#   VIDEO 3
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito','Pedro','Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10) # No es un objeto iterable
desplegarNombres((10,))  # La convertimos a una tupla. Para q sea una tupla de un elemento debe haber un coma
desplegarNombres([22, 55])  # La convertimos en una lista

#   VIDEO 4
# Funciones Recursivas
def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero-1) # Caso recursivo
resultado = factorial(5)    # Lo hacemos en codigo duro
print(f'El factorial del numero 5 es: {resultado}')

# Tarea: usar la funcion con un numero ingresado por el usuario
numero = int(input('Digite un numero para sacar su factorial: '))
print(f'El factorial del numero {numero} es: {factorial(numero)}')