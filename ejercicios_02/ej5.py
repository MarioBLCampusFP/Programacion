# Almacenar números en una lista
numeros = []

# Solicitar al usuario que ingrese números
while True:
    n = input("Ingrese un número: ")
    # Terminar el bucle
    if n == "hecho":
        break
    numeros.append(int(n))

# Buscar el número mayor
mayor = numeros[0]
for n in numeros:
    if n > mayor:
        mayor = n

# Mostrar el número mayor
print(f"El número mayor ingresado es: {mayor}")