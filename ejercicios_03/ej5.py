# Difinir menú
menu = {
    "Café": (1.5, 50),
    "Té": (1.0, 0),
    "Bocadillo": (3.0, 300),
    "Ensalada": (2.5, 150)
}

# Mostrar menú
print("Menú:")
for producto in menu:
    precio = menu[producto][0]
    cal = menu[producto][1]
    print(f"- {producto}: {precio}€ ({cal} cal)")


# Almacenar pedido
pedido = []
total = 0
cal_tot = 0

while True:
    # Pedir al usuario que añada productos
    producto = input("Ingresa el nombre del producto que deseas agregar (o 'fin' para terminar): ")
    # Parar bucle
    if producto == "fin":
        break
    # Añadir producto
    pedido.append(producto)
    # Sumar precio y calorías pedido
    total += menu[producto][0]
    cal_tot += menu[producto][1]

# Mostrar pedido
print("Tu pedido:")
for producto in pedido:
    print(f"- {producto}")

# Mostrar total a pagar y calorías totales
print(f"Total a pagar: {total}€")
print(f"Calorías totales: {cal_tot} cal")