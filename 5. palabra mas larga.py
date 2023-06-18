palabras = ["Lamborghini", "Porsche", "Ferrari", "Pagani"]
print("Bienvenido, averiguaremos cual es la palabra mas larga de la lista: ", palabras)
def palabra_mas_larga(lista_palabras):
    palabra_mas_larga = ''
    longitud_maxima = 0
    for palabra in lista_palabras:
        if len(palabra) > longitud_maxima:
            palabra_mas_larga = palabra
            longitud_maxima = len(palabra)
    return palabra_mas_larga
palabra_mas_larga = palabra_mas_larga(palabras)
print(palabra_mas_larga)