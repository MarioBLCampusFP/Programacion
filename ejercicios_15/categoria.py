import mysql.connector.errors


def crear_categoria(conexion, cursor):
    while True:
        try:
            id_categoria = int(input("Ingrese el ID de la nueva categoría: "))
            break
        except ValueError:
            print("El ID debe ser un número entero.")
    categoria = input("Ingrese el nombre de la nueva categoría: ")
    consulta = "INSERT INTO categoria (idcategoria, categoria) VALUES (%s, %s)"
    try:
        # Ejecutar consulta SQL
        cursor.execute(consulta, (id_categoria, categoria))
        # Confirmar los cambios en la base de datos
        conexion.commit()
        print(f"La categoría {categoria} ha sido creada con éxito.")
    except mysql.connector.errors.IntegrityError:
        print(f"Error: El ID de categoría {id_categoria} ya existe.")


def leer_categoria(cursor):
    print("Listado de Categorías: ")
    consulta = "SELECT idcategoria, categoria FROM categoria"
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    # Listar categorías
    for id, categoria in resultado:
        print(f"{id} - {categoria}")


def actualizar_categoria(conexion, cursor):
    while True:
        try:
            id_categoria = int(input("Ingrese el ID de la categoría a actualizar: "))
            break
        except ValueError:
            print("El ID debe ser un número entero.")
    categoria = input("Ingrese el nuevo nombre de la categoría: ")
    consulta = "UPDATE categoria SET categoria = %s WHERE idcategoria = %s"
    cursor.execute(consulta, (categoria, id_categoria))
    conexion.commit()
    print(f"La categoría con ID {id_categoria} ha sido actualizada a {categoria}")


def eliminar_categoria(conexion, cursor):
    while True:
        try:
            id_categoria = int(input("Ingrese el ID de la categoría a eliminar: "))
            break
        except ValueError:
            print("El ID debe ser un número entero.")
    consulta = "DELETE from categoria WHERE idcategoria = %s"
    cursor.execute(consulta, (id_categoria,))
    conexion.commit()
    print(f"La categoría con ID {id_categoria} ha sido eliminada.")
