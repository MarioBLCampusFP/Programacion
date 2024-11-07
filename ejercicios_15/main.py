from bdd import conectar_bdd
from menu import mostrar_menu

# Conexión a la base de datos
conexion = conectar_bdd("supermercado")

# Crear cursor
cursor = conexion.cursor()

# Mostrar menu
mostrar_menu(conexion, cursor)

# Cerrar cursor y conexión
cursor.close()
conexion.close()
