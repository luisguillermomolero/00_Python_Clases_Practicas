class Empleado:
    
    def __init__(self, nombre, salario):
        self._nombre = nombre
        self._salario = salario
        self.salarioMinimo = 1300000
    
    def mostarInformacion(self):
        return f"Nombre: {self._nombre}, Salario: {self._salario}"
    
    def obtenerSalario(self):
        return self._salario
    
    def establecerSalario(self, nuevoSalario):
        if nuevoSalario < self.salarioMinimo:
            return f"El salario no puede ser menor al salarior minimo"
        self._salario = nuevoSalario
        return f"El nuevo salario es: {self._salario}"
    
    def asignacionesSalariales(self):
        pass

    def deduccionesSalariales(self):
        pass

empleado1 = Empleado("Carlos", 1500000)

print(empleado1.mostarInformacion())
print(empleado1.obtenerSalario())
print(empleado1.establecerSalario(1200000))
print(empleado1.establecerSalario(2500000))
    