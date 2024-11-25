# Solicitar la calificación numérica
calificacion = float(input("Ingresa tu calificación numérica: "))

# Determinar la calificación en letra
if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion < 90:
    letra = "B"
elif 70 <= calificacion < 80:
    letra = "C"
elif 60 <= calificacion < 70:
    letra = "D"
elif calificacion < 60:
    letra = "F"
else:
    letra = "Calificación inválida."

# Mostrar el resultado
print(f"Tu calificación es {letra}.")
