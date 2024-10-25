def contar_vocales(cadena):
    # Contador de vocales
    vocales = 0
    # Recorrer la cadena de texto
    for letra in cadena:
        # Comprobar si la letra es vocal
        if letra.lower() in "aeiou":
            # Incrementar contador
            vocales += 1
    # Devolver contador
    return vocales
  