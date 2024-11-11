numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
else:
    print('Esto se terminó')

nombres = ["Mariela", "Carmen"]
for nombre in nombres:
    print(nombre)
else:
    print('termina y muestra el else')

#Uníca forma para que no se ejecute un else en el ciclo for
numeros = [0,1,3]
for n in numeros:
    print(n)
    if n == 3:
        break #agregando un break, para que no se ejecute el else
else:
    print("Esto se terminó")