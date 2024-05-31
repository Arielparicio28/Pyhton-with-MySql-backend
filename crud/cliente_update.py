from mysql.connector import Error
import sys
import os

# Agrega el directorio de `conexion` a sys.path
ruta_conexion_bd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conexion'))
sys.path.append(ruta_conexion_bd)


from conexion_bd import obtener_conexion, cerrar_conexion

def actualizarDatos():
    conexion = obtener_conexion()
    if conexion is None:
        print("No se ha podido establecer la conexión")
        return
    try:
        cursor = conexion.cursor()
        id_cliente = int(input("Ingrese el ID del cliente que desea actualizar: "))
        nombre = input("Indique su nombre: ").title()
        apellidos = input("Indique sus apellidos: ").title()
        direccion = input("Indique su dirección: ").title()
        codigo_postal = input("Indique su CP: ")
        provincia = input("Indique su provincia: ").capitalize()
        municipio = input("Indique su municipio: ")
        
        """%s es un marcador de posición para valores en una consulta preparada o parametrizada. 
         Estas consultas permiten ejecutar comandos SQL de forma segura al sustituir valores específicos
         en la consulta con los valores reales proporcionados por el usuario o el programa. """
        # Construye la consulta SQL para actualizar los datos del cliente
        # Marcadores de posición %s. Esto ayuda a prevenir ataques de inyección SQL y permite una separación clara entre la lógica de la consulta y los datos que se están utilizando.
        query = "UPDATE clientes_datos SET nombre = %s, apellidos = %s, direccion = %s, codigo_postal = %s,provincia = %s, municipio = %s WHERE id = %s"
        datos_nuevos = (nombre,apellidos,direccion,codigo_postal,provincia,municipio, id_cliente)
        
        # Ejecuta la consulta con los nuevos datos
        cursor.execute(query, datos_nuevos)
        conexion.commit()  # Confirma los cambios en la base de datos
        print("Datos actualizados exitosamente")
    except Error as e:
        print(f"Error al actualizar datos: {e}")
    finally:
        cursor.close()
        cerrar_conexion(conexion)
        
        
if __name__ == '__main__':
    actualizarDatos()        
