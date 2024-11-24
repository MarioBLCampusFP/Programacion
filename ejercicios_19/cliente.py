"""
Registro y edición de los usuarios del gimnasio.
"""

from bdd import conectar_bdd
from prettytable import from_db_cursor
from termcolor import cprint
import mysql.connector


def crear_cliente(nombre, edad, tipo_membresia):
    """Registra un nuevo cliente."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta = "INSERT INTO clientes (nombre, edad, tipo_membresia) VALUES (%s, %s, %s)"
        try:
            cursor.execute(consulta, (nombre, edad, tipo_membresia))
            conexion.commit()
            cprint(f"[Mensaje]: Cliente registrado exitosamente.", "green")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()


def ver_clientes():
    """Visualiza todos los clientes."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM clientes"
        try:
            cursor.execute(consulta)
            cprint(from_db_cursor(cursor), "cyan")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
        finally:
            cursor.close()
            conexion.close()


def actualizar_cliente(id_cliente, tipo_membresia):
    """Actualiza información de un cliente."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta = "UPDATE clientes SET tipo_membresia = %s WHERE id_cliente = %s"
        try:
            cursor.execute(consulta, (tipo_membresia, id_cliente))
            conexion.commit()
            if cursor.rowcount:
                cprint(f"[Mensaje]: Cliente actualizado exitosamente.", "green")
            else:
                cprint(f"[Error]: Cliente con ID {id_cliente} no encontrado.", "red")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()


def eliminar_cliente(id_cliente):
    """Elimina un cliente y sus inscripciones asociadas."""
    conexion = conectar_bdd()
    if conexion:
        cursor = conexion.cursor()
        consulta_inscripcion = "DELETE FROM inscripciones WHERE id_cliente = %s"
        consulta_cliente = "DELETE FROM clientes WHERE id_cliente = %s"
        try:
            cursor.execute(consulta_inscripcion, (id_cliente,))
            cursor.execute(consulta_cliente, (id_cliente,))
            conexion.commit()
            if cursor.rowcount:
                cprint(f"[Mensaje]: Cliente con ID {id_cliente} eliminado exitosamente.", "green")
            else:
                cprint(f"[Error]: Cliente con ID {id_cliente} no encontrado.", "red")
        except mysql.connector.Error as e:
            cprint(f"[Error]: {e}", "red")
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()
