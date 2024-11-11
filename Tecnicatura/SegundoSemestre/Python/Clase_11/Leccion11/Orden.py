#   CLASE 11 Parte 1
#   VIDEO 2
from Producto import Producto

class Orden:
    contador_ordenes = 0
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)
        
    def agregar_proucto(self, producto):
        self._productos.append(producto) # Esto es para agregar un nuevo producto

#   VIDEO 3
    def calcular_total(self):
        total = 0 # Variable temporal para almacenar el total temporal
        for producto in self._productos:
            total += producto.precio
        return total
    
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__()+'|'
        return f'Orden: {self._id_orden}, \nProducto/s: {productos_str}'
    
if __name__ == '__main__': 
    producto1 = Producto('Camiseta',100.00)
    producto2 = Producto('Pantalon',150.00)
    productos1 = [producto1,producto2] # Lista de productos
    orden1 = Orden(productos1) # Primer objeto orden pasando la lista de productos
    print(orden1)
    
    #   VIDEO 4
    orden2 = Orden(productos1)
    print(orden2)
# Tarea: Modificar la orden2 ingresando nuevos productos con sus nombres y precios
# crear una nueva lista de productos y agregarla a la orden2
    producto3 = Producto('Chomba', 250.00)
    producto4 = Producto('Cargo', 300.00)
    productos2 = [producto3,producto4]
    orden2 = Orden(productos2)
    print(orden2)