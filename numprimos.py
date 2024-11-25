# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Imprimir todos los números primos entre 1 y 50
for numero in range(1, 51):
    if es_primo(numero):
        print(numero, end=", " if numero < 47 else "\n")

