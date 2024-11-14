while True:
    # Mostrar menú
    print("MENU")
    print("1 - Cuadrado")
    print("2 - Rectangulo")
    print("3 - Salir")

    # Pedir al usuario que elija una opción
    opcion = input("Dime una opción: ")

    # Si ha seleccionado salir
    if opcion == '3':
        # Salir del bucle
        break

    # Si ha seleccionado un rectángulo
    elif opcion == '2':
        # Pedir al usuario la base y altura
        base = int(input("Dime la base del rectángulo: "))
        altura = int(input("Dime la altura del rectángulo: "))

        # Dibujar el rectángulo
        for _ in range(altura):
            print("*" * base)

        # Mostrar el área y perímetro
        print(f"Su área es {base * altura}")
        print(f"Su perímetro es {2 * (base + altura)}")

    # Si ha seleccionado un cuadrado
    elif opcion == '1':
        # Pedir al usuario el lado del cuadrado
        lado = int(input("Dime el lado del cuadrado: "))

        # Dibujar el cuadrado
        for _ in range(lado):
            print("*" * lado)

        # Mostrar el área y perímetro
        print(f"Su área es {lado * lado}")
        print(f"Su perímetro es {4 * lado}")

    # Mostrar error y volver al inicio del bucle
    else:
        print("Opción incorrecta")

    # Línea en blanco para mejorar la legibilidad
    print()