"""
Gestión de la conexión a la base de datos del centro deportivo.
"""

from termcolor import cprint
from getpass import getpass
import mysql.connector

# Variables globales para las credenciales
MYSQL_USER = ""
MYSQL_PASSWORD = ""


def obtener_credenciales():
    """Obtiene las credenciales MySQL del usuario."""
    global MYSQL_USER, MYSQL_PASSWORD
    MYSQL_USER = input("Ingrese el nombre de usuario de MySQL: ")
    MYSQL_PASSWORD = getpass("Ingrese la contraseña de MySQL: ")
    # Volver a pedir credenciales si la conexión no es exitosa
    if not conectar_bdd():
        obtener_credenciales()


def conectar_bdd():
    """Crea una conexión a la base de datos."""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database="centro_deportivo",
        )
        return conexion
    except mysql.connector.Error as e:
        cprint(f"[Error]: {e}", "red")
    return None
