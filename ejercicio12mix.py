import sqlite3

# Lista inicial de vuelos
vuelos = [
    {"origen": "Valencia", "destino": "Menorca", "dia": "15-08", "clase": "turista"},
    {"origen": "Valencia", "destino": "Tenerife", "dia": "20-08", "clase": "turista"},
    {"origen": "Paris", "destino": "Valencia", "dia": "15-08", "clase": "primera"},
    {"origen": "Atenas", "destino": "Valencia", "dia": "20-08", "clase": "primera"},
]

# Función para imprimir todos los vuelos
def imprimir(vuelos):
    for vuelo in vuelos:
        print(f"Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Dia: {vuelo['dia']}, Clase: {vuelo['clase']}")

# Función para buscar vuelos según el origen introducido por el usuario
def buscar_origen(vuelos):
    origen = input("Introduce el origen del vuelo: ")
    encontrados = [vuelo for vuelo in vuelos if vuelo['origen'].lower() == origen.lower()]
    if encontrados:
        for vuelo in encontrados:
            print(f"Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Dia: {vuelo['dia']}, Clase: {vuelo['clase']}")
    else:
        print("No se encontraron vuelos desde ese origen.")

# Función para imprimir el vuelo correspondiente al origen y destino introducido por el usuario
def imprimir_vuelo(vuelos):
    origen = input("Introduce el origen del vuelo: ")
    destino = input("Introduce el destino del vuelo: ")
    for vuelo in vuelos:
        if vuelo['origen'].lower() == origen.lower() and vuelo['destino'].lower() == destino.lower():
            print(f"Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Dia: {vuelo['dia']}, Clase: {vuelo['clase']}")
            return
    print("No se encontró el vuelo.")

# Función para cambiar la fecha de un vuelo existente
def cambiar_fecha(vuelos):
    origen = input("Introduce el origen del vuelo: ")
    destino = input("Introduce el destino del vuelo: ")
    for vuelo in vuelos:
        if vuelo['origen'].lower() == origen.lower() and vuelo['destino'].lower() == destino.lower():
            nueva_fecha = input("Introduce la nueva fecha: ")
            vuelo['dia'] = nueva_fecha
            print(f"La fecha del vuelo de {origen} a {destino} ha sido cambiada a {nueva_fecha}.")
            return
    print("No se encontró el vuelo.")

# Funciones para manejar jugadores y credenciales (similar a las del segundo ejercicio)
def crear_base_de_datos():
    try:
        conn = sqlite3.connect('ejer_obligatorio.db')
        c = conn.cursor()

        c.execute('''
        CREATE TABLE IF NOT EXISTS JUGADORES (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            nombre TEXT NOT NULL UNIQUE,    
            vida INTEGER NOT NULL     
        )
        ''')

        c.execute('''
        CREATE TABLE IF NOT EXISTS CREDENCIALES (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            jugador TEXT NOT NULL,   
            contrasena TEXT NOT NULL,  
            FOREIGN KEY (jugador) REFERENCES JUGADORES (nombre)  
        )
        ''')

        conn.commit()
        print("Base de datos y tablas creadas correctamente.")
    except sqlite3.Error as e:
        print(f"Error al crear la base de datos: {e}")
    finally:
        conn.close()

# Función para imprimir todos los jugadores
def imprimir_jugadores(c):
    try:
        c.execute("SELECT nombre, vida FROM JUGADORES")
        jugadores = c.fetchall()
        if not jugadores:
            print("No hay jugadores para imprimir.")
        else:
            print("IMPRIMIR JUGADORES")
            for jugador in jugadores:
                print(f"Nombre: {jugador[0]} - Vida: {jugador[1]}")
    except sqlite3.Error as e:
        print(f"Error al imprimir jugadores: {e}")

# Función principal para el menú
def menu():
    crear_base_de_datos()
    conn = sqlite3.connect('ejer_obligatorio.db')
    c = conn.cursor()

    while True:
        print("\nMenu:")
        print("1. Imprimir todos los vuelos")
        print("2. Buscar por origen")
        print("3. Imprimir vuelo específico")
        print("4. Cambiar fecha de vuelo")
        print("5. Imprimir jugadores")
        print("0. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            imprimir(vuelos)
        elif opcion == '2':
            buscar_origen(vuelos)
        elif opcion == '3':
            imprimir_vuelo(vuelos)
        elif opcion == '4':
            cambiar_fecha(vuelos)
        elif opcion == '5':
            imprimir_jugadores(c)
        elif opcion == '0':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

    conn.close()

# Ejecuta el menú al iniciar
if __name__ == "__main__":
    menu()