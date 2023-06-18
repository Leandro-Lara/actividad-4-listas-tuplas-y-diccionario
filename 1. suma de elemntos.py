lista1=[1,2,3,4,5]
lista2=[99,100,101,102,103]
print("Esta es la lista numero 1: ", lista1)
print("Esta es la lista numero 2: ", lista2)
number = int(input("Ingrese el numero de la lista que desea que se sumen los valores que esta contiene: "))
suma=0
if number==1:
  for _ in lista1:
    suma += _
  print(suma)
elif number==2:
  for elemento in lista2:
    suma += elemento
  print(suma)
else:
  print("El numero de lista seleccionado no existe")