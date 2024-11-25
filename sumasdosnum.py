# Definir la función de suma
def sumar(num1, num2):
    return num1 + num2

# Solicitar dos números al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Llamar a la función y mostrar el resultado
resultado = sumar(numero1, numero2)
print(f"La suma de {numero1} y {numero2} es: {resultado}")
