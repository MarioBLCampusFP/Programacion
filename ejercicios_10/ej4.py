import numpy as np

# Definier matriz
matriz = np.arange(1, 13).reshape(3, 4)

# Calcular el promedio de cada fila
print(np.mean(matriz, axis=1))