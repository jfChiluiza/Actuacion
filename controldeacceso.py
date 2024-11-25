# Credenciales correctas
usuario_correcto = "admin"
contraseña_correcta = "1234"

# Inicializar el contador de intentos
intentos = 0
max_intentos = 3

# Bucle para permitir hasta tres intentos
while intentos < max_intentos:
    # Solicitar nombre de usuario y contraseña
    usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    
    # Validar credenciales
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print(f"Bienvenido, {usuario}.")
        break
    else:
        intentos += 1
        print("Usuario o contraseña incorrectos.")
        
        # Verificar si se agotaron los intentos
        if intentos == max_intentos:
            print("Acceso bloqueado. Has excedido el número de intentos.")
