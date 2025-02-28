
# Preguntas Teóricas sobre SQLite y sqlite3

---

1. **¿Qué es SQLite?**  
   SQLite es una biblioteca de software que implementa un motor de base de datos SQL embebido. Es liviano, rápido y no requiere un servidor separado.

2. **¿Cómo se instala la librería sqlite3 en Python?**  
   sqlite3 está incluida en la biblioteca estándar de Python, por lo que no es necesario instalarla.

3. **¿Cuál es la sintaxis básica para conectarse a una base de datos en Python usando sqlite3?**  
   ```python
   conn = sqlite3.connect("nombre_base_datos.db")
   ```

4. **¿Qué función se usa para cerrar una conexión a una base de datos en SQLite?**  
   ```python
   conn.close()
   ```

5. **¿Qué es un cursor en el contexto de SQLite?**  
   Un cursor es un objeto que permite ejecutar comandos SQL y recuperar resultados de una base de datos.

6. **¿Cuál es la diferencia entre `fetchone()` y `fetchall()`?**  
   `fetchone()` devuelve una sola fila de la consulta, mientras que `fetchall()` devuelve todas las filas en una lista de tuplas.

7. **¿Cómo se crean tablas en SQLite usando Python?**  
   Se utilizan comandos SQL en combinación con el método `execute()` del cursor. Ejemplo:  
   ```python
   cursor.execute("CREATE TABLE nombre_tabla (...);")
   ```

8. **¿Qué es una clave primaria en una tabla de base de datos?**  
   Una clave primaria es un campo o combinación de campos que identifica de manera única cada fila en una tabla.

9. **¿Qué hace el método `commit()` en SQLite?**  
   `commit()` guarda todos los cambios realizados en la base de datos desde la última transacción.

10. **¿Cómo se manejan excepciones al trabajar con bases de datos en Python?**  
    Se utilizan bloques `try-except` para capturar y manejar errores de base de datos.

---

# Preguntas Prácticas sobre Programación

1. **Escribe un programa que cree una base de datos llamada `escuela.db` y una tabla llamada `alumnos` con columnas `id`, `nombre` y `curso`.**

   ```python
   import sqlite3

   conn = sqlite3.connect("escuela.db")
   cursor = conn.cursor()

   cursor.execute('''
   CREATE TABLE IF NOT EXISTS alumnos (
       id INTEGER PRIMARY KEY,
       nombre TEXT,
       curso TEXT
   )
   ''')

   conn.commit()
   conn.close()
   ```

2. **Crea un programa que inserte cinco alumnos en la tabla `alumnos`.**

   ```python
   import sqlite3

   conn = sqlite3.connect("escuela.db")
   cursor = conn.cursor()

   alumnos = [
       (1, "Pedro", "Matemáticas"),
       (2, "María", "Historia"),
       (3, "Javier", "Ciencias"),
       (4, "Laura", "Arte"),
       (5, "Ana", "Inglés")
   ]
   cursor.executemany("INSERT INTO alumnos (id, nombre, curso) VALUES (?, ?, ?)", alumnos)

   conn.commit()
   conn.close()
   ```

3. **Escribe un programa que consulte todos los registros de alumnos y los imprima.**

   ```python
   import sqlite3

   conn = sqlite3.connect("escuela.db")
   cursor = conn.cursor()

   cursor.execute("SELECT * FROM alumnos")
   registros = cursor.fetchall()

   for reg in registros:
       print(reg)

   conn.close()
   ```

4. **¿Cómo actualizar el curso de un alumno específico en la tabla `alumnos`?**

   ```python
   import sqlite3

   conn = sqlite3.connect("escuela.db")
   cursor = conn.cursor()

   cursor.execute("UPDATE alumnos SET curso = ? WHERE nombre = ?", ("Matemáticas Avanzadas", "Pedro"))

   conn.commit()
   conn.close()
   ```

5. **Escribe un programa que elimine un alumno de la tabla `alumnos` por su nombre.**

   ```python
   import sqlite3

   conn = sqlite3.connect("escuela.db")
   cursor = conn.cursor()

   cursor.execute("DELETE FROM alumnos WHERE nombre = ?", ("Ana",))

   conn.commit()
   conn.close()
   ```

6. **Crea un programa que maneje errores al intentar abrir una base de datos.**

   ```python
   import sqlite3

   try:
       conn = sqlite3.connect("escuela.db")
       cursor = conn.cursor()
   except sqlite3.Error as e:
       print(f"Error al conectar a la base de datos: {e}")
   finally:
       if conn:
           conn.close()
   ```

7. **Escribe un programa que cuente cuántos alumnos hay en la tabla `alumnos`.**

   ```python
   import sqlite3

   conn = sqlite3.connect("escuela.db")
   cursor = conn.cursor()

   cursor.execute("SELECT COUNT(*) FROM alumnos")
   total_alumnos = cursor.fetchone()[0]
   print(f"Total de alumnos: {total_alumnos}")

   conn.close()
   ```

8. **Crea un programa que use `executemany()` para insertar múltiples registros en la tabla `alumnos`.**

   ```python
   import sqlite3

   conn = sqlite3.connect("escuela.db")
   cursor = conn.cursor()

   lista_alumnos = [
       (6, "Sofia", "Física"),
       (7, "Carlos", "Química"),
       (8, "Elena", "Biología")
   ]
   cursor.executemany("INSERT INTO alumnos (id, nombre, curso) VALUES (?, ?, ?)", lista_alumnos)

   conn.commit()
   conn.close()
   ```

---

# Preguntas Adicionales

1. **¿Qué comando se utiliza para ver las tablas en una base de datos SQLite desde la consola?**  
   `.tables`

2. **¿Cómo se eliminan todas las filas de una tabla sin eliminar la tabla misma?**  
   `DELETE FROM nombre_tabla`
