#La palabra return en funciones
#creamos una función para sumar
def sumar(a,b):
    return a + b

resultado = sumar(54, 42)
print(f'El resultado es:  {resultado}')

def restar(a,b):
    return a - b
#llamo a la función directamente dentro del print
print(f'El resultado es {restar(90,50)}')