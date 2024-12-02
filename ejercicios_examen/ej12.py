def es_mayor_a_20(temperatura):
    return temperatura > 20


temperaturas = [15.5, 20.3, 18.2, 25.0, 30.5]
mayores_a_20 = list(filter(es_mayor_a_20, temperaturas))
print(list(mayores_a_20))
