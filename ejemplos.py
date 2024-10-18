#Ejercicio Obligatorio 
#Descripcion
#Crear una base de datos usando codigo .py directamente y manejar datos (crear,eliminar,modificar,comprobar...)
import sqlite3  # Importa el módulo sqlite3 para trabajar con bases de datos SQLite

# Función para crear la base de datos y las tablas
def crear_base_de_datos():
    conn = sqlite3.connect('ejer_obligatorio.db')  # Conecta a la base de datos 'jugadores.db' (la crea si no existe)
    c = conn.cursor()  # Crea un cursor para interactuar con la base de datos

    # Crea la tabla JUGADORES si no existe
    c.execute('''
    CREATE TABLE IF NOT EXISTS JUGADORES (
        id INTEGER PRIMARY KEY,  # Campo id como clave primaria
        nombre TEXT NOT NULL,    # Campo nombre, no puede ser nulo
        vida INTEGER NOT NULL     # Campo vida, no puede ser nulo
    )
    ''')

    # Crea la tabla CREDENCIALES si no existe
    c.execute('''
    CREATE TABLE IF NOT EXISTS CREDENCIALES (
        id INTEGER PRIMARY KEY,  # Campo id como clave primaria
        jugador TEXT NOT NULL,   # Campo jugador, no puede ser nulo
        contraseña TEXT NOT NULL,  # Campo contraseña, no puede ser nulo
        FOREIGN KEY (jugador) REFERENCES JUGADORES (nombre)  # Relación con la tabla JUGADORES
    )
    ''')
    
    conn.commit()  # Guarda los cambios en la base de datos
    conn.close()   # Cierra la conexión

# Función para imprimir todos los jugadores
def imprimir_jugadores(c):
    c.execute("SELECT nombre, vida FROM JUGADORES")  # Ejecuta la consulta para obtener nombres y vidas
    jugadores = c.fetchall()  # Obtiene todos los resultados de la consulta
    print("IMPRIMIR JUGADORES")  # Imprime un encabezado
    for jugador in jugadores:  # Itera sobre la lista de jugadores
        print(f"Nombre: {jugador[0]} - Vida: {jugador[1]}")  # Imprime el nombre y la vida de cada jugador

# Función para validar credencial
def validar_credencial(c):
    jugador = input("Dame jugador: ")  # Solicita el nombre del jugador
    contraseña = input("Dame contraseña: ")  # Solicita la contraseña
    
    # Comprueba si la credencial es válida
    if existe_credencial(c, jugador, contraseña):
        print(f"[{jugador}/{contraseña}] si es una credencial valida")  # Si es válida, lo indica
    else:
        print(f"[{jugador}/{contraseña}] no es una credencial valida")  # Si no es válida, lo indica

# Función para cambiar credencial
def cambiar_credencial(conn, c):
    jugador = input("Dame jugador: ")  # Solicita el nombre del jugador
    
    # Comprueba si el jugador existe
    if not existe_jugador(c, jugador):
        print("ERROR: El jugador no existe")  # Muestra error si no existe
        return  # Sale de la función

    contraseña_vieja = input("Dame contraseña vieja: ")  # Solicita la contraseña antigua
    
    # Comprueba si la credencial introducida es válida
    if not existe_credencial(c, jugador, contraseña_vieja):
        print(f"[{jugador}/{contraseña_vieja}] no es una credencial valida")  # Muestra error si no es válida
        return  # Sale de la función

    nueva_contraseña = input("Dame contraseña nueva: ")  # Solicita la nueva contraseña
    c.execute("UPDATE CREDENCIALES SET contraseña = ? WHERE jugador = ?", (nueva_contraseña, jugador))  # Actualiza la contraseña
    conn.commit()  # Guarda los cambios
    print(f"La contraseña del jugador <{jugador}> se ha modificado correctamente")  # Confirma el cambio

