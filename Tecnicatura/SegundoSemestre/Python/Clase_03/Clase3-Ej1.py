seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posición': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di María', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posición': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posición': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posición': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posición': 'Portero'},
    23: {'Nombre': 'Emiliano Martínez', 'Edad': 32, 'Altura': 1.96, 'Precio': '28 Millones', 'Posición': 'Portero'},
    3: {'Nombre': 'Nicolás Tagliafico', 'Edad': 32, 'Altura': 1.73, 'Precio': '8 Millones', 'Posición': 'Lateral'},
    7: {'Nombre': 'Rodrigo De Paul', 'Edad': 30, 'Altura': 1.80, 'Precio': '30 Millones', 'Posición': 'Media Punta'},
    5: {'Nombre': 'Leandro Paredes', 'Edad': 30, 'Altura': 1.82, 'Precio': '20 Millones', 'Posición': 'Volante'}
}
for valor in seleccionArgentina.items():
    print(valor)

print('Tenemos en el diccionario la cantidad de: ', end=' ')
print(len(seleccionArgentina))