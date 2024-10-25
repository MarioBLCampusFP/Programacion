# Definir ciudades a visitar
itinerario = ("Madrid", "Barcelona", "Valencia", "Sevilla")

# Mostrar en pantalla el itinerario completo
print("Itinerario de viaje:")
for i in range(len(itinerario)):
    print(f"{i + 1}. {itinerario[i]}")

# Pedir al usuario que ingrese una posición
pos = int(input("Ingresa la posición para saber qué ciudad visitarás: "))

# Mostrar la ciudad seleccionada
print(f"En la posición {pos} visitarás: {itinerario[pos - 1]}")