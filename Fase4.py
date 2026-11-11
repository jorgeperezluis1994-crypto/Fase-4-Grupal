from abc import ABC,abstractmethod
from datetime import datetime

# ========================== #
# Excepciones Personalizadas #
# ========================== #

class ClienteError(Exception):
    pass

class ReservaError(Exception):
    pass

# =============== #
#  Clase Cliente  #
# =============== #

class Cliente:
    
    def __init__(self, identificacion, nombre):
        self.__identificacion = identificacion
        self.__nombre = nombre
        
    @property
    def identificacion(self):
        return self.__identificacion
        
    @property
    def nombre(self):
        return self.__nombre
    
    def __str__(self):
        
        return f"{self.__nombre}({self.__identificacion})"
    
class servicio(ABC):
    def __init__(self, codigo, nombre, precio)
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        
    @abstractmethod
    def mostrar_detalle(self):
        pass
    
    def get_precio(self):
        return self.__precio
