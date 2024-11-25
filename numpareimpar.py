# Definir la función para verificar si un número es par
def es_par(numero):
    return numero % 2 == 0

# Solicitar un número al usuario
numero_usuario = int(input("Ingresa un número: "))

# Llamar a la función y mostrar el resultado
resultado = es_par(numero_usuario)
print(f"¿El número {numero_usuario} es par? {resultado}")
