# Solicitar la edad del usuario
edad = int(input("Ingresa tu edad: "))

# Clasificar al usuario según su edad
if edad >= 0 and edad <= 12:
    print("Eres niño.")
elif edad >= 13 and edad <= 17:
    print("Eres adolescente.")
else:
    print("Eres adulto.")
