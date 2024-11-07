import numpy as np

# Leer matriz de un archivo
matriz = np.loadtxt("matriz.txt", dtype=int, delimiter=",")

# Mostrar matriz
print(matriz)