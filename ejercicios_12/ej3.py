with open("notas.txt", "w") as archivo:
    for i in range(1, 4):
        nota = input(f"Nota {i}: ")
        archivo.write(nota + "\n")