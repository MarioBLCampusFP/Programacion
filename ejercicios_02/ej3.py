# Almacenar una lista de nombres
nombres = []

# Solicitar nombres al usuario
while True:
    nombre = input("Ingresa un nombre: ")
    if nombre == "fin":
        break
    nombres.append(nombre)

# Imprimir la lista de nombres
print(f"Los nombres ingresados son: {nombres}")

# Imprimir nombres uno a uno 
for nombre in nombres:
    print(nombre)