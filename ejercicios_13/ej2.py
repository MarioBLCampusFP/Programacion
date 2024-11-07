import numpy as np

# Leer las temperaturas
with open("temperaturas.txt", "r") as archivo:
    # Almacenar temperaturas
    temperaturas = [int(linea.strip()) for linea in archivo]
    
    # Convertir la lista a un array de NumPy
    temperaturas = np.array(temperaturas)

    # Calcular la temperatura promedio, la más alta y la más baja
    temperatura_promedio = np.mean(temperaturas)
    temperatura_maxima = np.max(temperaturas)
    temperatura_minima = np.min(temperaturas)

    # Mostrar temperaturas
    print(f"Temperatura promedio: {temperatura_promedio:.2f} °C")
    print(f"Temperatura más alta: {temperatura_maxima:.2f} °C")
    print(f"Temperatura más baja: {temperatura_minima:.2f} °C")