import numpy as np

# Crear matriz de 3x3 con números aleatorios del 1 al 10
matriz = np.random.randint(1, 11, size=(3, 3))

# Escribir matriz a un archivo
with open("matriz.txt", "w") as archivo:
    for fila in matriz:
        # Escribir cada fila con valores separados por comas
        archivo.write(",".join(map(str, fila)) + "\n")