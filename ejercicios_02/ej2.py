# Almacenar la suma y contador de números
suma = 0
contador = 0

# Pedir al usuario un número hasta que introduzca un 0
while True:
    n = int(input("Escriba un número: "))
    if n == 0:
        break
    suma += n
    contador += 1

# Calcular promedio
promedio = suma / contador

# Mostrar promedio
print(f"El promedio de los números introducidos es {promedio}")