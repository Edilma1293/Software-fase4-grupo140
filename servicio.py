from abc import ABC, abstractmethod
from excepciones import ServicioError

# CLASE ABSTRACTA

class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        if not nombre or not nombre.strip():
            raise ServicioError("El nombre del servicio no puede estar vacio")

        if not isinstance(tarifa, (int, float)) or tarifa <= 0:
            raise ServicioError("La tarifa debe ser un numero mayor a cero")

        self._nombre = nombre
        self._tarifa = tarifa

    def get_nombre(self):
        return self._nombre

    def get_tarifa(self):
        return self._tarifa

    @abstractmethod
    def calcular_costo(self, horas, descuento=0):
        pass

# SERVICIO 1: SALA

class ReservaSala(Servicio):

    def calcular_costo(self, horas, descuento=0):
        if horas <= 0:
            raise ServicioError("Horas invalidas")
        total = self._tarifa * horas
        return total - (total * descuento)


# SERVICIO 2: EQUIPOS

class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas, descuento=0):
        if horas <= 0:
            raise ServicioError("Horas invalidas")
        total = (self._tarifa * horas) + 2000 # cargo fijo
        return total - (total * descuento)


# SERVICIO 3: ASESORIA

class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas, descuento=0):
        if horas <= 0:
            raise ServicioError("Horas invalidas")
        total = (self._tarifa * horas) * 1.15 # impuesto de 15 %
        return total - (total * descuento)
