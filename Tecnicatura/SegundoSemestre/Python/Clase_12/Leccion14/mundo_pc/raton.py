#   CLASE 12
#   VIDEO 4
from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    
    contador_ratones = 0
    
    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)
    
    @property 
    def id_raton(self):
        return self._id_raton
    
    def __str__(self):
        return f'Id: {self._id_raton}, Marca: {self._marca}, Tipo Entrada: {self._tipo_entrada}'
    
# Hacemos pruebas
if __name__ == '__main__':
    raton1 = Raton('LogiTech', 'USB')
    print(raton1)
    raton2 = Raton('HyperX', 'Wireless/USB')
    print(raton2)