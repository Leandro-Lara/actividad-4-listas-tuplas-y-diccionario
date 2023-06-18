notas_valentina = [3.5, 4.3, 5.0, 3.9]
notas_julian = [2.5, 3.4, 4.3, 4.4]
print("Estas son las notas de Valentina", notas_valentina)
print("Estas son las notas de Julian", notas_julian)
alumno = int(input("Para ver la nota definitiva de valentina ingrese el numero 1 y para la de julian el 2: "))
valentina = 0
julian = 0
if alumno == 1:
  for _ in notas_valentina:
    valentina+=_
    definival= valentina/4
  print(definival)
elif alumno == 2:
  for _ in notas_julian:
    julian+=_
    definijul= julian/4
  print(definijul)
else:
  print("El numero ingresado no corresponde a ningun alumno de este salon.")
  

