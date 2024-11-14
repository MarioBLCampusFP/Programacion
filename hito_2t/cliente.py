import config


def registrar_cliente():
    """Registra un nuevo cliente."""
    # Leer dni
    dni = input("Ingrese el DNI del cliente: ")

    # Verificar si el cliente ya está registrado
    if dni in config.clientes:
        print(f"El cliente con dni {dni} ya está registrado.")
        return

    # Registrar datos personales del cliente
    nombre = input("Ingrese el nombre completo del cliente: ")
    email = input("Ingrese el correo electronico del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")

    # Crear un diccionario con los datos personales del cliente
    cliente = {
        "dni": dni,
        "nombre": nombre,
        "email": email,
        "dirección": direccion,
        "teléfono": telefono,
    }

    # Añadir cliente
    config.clientes[dni] = cliente
    print(f"El cliente {nombre} ha sido registrado con éxito.")


def visualizar_clientes():
    """Visualiza todos los clientes registrados."""
    # Mostrar los datos personales de todos los clientes
    for dni in config.clientes:
        buscar_cliente(dni)


def buscar_cliente(dni):
    """Realiza búsquedas de clientes a través de su campo único."""
    if dni in config.clientes:
        cliente = config.clientes[dni]
        # Listar todos los datos del cliente
        print(", ".join(f"{campo.capitalize()}: {cliente[campo]}" for campo in cliente))
    else:
        print(f"El cliente con dni {dni} no está registrado.")
