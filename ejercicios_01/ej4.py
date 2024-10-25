# Pedir al usuario una cadena de texto
texto = input("Escribe algo: ")

# Contar vocales
vocales = 0
for letra in texto:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
        vocales += 1

# Mostrar total vocales
print(vocales)