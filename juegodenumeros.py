import random

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

# Solicitar al usuario que adivine el número
intento = int(input("Adivina el número (entre 1 y 10): "))

# Verificar si el usuario acertó
if intento == numero_aleatorio:
    print("¡Felicidades, acertaste!")
else:
    print(f"Intenta de nuevo. El número era {numero_aleatorio}.")
