from mysql.connector import Error
import sys
import os
# Agrega el directorio de `conexion` a sys.path
ruta_conexion_bd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conexion'))
sys.path.append(ruta_conexion_bd)

from conexion_bd import obtener_conexion, cerrar_conexion


def insertarDatos():
    conexion = obtener_conexion()
    if conexion is None:
        print("No se establecio la conexión correctamente con mi base de datos")
        return
    
    try:
        cursor = conexion.cursor()
        
    #title() transforma la primera letra de cada palabra en mayúscula y el resto en minúsculas. Esto es útil para nombres completos.
        nombre = input("Indique su nombre: ").title()
        apellidos = input("Indique sus apellidos: ").title()
        direccion = input("Indique su dirección: ").title()
        codigo_postal = input("Indique su CP: ")
        provincia = input("Indique su provincia: ").capitalize()
        municipio = input("Indique su municipio: ")
        
        #Query para insertar datos en la tabla clientes_datos
        query = "INSERT INTO clientes_datos(nombre,apellidos,direccion,codigo_postal,provincia,municipio) VALUES(%s, %s, %s,%s, %s, %s)"
        valores = (nombre,apellidos,direccion,codigo_postal,provincia,municipio)
        cursor.execute(query,valores)
        #Al llamar a commit(), confirmas que todos los cambios realizados en la transacción actual se guarden de manera permanente en la base de datos.
        conexion.commit()
        
        print(f"{cursor.rowcount} registro(s) insertado(s)")
    except Error as e:
        print(f"error al insertar datos: {e}")
    finally:
        cursor.close()
        cerrar_conexion(conexion)    


if __name__ == "__main__":
    insertarDatos()        
        