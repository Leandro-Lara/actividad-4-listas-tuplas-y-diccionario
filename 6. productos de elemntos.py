my_tupla = (2, 4, 6, 8, 10)
print("Bienvenido, averiguaremos cual es el producto final que se obtiene de esta tupla: ", my_tupla)
def producto_tupla(my_tupla):
    producto = 1
    for _ in my_tupla:
        producto *= _
    return producto
resultado = producto_tupla(my_tupla)
print(resultado)