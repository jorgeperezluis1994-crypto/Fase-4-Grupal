# Sistema Integral de Gestion de Clientes, Servicios y Reservas

print("Bienvenido al Software FJ")

from abc import ABC, abstractmethod
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
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        
    @abstractmethod
    def mostrar_detalle(self):
        pass
    
    def get_precio(self):
        return self.precio  
    
# ============================== #
# clase heredada reserva de sala #
# ============================== #
    
class reservasala(servicio):
    def __init__(self, codigo, nombre, precio, capacidad):
        super().__init__(codigo, nombre, precio,)
        self.capacidad = capacidad
        
    def mostrar_detalle(self):
        return f"sala: {self.nombre} -capacidad: {self.capacidad}"
    
# ===================================== #
# clase heredada de reserva de equipos  #
# ===================================== #

class alquilerequipo(servicio):
    def __init__(self, codigo, nombre, precio, tipo):
        super().__init__(codigo, nombre, precio)
        self.tipo = tipo
        
    def mostrar_detalle(self):
        return f"equipo: {self.nombre}  tipo: {self.tipo}"
    
# ================================= #
# clase heredada servicio asesoria  #
# ================================= #

class asesoriaespecializada(servicio):
    def __init__(self, codigo, nombre, precio, area):
        super().__init__(codigo, nombre, precio)
        self.area = area
        
    def mostrar_detalle(self):
        return f"asesoria: {self.nombre}  area: {self.area}"

# ================================= #
# clase de reservas para el cliente #
# ================================= #

class reserva:
    def __init__(self, cliente, servicio, fecha):
        if fecha < datetime.now():
            raise ReservaError(" no se puede realizar reserva en fechas pasadas")
        
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha
        
    def mostrar_detalles(self):
        return(
            f"cliente: {self.cliente.nombre} | "
            f"servicio: {self.servicio.mostrar_detalle()} | " 
            f"fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}" 
        )
