ingresos = [int(input(f"Ingreso {i}: ")) for i in range(1, 4)]
gastos = [int(input(f"Gasto {i}: ")) for i in range(1, 4)]

total = sum(ingresos) - sum(gastos)
print(total)

if total > 0:
    print("Balance positivo.")
elif total < 0:
    print("Balance negativo.")
else:
    print("El balance es 0.")
