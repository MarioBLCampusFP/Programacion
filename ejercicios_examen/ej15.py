import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="inventario"
)

cursor = conexion.cursor()

consulta = """
CREATE TABLE IF NOT EXISTS productos (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(30),
    precio DECIMAL(5,2)
)
"""

# Crear la tabla
cursor.execute(consulta)

consulta = "INSERT INTO productos VALUES (%s, %s, %s)"

# Insertar registros
try:
    cursor.execute(consulta, (1, "Mesa", 150.00))
    cursor.execute(consulta, (2, "Silla", 75.00))
    conexion.commit()
    print("Productos registrados correctamente.")
except mysql.connector.errors.IntegrityError:
    print("Los productos ya están registrados.")

# Cerrar conexión y cursor
cursor.close()
conexion.close()
