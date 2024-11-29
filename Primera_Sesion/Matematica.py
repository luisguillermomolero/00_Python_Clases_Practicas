# Métodos Estáticos
class Matematica:
    
    @staticmethod
    def suma(a, b):
        return a +b
    
    @staticmethod
    def resta(a, b):
        return a - b
    
print(Matematica.suma(10, 10))
print(Matematica.resta(10, 5))
