import random

# Definir número secreto
n_secreto = random.randint(1, 100)

# Mientras el usuario no acierte
while True:
    # Pedir al usuario que inserte un número
    n = int(input("Adivina el número: "))
    # Si acierta indicarlo y salir
    if n == n_secreto:
        print("El número es correcto!")
        break
    # Si no acierta, dar pistas
    elif n > n_secreto:
        print("El número ingresado es demasiado alto.")
    elif n < n_secreto:
        print("El número ingresado es demasiado bajo.")