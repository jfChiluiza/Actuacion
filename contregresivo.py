# Imprimir los números del 10 al 1 en orden descendente
for numero in range(10, 0, -1):
    print(numero, end=", " if numero > 1 else "\n")
