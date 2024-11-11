#   CLASE 12
#   VIDEO 7
from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Computadora:
    
    contador_computadoras = 0
    
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras 
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        
    @property
    def id_computadora(self):
        return self._id_computadora
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def monitor(self):
        return self._monitor
    
    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor
        
    @property
    def teclado(self):
        return self._teclado
    
    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado
        
    @property
    def raton(self):
        return self._raton
    
    @raton.setter
    def raton(self, raton):
        self._raton = raton
    
    def __str__(self):
        return f'''
            {self._nombre}: {self._id_computadora}
            Monitor: {self._monitor}
            Teclado: {self._teclado}
            Raton: {self._raton}
        '''
        
if __name__ == '__main__':
    teclado1 = Teclado('LogiTech', 'Wireless')
    monitor1 = Monitor('Zowie',"24'")
    raton1 = Raton('Hyperx', 'Wireless')
    computadora1 = Computadora('HP',monitor1,teclado1,raton1)
    print(computadora1)
    
    teclado2 = Teclado('Noga', 'USB')
    monitor2 = Monitor('Samsung',"18'")
    raton2 = Raton('Redragon', 'USB')
    computadora2 = Computadora('ACER',monitor2,teclado2,raton2)
    print(computadora2)