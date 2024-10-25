# Solicitar al usuario una palabra
palabra = input("Escribe una palabra: ")

# Almacenar la palabra inversa en una nueva cadena
palabra_inversa = ""

# Recorrer la palabra de forma inversa
for letra in reversed(palabra):
    palabra_inversa += letra

# Mostrar la palabra invertida
print(palabra_inversa)