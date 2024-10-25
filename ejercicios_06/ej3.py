empleados = {}

while True:
    # Pedir input al usuario hasta que escriba fin
    empleado = input("Empleado: ")
    if empleado.lower() == "fin":
        break
    # Pedir al usuario que elija el estado laboral del empleado
    estado = input(f"0- Inactivo\n1- Activo\nEstado laboral: ")
    # Validar entrada y almacenarla en el diccionario
    if estado in ['0', '1']:
        empleados[empleado] = bool(int(estado))
    else:
        print("Ingrese un estado válido.")

# Mostrar empleados activos
print(list(filter(lambda v: empleados[v], empleados)))