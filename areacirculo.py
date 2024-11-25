import math

# Definir la función para calcular el área del círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Solicitar el radio al usuario
radio_usuario = float(input("Ingresa el radio del círculo: "))

# Llamar a la función y mostrar el resultado
area = calcular_area_circulo(radio_usuario)
print(f"El área del círculo con radio {radio_usuario} es: {area:.2f}")
