# Imprimir todos los números pares entre 1 y 20
for numero in range(2, 21, 2):
    print(numero, end=", " if numero < 20 else "\n")
