mi_tupla=(1, 2, 3, 2, 1, 4, 2, 5, 3)
print("Bienvenido, vamos a encontrar un determinado indice en esta tupla", mi_tupla)
def encontrar_indices(tupla, elemento):
    indices = []
    for _ in range(len(tupla)):
        if tupla[_] == elemento:
            indices.append(_)
    return indices
elemento = 2
indices = encontrar_indices(mi_tupla, elemento)
print(indices)