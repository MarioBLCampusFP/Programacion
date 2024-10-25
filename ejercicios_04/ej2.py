def encontrar_maximo(numeros):
    # Definir temporalmente máximo
    maximo = numeros[0]
    # Recorrer la lista de números
    for n in numeros:
        # Comprobar si el número actual es mayor
        if n > maximo:
            # Actualizar el máximo
            maximo = n
    # Devolver máximo
    return maximo
