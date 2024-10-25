libros = []

while True:
    # Pedir input al usuario hasta que escriba fin
    titulo = input("Libro: ")
    if titulo.lower() == "fin":
        break
    # Crear diccionario para almacenar el libro
    libro = {}
    # Pedir al usuario que elija la categoría del libro
    categoria = input(f"Categoría: ")
    # Almacenar el título y categoría en el diccionario libro
    libro["titulo"] = titulo
    libro["categoria"] = categoria
    # Añadir el diccionario a la lista libros
    libros.append(libro)

# Almacenar novelas
novelas = list(filter(lambda v: v["categoria"] == "novela", libros))

# Mostrar títulos de las novelas
for novela in novelas:
    print(novela["titulo"])