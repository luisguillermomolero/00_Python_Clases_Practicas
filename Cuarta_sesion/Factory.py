from abc import ABC, abstractmethod

#Clase abstracta = Superclase "Clases"
class Clases(ABC):
    @abstractmethod
    def operacion(self):
        pass

# Creacion de subclases
class ClaseA(Clases):
    def operacion(self):
        return "Esta es la clase A"
    
class ClaseB(Clases):
    def operacion(self):
        return "Esta es la clase B"
    
    def impresion(self):
        pass
    
    def consulta(self):
        pass
    
    def retiro(self):
        pass
    

# Clase Factory: Factoria, Fabrica
class FabricaClases:
    
    @staticmethod
    def creacionObjetos(tipoObjeto):
        if tipoObjeto == "A":
            return ClaseA()
        elif tipoObjeto == "B":
            return ClaseB()
        else:
            raise ValueError(f"La clase {tipoObjeto} no existe")

#objeto1 = FabricaClases.creacionObjetos("A")
objeto2 = FabricaClases.creacionObjetos("B")

#print(objeto1.operacion())
print(objeto2.operacion())


