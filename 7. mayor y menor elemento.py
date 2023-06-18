tupla = (34, 98, 76, 26)
print("Bienvenido, encontraremos el valor maximo y el valor minimo que hay en esta tupla: ", tupla)
def encontrar_maximo_minimo(tupla):
    maximo = max(tupla)
    minimo = min(tupla)
    return maximo, minimo
maximo, minimo = encontrar_maximo_minimo(tupla)
print("Máximo:", maximo)
print("Mínimo:", minimo)