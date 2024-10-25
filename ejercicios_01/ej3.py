# Pedir al usuario un número entero positivo
n = int(input("Escribe un número entero positivo: "))

# Almacenar el resultado de la suma
suma = 0

# Sumar todos los números desde 1 a n (inclusive)
for i in range(1, n + 1):
    suma += i

# Mostrar la suma
print(suma)