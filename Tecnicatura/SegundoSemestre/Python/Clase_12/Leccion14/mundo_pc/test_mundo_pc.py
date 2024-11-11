#   CLASE 12
#   VIDEO 9
from orden import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado


teclado1 = Teclado('LogiTech', 'Wireless')
monitor1 = Monitor('Zowie',"24'")
raton1 = Raton('Hyperx', 'Wireless')
computadora1 = Computadora('HP',monitor1,teclado1,raton1)
#print(computadora1)

teclado2 = Teclado('Noga', 'USB')
monitor2 = Monitor('Samsung',"18'")
raton2 = Raton('Redragon', 'USB')
computadora2 = Computadora('ACER',monitor2,teclado2,raton2)
#print(computadora2)

teclado3 = Teclado('Hyperx', 'USB')
monitor3 = Monitor('LG',"20'")
raton3 = Raton('LogiTech', 'Wireless')
computadora3 = Computadora('ASUS',monitor3,teclado3,raton3)
#print(computadora3)

teclado4 = Teclado('Redragon', 'Wireless')
monitor4 = Monitor('Samsung',"27'")
raton4 = Raton('Noga', 'USB')
computadora4 = Computadora('Philips',monitor4,teclado4,raton4)
#print(computadora4)

teclado5 = Teclado('Logitech', 'Wireless')
monitor5 = Monitor('Zowie',"30'")
raton5 = Raton('Logitech', 'Wireless')
computadora5 = Computadora('AORUS',monitor5,teclado5,raton5)
#print(computadora5)

computadora6 = Computadora('AORUS', monitor1, teclado2, raton4)
computadora7 = Computadora('ASUS', monitor2, teclado3, raton5)

computadoras1 = [computadora1,computadora2, computadora7, computadora4]
orden1 = Orden(computadoras1)
orden1.agregar_computadoras(computadora3)
print(orden1)

computadoras2 = [computadora3,computadora5,computadora6]
orden2 = Orden(computadoras2)
orden2.agregar_computadoras(computadora1)
print(orden2)