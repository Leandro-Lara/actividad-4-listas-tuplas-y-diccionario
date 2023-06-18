texto = "El perro juega con el perro y el gato"
print("Bienvenido, contaremos cuantas veces se repiten las mismas palabras en el siguiente texto: ", texto)
def contar_palabras(texto):
    contador = {}
    palabras = texto.lower().split()
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador
resultado = contar_palabras(texto)
print("palabra: numero de veces que se repite")
print(resultado)