"""
Gestión de las actividades ofrecidas en el gimnasio.
"""

from bdd import conectar_bdd
from prettytable import from_db_cursor
from termcolor import cprint
import mysql.connector


def crear_actividad(nombre, horario, duracion, id_entrenador):
    """Registra una nueva actividad."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta = "INSERT INTO actividades (nombre_actividad, horario, duracion, id_entrenador) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(consulta, (nombre, horario, duracion, id_entrenador))
            conexion.commit()
            cprint(f"[Mensaje]: Actividad registrada exitosamente.", "green")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()


def ver_actividades():
    """Visualiza todas las actividades."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM actividades"
        try:
            cursor.execute(consulta)
            cprint(from_db_cursor(cursor), "cyan")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
        finally:
            cursor.close()
            conexion.close()


def actualizar_actividad(id_actividad, horario):
    """Actualiza información de una actividad."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta = "UPDATE actividades SET horario = %s WHERE id_actividad = %s"
        try:
            cursor.execute(consulta, (horario, id_actividad))
            conexion.commit()
            if cursor.rowcount:
                cprint(f"[Mensaje]: Actividad actualizada exitosamente.", "green")
            else:
                cprint(f"[Error]: Actividad con ID {id_actividad} no encontrada.", "red")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()


def eliminar_actividad(id_actividad):
    """Elimina una actividad y sus inscripciones asociadas."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta_inscripcion = "DELETE FROM inscripciones WHERE id_actividad = %s"
        consulta_actividad = "DELETE FROM actividades WHERE id_actividad = %s"
        try:
            cursor.execute(consulta_inscripcion, (id_actividad,))
            cursor.execute(consulta_actividad, (id_actividad,))
            conexion.commit()
            if cursor.rowcount:
                cprint(f"[Mensaje]: Actividad con ID {id_actividad} eliminada exitosamente.", "green")
            else:
                cprint(f"[Error]: Actividad con ID {id_actividad} no encontrada.", "red")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()
