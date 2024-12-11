# CLASES ABSTRACTAS EN PYTHON

from abc import ABC, abstractmethod

class Forma(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
class Circulo(Forma):
    
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return f"El área de un circulo es {3.14 * self.radio ** 2}"
    
    def perimetro(self):
        return f"El perimetro de un circulo es: {2 * 3.14 * self.radio}"
    
class Rectangulo(Forma):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return f"El área de un rectangulo es {self.base * self.altura}"
    
    def perimetro(self):
        return f"El perimetro de un rectangulo es: {2 * (self.base + self.altura)}"
        
class Cuadrado(Forma):
    
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return f"El área de un cuadraro es {self.lado ** 2}"
    
formas = [Circulo(5),
          Rectangulo(2, 10),
          Cuadrado(8),
          Rectangulo(10, 20),
          Circulo(22)
]

print("Area de las formas")
for forma in formas:
    print(forma.area())

circulo1 = Circulo(5)
rectangulo1 = Rectangulo(2, 10)

print(circulo1.perimetro())
print(rectangulo1.perimetro())
