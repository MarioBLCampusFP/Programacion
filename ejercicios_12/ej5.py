with open("diario.txt", "a") as archivo:
    entrada_diario = input("Nueva entrada en el diario: ")
    archivo.write("\n" + entrada_diario)

with open("diario.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)