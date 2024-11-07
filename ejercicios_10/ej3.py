import numpy as np

# Matriz de 4x4 con números enteros consecutivos
matriz = np.arange(1, 17).reshape((4, 4))

# Mostrar solo la tercera columna
print(matriz[:, 2])