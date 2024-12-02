gastos = ["electricidad", "agua", "gas", "comida"]

gasto_total = 0
for gasto in gastos:
    gasto_total += int(input(f"Ingrese el gasto mensual de {gasto}: "))

print(f"Gasto total: {gasto_total}")
if gasto_total > 500:
    print("Estás gastando mucho!")
