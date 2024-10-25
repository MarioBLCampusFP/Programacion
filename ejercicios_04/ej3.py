def es_primo(numero):
    # Dividir el número de 2 a n - 1
    for n in range(2, numero):
        # Si es divisible por un número diferente a 1 y el mismo
        if numero % n == 0:
            # El número no es primo
            return False
    # Se ha encontrado un número primo
    return True
