# Inicializar variables
total_calificaciones = 0
cantidad_calificaciones = 0

# Solicitar calificaciones al usuario
while True:
    calificacion = float(input("Ingresa una calificación (o -1 para terminar): "))
    
    if calificacion == -1:
        break
    
    total_calificaciones += calificacion
    cantidad_calificaciones += 1

# Calcular y mostrar el promedio
if cantidad_calificaciones > 0:
    promedio = total_calificaciones / cantidad_calificaciones
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones.")
