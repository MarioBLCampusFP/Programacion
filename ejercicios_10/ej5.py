import numpy as np

# Definir matriz
matriz = np.random.randint(1, 51, size=(4, 3))

# Mostrar el valor máximo de cada columna
print(np.max(matriz, axis=0))