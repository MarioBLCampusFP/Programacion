# Definir contraseña predeterminada
contraseña = "python123"

# Mostrar contraseña
print(f"Contraseña establecida: {contraseña}")

# Solicitar al usuario que ingrese la contraseña
while True:
    contraseña_solicitada = input("Ingrese la contraseña: ")
    # Informar al usuario
    if contraseña_solicitada == contraseña:
        print("¡Acceso concedido!")
        break
    else:
        print("Contraseña incorrecta, intenta de nuevo.")