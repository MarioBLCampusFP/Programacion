def es_perecedero(producto):
    # Devolver el valor almacenado junto a cada producto
    return productos[producto]


# Definir productos como un diccionario producto:perecedero
productos = {
    "Plátano": True,
    "Arroz": False,
    "Lentejas": False,
    "Espinaca": True
}

# Mostrar productos perecederos
print(list(filter(es_perecedero, productos)))