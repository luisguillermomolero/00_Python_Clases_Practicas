from abc import ABC, abstractmethod

class EstrategiaDescuento(ABC):
    
    @abstractmethod
    def calcular(self, monto):
        pass
    
class SinDescuento(EstrategiaDescuento):
    
    def calcular(self, monto):
        return monto

class DescuentoPorcentaje(EstrategiaDescuento):
    
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje
        
    def calcular(self, monto):
        return monto - (monto * self.porcentaje / 100)

class DescuentoFijo(EstrategiaDescuento):
    
    def __init__(self, montoDescuento):
        self.montoDescuento = montoDescuento
    
    def calcular(self, monto):
        return monto - self.montoDescuento

class Pedido:
    def __init__(self, monto, estrategiaDescuento: EstrategiaDescuento):
        self.monto = monto
        self.estrategiaDescuento = estrategiaDescuento
    
    def calcularTotal(self):
        return self.estrategiaDescuento.calcular(self.monto)

pedido1 = Pedido(1000, SinDescuento())
print(f"Total sin descuento: ${pedido1.calcularTotal()}")

pedido2 = Pedido(1000, DescuentoPorcentaje(50))
print(f"Total con 50% de descuento: ${pedido2.calcularTotal()}")

pedido3 = Pedido(1000, DescuentoFijo(100))
print(f"Total con descuento fijo de $100: ${pedido3.calcularTotal()}")

    