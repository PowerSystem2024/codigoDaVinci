#Ejercicio 11: Agenda telefónica
#Hacer un programa que simule una agenda de contactos. Crear un diccionario donde la clave
#sea el nombre del usuario y el valor sea el teléfono, el programa tendrá el siguiente menú
#de opciones:

#  1. Nuevo contacto
#  2. Borrar contacto
#  3. Ver contactos existentes
#  4. Salir

agenda = {}
while True:
    print('\t Menú: ')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input("Digite una opción del menú: "))
    if opcion == 1:
        nombre = input('Digite el nombre del contacto: ')
        telefono = input('Digite el telefono del contacto: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente!')
        else:
            print('Este nombre de contacto ya existe')
    elif opcion == 2:
        nombre = input('cuál es el nombre del contacto: ')
        if nombre in agenda:
            del(agenda[nombre])
            print('Se ha elimnado el contacto requerido')
        else:
            print('Este contacto no existe en la agenda')

    elif opcion == 3:
        print('Agenda de contactos')
        for clave, valor in agenda.items(): #declaramos dos variables dentro del for y le indicamos el diccionario en este caso
            print(f'Nombre: {clave}, Teléfono: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos')
        break
