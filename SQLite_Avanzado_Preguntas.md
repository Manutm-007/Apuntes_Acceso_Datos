
# Preguntas Teóricas sobre SQLite y sqlite3

## ¿Qué es SQLite?
SQLite es una biblioteca de software que implementa un motor de base de datos SQL embebido. Es liviano, rápido y no requiere un servidor separado.

## ¿Cómo se instala la librería sqlite3 en Python?
sqlite3 está incluida en la biblioteca estándar de Python, por lo que no es necesario instalarla.

## ¿Cuál es la sintaxis básica para conectarse a una base de datos en Python usando sqlite3?
```python
conn = sqlite3.connect("nombre_base_datos.db")
```

## ¿Qué función se usa para cerrar una conexión a una base de datos en SQLite?
```python
conn.close()
```

## ¿Qué es un cursor en el contexto de SQLite?
Un cursor es un objeto que permite ejecutar comandos SQL y recuperar resultados de una base de datos.

## ¿Cuál es la diferencia entre fetchone() y fetchall()?
`fetchone()` devuelve una sola fila de la consulta, mientras que `fetchall()` devuelve todas las filas en una lista de tuplas.

## ¿Cómo se crean tablas en SQLite usando Python?
Se utilizan comandos SQL en combinación con el método `execute()` del cursor. Ejemplo:
```python
cursor.execute("CREATE TABLE nombre_tabla (...);")
```

## ¿Qué es una clave primaria en una tabla de base de datos?
Una clave primaria es un campo o combinación de campos que identifica de manera única cada fila en una tabla.

## ¿Qué hace el método commit() en SQLite?
`commit()` guarda todos los cambios realizados en la base de datos desde la última transacción.

## ¿Cómo se manejan excepciones al trabajar con bases de datos en Python?
Se utilizan bloques `try-except` para capturar y manejar errores de base de datos.


# Preguntas Prácticas sobre Programación

## Escribe un programa que cree una base de datos llamada `escuela.db` y una tabla llamada `alumnos` con columnas `id`, `nombre` y `curso`.
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

## Crea un programa que inserte cinco alumnos en la tabla `alumnos`.
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

## Escribe un programa que consulte todos los registros de alumnos y los imprima.
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

## ¿Cómo actualizar el curso de un alumno específico en la tabla `alumnos`?
```python
import sqlite3

conn = sqlite3.connect("escuela.db")
cursor = conn.cursor()

cursor.execute("UPDATE alumnos SET curso = ? WHERE nombre = ?", ("Matemáticas Avanzadas", "Pedro"))

conn.commit()
conn.close()
```

## Escribe un programa que elimine un alumno de la tabla `alumnos` por su nombre.
```python
import sqlite3

conn = sqlite3.connect("escuela.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM alumnos WHERE nombre = ?", ("Ana",))

conn.commit()
conn.close()
```

## Crea un programa que maneje errores al intentar abrir una base de datos.
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

## Escribe un programa que cuente cuántos alumnos hay en la tabla `alumnos`.
```python
import sqlite3

conn = sqlite3.connect("escuela.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM alumnos")
total_alumnos = cursor.fetchone()[0]
print(f"Total de alumnos: {total_alumnos}")

conn.close()
```

## Crea un programa que use `executemany()` para insertar múltiples registros en la tabla `alumnos`.
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

# Preguntas Adicionales

## ¿Qué comando se utiliza para ver las tablas en una base de datos SQLite desde la consola?
```
.tables
```

## ¿Cómo se eliminan todas las filas de una tabla sin eliminar la tabla misma?
```
DELETE FROM nombre_tabla;
```

# Preguntas Avanzadas

## ¿Qué es una transacción en SQLite y cómo se maneja en Python?
Una transacción es un conjunto de operaciones SQL que se ejecutan como una unidad. En Python, puedes manejar transacciones con `commit()` y `rollback()`.

## ¿Qué es el modo WAL (Write-Ahead Logging) en SQLite y cómo afecta al rendimiento?
El modo WAL mejora la concurrencia permitiendo escrituras mientras otras transacciones están leyendo. Se habilita con:
```
PRAGMA journal_mode=WAL;
```

## ¿Qué son los PRAGMAs en SQLite?
Los PRAGMAs son comandos para configurar el comportamiento de SQLite, como habilitar claves foráneas o mejorar el rendimiento:
```
PRAGMA foreign_keys = ON;
```

## Escribe un programa que realice una inserción masiva de 10,000 registros en una tabla llamada `grandes_datos`.
```python
import sqlite3

conn = sqlite3.connect("grandes_datos.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS grandes_datos (
    id INTEGER PRIMARY KEY,
    valor TEXT
)
''')

datos = [(i, f"Valor-{i}") for i in range(1, 10001)]

conn.execute("BEGIN TRANSACTION")
cursor.executemany("INSERT INTO grandes_datos (id, valor) VALUES (?, ?)", datos)
conn.commit()
conn.close()
```

## ¿Cómo consultar registros de forma paginada en SQLite para manejar grandes volúmenes de datos?
```python
import sqlite3

def obtener_pagina(pagina, tamano_pagina):
    offset = (pagina - 1) * tamano_pagina
    conn = sqlite3.connect("grandes_datos.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM grandes_datos LIMIT {tamano_pagina} OFFSET {offset}")
    registros = cursor.fetchall()

    conn.close()
    return registros

print(obtener_pagina(2, 100))
```
