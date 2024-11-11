#Ejercicio 8: Menú interactivo - Cajero automático
#Hacer un programa que simule un cajero automático con un saldo inicial de 1000$
#y tendrá el siguiente menú de opciones:
# 1.Ingresar dinero en la cuenta
# 2.Retirar dinero de la cuenta
# 3.Mostrar dinero disponible
# 4.Salir

saldo = 1000
while True: #se ejecuta mientras sea verdadero
    print("\t Menú: ")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opción del menú: "))
    print()
    if opcion == 1:
        extra = float(input("Cuánto deseas ingresar -> "))
        saldo += extra
        print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 2:
        retirar = float(input("Cuanto dinero desea retirar -> "))
        if retirar > saldo:
            print("No tiene esa cantidad de dinero ")
        else:
            saldo -= retirar
            print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 3:
        print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 4:
        print(f'Gracias por utilizar su cajero automático, hasta pronto')
        break
    #si digita cualquier otro número diferente a los del menú , lanza el error
    else:
        print('Error, se equivocó de opción de menú')
        print()