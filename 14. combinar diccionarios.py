diccionario1 = {'a': 5, 'b': 7, 'c': 9}
diccionario2 = {'b': 1, 'c': 6, 'd': 5}
print("Bienvenido, combinaremos los iguientes diccionarios: ", diccionario1, diccionario2)
def combinar_diccionarios(diccionario1, diccionario2):
    diccionario_combinado = diccionario1.copy()

    for clave, valor in diccionario2.items():
        if clave in diccionario_combinado:
            diccionario_combinado[clave] += valor
        else:
            diccionario_combinado[clave] = valor

    return diccionario_combinado
resultado = combinar_diccionarios(diccionario1, diccionario2)
print("Suma de todos los valores que tienen la misma letra: ")
print(resultado)