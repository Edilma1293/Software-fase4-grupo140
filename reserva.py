from excepciones import ReservaError

class Reserva:

    def __init__(self, cliente, servicio, horas):

        #  Validamos el cliente
        if cliente is None:
            raise ReservaError("El cliente no puede ser nulo")

        #  Validamos el servicio
        if servicio is None:
            raise ReservaError("El servicio no puede ser nulo")

        # validamos las horas (tipo + valor)
        try:
            if not isinstance(horas, (int, float)) or horas <= 0:
                raise ValueError("Horas invalidas")
        except ValueError as e:
            raise ReservaError("Las horas deben ser un numero mayor a cero") from e

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"
        
    # CAMBIOS DE ESTADO

    def confirmar(self):
        if self.estado != "Pendiente":
            raise ReservaError("La reserva no se puede confirmar en este estado")
        self.estado = "Confirmada"

    def cancelar(self):
        if self.estado == "Cancelada":
            raise ReservaError("La reserva ya esta cancelada")
        self.estado = "Cancelada"

    # PROCESO PRINCIPAL

    def procesar(self):
        return self.servicio.calcular_costo(self.horas)

    # REPRESENTACIÓN

    def __str__(self):
        return f"{self.cliente} - {self.servicio.get_nombre()} - {self.estado}"
