from categoria import *


def mostrar_menu(conexion, cursor):
    while True:
        menu = """
=== Gestión de Categorías ===
Seleccione una opción:
1. Crear nueva categoría
2. Leer categorías existentes
3. Actualizar una categoría
4. Eliminar una categoría
5. Salir
"""
        print(menu)
        opcion = input("Opción: ")
        if opcion == "1":
            crear_categoria(conexion, cursor)
        elif opcion == "2":
            leer_categoria(cursor)
        elif opcion == "3":
            actualizar_categoria(conexion, cursor)
        elif opcion == "4":
            eliminar_categoria(conexion, cursor)
        elif opcion == "5":
            exit()
        else:
            print("Opción inválida.")
