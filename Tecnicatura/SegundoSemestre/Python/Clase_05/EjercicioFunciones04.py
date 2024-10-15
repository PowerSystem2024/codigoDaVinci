"""
Ejercicio 4: Calculadora de Impuestos
Crear una funcion para calcular el total de un pago incluyendo
un impuesto aplicado. (IVA)
Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
Proporcione el pago sin impuesto: 1000
Proporcione el monto del impuesto: 21%
Pago con impuesto: xxxxx
"""
# Definimos la funcion
def calcularImpuesto(pago,impuesto):
    pagoTotal = pago + (pago * (impuesto/100))
    return pagoTotal
pagoSinImpuesto = int(input('Digite el pago sin impuesto: '))
impuesto = int(input('Digite el porcentaje de impuesto (sin %): '))
print(f'El pago total con impuesto seria: {calcularImpuesto(pagoSinImpuesto,impuesto)}')