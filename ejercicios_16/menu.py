from categoria import *
from producto import *


def gestionar_categoria(conexion):
    """Gestiona las operaciones de categorías."""
    while True:
        print("=== Gestión de Categorías ===")
        print("Seleccione una opción:")
        print("1. Crear nueva categoría")
        print("2. Leer categorías existentes")
        print("3. Actualizar una categoría")
        print("4. Eliminar una categoría")
        print("5. Salir")

        opcion = input("Opción: ")
        if opcion == "1":
            crear_categoria(conexion)
        elif opcion == "2":
            leer_categoria(conexion)
        elif opcion == "3":
            actualizar_categoria(conexion)
        elif opcion == "4":
            eliminar_categoria(conexion)
        elif opcion == "5":
            exit()
        else:
            print("Opción inválida.")


def gestionar_producto(conexion):
    """Gestiona las operaciones de productos."""
    while True:
        print("=== Gestión de Productos ===")
        print("Seleccione una opción:")
        print("1. Crear nuevo producto")
        print("2. Leer productos existentes")
        print("3. Actualizar un producto")
        print("4. Eliminar un producto")
        print("5. Salir")

        opcion = input("Opción: ")
        if opcion == "1":
            crear_producto(conexion)
        elif opcion == "2":
            leer_producto(conexion)
        elif opcion == "3":
            actualizar_producto(conexion)
        elif opcion == "4":
            eliminar_producto(conexion)
        elif opcion == "5":
            exit()
        else:
            print("Opción inválida.")


def mostrar_menu(conexion):
    """Muestra el menú principal para seleccionar la tabla."""
    while True:
        print("=== Seleccione una tabla ===")
        print("1. Categoría")
        print("2. Producto")

        tabla = input("Tabla: ")
        if tabla == "1":
            gestionar_categoria(conexion)
        elif tabla == "2":
            gestionar_producto(conexion)
        else:
            print("Seleccione una tabla listada.")