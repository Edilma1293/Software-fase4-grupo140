from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ClienteError, ServicioError, ReservaError

def registrar_log(mensaje):
    with open("logs.txt", "a") as archivo:
        archivo.write(str(mensaje) + "\n")

print(" SISTEMA SOFTWARE FJ ")

while True:
    try:
        print("\n MENÚ PRINCIPAL ")
        print("1. Crear reserva")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            # CLIENTE
            nombre = input("Ingrese el nombre del cliente: ")
            documento = input("Ingrese el documento: ")
            cliente = Cliente(nombre, documento)

            # SERVICIO
            print("\nSERVICIOS DISPONIBLES")
            print("1. Sala VIP: 50.000 COP/hora")
            print("2. Alquiler Equipo: 30.000 COP/hora + 2.000 COP cargo fijo")
            print("3. Asesoría: 60.000 COP/hora + 15% adicional")

            op_servicio = input("Seleccione el servicio: ")

            horas = int(input("Ingrese horas de uso: "))

            if op_servicio == "1":
                servicio = ReservaSala("Sala VIP", 50000)

            elif op_servicio == "2":
                servicio = AlquilerEquipo("Equipo", 30000)

            elif op_servicio == "3":
                servicio = AsesoriaEspecializada("Asesoria", 60000)

            else:
                raise ServicioError("Servicio inválido")
                

            # RESERVA
            reserva = Reserva(cliente, servicio, horas)
            reserva.confirmar()
            registrar_log("Reserva creada exitosamente")

            print("\n✔ RESERVA EXITOSA")
            print("Cliente:", cliente)
            print("Estado:", reserva.estado)
            print("Total:", reserva.procesar())

        elif opcion == "2":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")

    except ClienteError as e:
        registrar_log(e)
        print("Error de cliente:", e)
    
    except ServicioError as e:
        registrar_log(e)
        print("Error de servicio:", e)
    
    except ReservaError as e:
        registrar_log(e)
        print("Error de reserva:", e)

    except ValueError:
        print("Error: las horas deben ser un número válido")



