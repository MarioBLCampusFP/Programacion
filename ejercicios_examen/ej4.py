import math


def raiz_cuadrada(n):
    return math.sqrt(n)


numeros = [4, 9, 16, 25, 36]
raices = map(raiz_cuadrada, numeros)
print(list(raices))
