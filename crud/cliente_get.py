from mysql.connector import Error
import sys
import os
from tabulate import tabulate

# Agrega el directorio de `conexion` a sys.path
ruta_conexion_bd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conexion'))
sys.path.append(ruta_conexion_bd)

from conexion_bd import obtener_conexion, cerrar_conexion

def obtenerDatos():
    conexion = obtener_conexion()
    if conexion is None:
        print("No se estableció la conexión correctamente")
        return
    try:
        cursor = conexion.cursor()
        query = "SELECT * FROM clientes_datos"
        cursor.execute(query)
        
        datos = cursor.fetchall()
        
        print(f"{tabulate(datos,headers=["ID","Nombre","Apellidos","Direccion","CP","Provincia","Municipio","Empresa_id"],tablefmt="grid")}")
    except Error as e:
        print(f"Error al obtener datos: {e}")
    finally:
        cursor.close()
        cerrar_conexion(conexion)    

if __name__ == "__main__":
    obtenerDatos()
