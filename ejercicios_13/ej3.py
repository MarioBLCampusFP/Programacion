import numpy as np

# Leer el archivo
with open("notas_estudiantes.txt", "r") as archivo:
    # Almacenar las notas como una lista de listas
    notas = [list(map(int, linea.strip().split(","))) for linea in archivo]
    # Convertir la lista a array
    notas = np.array(notas)

    # Calcular promedios
    promedio_estudiantes = np.mean(notas, axis=1)
    promedio_general = np.mean(notas)

    # Mostrar promedios
    for i, promedio in enumerate(promedio_estudiantes):
        print(f"Promedio estudiante {i}: {promedio:.2f}")
    print(f"Promedio general: {promedio_general}")