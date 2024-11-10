import mysql.connector.errors


def crear_categoria(conexion):
    """Inserta una nueva categoría."""
    while True:
        try:
            id_categoria = int(input("Ingrese el ID de la nueva categoría: "))
            break
        except ValueError:
            print("El ID debe ser un número entero.")
    categoria = input("Ingrese el nombre de la nueva categoría: ")
    cursor = conexion.cursor()
    consulta = "INSERT INTO categoria (idcategoria, categoria) VALUES (%s, %s)"
    try:
        cursor.execute(consulta, (id_categoria, categoria))
        conexion.commit()
        print(f"La categoría {categoria} ha sido creada con éxito.")
    except mysql.connector.errors.IntegrityError:
        print(f"Error: El ID de categoría {id_categoria} ya existe.")
    except mysql.connector.Error as e:
        print(f"Error al insertar la categoría: {e}")
    finally:
        cursor.close()


def leer_categoria(conexion):
    """Devuelve una lista de todas las categorías."""
    print("Listado de Categorías: ")
    cursor = conexion.cursor()
    consulta = "SELECT idcategoria, categoria FROM categoria"
    try:
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        # Verificar si hay resultados
        if resultado:
            # Listar categorías
            for id_categoria, categoria in resultado:
                print(f"{id_categoria} - {categoria}")
        else:
            print("No hay categorías en la base de datos.")
    except mysql.connector.Error as e:
        print(f"Error al leer las categorías: {e}")
    finally:
        cursor.close()


def actualizar_categoria(conexion):
    """Actualiza el nombre de una categoría existente."""
    while True:
        try:
            id_categoria = int(input("Ingrese el ID de la categoría a actualizar: "))
            break
        except ValueError:
            print("El ID debe ser un número entero.")
    categoria = input("Ingrese el nuevo nombre de la categoría: ")
    cursor = conexion.cursor()
    consulta = "UPDATE categoria SET categoria = %s WHERE idcategoria = %s"
    try:
        cursor.execute(consulta, (categoria, id_categoria))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"La categoría con ID {id_categoria} ha sido actualizada a {categoria}.")
        else:
            print(f"No se encontró una categoría con ID {id_categoria}.")
    except mysql.connector.Error as e:
        print(f"Error al actualizar la categoría: {e}")
    finally:
        cursor.close()


def eliminar_categoria(conexion):
    """Elimina una categoría de la tabla `categoria`."""
    while True:
        try:
            id_categoria = int(input("Ingrese el ID de la categoría a eliminar: "))
            break
        except ValueError:
            print("El ID debe ser un número entero.")
    cursor = conexion.cursor()
    consulta = "DELETE FROM categoria WHERE idcategoria = %s"
    try:
        cursor.execute(consulta, (id_categoria,))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"La categoría con ID {id_categoria} ha sido eliminada.")
        else:
            print(f"No se encontró una categoría con ID {id_categoria}.")
    except mysql.connector.Error as e:
        print(f"Error al eliminar la categoría: {e}")
    finally:
        cursor.close()
