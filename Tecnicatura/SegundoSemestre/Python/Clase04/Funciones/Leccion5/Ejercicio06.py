#Ejercicio 6: tabla de multiplicar
#Hacer un programa que pida un número por teclado y guarde
#en una lista, su tabla de multiplicar hasta el 10
#Ej: si digita 5, obtendrá:
# 5,10,15,20,25,30...50

numero = int(input("Digite un número: "))
lista = [] #creamos una lista vacía
for i in range(1 , 11):
    lista.append(i*numero)
print(f'\nTabla de multiplicar del {numero}: \n {lista}')

for indice, i in enumerate(lista):
    print(f'{numero} x {i} = {lista[indice]}')