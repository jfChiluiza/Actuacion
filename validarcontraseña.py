# Contraseña fija
contraseña_fija = "12345"

# Solicitar la contraseña al usuario
contraseña = input("Ingresa la contraseña: ")

# Validar si la contraseña es correcta
if contraseña == contraseña_fija:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")
