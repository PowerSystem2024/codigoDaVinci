'''
Ejercicio 11: Agenda telefomica
Hacer un programa que simule una agenda de contactos. Crear un 
diccionario donde la clave sea el nombre del usuario y el valor 
sea el telefono, el programa tendra el siguiente menu de opciones:
1. Nuevo contacto
2. Borrar contacto
3. Ver contactos existentes
4. Salir
'''
listaDeContactos = {}
while True:
    opicion = int(input(f'Que accion desea realizar?\n 1. Nuevo contacto\n 2. Borrar contacto\n 3. Ver contactos existentes\n 4. Salir\n.'))
    print("")
    #   Nuevo contacto
    if opicion == 1:
        print("     NUEVO CONTACTO")
        nombreContacto = str(input("Nombre del contacto: "))
        #   Comprobamos si el elemento existe
        if (nombreContacto in listaDeContactos) == True:
            seguro = int(input('\nEste nombre de contacto ya existe, que desea hacer?:\n 1. Modificar numero\n 2. Cancelar accion\n'))
            while seguro != 1 and seguro != 2:                
                seguro = int(input(' 1. Modificar numero\n 2. Cancelar accion\n'))
            if seguro == 1:
                listaDeContactos[nombreContacto] = int(input('Nuevo numero: '))
        else:
            numeroContacto = int(input("Numero del contacto: "))
            listaDeContactos[nombreContacto] = numeroContacto
        print("El numero fue ingresado correctamente.\n")
    #   Borrar contacto
    elif opicion == 2:
        print("     BORRAR CONTACTO")
        while True:
            nombreContacto = str(input("Nombre del contacto: "))
            #   Comprueba si el elemento existe
            if (nombreContacto in listaDeContactos) == True:                
                seguro = str(input(f"Seguro que deseas eliminar el contacto {nombreContacto}? (Si/No): "))
                while seguro.capitalize() != "Si" and seguro.capitalize() != "No":
                    seguro = str(input(f"Seguro que deseas eliminar el contacto {nombreContacto}? (Si/No): "))
                if seguro.capitalize() == "Si":
                    listaDeContactos.pop(nombreContacto)
                    break
                elif seguro.capitalize() == "No":
                    seguro = int(input(' 1. Borrar un numero\n 2.Salir de borrar numero'))
                    if seguro == 1:
                        break
                    elif seguro == 2:
                        continue
            else:
                print("\nCONTACTO NO ENCONTRADO")
                seguro = str(input("Quiere seguir con esta funcion? (Si/No): "))
                while seguro.capitalize() != "Si" and seguro.capitalize() != "No":
                    seguro = str(input("Quiere seguir con esta funcion? (Si/No): "))
                if seguro.capitalize() == "Si":
                    continue
                elif seguro.capitalize == "No":
                    break                                       
    elif opicion == 3:
        print("     LISTA DE CONTACTOS")
        for nombre,numero in listaDeContactos.items():
            print(f"{nombre}: {numero}")
    elif opicion == 4:
        break
    else:
        print("VALOR INCORRECTO")
    print('')