# Segundo ejercicio de Composición
class Tarea:
    def __init__(self):
        pass
    
    def ejecutar(self):
        pass

class TrabajoProyecto(Tarea):
    
    def __init__(self):
        pass
    
    def ejecutar(self):
        return("Trabajando en un proyecto")

class Capacitacion(Tarea):
    
    def __init__(self):
        pass
    
    def ejecutar(self):
        return "Tomando una capacitación"

class Evaluacion(Tarea):
    
    def __init__(self):
        pass
    
    def ejecutar(self):
        return "Desarrollando una evaluación de personal"

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []
        
    def asignar_tarea(self, tarea):
        self.tareas.append(tarea)
    
    def realizar_tarea(self):
        print(f"{self.nombre}, esta desarrollando las siguientes tareas:")
        for tarea in self.tareas:
            print(f"- {tarea.ejecutar()}")

proyecto = TrabajoProyecto()
capacitacion = Capacitacion()
evaluacion = Evaluacion()

empleado = Empleado("Luis")
empleado.asignar_tarea(proyecto)
empleado.asignar_tarea(evaluacion)
empleado.asignar_tarea(evaluacion)
empleado.asignar_tarea(capacitacion)

empleado.realizar_tarea()
