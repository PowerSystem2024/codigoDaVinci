#   CLASE 12
#   VIDEO 3
class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._marca = marca
        self._tipo_entrada = tipo_entrada
        
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self,marca):
        self._marca = marca
        
    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    
    @tipo_entrada.setter
    def tipo_entrada(self,tipo_entrada):
        self._tipo_entrada = tipo_entrada
    