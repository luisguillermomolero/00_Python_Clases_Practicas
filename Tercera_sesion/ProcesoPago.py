# INTERFASES EN PYTHON

from abc import ABC, abstractmethod

class ProcesoPago(ABC):
    
    @abstractmethod
    def procesoPago(self, cantidad: float) -> None:
        pass
    
    @abstractmethod
    def reembolsoPago(self, transaccionId: str) -> None:
        pass

class Paypal(ProcesoPago):
    
    def procesoPago(self, cantidad: float) -> None:
        print(f"Procesando pago de ${cantidad} por Paypal")
        
    def reembolsoPago(self, transaccionId: str) -> None:
        print(f"Reembolsando Id transacción número {transaccionId} por Paypal")

class Stripe(ProcesoPago):
    
    def procesoPago(self, cantidad: float) -> None:
        print(f"Procesando pago de ${cantidad} por Stripe")
    
    def reembolsoPago(self, transaccionId: str) -> None:
        print(f"Reembolsando Id transacción número {transaccionId} por Stripe")
    

if __name__ == "__main__":
    procesoPaypal = Paypal()
    procespStripe = Stripe()
    
    procesoPaypal.procesoPago(500.0)
    procesoPaypal.reembolsoPago("FDCS1254XE987")
    
    procespStripe.procesoPago(1000.0)
    procespStripe.reembolsoPago("FDCS1254XE987")

