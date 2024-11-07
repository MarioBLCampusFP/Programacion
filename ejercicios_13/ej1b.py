import numpy as np

# Leer números desde archivo
with open("numeros.txt", "r") as archivo:
    # Almacenar números en una lista
    numeros = [int(linea.strip()) for linea in archivo]
    # Convertir la lista a un array de NumPy
    numeros = np.array(numeros)
    # Mostrar array
    print(numeros)