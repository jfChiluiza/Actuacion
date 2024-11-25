# Definir la función de saludo
def saludar(nombre):
    return f"Hola, {nombre}!"

# Solicitar el nombre al usuario
nombre_usuario = input("Ingresa tu nombre: ")

# Llamar a la función y mostrar el saludo
saludo = saludar(nombre_usuario)
print(saludo)
