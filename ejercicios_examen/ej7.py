import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="tienda"
)

cursor = conexion.cursor()

consulta = """
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(30),
    edad TINYINT
)
"""

# Crear la tabla
cursor.execute(consulta)

consulta = "INSERT INTO clientes VALUES (%s, %s, %s)"

# Insertar registros
try:
    cursor.execute(consulta, (1, "Ana", 30))
    cursor.execute(consulta, (2, "Luis", 25))
    conexion.commit()
    print("Clientes registrados correctamente.")
except mysql.connector.errors.IntegrityError:
    print("Los clientes ya están registrados.")

# Cerrar conexión y cursor
cursor.close()
conexion.close()
