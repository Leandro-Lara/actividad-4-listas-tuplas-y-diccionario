lista_desordenada = [6,9,7,2,3,4]
print("Bienvenido, vamos a organizar la siguiente lista: ",lista_desordenada)
def ordenar_lista(lista_desordenada):
    k = len(lista_desordenada)
    for i in range(k):
        for j in range(0, k-i-1):
            if lista_desordenada[j] > lista_desordenada[j+1]:
                lista_desordenada[j], lista_desordenada[j+1] = lista_desordenada[j+1], lista_desordenada[j]
    return lista_desordenada
lista_ordenada = ordenar_lista(lista_desordenada)
print(lista_ordenada)
