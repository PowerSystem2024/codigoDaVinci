#   CLASE 12
#   VIDEO 6
class Monitor:

    contador_monitores = 0
    
    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamanio = tamanio
    
    @property     
    def id_monitor(self):
        return self._id_monitor
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca
        
    @property
    def tamanio(self):
        return self._tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio
        
    def __str__(self):
        return f'Id: {self._id_monitor}, Marca: {self._marca}, Tamanio: {self._tamanio}'
    
if __name__ == "__main__":
    monitor1 = Monitor("Samsung", "15'")
    print(monitor1)
    monitor2 = Monitor("Zowie", "24'")
    print(monitor2)