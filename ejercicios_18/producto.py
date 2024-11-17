import mysql.connector.errors


def crear_producto(conexion):
    """Inserta un nuevo producto."""
    while True:
        try:
            id_producto = int(input("Ingrese el ID del nuevo producto: "))
            break
        except ValueError:
            print("El ID debe ser un número entero.")
    nombre_producto = input("Ingrese el nombre del nuevo producto: ")
    cursor = conexion.cursor()
    consulta = "INSERT INTO producto (idproducto, nombre) VALUES (%s, %s)"
    try:
        cursor.execute(consulta, (id_producto, nombre_producto))
        conexion.commit()
        print(f"El producto {nombre_producto} ha sido añadido con éxito.")
    except mysql.connector.errors.IntegrityError:
        print(f"Error: El ID del producto {id_producto} ya existe.")
    except mysql.connector.Error as e:
        print(f"Error al insertar el producto: {e}")
    finally:
        cursor.close()


def leer_producto(conexion):
    """Devuelve una lista de todos los productos."""
    print("Listado de Productos: ")
    cursor = conexion.cursor()
    consulta = "SELECT idproducto, nombre FROM producto"
    try:
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        # Verificar si hay resultados
        if resultado:
            # Listar productos
            for id, producto in resultado:
                print(f"{id} - {producto}")
        else:
            print("No hay productos en la base de datos.")
    except mysql.connector.Error as e:
        print(f"Error al leer los productos: {e}")
    finally:
        cursor.close()


def actualizar_producto(conexion):
    """Actualiza el nombre de un producto existente."""
    while True:
        try:
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            break
        except ValueError:
            print("El ID debe ser un número entero.")
    nombre_producto = input("Ingrese el nuevo nombre del producto: ")
    cursor = conexion.cursor()
    consulta = "UPDATE nombre SET nombre = %s WHERE idproducto = %s"
    try:
        cursor.execute(consulta, (nombre_producto, id_producto))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"El producto con ID {id_producto} ha sido actualizado a {nombre_producto}.")
        else:
            print(f"No se encontró un producto con ID {id_producto}.")
    except mysql.connector.Error as e:
        print(f"Error al actualizar el producto: {e}")
    finally:
        cursor.close()


def eliminar_producto(conexion):
    """Elimina un producto de la tabla `producto`."""
    while True:
        try:
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            break
        except ValueError:
            print("El ID debe ser un número entero.")
    cursor = conexion.cursor()
    consulta = "DELETE from producto WHERE idproducto = %s"
    try:
        cursor.execute(consulta, (id_producto,))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"El producto con ID {id_producto} ha sido eliminado.")
        else:
            print(f"No se encontró un producto con ID {id_producto}.")
    except mysql.connector.Error as e:
        print(f"Error al eliminar el producto: {e}")
    finally:
        cursor.close()
