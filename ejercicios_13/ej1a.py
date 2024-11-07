import numpy as np

# Generar un array con 10 números aleatorios entre 1 y 100
array = np.random.randint(1, 101, size=10)

# Almacenar los números en un archivo de texto
with open("numeros.txt", "w") as archivo:
    for n in array:
        archivo.write(f"{n}\n")