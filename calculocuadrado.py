# Definir la función para calcular el cuadrado
def calcular_cuadrado(numero):
    return numero ** 2

# Solicitar un número al usuario
numero_usuario = float(input("Ingresa un número: "))

# Llamar a la función y mostrar el resultado
resultado = calcular_cuadrado(numero_usuario)
print(f"El cuadrado de {numero_usuario} es: {resultado}")
