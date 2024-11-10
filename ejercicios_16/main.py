from bdd import conectar_bdd
from menu import mostrar_menu

# Conexión a la base de datos
conexion = conectar_bdd("supermercado")

# Si la conexión es exitosa
if conexion and conexion.is_connected():
    # Mostrar menu
    mostrar_menu(conexion)

    # Cerrar conexión
    conexion.close()
