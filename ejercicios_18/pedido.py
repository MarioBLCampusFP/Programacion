import mysql.connector


def crear_pedido(conexion):
    """Inserta un nuevo pedido."""
    while True:
        try:
            id_pedido = int(input("Ingrese el ID del nuevo pedido: "))
            break
        except ValueError:
            print("Ingrese un número válido.")
    id_cliente = input("Ingrese el ID del cliente: ")
    cursor = conexion.cursor()
    consulta = "INSERT INTO pedido (idpedido, idcliente, fechapedido) VALUES (%s, %s, CURDATE())"
    try:
        cursor.execute(consulta, (id_pedido, id_cliente))
        conexion.commit()
        print(f"El pedido {id_pedido} ha sido añadido con éxito.")

        # Crear detalles del pedido
        id_producto = int(input("Ingrese el ID del producto: "))
        unidades = int(input("Ingrese las unidades: "))
        consulta = "INSERT INTO detalle (idpedido, idproducto, unidades) VALUES (%s, %s, %s)"
        cursor.execute(consulta, (id_pedido, id_producto, unidades))
        conexion.commit()
        print("Detalle añadido exitosamente.")
    except mysql.connector.Error as e:
        print(f"Error al insertar el pedido: {e}")
    except ValueError:
        print("Ingrese un número válido.")
    finally:
        cursor.close()


def leer_pedido(conexion):
    """Devuelve una lista de todos los pedidos y sus detalles."""
    print("Listado de pedidos: ")
    cursor = conexion.cursor()
    consulta = """
    SELECT p.idpedido, pr.nombre, d.unidades
    FROM pedido p
    JOIN detalle d ON p.idpedido = d.idpedido
    JOIN producto pr ON d.idproducto = pr.idproducto
    ORDER BY p.idpedido
    """
    try:
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        # Verificar si hay resultados
        if resultado:
            # Listar pedidos
            for idpedido, producto, unidades in resultado:
                print(f"ID: {idpedido}, Producto: {producto}, Unidades: {unidades}")
        else:
            print("No hay pedidos en la base de datos.")
    except mysql.connector.Error as e:
        print(f"Error al leer los pedidos: {e}")
    finally:
        cursor.close()


def actualizar_pedido(conexion):
    """Actualiza las unidades de un pedido existente."""
    while True:
        try:
            id_pedido = int(input("Ingrese el ID del pedido a actualizar: "))
            break
        except ValueError:
            print("El ID debe ser un número entero.")
    while True:
        try:
            unidades_pedido = int(input("Nueva cantidad de unidades: "))
            break
        except ValueError:
            print("Ingrese un número válido para las unidades.")
    cursor = conexion.cursor()
    consulta = "UPDATE detalle SET unidades = %s WHERE idpedido = %s"
    try:
        cursor.execute(consulta, (unidades_pedido, id_pedido))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"Unidades del pedido {id_pedido} actualizadas a {unidades_pedido}.")
        else:
            print(f"No se encontró un pedido con ID {id_pedido}.")
    except mysql.connector.Error as e:
        print(f"Error al actualizar el pedido: {e}")
    finally:
        cursor.close()


def eliminar_pedido(conexion):
    """Elimina un pedido de la tabla `pedido`."""
    while True:
        try:
            id_pedido = int(input("Ingrese el ID del pedido a eliminar: "))
            break
        except ValueError:
            print("El ID debe ser un número entero.")
    cursor = conexion.cursor()
    # Eliminar primero el detalle debido a la restricción de la clave foránea
    consulta_detalle = "DELETE from detalle WHERE idpedido = %s"
    consulta_pedido = "DELETE from pedido WHERE idpedido = %s"
    try:
        cursor.execute(consulta_detalle, (id_pedido,))
        cursor.execute(consulta_pedido, (id_pedido,))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"El pedido con ID {id_pedido} ha sido eliminado.")
        else:
            print(f"No se encontró un pedido con ID {id_pedido}.")
    except mysql.connector.Error as e:
        print(f"Error al eliminar el pedido: {e}")
    finally:
        cursor.close()
