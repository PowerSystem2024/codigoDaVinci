class Persona:
    contador_persona = 0 # Variable de clase

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1 #vamos incrementando
        return cls.contador_persona

    def __init__(self, nombre, edad):
        Persona.contador_persona += 1 #vamos incrementando
        self.id_persona = Persona.contador_persona
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f' Persona [{self.id_persona} = {self.nombre} {self.edad}]'


persona1 = Persona('Ariel' , 40)
print(persona1)
persona2 = Persona('Osvaldo', 45)
print(persona2)
persona3 = Persona('Sammy' , 13)
print(persona3)
Persona.generar_siguiente_valor()
Persona4 = Persona('Naty', 35)
print(Persona4)
print(f'Valor contador personas: {Persona.contador_persona}')
