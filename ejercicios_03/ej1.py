# Almacenar una lista de reproducción
lista_canciones = []
contador = 0

while True:
    # Solicitar al usuario que ingrese nombres de canciones
    cancion = input("Ingresa el nombre de la canción (o 'fin' para terminar): ")
    # Dejar de pedir canciones
    if cancion == "fin":
        break
    # Añadir la canción a la lista
    lista_canciones.append(cancion)

# Mostrar la lista de canciones
print("Tu lista de reproducción:")
for cancion in lista_canciones:
    contador += 1
    print(f"{contador}. {cancion}")

# Pedir al usuario que ingrese el número de canción
indice = int(input("Ingresa el número de la canción que quieres reproducir: ")) - 1

# Mostrar la canción elegida
print(f'Reproduciendo "{lista_canciones[indice]}"...')