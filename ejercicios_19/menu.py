"""
Gestión del menú principal y las operaciones de clientes, actividades, entrenadores e inscripciones.
"""

from actividad import crear_actividad, ver_actividades, actualizar_actividad, eliminar_actividad
from cliente import crear_cliente, ver_clientes, actualizar_cliente, eliminar_cliente
from entrenador import crear_entrenador, ver_entrenadores, actualizar_entrenador, eliminar_entrenador
from inscripcion import crear_inscripcion, ver_inscripciones, eliminar_inscripcion
from termcolor import cprint


def solicitar_numero(mensaje):
    """Solicita un número al usuario y maneja errores."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            cprint("[Mensaje]: Ingrese un valor numérico.", "yellow")


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n=== Gestión del Centro Deportivo ===")
    print("1. Gestión de Clientes")
    print("2. Gestión de Actividades")
    print("3. Gestión de Entrenadores")
    print("4. Gestión de Inscripciones")
    print("5. Salir")


def ejecutar_opcion(opcion):
    """Ejecuta la opción seleccionada por el usuario en el menú."""
    if opcion == "1":
        gestionar_clientes()
    elif opcion == "2":
        gestionar_actividades()
    elif opcion == "3":
        gestionar_entrenadores()
    elif opcion == "4":
        gestionar_inscripciones()
    elif opcion == "5":
        exit()
    else:
        cprint("[Error]: Opción inválida.", "red")


def gestionar_clientes():
    """Gestiona las operaciones CRUD de los clientes."""
    while True:
        print("\n=== Gestión de Clientes ===")
        print("1. Crear un nuevo cliente")
        print("2. Ver todos los clientes")
        print("3. Actualizar un cliente")
        print("4. Eliminar un cliente")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            edad = solicitar_numero("Ingrese la edad: ")
            while True:
                membresia = input("Ingrese el tipo de membresía (Semanal, Mensual o Anual): ").capitalize()
                if membresia in ["Semanal", "Mensual", "Anual"]:
                    break
                cprint("Ingrese una membresía válida: Semanal, Mensual o Anual.", "yellow")
            crear_cliente(nombre, edad, membresia)
        elif opcion == "2":
            ver_clientes()
        elif opcion == "3":
            id_cliente = solicitar_numero("Ingrese el ID del cliente a modificar: ")
            membresia = input("Ingrese el nuevo tipo de membresía: ")
            actualizar_cliente(id_cliente, membresia)
        elif opcion == "4":
            id_cliente = solicitar_numero("Ingrese el ID del cliente a eliminar: ")
            eliminar_cliente(id_cliente)
        elif opcion == "5":
            break
        else:
            cprint("[Error]: Opción inválida.", "red")


def gestionar_actividades():
    """Gestiona las operaciones CRUD de las actividades."""
    while True:
        print("\n=== Gestión de Actividades ===")
        print("1. Crear un nueva actividad")
        print("2. Ver todas las actividades")
        print("3. Actualizar una actividad")
        print("4. Eliminar una actividad")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre de la actividad: ")
            horario = input("Ingrese el horario: ")
            duracion = solicitar_numero("Ingrese la duración (minutos): ")
            id_entrenador = solicitar_numero("Ingrese el ID del entrenador: ")
            crear_actividad(nombre, horario, duracion, id_entrenador)
        elif opcion == "2":
            ver_actividades()
        elif opcion == "3":
            id_actividad = solicitar_numero("Ingrese el ID de la actividad a modificar: ")
            horario = input("Ingrese el nuevo horario: ")
            actualizar_actividad(id_actividad, horario)
        elif opcion == "4":
            id_actividad = solicitar_numero("Ingrese el ID de la actividad a eliminar: ")
            eliminar_actividad(id_actividad)
        elif opcion == "5":
            break
        else:
            cprint("[Error]: Opción inválida.", "red")


def gestionar_entrenadores():
    """Gestiona las operaciones CRUD de los entrenadores."""
    while True:
        print("\n=== Gestión de Entrenadores ===")
        print("1. Crear un nuevo entrenador")
        print("2. Ver todos los entrenadores")
        print("3. Actualizar un entrenador")
        print("4. Eliminar un entrenador")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del entrenador: ")
            especialidad = input("Ingrese el tipo de especialidad: ")
            crear_entrenador(nombre, especialidad)
        elif opcion == "2":
            ver_entrenadores()
        elif opcion == "3":
            id_entrenador = solicitar_numero("Ingrese el ID del entrenador a modificar: ")
            especialidad = input("Ingrese el nuevo tipo de especialidad: ")
            actualizar_entrenador(id_entrenador, especialidad)
        elif opcion == "4":
            id_entrenador = solicitar_numero("Ingrese el ID del entrenador a eliminar: ")
            eliminar_entrenador(id_entrenador)
        elif opcion == "5":
            break
        else:
            cprint("[Error]: Opción inválida.", "red")


def gestionar_inscripciones():
    """Gestiona las operaciones CRUD de las inscripciones."""
    while True:
        print("\n=== Gestión de Inscripciones ===")
        print("1. Crear una nueva inscripcion")
        print("2. Ver todas las inscripciones")
        print("3. Eliminar inscripcion")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            id_cliente = solicitar_numero("Ingrese el ID del cliente: ")
            id_actividad = solicitar_numero("Ingrese el ID de la actividad: ")
            crear_inscripcion(id_cliente, id_actividad)
        elif opcion == "2":
            ver_inscripciones()
        elif opcion == "3":
            id_inscripcion = solicitar_numero("Ingrese el ID de la inscripcion a eliminar: ")
            eliminar_inscripcion(id_inscripcion)
        elif opcion == "4":
            break
        else:
            cprint("[Error]: Opción inválida.", "red")
