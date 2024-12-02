palabras = ["hola", "mundo", "Python", "programación"]
maxima = ""
for palabra in palabras:
    if len(palabra) > len(maxima):
        maxima = palabra
print(maxima)
