# Almacenar calificaciones
calificaciones = {}
suma = 0

while True:
    # Pedir al usuario que ingrese la asignatura
    asignatura = input("Ingresa el nombre de la asignatura (o 'fin' para terminar): ")
    # Parar el bucle si se introduce 'fin'
    if asignatura == "fin":
        break
    # Pedir al usuario que ingrese la calificación
    calificacion = int(input(f"Ingresa la calificación de {asignatura}: "))
    # Añadir calificacion
    if asignatura not in calificaciones:
        calificaciones[asignatura] = []
    calificaciones[asignatura].append(calificacion)

# Mostrar calificaciones
print("Resumen de calificaciones:")
for k, v in calificaciones.items():
    print(f"- {k}: {v}")
    # Sumar calificaciones
    for i in range(len(v)):
        suma += v[i]

# Calcular calificación media
media = suma / len(calificaciones)
print(f"Calificación media: {media}")