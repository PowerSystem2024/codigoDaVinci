class MiClase:
    #Variable de clase, este atributro dara a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase' #Esta en el contexto estatico

    def __init__(self, variable_instancia): #la variable de instancia q da dif. valores
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico(): #Metodo estatico, al ser de la clase no se aplica a los objetos y por ende no nos proporciona la palabra self
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)


print(MiClase.variable_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

MiClase.variable_clase2 = 'Se le puede asignar a la variable de clase, otro valor'
print(MiClase.variable_clase2) #Llamada desde la clase
print(miClase1.variable_clase2) #Llamada a los objetos
print(miClase2.variable_clase2) #Llamada a los objetos

MiClase.metodo_estatico()

MiClase.metodo_clase()
miObjeto1 = MiClase('Variable de instancia objeto')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()

