#List comprehension, lista de comprensión
names = ['Lautaro', 'Abel', 'Marta', 'Pepe', 'Polaroid']
alongP = [p for p in names if p[0] == 'P'] # el p for p va a reccorer toda la lista , el if dice que desde
#la posición cero verifica si existe un nombre que comience con P lo agregará a alongP
print(alongP)

#lista de diccionario
botellasCerv = [{"name": "Quilmes", "country": "Argentina"},
                {"name": "Corona", "country": "Mexico"},
                {"name": "Stella Artois", "country": "Bélgica"},]

#extraemos del diccionario la información que necesitamos
#utilizamos list comprehension, forma consisa de crear una nueva lista
#la primera b es una variable que representa c/elemento de la lista
#cada vez que se pasa al siguiente elemento de la lista , "b" toma el valor de ese elemento
#la segunga variable b es el valor que se agrega a la nueva lista, si se cumple la condición se incluye el diccionario b en la lista resultante
cervArg = [b for b in botellasCerv if b["country"] == "Argentina"]
print(cervArg)