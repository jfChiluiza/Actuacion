# Solicitar un número al usuario
numero = int(input("Ingresa un número: "))

# Mostrar la tabla de multiplicar del 1 al 10
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
