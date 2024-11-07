'''
Ejercicio 5: Comvertidor de temperaturas
Realizar dos funciones para convertir de grados celsius
a fahrenheit y viseversa
Investigar las formulas
'''
# Definimos la funcion para convertir grados celsius a fahrenheit
def celsiusFahrenheit(celsius):
    fahrenheit = (celsius * 9/5 ) + 32
    return fahrenheit
# Definimos la funcion para convertir grados fahrenheit a celsius
def fahrenheitCelsius(fahrenheit):
    celcius = (fahrenheit -32) * 5/9
    return celcius

while True:
    opcion = int(input('Que quiere calcular?:\n 1. Grados celsius a fahrenheit \n 2. Grados fahrenheit a celsius\n_'))
    # Seguro para que solo se elijan una de las dos opciones
    while opcion != 1 and opcion != 2:
        opcion = int(input('Que quiere calcular?:\n 1. Grados celsius a fahrenheit \n 2. Grados fahrenheit a celsius\n_'))
    if opcion == 1:
        C = float(input('\nDigite los grados celsius: '))
        print(f'{C} grados celsius son {celsiusFahrenheit(C)} grados fahrenheit')
    else:
        F = float(input('\nDigite los grados fahrenheit: '))
        print(f'{F} grados fahrenheit son {fahrenheitCelsius(F)} grados celsius')
    opcion = str(input('\nSeguir calculando?:\n Si\n No\n_'))
    # Otro seguro
    while opcion.capitalize() != 'Si' and opcion.capitalize() != 'No':
        opcion = str(input('\nSeguir calculando?:\n Si\n No\n_'))
    if opcion.capitalize() == 'No':
        break
