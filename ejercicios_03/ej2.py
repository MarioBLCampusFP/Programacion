# Almacenar contactos
contactos = {}

while True:
    # Pedir al usuario que ingrese el nombre del contacto
    nombre = input("Ingresa el nombre del contacto (o 'fin' para terminar): ")
    # Parar el bucle en caso de introducir 'fin'
    if nombre == "fin":
        break
    # Pedir al usuario que ingrese el número de teléfono
    tel = input(f"Ingresa el número de teléfono de {nombre}: ")
    # Añadir contacto
    contactos[nombre] = tel

# Mostrar todos los contactos almacenados
print("Tus contactos:")
for nombre in contactos:
    print(f"- {nombre}: {contactos[nombre]}")

# Pedir al usuario que ingrese el nombre de un contacto a buscar
contacto = input("Ingresa el nombre del contacto que deseas buscar: ")

# Mostrar el número de teléfono de ese contacto
print(f"El número de teléfono de {contacto} es {contactos[contacto]}.")