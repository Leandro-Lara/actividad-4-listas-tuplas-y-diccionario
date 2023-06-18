mi_tupla = ('manzana', 'pera', 'plátano', 'kiwi', 'uva', 'limón')
print("Bienvenido, en obtendremos dos tuplas apartir de esta: ", mi_tupla)
def separar_cadenas_por_vocal(tupla_cadenas):
    vocales = ('a', 'e', 'i', 'o', 'u')
    cadenas_con_vocal = []
    cadenas_sin_vocal = []
    
    for cadena in tupla_cadenas:
        if cadena[0].lower() in vocales:
            cadenas_con_vocal.append(cadena)
        else:
            cadenas_sin_vocal.append(cadena)
    
    return tuple(cadenas_con_vocal), tuple(cadenas_sin_vocal)
con_vocal, sin_vocal = separar_cadenas_por_vocal(mi_tupla)
print("Cadenas con vocal:", con_vocal)
print("Cadenas sin vocal:", sin_vocal)