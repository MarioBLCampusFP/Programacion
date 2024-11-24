"""
Relación entre clientes y actividades.
"""

from bdd import conectar_bdd
from prettytable import from_db_cursor
from termcolor import cprint
import mysql.connector


def crear_inscripcion(id_cliente, id_actividad):
    """Registra una nueva inscripcion."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta = "INSERT INTO inscripciones (id_cliente, id_actividad) VALUES (%s, %s)"
        try:
            cursor.execute(consulta, (id_cliente, id_actividad))
            conexion.commit()
            cprint(f"[Mensaje]: Inscripcion registrada exitosamente.", "green")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()


def ver_inscripciones():
    """Visualiza todas las inscripciones."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta = (
            "SELECT i.id_inscripcion, c.*, a.*, e.nombre_entrenador "
            "FROM inscripciones i "
            "JOIN clientes c ON i.id_cliente = c.id_cliente "
            "JOIN actividades a ON i.id_actividad = a.id_actividad "
            "JOIN entrenadores e ON a.id_entrenador = e.id_entrenador"
        )
        try:
            cursor.execute(consulta)
            cprint(from_db_cursor(cursor), "cyan")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
        finally:
            cursor.close()
            conexion.close()


def eliminar_inscripcion(id_inscripcion):
    """Elimina una inscripcion."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta = "DELETE FROM inscripciones WHERE id_inscripcion = %s"
        try:
            cursor.execute(consulta, (id_inscripcion,))
            conexion.commit()
            if cursor.rowcount:
                cprint(f"[Mensaje]: Inscripcion con ID {id_inscripcion} eliminada exitosamente.", "green")
            else:
                cprint(f"[Error]: Inscripcion con ID {id_inscripcion} no encontrada.", "red")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()
