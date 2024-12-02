def es_multiplo_de_tres(n):
    return n % 3 == 0


numeros = [12, 14, 18]
for numero in numeros:
    print(es_multiplo_de_tres(numero))
