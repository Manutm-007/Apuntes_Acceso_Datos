import sqlite3#Importa el modulo sqlite3 para trabajar con bases de datos SQLite

#Funcion para crear la base de datos y las tablas
def crear_base_de_datos():
    try:
        conn = sqlite3.connect('ejer_obligatorio.db')#Conecta a la base de datos
        c = conn.cursor()#Crea un cursor para interactuar con la base de datos

      #Crea la tabla JUGADORES si no existe
        c.execute('''
        CREATE TABLE IF NOT EXISTS JUGADORES (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            nombre TEXT NOT NULL UNIQUE,    
            vida INTEGER NOT NULL     
        )
        ''')

      #Crea la tabla CREDENCIALES si no existe
        c.execute('''
        CREATE TABLE IF NOT EXISTS CREDENCIALES (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            jugador TEXT NOT NULL,   
            contrasena TEXT NOT NULL,  
            FOREIGN KEY (jugador) REFERENCES JUGADORES (nombre)  
        )
        ''')

        conn.commit()#Guarda los cambios en la base de datos
        print("Base de datos y tablas creadas correctamente.")#Mensaje de confirmacion
    except sqlite3.Error as e:
        print(f"Error al crear la base de datos: {e}")#Imprime el error si ocurre
    finally:
        conn.close()#Cierra la conexion

#Funcion para imprimir todos los jugadores
def imprimir_jugadores(c):
    try:
        c.execute("SELECT nombre, vida FROM JUGADORES")#Ejecuta la consulta para obtener nombres y vidas
        jugadores = c.fetchall()#Obtiene todos los resultados de la consulta
        if not jugadores:
            print("No hay jugadores para imprimir.")#Mensaje si no hay jugadores
        else:
            print("IMPRIMIR JUGADORES")#Imprime un encabezado
            for jugador in jugadores:#Itera sobre la lista de jugadores
                print(f"Nombre: {jugador[0]} - Vida: {jugador[1]}")#Imprime el nombre y la vida de cada jugador
    except sqlite3.Error as e:
        print(f"Error al imprimir jugadores: {e}")#Imprime el error si ocurre

#Funcion para validar credencial
def validar_credencial(c):
    jugador = input("Dame jugador: ")#Solicita el nombre del jugador
    contrasena = input("Dame contrasena: ")#Solicita la contrasena
    
    try:
      #Verifica si la credencial es valida
        if existe_credencial(c, jugador, contrasena):
            print(f"[{jugador}/{contrasena}] si es una credencial valida")#Indica que es valida
        else:
            print(f"[{jugador}/{contrasena}] no es una credencial valida")#Indica que no es valida
    except sqlite3.Error as e:
        print(f"Error al validar credencial: {e}")#Imprime el error si ocurre

#Funcion para cambiar credencial
def cambiar_credencial(conn, c):
    jugador = input("Dame jugador: ")#Solicita el nombre del jugador
    
    try:
      #Comprueba si el jugador existe
        if not existe_jugador(c, jugador):
            print("ERROR: El jugador no existe")#Mensaje si no existe
            return#Sale de la funcion

        contrasena_vieja = input("Dame contrasena vieja: ")#Solicita la contrasena antigua
        
      #Verifica si la credencial es valida
        if not existe_credencial(c, jugador, contrasena_vieja):
            print(f"[{jugador}/{contrasena_vieja}] no es una credencial valida")#Mensaje si no es valida
            return#Sale de la funcion

        nueva_contrasena = input("Dame contrasena nueva: ")#Solicita la nueva contrasena
      #Actualiza la contrasena en la base de datos
        c.execute("UPDATE CREDENCIALES SET contrasena = ? WHERE jugador = ?", (nueva_contrasena, jugador))
        conn.commit()#Guarda los cambios
        print(f"La contrasena del jugador <{jugador}> se ha modificado correctamente")#Confirma el cambio
    except sqlite3.Error as e:
        print(f"Error al cambiar credencial: {e}")#Imprime el error si ocurre

