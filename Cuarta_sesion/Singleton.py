# Patrón de diseño Singleton

class SingletonCreacionInstancia:
    
    _instancia = None
    
    def __new__(cls, *args, **kwargs):
        
        if not cls._instancia:
            cls._instancia = super(SingletonCreacionInstancia, cls)._new_(cls)
        return cls._instancia
    
    