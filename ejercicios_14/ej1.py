import numpy as np
import os
import random

# Definir propiedades de la partida
dimension_tablero = (20, 20)
dimension_barcos = [2, 3, 4]

# Archivo en el que se guarda el estado de la partida
estado_partida = "partida_comenzada.txt"


def jugar():
    # Comprobar si hay una partida guardada
    try:
        with open(estado_partida) as archivo:
            # El número de intentos se encontrará en la primera línea del archivo
            intentos = int(archivo.readline().strip())
            # Recuperar la partida
            tablero = np.loadtxt(archivo, dtype=int)
            print("Partida cargada.")
    except FileNotFoundError:
        # Llevar la cuenta de intentos realizados
        intentos = 0
        # Crear una nueva partida si no existe el fichero
        tablero = crear_tablero()

    while True:
        # Solicitar coordenadas
        coordenadas = input("Ingrese las coordenadas de ataque (x,y) [0-19]: ")
        # Mostrar menú en las cordenadas 111
        if coordenadas == "111":
            while True:
                print("1.- Guardar\n2.- Salir")
                opcion = input("Elije una opción: ")
                # Guardar el estado de la partida
                if opcion == "1":
                    guardar_partida(tablero, intentos)
                    print("Partida guardada.")
                    exit()
                # Salir del juego sin guardar
                elif opcion == "2":
                    exit()
                else:
                    print("Elije una opción válida.")
        try:
            # Extraer coordenadas
            x, y = map(int, coordenadas.split(","))
            # Comprobar si ha tocado el barco
            if tablero[x, y] == 1:
                print("¡Tocado!")
                # Marcar como tocado
                tablero[x, y] = 2
            elif tablero[x, y] == 0:
                print("Agua.")
                # Marcar como visitado
                tablero[x, y] = -1
            intentos += 1
        # Manejar entradas no válidas
        except (ValueError, IndexError):
            print("Ingrese una posición válida.")
            continue

        # Mostrar el tablero sin revelar la posición de los barcos
        print(np.where(tablero == 1, 0, tablero))
        # Mostrar el número de intentos
        print(f"Intentos: {intentos}")

        # Comprobar si el jugador ha ganado al revisar si quedan barcos por hundir
        if tablero[tablero == 1].size == 0:
            print("¡Has hundido todos los barcos! ¡Ganaste!")
            # Borrar la partida guardada
            if os.path.exists(estado_partida):
                os.remove(estado_partida)
            # Salir del bucle
            break


def crear_tablero():
    # Crear tablero
    tablero = np.zeros(dimension_tablero, dtype=int)
    # Crear los barcos
    barcos = crear_barcos()
    # Colocar barcos en el tablero
    tablero = colocar_barcos(tablero, barcos)
    # Devolver el tablero de la nueva partida
    return tablero


def crear_barcos():
    # Devolver una lista de arrays con las dimensiones de los barcos
    return [np.ones(barco) for barco in dimension_barcos]


def colocar_barcos(tablero, barcos):
    # Extraer las dimensiones del tablero
    num_filas = dimension_tablero[0]
    num_columnas = dimension_tablero[1]

    # Colocar los barcos con las dimensiones requeridas en el tablero
    for barco in barcos:
        longitud = len(barco)
        while True:
            # Crear las coordenadas de inicio de cada barco
            fila = random.randint(0, num_filas - 1)
            columna = random.randint(0, num_columnas - 1)
            orientacion = random.choice(["horizontal", "vertical"])

            if orientacion == "horizontal":
                # Comprobar si hay espacio suficiente en la fila
                if columna + longitud <= num_columnas:
                    espacio_ocupado = tablero[fila, columna : columna + longitud]
                    # Comprobar si el espacio está ocupado por otro barco
                    if espacio_ocupado[espacio_ocupado == 1].size == 0:
                        # Colocar el barco en el tablero
                        tablero[fila, columna : columna + longitud] = barco
                        break
            else:
                # Comprobar si hay espacio suficiente en la columna
                if fila + longitud <= num_filas:
                    espacio_ocupado = tablero[fila : fila + longitud, columna]
                    # Comprobar si el espacio está ocupado por otro barco
                    if espacio_ocupado[espacio_ocupado == 1].size == 0:
                        # Colocar el barco en el tablero
                        tablero[fila : fila + longitud, columna] = barco
                        break
    return tablero


def guardar_partida(tablero, intentos):
    with open(estado_partida, "w") as archivo:
        # Guardar los intentos en la primera línea del archivo
        archivo.write(f"{intentos}\n")
        # Guardar tablero
        np.savetxt(archivo, tablero, fmt="%d")


if __name__ == "__main__":
    jugar()