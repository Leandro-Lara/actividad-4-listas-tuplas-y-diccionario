mi_tupla = (1, 1, 2, 2, 3, 3, 4, 4, 4)
print("Bienvenido, contaremos cuantas veces se repiten los mismos valores en esta tupla: ", mi_tupla)
def contar_ocurrencias(mi_tupla):
    diccionario = {}
    for elemento in mi_tupla:
        if elemento in diccionario:
            diccionario[elemento] += 1
        else:
            diccionario[elemento] = 1
    return diccionario
ocurrencias = contar_ocurrencias(mi_tupla)
print("Valor: veces que se repite")
print(ocurrencias)