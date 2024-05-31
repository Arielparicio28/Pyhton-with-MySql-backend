import os
import sys


menu = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'crud'))
sys.path.append(menu)

from cliente_delete import eliminarDatos
from cliente_get import obtenerDatos
from cliente_insert import insertarDatos
from cliente_update import actualizarDatos


def mostrar_menu():
    print("Menú:")
    print("1. Insertar datos")
    print("2. Actualizar datos")
    print("3. Eliminar datos")
    print("4. Obtener datos")
    print("5. Salir")
    

def continuar():
    while True:
        respuesta = input("¿Desea continuar? (s/n): ").lower()
        if respuesta in ('s', 'si'):
            return True
        elif respuesta in ('n', 'no'):
            return False
        else:
            print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            insertarDatos()
            if not continuar():
                break
        elif opcion == "2":
            actualizarDatos()
            if not continuar():
                break
        elif opcion == "3":
            eliminarDatos()
            if not continuar():
                break
        elif opcion == "4":
            obtenerDatos()   
            if not continuar():
                break
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
