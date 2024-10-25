import random

# Lista de monstruos y sus niveles de dificultad
monstruos = {"vampiro": 3, "momia": 2, "bruja": 4, "esqueleto": 1, "fantasma": 5}

# Lista de objetos para capturar y sus factores de efectividad
objetos = {"estaca": 0.35, "poción mágica": 0.65, "hechizo": 0.75}

# Generar monstruo aleatorio y obtener su nivel de dificultad
monstruo = random.choice(list(monstruos.keys()))
dificultad = monstruos[monstruo]

# Almacenar intentos
intentos = 3

# Mensaje introductorio
print("¡Bienvenido a la caza de monstruos de Halloween!")
print(f"Un/a {monstruo} ha aparecido con dificultad {dificultad}.")

# Mientras haya intentos restantes
while intentos > 0:
    # Mostrar cantidad de intentos restantes
    print(f"\nTienes {intentos} intentos restantes.")

    # Pedir al usuario que elija un objeto
    print(f"Elige un objeto para intentar capturar a un/a {monstruo}: {', '.join(objetos)}")
    objeto = input("Escribe el nombre del objeto: ")

    # Rechazar objetos no válidos
    if objeto not in objetos:
        print("Objeto no valido. Intentalo de nuevo.")
        continue

    # Calcular probabilidad basada en el nivel de monstruo y el objeto elegido
    probabilidad = objetos[objeto] / dificultad

    # Generar un valor aleatorio entre 0 y 1
    valor_aleatorio = random.random()

    # El éxito se basa en que el valor aleatorio sea menor que la probabilidad
    if valor_aleatorio < probabilidad:
        print(f"¡Has capturado al {monstruo} con un/a {objeto}!")
        break

    # Restar un intento si ha fallado
    print(f"Fallaste al intentar capturar al {monstruo} con un/a {objeto}.")
    intentos -= 1