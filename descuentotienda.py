# Solicitar el monto gastado por el cliente
monto = float(input("Ingresa el monto gastado: $"))

# Calcular el monto final
if monto > 100:
    descuento = monto * 0.20
    monto_final = monto - descuento
else:
    monto_final = monto

# Mostrar el monto final
print(f"Monto final: ${monto_final:.2f}")
