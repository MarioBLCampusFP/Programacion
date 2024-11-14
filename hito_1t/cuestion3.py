def obtener_cantidad(mensaje):
    # Validar la entrada antes de devolver la cantidad
    while True:
        try:
            # Pedir cantidad con mensaje personalizado
            cantidad = float(input(mensaje))
        except ValueError:
            continue
        # Devolver cantidad
        return cantidad


# Almacenar datos para estadísticas
ingresos = 0
retiros = 0

while True:
    # Pedir saldo inicial de la cuenta
    saldo = obtener_cantidad("Saldo inicial de la cuenta: ")

    # Salir del bucle si el saldo es positivo
    if saldo >= 0:
        break

while True:
    # Mostrar menú
    print("MENU")
    print("1 - Ingresar dinero")
    print("2 - Retirar dinero")
    print("3 - Mostrar saldo")
    print("4 - Estadísticas")
    print("5 - Salir")

    # Pedir al usuario que elija una opción
    opcion = input("Dime una opción: ")

    # Ingresar dinero
    if opcion == '1':
        # Pedir cantidad a ingresar
        cantidad = obtener_cantidad("Dinero a ingresar: ")

        # Comprobar si es una cantidad negativa
        if cantidad < 0:
            print("No se puede ingresar cantidades negativas.")
        else:
            # Ingresar dinero
            saldo += cantidad
            # Incrementar contador para las estadísticas
            ingresos += 1

    # Retirar dinero
    elif opcion == '2':
        # Pedir cantidad a retirar
        cantidad = obtener_cantidad("Dinero a retirar: ")

        # Comprobar si es una cantidad negativa
        if cantidad < 0:
            print("No se puede retirar cantidades negativas.")
        elif cantidad > saldo:
            print("No se puede retirar más de lo que hay en la cuenta.")
        else:
            # Retirar dinero
            saldo -= cantidad
            # Incrementar contador para las estadísticas
            retiros += 1

    # Mostrar saldo
    elif opcion == '3':
        print(f"Saldo actual: {saldo}")

    # Estadísticas
    elif opcion == '4':
        print(f"Ingresos: {ingresos}")
        print(f"Retiros: {retiros}")

    # Salir
    elif opcion == '5':
        break

    # Mostrar error y volver al inicio del bucle
    else:
        print("Opción incorrecta")

    # Línea en blanco para mejorar la legibilidad
    print()