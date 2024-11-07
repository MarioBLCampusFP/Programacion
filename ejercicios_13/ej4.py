import numpy as np

# Almacenar valores de un archivo en un array
valores = np.loadtxt("valores.txt", dtype=int)

# Filtrar solo los valores positivos
valores_positivos = valores[valores > 0]

# Guardar los valores positivos en un archivo de texto
with open("valores_positivos.txt", "w") as archivo:
    for n in valores_positivos:
        archivo.write(f"{n}\n")