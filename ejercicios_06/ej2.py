vehiculos = {}

while True:
    # Pedir input al usuario hasta que escriba fin
    vehiculo = input("Vehículo: ")
    if vehiculo.lower() == "fin":
        break
    # Pedir al usuario que elija el estado de revisión
    revision = input(f"0- Pendiente\n1- Aprobada\nRevisión: ")
    # Validar entrada y almacenarla en el diccionario vehículos
    if revision in ['0', '1']:
        vehiculos[vehiculo] = bool(int(revision))
    else:
        print("Revisión incorrecta.")

# Mostrar vehículos que han pasado la revisión
print(list(filter(lambda v: vehiculos[v], vehiculos)))