# Solicitar al usuario dos números
a = int(input("Primer número: "))
b = int(input("Segundo número: "))

# Solicitar al usuario que operación realizar
operacion = input("¿Qué operación desea realizar? (+, -, *, /): ")

# Calcular el resultado
if operacion == "+":
    print(a + b)
elif operacion == "-":
    print(a - b)
elif operacion == "*":
    print(a * b)
elif operacion == "/":
    # Mostrar error en división por 0
    if b == 0:
        print("Error: No puedes dividir por 0.")
    else:
        print(a / b)