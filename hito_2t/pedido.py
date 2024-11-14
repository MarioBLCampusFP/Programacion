from cliente import buscar_cliente
import config

def realizar_compra():
    """Crea un pedido a partir de los productos seleccionados."""
    # Leer dni
    dni = input("Ingrese el DNI del cliente: ")

    # Comprobar que el cliente esté registrado
    if dni not in config.clientes:
        print(f"El cliente con dni {dni} no está registrado.")
        return

    # Generar el id del pedido
    id_pedido = len(config.pedidos) + 1

    # Crear cesta de compra
    cesta_compra = []

    # Listar productos
    print("\nProductos a la venta:")
    for id, producto in config.productos.items():
        print(f"ID: {id}, Nombre: {producto['nombre']}, Precio: {producto['precio']:.2f}€")

    while True:
        # Leer id del producto
        id_producto = input("Ingrese el ID del producto (o 'fin' para terminar): ")

        # Finalizar compra
        if id_producto == "fin":
            break

        try:
            producto = config.productos[int(id_producto)]
            # Añadir el producto a la lista de productos a comprar
            cesta_compra.append(producto)
            print(f"El producto {producto['nombre']} ha sido añadido a la cesta.")
        except (ValueError, KeyError):
            print("Ingrese un ID válido.")

    # Crear el pedido
    pedido = {"productos": cesta_compra, "cliente": dni}

    # Añadir pedido
    config.pedidos[id_pedido] = pedido

    # Mostrar el id del pedido
    print(f"ID del pedido: {id_pedido}")


def seguir_compra(id_pedido):
    """Visualiza todos los datos relacionados a un pedido."""
    try:
        pedido = config.pedidos[int(id_pedido)]
    except (ValueError, KeyError):
        print("ID del pedido inválido.")
        return

    # Listar datos del cliente
    print("\nDatos del cliente:")
    buscar_cliente(pedido["cliente"])

    # Almacenar el precio total de la compra
    total = 0

    # Listar datos del pedido
    print("\nPedido:")
    for producto in pedido["productos"]:
        print(f"{producto["nombre"]} - {producto["precio"]:.2f}€")
        # Sumar el precio del producto al total
        total += producto["precio"]
    # Mostrar el total a pagar
    print(f"\nTotal a pagar: {total:.2f}€")
