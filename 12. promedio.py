estudiantes = {'Juan': 85, 'María': 90, 'Carlos': 78, 'Ana': 95}
print("Bienvenido, averiguaremos cual es el promedio de todos los siguientes estudiantes con base en sus calificaciones: ", estudiantes)
def calcular_promedio_calificaciones(estudiantes):
    total_calificaciones = 0
    cantidad_estudiantes = len(estudiantes)

    for estudiante, calificacion in estudiantes.items():
        total_calificaciones += calificacion

    promedio = total_calificaciones / cantidad_estudiantes
    return promedio
promedio = calcular_promedio_calificaciones(estudiantes)
print("El promedio de calificaciones es:", promedio)