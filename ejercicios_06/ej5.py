tareas = []

while True:
    # Pedir input al usuario hasta que escriba fin
    nombre_tarea = input("Tarea: ")
    if nombre_tarea.lower() == "fin":
        break
    # Crear diccionario para almacenar la tarea
    tarea = {}
    # Pedir al usuario que elija si la tarea es urgente
    urgente = input("¿Es urgente? (si/no): ").lower()
    # Almacenar el nombre y urgencia en el diccionario tarea
    tarea["nombre"] = nombre_tarea
    tarea["urgente"] = urgente
    # Añadir el diccionario a la lista tareas
    tareas.append(tarea)

# Filtrar tareas urgentes
tareas_urgentes = list(filter(lambda t: t["urgente"] == "si", tareas))

# Mostrar nombres de las tareas urgentes
for tarea in tareas_urgentes:
    print(tarea["nombre"])