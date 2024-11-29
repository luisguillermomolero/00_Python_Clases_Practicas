class Banco:
    
    TASA_INTERES = 0.03
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    @classmethod
    def cambiarTasa(cls, nuevaTasa):
        cls.TASA_INTERES = nuevaTasa
    
    @staticmethod
    def conversionDolaresEuros(dolares):
        return dolares * 0.85

