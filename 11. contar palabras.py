lista = ['hola', 'mundo', 'hola', 'Python', 'mundo', 'Python', 'Hola']
print("Bienvenido, veremos cuantas veces se repite cada palabra que hay en esta lita: ", lista)
def contar_palabras(lista_palabras):
    contador = {}
    for palabra in lista_palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador
resultado = contar_palabras(lista)
print(resultado)