import numpy as np

# Crear el tablero
tablero = np.zeros((5, 5))

# Crear una copia del tablero para mostrar al usuario
tablero_mostrar = tablero.copy()

# Colocar el barco en una posición aleatoria
r1, r2 = np.random.randint(0, 5, size=2)
tablero[r1, r2] = 1

# Llevar la cuenta de intentos
intentos = 0

# Estado inicial
hundido = False

# Realizar intentos
while not hundido:
    # Preguntar por las coordenadas
    print("Ingrese las coordenadas de ataque.")
    try:
        x = int(input("x: "))
        y = int(input("y: "))
    except ValueError:
        print("Ingresa números enteros para las coordenadas.")
        continue
    
    # Comprobar si las coordenadas están dentro del rango del tablero
    if (x < 0 or x > 4) or (y < 0 or y > 4):
        print("Coordenadas fuera del rango. Intenta de nuevo.")
        continue
    # Comprobar si se ha hundido el barco en el tablero original
    else:
        intentos += 1
        if tablero[x, y]:
            print("¡Has hundido el barco!")
            print(f"Número de intentos: {intentos}")
            tablero_mostrar[r1, r2] = 1
            hundido = True
        else:
            print("Agua\nIntenta de nuevo.")
            tablero_mostrar[x, y] = -1
    
    # Mostrar el estado del tablero de la partida
    print(tablero_mostrar)