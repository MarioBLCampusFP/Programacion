def contar_pares(numeros):
    # Contador números pares
    pares = 0
    # Recorrer lista
    for n in numeros:
        # Comprobar si es un número par
        if n % 2 == 0:
            # Incrementar contador
            pares += 1

    # Devolver valor
    return pares
