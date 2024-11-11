#   CLASE 11 Parte 2
#   VIDEO 4
from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    #print(objeto) # De manera indirecta llama al str de la clase Empleado o Gerente
    print(type(objeto)) # Esto es para saber el tipo de dato que recibe
    #   VIDEO 5
    print(objeto.mostrar_detalles())
    #   VIDEO 6
    if(isinstance(objeto, Gerente)): # isinstance(miObjeto, tipoDeObjeto) devuelve un booleano en relacion si son objetos del mismo tipo
        print(objeto.departamento)
    
empleado = Empleado("Ariel", 50000.00)
imprimir_detalles(empleado)

#   VIDEO 5
gerente = Gerente('Natalia', 60000, 'Sistema')
imprimir_detalles(gerente)