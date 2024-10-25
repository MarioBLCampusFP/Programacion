frases = [
    "El sol brilla en el cielo.",
    "Los pájaros cantan en la mañana.",
    "La vida es un hermoso viaje."
]

# Definir función que pasa el inicio de una palabra a mayúscula
def capitalizar_frase(frase):
    return frase.title()

# Mostrar resultado
print(list(map(capitalizar_frase, frases)))