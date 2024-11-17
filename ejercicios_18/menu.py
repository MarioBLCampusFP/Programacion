from categoria import crear_categoria, leer_categoria, actualizar_categoria, eliminar_categoria
from producto import crear_producto, leer_producto, actualizar_producto, eliminar_producto
from cliente import crear_cliente, leer_cliente, actualizar_cliente, eliminar_cliente
from pedido import crear_pedido, leer_pedido, actualizar_pedido, eliminar_pedido


def gestionar_categoria(conexion):
    """Gestiona las operaciones de categorías."""
    while True:
        print("\n=== Gestión de Categorías ===")
        print("Seleccione una opción:")
        print("1. Crear nueva categoría")
        print("2. Leer categorías existentes")
        print("3. Actualizar una categoría")
        print("4. Eliminar una categoría")
        print("5. Elejir otra tabla")
        print("6. Salir")

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
            mostrar_menu(conexion)
        elif opcion == "6":
            exit()
        else:
            print("Opción inválida.")


def gestionar_producto(conexion):
    """Gestiona las operaciones de productos."""
    while True:
        print("\n=== Gestión de Productos ===")
        print("Seleccione una opción:")
        print("1. Crear nuevo producto")
        print("2. Leer productos existentes")
        print("3. Actualizar un producto")
        print("4. Eliminar un producto")
        print("5. Elejir otra tabla")
        print("6. Salir")

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
            mostrar_menu(conexion)
        elif opcion == "6":
            exit()
        else:
            print("Opción inválida.")


def gestionar_cliente(conexion):
    """Gestiona las operaciones de clientes."""
    while True:
        print("\n=== Gestión de Clientes ===")
        print("Seleccione una opción:")
        print("1. Crear nuevo cliente")
        print("2. Leer clientes existentes")
        print("3. Actualizar un cliente")
        print("4. Eliminar un cliente")
        print("5. Elejir otra tabla")
        print("6. Salir")

        opcion = input("Opción: ")
        if opcion == "1":
            crear_cliente(conexion)
        elif opcion == "2":
            leer_cliente(conexion)
        elif opcion == "3":
            actualizar_cliente(conexion)
        elif opcion == "4":
            eliminar_cliente(conexion)
        elif opcion == "5":
            mostrar_menu(conexion)
        elif opcion == "6":
            exit()
        else:
            print("Opción inválida.")


def gestionar_pedidos(conexion):
    """Gestiona las operaciones de pedidos."""
    while True:
        print("\n=== Gestión de Pedidos ===")
        print("Seleccione una opción:")
        print("1. Crear nuevo pedido")
        print("2. Leer pedidos existentes")
        print("3. Actualizar un pedido")
        print("4. Eliminar un pedido")
        print("5. Elejir otra tabla")
        print("6. Salir")

        opcion = input("Opción: ")
        if opcion == "1":
            crear_pedido(conexion)
        elif opcion == "2":
            leer_pedido(conexion)
        elif opcion == "3":
            actualizar_pedido(conexion)
        elif opcion == "4":
            eliminar_pedido(conexion)
        elif opcion == "5":
            mostrar_menu(conexion)
        elif opcion == "6":
            exit()
        else:
            print("Opción inválida.")


def mostrar_menu(conexion):
    """Muestra el menú principal para seleccionar la tabla."""
    while True:
        print("\n=== Seleccione una tabla ===")
        print("1. Categoría")
        print("2. Producto")
        print("3. Cliente")
        print("4. Pedido")
        print("5. Salir")

        tabla = input("Tabla: ")
        if tabla == "1":
            gestionar_categoria(conexion)
        elif tabla == "2":
            gestionar_producto(conexion)
        elif tabla == "3":
            gestionar_cliente(conexion)
        elif tabla == "4":
            gestionar_pedidos(conexion)
        elif tabla == "5":
            exit()
        else:
            print("Seleccione una tabla listada.")
