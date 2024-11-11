#   CLASE 12
#   VIDEO 5
from dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    
    contador_teclado = 0
    
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self._id_teclados = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)
    
    @property     
    def id_teclados(self):
        return self._id_teclados
    
    def __str__(self):
        return f'Id : {self._id_teclados}, Marca: {self._marca}, Tipo Entrada: {self._tipo_entrada}'
    
    # Hacemos pruebas
if __name__ == '__main__':
    teclado1 = Teclado('LogiTech', 'USB')
    print(teclado1)
    teclado2 = Teclado('HyperX', 'USB')
    print(teclado2)