#Funcion para insertar un nuevo jugador
def insertar_jugador(conn, c):
    nombre = input("Dame nombre: ")#Solicita el nombre del nuevo jugador
    
    try:
      #Comprueba si el jugador ya existe
        if existe_jugador(c, nombre):
            print("ERROR: El jugador ya existe")#Mensaje si ya existe
            return#Sale de la funcion

        vida = int(input("Dame vida: "))#Solicita la vida del jugador
        contrasena = input("Dame contrasena: ")#Solicita la contrasena del jugador

      #Inserta el nuevo jugador en la tabla JUGADORES
        c.execute("INSERT INTO JUGADORES (nombre, vida) VALUES (?, ?)", (nombre, vida))
      #Inserta la credencial del nuevo jugador en la tabla CREDENCIALES
        c.execute("INSERT INTO CREDENCIALES (jugador, contrasena) VALUES (?, ?)", (nombre, contrasena))
        conn.commit()#Guarda los cambios
        print(f"El jugador <{nombre}> se ha insertado correctamente")#Confirma la insercion
    except sqlite3.Error as e:
        print(f"Error al insertar jugador: {e}")#Imprime el error si ocurre
    except ValueError:
        print("ERROR: La vida debe ser un numero.")#Mensaje si hay un error de conversion

#Funcion para borrar un jugador
def borrar_jugador(conn, c):
    nombre = input("Dame el nombre del jugador: ")#Solicita el nombre del jugador a borrar
    
    try:
      #Comprueba si el jugador existe
        if not existe_jugador(c, nombre):
            print("ERROR: El jugador no existe")#Mensaje si no existe
            return#Sale de la funcion

      #Elimina el jugador de la tabla JUGADORES
        c.execute("DELETE FROM JUGADORES WHERE nombre = ?", (nombre,))
      #Elimina las credenciales del jugador de la tabla CREDENCIALES
        c.execute("DELETE FROM CREDENCIALES WHERE jugador = ?", (nombre,))
        conn.commit()#Guarda los cambios
        print(f"Se ha eliminado el jugador <{nombre}> correctamente")#Confirma la eliminacion
    except sqlite3.Error as e:
        print(f"Error al borrar jugador: {e}")#Imprime el error si ocurre

#Funcion para comprobar si existe un jugador
def existe_jugador(c, nombre):
    try:
      #Ejecuta la consulta para buscar el jugador
        c.execute("SELECT 1 FROM JUGADORES WHERE nombre = ?", (nombre,))
        return c.fetchone() is not None#Devuelve True si el jugador existe, False en caso contrario
    except sqlite3.Error as e:
        print(f"Error al verificar si existe el jugador: {e}")#Imprime el error si ocurre
        return False#Devuelve False en caso de error

#Funcion para comprobar si existe una credencial
def existe_credencial(c, jugador, contrasena):
    try:
      #Ejecuta la consulta para verificar la credencial
        c.execute("SELECT 1 FROM CREDENCIALES WHERE jugador = ? AND contrasena = ?", (jugador, contrasena))
        return c.fetchone() is not None#Devuelve True si la credencial es valida, False en caso contrario
    except sqlite3.Error as e:
        print(f"Error al verificar credencial: {e}")#Imprime el error si ocurre
        return False#Devuelve False en caso de error

#Funcion principal para el menu
def menu():
    crear_base_de_datos()#Llama a la funcion para crear la base de datos y las tablas
    conn = sqlite3.connect('ejer_obligatorio.db')#Conecta a la base de datos
    c = conn.cursor()#Crea un cursor para interactuar con la base de datos

    while True:#Bucle infinito para mostrar el menu
        print("==========================")
        print("       CREDENCIALES DE JUGADORES")
        print("==========================")
        print("1 - imprimir jugadores")#Opcion 1
        print("2 - Validar credencial")#Opcion 2
        print("3 - Cambiar credencial")#Opcion 3
        print("4 - insertar nuevo jugador")#Opcion 4
        print("5 - borrar jugador")#Opcion 5
        print("0 - salir")#Opcion 0 para salir
        print("--------------------------------------------")

        opcion = input("Selecciona una opcion: ")#Solicita al usuario que seleccione una opcion

        if opcion == "1":
            imprimir_jugadores(c)#Llama a la funcion para imprimir jugadores
        elif opcion == "2":
            validar_credencial(c)#Llama a la funcion para validar credencial
        elif opcion == "3":
            cambiar_credencial(conn, c)#Llama a la funcion para cambiar credencial
        elif opcion == "4":
            insertar_jugador(conn, c)#Llama a la funcion para insertar un nuevo jugador
        elif opcion == "5":
            borrar_jugador(conn, c)#Llama a la funcion para borrar un jugador
        elif opcion == "0":
            break#Sale del bucle y termina el programa
        else:
            print("ERROR: Opcion no valida")#Mensaje si la opcion no es valida

    conn.close()#Cierra la conexion al salir

#Llama a la funcion del menu
menu()
