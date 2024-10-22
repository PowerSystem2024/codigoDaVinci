class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    Esto es documentaciom de la clase de python
    Vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicacion y division
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
        
    def sumar(self):
        return self.operandoA + self.operandoB
    
    def resta(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB 
    
aritmetica1 = Aritmetica(7, 9)
print(aritmetica1.sumar())
print(f'La resta de los numeros es: {aritmetica1.resta()}')
print(f'La multiplicacion de los numeros es: {aritmetica1.multiplicar()}')
print(f'La division de los numeros es: {aritmetica1.dividir():.2f}')   
    
    

    