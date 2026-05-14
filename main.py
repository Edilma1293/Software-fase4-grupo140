from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ClienteError, ServicioError, ReservaError

def registrar_log(mensaje):
    with open("logs.txt", "a") as archivo:
        archivo.write(str(mensaje) + "\n")

def pruebas_automaticas():
    print("\n EJECUTANDO 10 PRUEBAS AUTOMÁTICAS \n")

    pruebas = [
        ("Cliente valido", lambda: Cliente("Ana Maria Gomez", "1234338129")),
        ("Cliente invalido", lambda: Cliente("", "1234341480")),
        ("Servicio valido", lambda: ReservaSala("Sala VIP", 50000)),
        ("Servicio invalido", lambda: ReservaSala("Sala VIP", -100)),
        ("Reserva valida", lambda: Reserva(Cliente("Luis Sepulveda", "62828840"), ReservaSala("Sala 1", 40000), 2 )),
        ("Reserva invalida", lambda: Reserva( Cliente("Carlos Vargas", "1098285448"), ReservaSala("Sala 2", 30000),  -1 )),
        ("Equipo valido", lambda: AlquilerEquipo("Portatil", 30000)),
        ("Asesoría valida", lambda: AsesoriaEspecializada("Excel", 60000)),
        ("Documento invalido", lambda: Cliente("Maria Fernanda", "")),
        ("Reserva valida", lambda: Reserva( Cliente("Laura Salome", "1099662534"),AsesoriaEspecializada("Inteligencia Artificial", 60000),3))]

    for i, (descripcion, prueba) in enumerate(pruebas, 1):
        try:
            prueba()
            registrar_log(f"Prueba {i}: {descripcion} exitosa")

        except (ClienteError, ServicioError, ReservaError) as e:
            registrar_log(f"Prueba {i}: Error -> {e}")
            print(f"Prueba {i}: Error -> {e}")

        else:
            print(f"Prueba {i}: Exitosa")

        finally:
            print("Prueba finalizada\n")

print(" SISTEMA SOFTWARE FJ ")
pruebas_automaticas()
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
                raise ServicioError("Servicio invalido")
                

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

    except ValueError as e:
        registrar_log(e)
        print("Error: las horas deben ser un número válido")
        



