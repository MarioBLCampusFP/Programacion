import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="inventario"
)

cursor = conexion.cursor()

consulta = """
SELECT nombre
FROM productos
WHERE precio > 100
"""

cursor.execute(consulta)
productos = cursor.fetchall()
if productos:
    print(f"Productos con precio mayor a 100€: {[producto[0] for producto in productos]}")
else:
    print("No hay productos con precio superior a 100€.")

consulta = "SELECT AVG(precio) FROM productos"
cursor.execute(consulta)

promedio = cursor.fetchone()
if promedio[0] is not None:
    print(f"Promedio: {promedio[0]:.2f}€")
else:
    print("No hay precios registrados para hacer el promedio.")

cursor.close()
conexion.close()
