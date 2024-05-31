from mysql.connector import Error
import sys
import os

# Agrega el directorio de `conexion` a sys.path
ruta_conexion_bd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conexion'))
sys.path.append(ruta_conexion_bd)

from conexion_bd import obtener_conexion, cerrar_conexion

def eliminarDatos():
    conexion = obtener_conexion()
    if conexion is None:
        print("No se ha podido establecer la conexión")
        return
    try:
        cursor = conexion.cursor()
        numero = int(input("Ingrese el ID del cliente que desea eliminar: "))
        query = "DELETE FROM clientes_datos WHERE id = %s"  # Suponiendo que el identificador de cliente es 'id'
        cursor.execute(query, (numero,))
        conexion.commit()  # Confirma la eliminación
        print("Registro eliminado exitosamente")
    except Error as e:
        print(f"Error al eliminar datos: {e}")
    finally:
        cursor.close()
        cerrar_conexion(conexion)


if __name__ == "__main__":
    eliminarDatos()
        