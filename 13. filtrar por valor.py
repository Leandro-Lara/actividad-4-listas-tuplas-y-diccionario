diccionario = {'carro': 1, 'bicicleta': 2, 'moto': 3, 'avion': 2, 'barco': 1}
print("Bienvenido, se solicitara un valor y veremos que medio de transporte este relacionado con este valor: ", diccionario)
def filtrar_diccionario(diccionario, valor):
    nuevo_diccionario = {}
    for clave, v in diccionario.items():
        if v == valor:
            nuevo_diccionario[clave] = v
    return nuevo_diccionario
valor_deseado = 2
resultado = filtrar_diccionario(diccionario, valor_deseado)
print(resultado)