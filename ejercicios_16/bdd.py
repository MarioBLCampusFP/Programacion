import getpass
import mysql.connector
from mysql.connector import errorcode


def conectar_bdd(bdd):
    """Crea una conexión a la base de datos especificada."""
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user=input("Usuario: "),
            password=getpass.getpass("Contraseña: "),
            database=bdd,
        )
        print(f"Conexión exitosa a la base de datos {bdd}.")
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error de acceso a la base de datos.")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"La base de datos {bdd} no existe.")
        else:
            print(f"Error al conectar a la base de datos: {e}")
    return conexion