# Función para insertar un nuevo jugador
def insertar_jugador(conn, c):
    nombre = input("Dame nombre: ")  # Solicita el nombre del nuevo jugador
    
    # Comprueba si el jugador ya existe
    if existe_jugador(c, nombre):
        print("ERROR: El jugador ya existe")  # Muestra error si ya existe
        return  # Sale de la función

    vida = int(input("Dame vida: "))  # Solicita la vida del jugador
    contraseña = input("Dame contraseña: ")  # Solicita la contraseña del jugador

    # Inserta el nuevo jugador en la tabla JUGADORES
    c.execute("INSERT INTO JUGADORES (nombre, vida) VALUES (?, ?)", (nombre, vida))
    # Inserta la credencial del nuevo jugador en la tabla CREDENCIALES
    c.execute("INSERT INTO CREDENCIALES (jugador, contraseña) VALUES (?, ?)", (nombre, contraseña))
    conn.commit()  # Guarda los cambios
    print(f"El jugador <{nombre}> se ha insertado correctamente")  # Confirma la inserción

# Función para borrar un jugador
def borrar_jugador(conn, c):
    nombre = input("Dame el nombre del jugador: ")  # Solicita el nombre del jugador a borrar
    
    # Comprueba si el jugador existe
    if not existe_jugador(c, nombre):
        print("ERROR: El jugador no existe")  # Muestra error si no existe
        return  # Sale de la función

    # Elimina el jugador de la tabla JUGADORES
    c.execute("DELETE FROM JUGADORES WHERE nombre = ?", (nombre,))
    # Elimina las credenciales del jugador de la tabla CREDENCIALES
    c.execute("DELETE FROM CREDENCIALES WHERE jugador = ?", (nombre,))
    conn.commit()  # Guarda los cambios
    print(f"Se ha eliminado el jugador <{nombre}> correctamente")  # Confirma la eliminación

# Función para comprobar si existe un jugador
def existe_jugador(c, nombre):
    c.execute("SELECT 1 FROM JUGADORES WHERE nombre = ?", (nombre,))  # Ejecuta la consulta para buscar el jugador
    return c.fetchone() is not None  # Devuelve True si el jugador existe, False en caso contrario

# Función para comprobar si existe una credencial
def existe_credencial(c, jugador, contraseña):
    c.execute("SELECT 1 FROM CREDENCIALES WHERE jugador = ? AND contraseña = ?", (jugador, contraseña))  # Ejecuta la consulta
    return c.fetchone() is not None  # Devuelve True si la credencial es válida, False en caso contrario

# Función principal para el menú
def menu():
    crear_base_de_datos()  # Llama a la función para crear la base de datos y las tablas
    conn = sqlite3.connect('jugadores.db')  # Conecta a la base de datos
    c = conn.cursor()  # Crea un cursor para interactuar con la base de datos

    while True:  # Bucle infinito para mostrar el menú
        print("==========================")
        print("       CREDENCIALES DE JUGADORES")
        print("==========================")
        print("1 - imprimir jugadores")  # Opción 1
        print("2 - Validar credencial")  # Opción 2
        print("3 - Cambiar credencial")  # Opción 3
        print("4 - insertar nuevo jugador")  # Opción 4
        print("5 - borrar jugador")  # Opción 5
        print("0 - salir")  # Opción 0 para salir
        print("--------------------------------------------")

        opcion = input("Selecciona una opción: ")  # Solicita la opción al usuario
        
        # Ejecuta la función correspondiente según la opción seleccionada
        if opcion == '1':
            imprimir_jugadores(c)
        elif opcion == '2':
            validar_credencial(c)
        elif opcion == '3':
            cambiar_credencial(conn, c)
        elif opcion == '4':
            insertar_jugador(conn, c)
        elif opcion == '5':
            borrar_jugador(conn, c)
        elif opcion == '0':
            break  # Sale del bucle y termina el programa
        else:
            print("Opción no válida")  # Muestra un mensaje si la opción es inválida

    conn.close()  # Cierra la conexión a la base de datos al salir del menú

if __name__ == "__main__":
    menu()  # Llama a la función del menú al ejecutar el script


1. Gestión de Estudiantes
#Descripción
#Este programa permite agregar, eliminar, y listar estudiantes en una base de datos.

python
Copiar código
import sqlite3

