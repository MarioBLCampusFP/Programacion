from cliente import registrar_cliente, visualizar_clientes, buscar_cliente
from pedido import realizar_compra, seguir_compra
import config


def mostrar_menu():
    """Mostrar menú de gestión de pedidos."""
    print("\n=== Menú de gestión de pedidos ===")
    # Mostrar las opciones
    for i, opcion in enumerate(config.opciones, 1):
        print(f"{i}. {opcion}")


def ejecutar_opcion(opcion):
    """Ejecuta la opción seleccionada por el usuario en el menú."""
    # Verificar que la opción esté dentro del rango de opciones
    if 1 <= opcion < len(config.opciones):
        # Mostrar un subtitulo para la opción seleccionada
        print(f"\n--- {config.opciones[opcion - 1]} ---")

    if opcion == 1:
        registrar_cliente()
    elif opcion == 2:
        if config.clientes:
            visualizar_clientes()
        else:
            print("No hay clientes registrados.")
    elif opcion == 3:
        dni = input("Ingrese el DNI del cliente a buscar: ")
        buscar_cliente(dni)
    elif opcion == 4:
        realizar_compra()
    elif opcion == 5:
        if config.pedidos:
            id_pedido = input("Ingrese el ID del pedido: ")
            seguir_compra(id_pedido)
        else:
            print("No hay pedidos registrados.")
    elif opcion == 6:
        # Salir del programa
        exit()
    else:
        print("Opción no válida.")
