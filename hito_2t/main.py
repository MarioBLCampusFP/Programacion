from funciones import mostrar_menu, ejecutar_opcion


def main():
    """Función principal del programa."""
    while True:
        # Mostrar el menú de opciones
        mostrar_menu()
        try:
            # Leer opción
            opcion = int(input("Seleccione una opción: "))
            # Ejecutar opción
            ejecutar_opcion(opcion)
        except ValueError:
            print("Opción no válida.")


# Ejecutar función principal
if __name__ == "__main__":
    main()
