import mysql.connector


# Conexión a la base de datos
def conectar_bdd(bdd):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user=input("Usuario: "),
            password=input("Contraseña: "),
            database=bdd,
        )
        if conexion.is_connected():
            print(f"Conexión exitosa a la base de datos {bdd}.")
            return conexion
    except mysql.connector.Error:
        print(f"Error al conectar a la base de datos.")
        exit()
