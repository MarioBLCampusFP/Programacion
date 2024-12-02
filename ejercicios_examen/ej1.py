numeros = [5, 15, 25, 35, 45]

# Calcular el promedio
promedio = sum(numeros) / len(numeros)
print(promedio)

# Mostrar los números mayores al promedio
mayores = list(filter(lambda n: n > promedio, numeros))
print(mayores)
