"""
Administración de los entrenadores.
"""

from bdd import conectar_bdd
from prettytable import from_db_cursor
from termcolor import cprint
import mysql.connector


def crear_entrenador(nombre, especialidad):
    """Registra un nuevo entrenador."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta = "INSERT INTO entrenadores (nombre_entrenador, especialidad) VALUES (%s, %s)"
        try:
            cursor.execute(consulta, (nombre, especialidad))
            conexion.commit()
            cprint(f"[Mensaje]: Entrenador registrado exitosamente.", "green")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()


def ver_entrenadores():
    """Visualiza todos los entrenadores."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM entrenadores"
        try:
            cursor.execute(consulta)
            cprint(from_db_cursor(cursor), "cyan")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
        finally:
            cursor.close()
            conexion.close()


def actualizar_entrenador(id_entrenador, especialidad):
    """Actualiza información de un entrenador."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta = "UPDATE entrenadores SET especialidad = %s WHERE id_entrenador = %s"
        try:
            cursor.execute(consulta, (especialidad, id_entrenador))
            conexion.commit()
            if cursor.rowcount:
                cprint(f"[Mensaje]: Entrenador actualizado exitosamente.", "green")
            else:
                cprint(f"[Error]: Entrenador con ID {id_entrenador} no encontrado.", "red")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()


def eliminar_entrenador(id_entrenador):
    """Elimina un entrenador y sus actividades asociadas."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta_actividades = "DELETE FROM actividades WHERE id_entrenador = %s"
        consulta_entrenadores = "DELETE FROM entrenadores WHERE id_entrenador = %s"
        try:
            cursor.execute(consulta_actividades, (id_entrenador,))
            cursor.execute(consulta_entrenadores, (id_entrenador,))
            conexion.commit()
            if cursor.rowcount:
                cprint(f"[Mensaje]: Entrenador con ID {id_entrenador} eliminado exitosamente.", "green")
            else:
                cprint(f"[Error]: Entrenador con ID {id_entrenador} no encontrado.", "red")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()
