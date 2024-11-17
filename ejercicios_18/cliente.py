import mysql.connector.errors


def crear_cliente(conexion):
    """Inserta un nuevo cliente."""
    while True:
        id_cliente = input("Ingrese el ID del nuevo cliente: ")
        if len(id_cliente) == 5:
            break
        else:
            print("El ID debe contener exactamente 5 caracteres.")
    nombre_cliente = input("Ingrese el nombre del nuevo cliente: ")
    cursor = conexion.cursor()
    consulta = "INSERT INTO cliente (idcliente, contacto) VALUES (%s, %s)"
    try:
        cursor.execute(consulta, (id_cliente, nombre_cliente))
        conexion.commit()
        print(f"El cliente {nombre_cliente} ha sido añadido con éxito.")
    except mysql.connector.errors.IntegrityError:
        print(f"Error: El ID del cliente {id_cliente} ya existe.")
    except mysql.connector.Error as e:
        print(f"Error al insertar el cliente: {e}")
    finally:
        cursor.close()


def leer_cliente(conexion):
    """Devuelve una lista de todos los clientes."""
    print("Listado de Clientes: ")
    cursor = conexion.cursor()
    consulta = "SELECT idcliente, contacto FROM cliente"
    try:
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        # Verificar si hay resultados
        if resultado:
            # Listar clientes
            for id, cliente in resultado:
                print(f"{id} - {cliente}")
        else:
            print("No hay clientes en la base de datos.")
    except mysql.connector.Error as e:
        print(f"Error al leer los clientes: {e}")
    finally:
        cursor.close()


def actualizar_cliente(conexion):
    """Actualiza el nombre de un cliente existente."""
    while True:
        id_cliente = input("Ingrese el ID del cliente a actualizar: ")
        if len(id_cliente) == 5:
            break
        else:
            print("El ID debe contener exactamente 5 caracteres.")
    nombre_cliente = input("Ingrese el nuevo nombre del cliente: ")
    cursor = conexion.cursor()
    consulta = "UPDATE cliente SET contacto = %s WHERE idcliente = %s"
    try:
        cursor.execute(consulta, (nombre_cliente, id_cliente))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"El cliente con ID {id_cliente} ha sido actualizado a {nombre_cliente}.")
        else:
            print(f"No se encontró un cliente con ID {id_cliente}.")
    except mysql.connector.Error as e:
        print(f"Error al actualizar el cliente: {e}")
    finally:
        cursor.close()


def eliminar_cliente(conexion):
    """Elimina un cliente de la tabla `cliente`."""
    while True:
        id_cliente = input("Ingrese el ID del cliente a eliminar: ")
        if len(id_cliente) == 5:
            break
        else:
            print("El ID debe contener exactamente 5 caracteres.")
    cursor = conexion.cursor()
    consulta = "DELETE FROM cliente WHERE idcliente = %s"
    try:
        cursor.execute(consulta, (id_cliente,))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"El cliente con ID {id_cliente} ha sido eliminado.")
        else:
            print(f"No se encontró un cliente con ID {id_cliente}.")
    except mysql.connector.Error as e:
        print(f"Error al eliminar el cliente: {e}")
    finally:
        cursor.close()
