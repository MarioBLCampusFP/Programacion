from bdd import obtener_credenciales
from menu import ejecutar_opcion, mostrar_menu


def main():
    """Función principal del programa."""
    obtener_credenciales()
    while True:
        mostrar_menu()
        opcion = input("Elije una opción: ")
        ejecutar_opcion(opcion)


if __name__ == "__main__":
    main()
