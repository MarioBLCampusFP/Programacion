import random

# Almacenar partidas ganadas
victorias_maquina = 0
victorias_jugador = 0

# Almacenar lista de opciones
opciones = ["Piedra", "Papel", "Tijera"]

# El juego finalizará cuando se ganen 3 partidas
while (victorias_maquina < 3) and (victorias_jugador < 3):
    try:
        # Pedir al usuario que elija una opción
        opcion_jugador = int(input(f"Elige 1-{opciones[0]} | 2-{opciones[1]} | 3-{opciones[2]}: "))
    # Si no obtenemos un valor numérico
    except ValueError:
        # Volver al inicio del bucle
        continue
    
    # Aceptar solo opciones válidas
    if opcion_jugador <= 0 or opcion_jugador > 3:
        continue

    # Generar un valor aleatorio del 1 al 3 para la máquina
    opcion_maquina = random.randint(1, 3)

    # Mostrar opciones
    print(f"El jugador ha elegido {opciones[opcion_jugador - 1]}")
    print(f"La máquina ha elegido {opciones[opcion_maquina - 1]}")

    # Comprobar si se ha empatado
    if opcion_jugador == opcion_maquina:
        print("Habeis empatado")

    # Comprobar ganador
    elif (
        (opcion_jugador == 1 and opcion_maquina == 3)
        or (opcion_jugador == 2 and opcion_maquina == 1)
        or (opcion_jugador == 3 and opcion_maquina == 2)
    ):
        print("Has ganado!! :)")
        victorias_jugador += 1
    else:
        print("Has perdido!! :)")
        victorias_maquina += 1

    # Línea en blanco para mejorar la legibilidad
    print()

# Mostrar resultado final
if victorias_jugador == 3:
    print("Has ganado el juego! :)")
else:
    print("La máquina ha ganado el juego! :)")