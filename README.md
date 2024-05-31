# Proyecto CRUD en Python

Este proyecto consiste en un sistema CRUD (Crear, Leer, Actualizar, Eliminar) desarrollado en Python para interactuar con una base de datos MySQL. El proyecto está organizado en varias carpetas que contienen diferentes componentes del sistema.


# Estructura de carpetas

El proyecto tiene la siguiente estructura de carpetas:

. conexion: Contiene los archivos relacionados con la conexión a la base de datos MySQL.
. crud: Contiene los archivos que realizan las consultas a la base de datos para llevar a cabo las operaciones CRUD.
. menu: Contiene el archivo que despliega el menú de opciones en la consola para que el usuario interactúe con el sistema.

# Componentes

`conexion`
En esta carpeta se encuentra el archivo conexion_bd.py que contiene funciones para establecer y cerrar la conexión a la base de datos MySQL.

`crud`
Esta carpeta contiene varios archivos, cada uno con funciones para realizar operaciones CRUD en la base de datos:

. `cliente_delete.py`: Funciones para eliminar registros de la base de datos.
. `cliente_get.py`: Funciones para obtener datos de la base de datos.
. `cliente_insert.py`: Funciones para insertar nuevos registros en la base de datos.
.`clientes_update.py`: Funciones para actualizar registros en la base de datos.

`menu`
En esta carpeta se encuentra el archivo main.py, que despliega un menú de opciones en la consola para que el usuario pueda interactuar con el sistema. Este archivo llama a las funciones definidas en la carpeta crud según la opción seleccionada por el usuario.

# Uso

1. Asegúrate de tener Python y MySQL instalados en tu sistema.
2. Configura la conexión a tu base de datos MySQL en el archivo conexion_bd.py.
3. Ejecuta el archivo menu.py para comenzar a interactuar con el sistema CRUD.


# Contacto
email:arielaparicio100@gmail.com
linkedin:https://www.linkedin.com/in/arielaparicio