def crear_base_de_datos():
    conn = sqlite3.connect('estudiantes.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS ESTUDIANTES (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def agregar_estudiante(conn, c):
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad del estudiante: "))
    c.execute("INSERT INTO ESTUDIANTES (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()
    print("Estudiante agregado.")

def listar_estudiantes(c):
    c.execute("SELECT nombre, edad FROM ESTUDIANTES")
    estudiantes = c.fetchall()
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante[0]}, Edad: {estudiante[1]}")

def eliminar_estudiante(conn, c):
    nombre = input("Nombre del estudiante a eliminar: ")
    c.execute("DELETE FROM ESTUDIANTES WHERE nombre = ?", (nombre,))
    conn.commit()
    print("Estudiante eliminado.")

def menu():
    crear_base_de_datos()
    conn = sqlite3.connect('estudiantes.db')
    c = conn.cursor()
    while True:
        print("1 - Agregar estudiante")
        print("2 - Listar estudiantes")
        print("3 - Eliminar estudiante")
        print("0 - Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            agregar_estudiante(conn, c)
        elif opcion == '2':
            listar_estudiantes(c)
        elif opcion == '3':
            eliminar_estudiante(conn, c)
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")
    conn.close()

if __name__ == "__main__":
    menu()
    
2. Gestión de Inventario
#Descripción
#Este programa permite agregar, eliminar y consultar productos en un inventario.

import sqlite3

def crear_base_de_datos():
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS PRODUCTOS (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        cantidad INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def agregar_producto(conn, c):
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad del producto: "))
    c.execute("INSERT INTO PRODUCTOS (nombre, cantidad) VALUES (?, ?)", (nombre, cantidad))
    conn.commit()
    print("Producto agregado.")

def listar_productos(c):
    c.execute("SELECT nombre, cantidad FROM PRODUCTOS")
    productos = c.fetchall()
    for producto in productos:
        print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}")

def eliminar_producto(conn, c):
    nombre = input("Nombre del producto a eliminar: ")
    c.execute("DELETE FROM PRODUCTOS WHERE nombre = ?", (nombre,))
    conn.commit()
    print("Producto eliminado.")

def menu():
    crear_base_de_datos()
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    while True:
        print("1 - Agregar producto")
        print("2 - Listar productos")
        print("3 - Eliminar producto")
        print("0 - Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            agregar_producto(conn, c)
        elif opcion == '2':
            listar_productos(c)
        elif opcion == '3':
            eliminar_producto(conn, c)
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")
    conn.close()

if __name__ == "__main__":
    menu()

3. Gestión de Tareas
#Descripción
#Este programa permite gestionar tareas pendientes.

import sqlite3

def crear_base_de_datos():
    conn = sqlite3.connect('tareas.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS TAREAS (
        id INTEGER PRIMARY KEY,
        descripcion TEXT NOT NULL,
        completada INTEGER NOT NULL DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

def agregar_tarea(conn, c):
    descripcion = input("Descripción de la tarea: ")
    c.execute("INSERT INTO TAREAS (descripcion) VALUES (?)", (descripcion,))
    conn.commit()
    print("Tarea agregada.")

def listar_tareas(c):
    c.execute("SELECT id, descripcion, completada FROM TAREAS")
    tareas = c.fetchall()
    for tarea in tareas:
        estado = "Completada" if tarea[2] else "Pendiente"
        print(f"ID: {tarea[0]}, Descripción: {tarea[1]}, Estado: {estado}")

def marcar_tarea_completada(conn, c):
    id_tarea = int(input("ID de la tarea a marcar como completada: "))
    c.execute("UPDATE TAREAS SET completada = 1 WHERE id = ?", (id_tarea,))
    conn.commit()
    print("Tarea marcada como completada.")

def menu():
    crear_base_de_datos()
    conn = sqlite3.connect('tareas.db')
    c = conn.cursor()
    while True:
        print("1 - Agregar tarea")
        print("2 - Listar tareas")
        print("3 - Marcar tarea como completada")
        print("0 - Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            agregar_tarea(conn, c)
        elif opcion == '2':
            listar_tareas(c)
        elif opcion == '3':
            marcar_tarea_completada(conn, c)
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")
    conn.close()

if __name__ == "__main__":
    menu()
4. Gestión de Clientes
Descripción
Este programa permite agregar, eliminar y consultar clientes en una base de datos.

python
Copiar código
import sqlite3

def crear_base_de_datos():
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS CLIENTES (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def agregar_cliente(conn, c):
    nombre = input("Nombre del cliente: ")
    email = input("Email del cliente: ")
    c.execute("INSERT INTO CLIENTES (nombre, email) VALUES (?, ?)", (nombre, email))
    conn.commit()
    print("Cliente agregado.")

def listar_clientes(c):
    c.execute("SELECT nombre, email FROM CLIENTES")
    clientes = c.fetchall()
    for cliente in clientes:
        print(f"Nombre: {cliente[0]}, Email: {cliente[1]}")

def eliminar_cliente(conn, c):
    nombre = input("Nombre del cliente a eliminar: ")
    c.execute("DELETE FROM CLIENTES WHERE nombre = ?", (nombre,))
    conn.commit()
    print("Cliente eliminado.")

def menu():
    crear_base_de_datos()
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    while True:
        print("1 - Agregar cliente")
        print("2 - Listar clientes")
        print("3 - Eliminar cliente")
        print("0 - Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            agregar_cliente(conn, c)
        elif opcion == '2':
            listar_clientes(c)
        elif opcion == '3':
            eliminar_cliente(conn, c)
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")
    conn.close()

if __name__ == "__main__":
    menu()
"""
1-Comprende la Estructura: Todos los ejemplos siguen una estructura similar: crear base de datos, definir funciones para cada operación, y un menú principal. Familiarízate con esta estructura.
2-Practica: Modifica los ejemplos, añade nuevas funcionalidades o cambia tipos de datos. Practicar variaciones te ayudará a sentirte más cómodo.
3-Entiende el Uso de SQLite: Asegúrate de entender cómo funcionan las operaciones CRUD (Crear, Leer, Actualizar, Borrar) y cómo interactuar con SQLite.
4-Errores Comunes: Revisa cómo manejar errores, como entradas inválidas o intentos de eliminar un elemento que no existe.
5-Documentación: Si algo no está claro, consulta la documentación de SQLite y Python. Entender cómo funcionan las funciones que utilizas es clave.

resumen:

Conceptos Clave
Conexión a la Base de Datos:
    Cómo conectarse y desconectarse de una base de datos usando sqlite3.connect() y conn.close().
Creación de Tablas:
    Uso de SQL para crear tablas y definir sus campos con tipos de datos adecuados.
Operaciones CRUD:
    Crear: Inserción de nuevos registros con INSERT.
    Leer: Consultas para obtener datos con SELECT.
    Actualizar: Modificación de registros existentes con UPDATE.
    Borrar: Eliminación de registros con DELETE.
Uso de Cursores:
    Cómo usar un cursor (conn.cursor()) para ejecutar comandos SQL y manejar resultados.
Funciones:
    Organización del código en funciones para mantener la claridad y la modularidad.
Validaciones:
    Comprobación de la existencia de registros antes de realizar acciones, como eliminar o actualizar.
Interacción con el Usuario:
    Uso de input() para obtener datos del usuario y mostrar información en la consola.
Consejos Adicionales
    Práctica Regular: La mejor manera de consolidar tu conocimiento es practicar. Intenta modificar los ejemplos o crear nuevos desde cero.
    Resuelve Problemas Comunes: Familiarízate con errores comunes y cómo solucionarlos. Por ejemplo, manejar entradas inválidas.
    Consulta la Documentación: La documentación de Python y SQLite es un recurso invaluable para resolver dudas y aprender más.
Preguntas Potenciales
    Explicar cómo crear una tabla y qué tipos de datos se pueden usar.
    Describir cómo realizar una operación de actualización en la base de datos.
    Escribir una función que maneje la validación de datos.
Si te sientes cómodo con estos conceptos y puedes aplicarlos, ¡estarás bien preparado para tu examen! Si tienes más dudas o necesitas practicar más, no dudes en preguntar.
"""


