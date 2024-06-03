from mysql.connector import Error
import sys
import os
from fpdf import FPDF

# Agrega el directorio de `conexion` a sys.path
ruta_conexion_bd = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'conexion'))
sys.path.append(ruta_conexion_bd)

from conexion_bd import obtener_conexion, cerrar_conexion

conexion = obtener_conexion()
cursor = conexion.cursor()
query = "SELECT * FROM clientes_datos"
cursor.execute(query)
datos = cursor.fetchall()

# Obtener los nombres de las columnas
columnas = [i[0] for i in cursor.description]

# Crear la clase PDF heredando de FPDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Reporte de Empresas', 0, 1, 'C')
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 14)
        self.multi_cell(0, 10, body)
        self.ln()

# Crear el archivo PDF
def crear_archivo(nombre_archivo):
    pdf = PDF()
    pdf.add_page()

    # Ancho fijo para cada columna
    ancho_columna = 50

    # Títulos de columnas
    pdf.set_font('Arial', 'B', 14)
    for columna in columnas:
        pdf.cell(ancho_columna, 10, columna, 1)
    pdf.ln()

    # Filas de datos
    pdf.set_font('Arial', '', 12)
    for row in datos:
        for item in row:
            pdf.cell(ancho_columna, 10, str(item), 1)
        pdf.ln()

    pdf.output(nombre_archivo)

# Llamada a la función para crear el archivo
crear_archivo('cliente.pdf')
