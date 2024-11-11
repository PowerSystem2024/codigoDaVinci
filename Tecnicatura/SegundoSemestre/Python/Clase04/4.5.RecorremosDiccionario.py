
#Recorremos el diccionario de la selección
seleccionArgentina = {
    10: {'Nombre': 'Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo derecho' },
    22: {'Nombre': 'Martínez', 'Edad': 31, 'Altura': 1.90, 'Precio': '20 millones', 'Posicion': 'Arquero' },
    5:  {'Nombre': 'De Paul', 'Edad': 29, 'Altura': 1.82, 'Precio': '40 millones', 'Posicion': 'Centrocampista' },
    14: {'Nombre': 'Otamendi', 'Edad': 36, 'Altura': 1.83, 'Precio': '15 millones', 'Posicion': 'Defensa'},
    8:  {'Nombre': 'Paredes', 'Edad': 29, 'Altura': 1.80, 'Precio': '25 millones', 'Posicion': 'Centrocampista'}
}

for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')

for llave, valor in seleccionArgentina.items():
    print(llave, valor)