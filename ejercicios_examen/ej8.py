import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="tienda"
)

cursor = conexion.cursor()

consulta = """
SELECT nombre
FROM clientes
WHERE edad > 25
"""

cursor.execute(consulta)
clientes = cursor.fetchall()
if clientes:
    print(f"Mayores de 25: {[cliente[0] for cliente in clientes]}")
else:
    print("No hay clientes mayores a 25 años.")

consulta = "SELECT AVG(edad) FROM clientes"
cursor.execute(consulta)

promedio = cursor.fetchone()
if promedio[0] is not None:
    print(f"Promedio: {promedio[0]}")
else:
    print("No hay edades registradas para hacer el promedio.")

cursor.close()
conexion.close()
