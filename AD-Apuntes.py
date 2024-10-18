# Preguntas Teóricas sobre SQLite (Consola)

## 1. ¿Qué es SQLite y para qué se utiliza?
SQLite es una biblioteca de software que implementa un motor de base de datos SQL embebido. Se utiliza para manejar bases de datos sin necesidad de un servidor independiente.

## 2. ¿Cuál es el comando para crear una nueva base de datos SQLite?
Se crea automáticamente al conectarse con:
```bash
sqlite3 nombre_base_datos.db
3. ¿Qué comando se usa para listar las tablas en una base de datos SQLite?
bash

.tables
4. ¿Cómo se muestra la estructura de una tabla en SQLite?
bash

.schema nombre_tabla
5. ¿Cómo insertar datos en una tabla de SQLite desde la consola?
sql

INSERT INTO nombre_tabla (columna1, columna2) VALUES (valor1, valor2);
6. ¿Cómo se actualizan los registros de una tabla en SQLite?
sql

UPDATE nombre_tabla SET columna = valor WHERE condicion;
7. ¿Cómo se eliminan filas de una tabla en SQLite?
sql

DELETE FROM nombre_tabla WHERE condicion;
8. ¿Qué comando se utiliza para eliminar una tabla en SQLite?
sql

DROP TABLE nombre_tabla;
9. ¿Cómo se crea una tabla con una clave primaria en SQLite?
sql

CREATE TABLE nombre_tabla (
    id INTEGER PRIMARY KEY,
    columna1 TEXT
);
10. ¿Cómo se seleccionan todos los registros de una tabla en SQLite?
sql

SELECT * FROM nombre_tabla;
11. ¿Cómo se seleccionan registros con una condición específica en SQLite?
sql

SELECT * FROM nombre_tabla WHERE columna = valor;
12. ¿Cómo se seleccionan registros ordenados en SQLite?
sql

SELECT * FROM nombre_tabla ORDER BY columna ASC;
13. ¿Cómo se cuentan los registros de una tabla en SQLite?
sql

SELECT COUNT(*) FROM nombre_tabla;
14. ¿Cómo se seleccionan registros únicos en SQLite?
sql

SELECT DISTINCT columna FROM nombre_tabla;
15. ¿Cómo eliminar duplicados en una tabla de SQLite?
SQLite no tiene un comando específico para eliminar duplicados. Generalmente se hace usando subconsultas o creando una nueva tabla sin duplicados.

16. ¿Cómo agregar una columna nueva a una tabla existente en SQLite?
sql

ALTER TABLE nombre_tabla ADD COLUMN nueva_columna TEXT;
17. ¿Qué comando se usa para eliminar todas las filas de una tabla sin eliminar la tabla misma?
sql

DELETE FROM nombre_tabla;
18. ¿Cómo renombrar una tabla en SQLite?
sql

ALTER TABLE nombre_tabla RENAME TO nuevo_nombre_tabla;
19. ¿Cómo habilitar las claves foráneas en SQLite?
sql

PRAGMA foreign_keys = ON;
20. ¿Cómo crear una tabla con clave foránea en SQLite?
sql

CREATE TABLE nombre_tabla (
    id INTEGER PRIMARY KEY,
    columna1 TEXT,
    columna2 INTEGER,
    FOREIGN KEY (columna2) REFERENCES otra_tabla(id)
);
21. ¿Cómo consultar registros con claves foráneas en SQLite?
sql

SELECT * FROM nombre_tabla INNER JOIN otra_tabla ON nombre_tabla.columna2 = otra_tabla.id;
22. ¿Cómo realizar una consulta con agrupación en SQLite?
sql

SELECT columna, COUNT(*) FROM nombre_tabla GROUP BY columna;
23. ¿Cómo se limitan los resultados de una consulta en SQLite?
sql

SELECT * FROM nombre_tabla LIMIT 10;
24. ¿Cómo realizar una consulta con paginación en SQLite?
sql

SELECT * FROM nombre_tabla LIMIT 10 OFFSET 20;
25. ¿Qué comando se utiliza para crear un índice en SQLite?
sql

CREATE INDEX nombre_indice ON nombre_tabla(columna);
26. ¿Cómo eliminar un índice en SQLite?
sql

DROP INDEX nombre_indice;
27. ¿Cómo obtener la versión de SQLite instalada?
bash

sqlite3 --version
28. ¿Cómo exportar una tabla a un archivo CSV desde la consola de SQLite?
bash

sqlite3 nombre_base_datos.db ".headers on" ".mode csv" ".output archivo.csv" "SELECT * FROM nombre_tabla;"
29. ¿Cómo importar datos desde un archivo CSV a una tabla en SQLite?
bash

sqlite3 nombre_base_datos.db ".mode csv" ".import archivo.csv nombre_tabla"
30. ¿Qué es una transacción en SQLite?
Es un conjunto de operaciones que se ejecutan como una sola unidad para garantizar la integridad de los datos.

31. ¿Qué comando se utiliza para iniciar una transacción en SQLite?
sql

BEGIN TRANSACTION;
32. ¿Cómo confirmar (commit) una transacción en SQLite?
sql

COMMIT;
33. ¿Cómo revertir (rollback) una transacción en SQLite?
sql

ROLLBACK;
34. ¿Cómo habilitar el modo WAL (Write-Ahead Logging) en SQLite?
sql

PRAGMA journal_mode = WAL;
35. ¿Cómo deshabilitar el modo WAL en SQLite?
sql

PRAGMA journal_mode = DELETE;
36. ¿Qué son los PRAGMAs en SQLite?
Son comandos especiales que permiten modificar configuraciones internas de SQLite.

37. ¿Cómo verificar el estado de las claves foráneas en SQLite?
sql

PRAGMA foreign_keys;
38. ¿Cómo cambiar el tamaño máximo de una base de datos en SQLite?
SQLite no impone un tamaño máximo predeterminado para una base de datos, pero puedes usar PRAGMA max_page_count para establecer un límite.

39. ¿Cómo hacer una copia de seguridad de una base de datos en SQLite?
bash

sqlite3 nombre_base_datos.db ".backup archivo_backup.db"
40. ¿Cómo restaurar una base de datos desde una copia de seguridad en SQLite?
bash

sqlite3 nombre_base_datos.db ".restore archivo_backup.db"
41. ¿Cómo realizar una consulta con funciones agregadas en SQLite?
sql

SELECT SUM(columna) FROM nombre_tabla;
42. ¿Cómo eliminar todas las filas de una tabla de forma eficiente en SQLite?
sql

DELETE FROM nombre_tabla WHERE 1=1;
43. ¿Cómo renombrar una columna en SQLite?
SQLite no permite renombrar columnas directamente. La mejor opción es crear una nueva tabla con el esquema correcto y copiar los datos.

44. ¿Qué comando se utiliza para mostrar los registros de una tabla con formato legible en SQLite?
bash

sqlite3 nombre_base_datos.db ".mode column" ".headers on" "SELECT * FROM nombre_tabla;"
45. ¿Cómo agregar una restricción UNIQUE a una columna en una tabla SQLite?
sql

CREATE TABLE nombre_tabla (
    columna1 TEXT UNIQUE
);
46. ¿Cómo eliminar filas duplicadas en una tabla SQLite sin usar subconsultas?
Se recomienda crear una nueva tabla con los datos correctos y luego eliminar la antigua.

47. ¿Cómo realizar un respaldo automático de una base de datos en SQLite?
Esto generalmente se maneja fuera de SQLite, usando scripts externos o cron jobs.

48. ¿Qué es el auto-incremento en SQLite?
Es una opción para columnas que asegura que cada nuevo valor sea mayor que el anterior en una columna INTEGER PRIMARY KEY.

49. ¿Cómo deshabilitar las claves foráneas en SQLite temporalmente?
sql

PRAGMA foreign_keys = OFF;
50. ¿Qué diferencia hay entre DELETE y TRUNCATE en SQLite?
SQLite no tiene un comando TRUNCATE. DELETE se usa para eliminar todas las filas manualmente.

Preguntas Prácticas sobre SQLite (Código Python)
1. Escribe un programa en Python para conectar con una base de datos SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
2. Escribe un programa en Python para crear una tabla en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (id INTEGER PRIMARY KEY, nombre TEXT)''')
conn.commit()
conn.close()
3. Escribe un programa para insertar datos en una tabla SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO empleados (nombre) VALUES ('Juan')")
conn.commit()
conn.close()
4. Escribe un programa en Python que consulte todos los registros de una tabla en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM empleados")
registros = cursor.fetchall()
print(registros)
conn.close()
5. Escribe un programa para actualizar registros en una tabla SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("UPDATE empleados SET nombre = 'Carlos' WHERE id = 1")
conn.commit()
conn.close()
6. Escribe un programa para eliminar registros de una tabla SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("DELETE FROM empleados WHERE id = 1")
conn.commit()
conn.close()
7. Escribe un programa en Python para realizar una consulta con filtro en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM empleados WHERE nombre = 'Juan'")
registros = cursor.fetchall()
print(registros)
conn.close()
8. Escribe un programa en Python para contar los registros de una tabla en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM empleados")
total = cursor.fetchone()[0]
print(f"Total de empleados: {total}")
conn.close()
9. Escribe un programa para crear una tabla con clave foránea en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS departamentos (
    id INTEGER PRIMARY KEY, 
    nombre TEXT
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY, 
    nombre TEXT, 
    departamento_id INTEGER,
    FOREIGN KEY(departamento_id) REFERENCES departamentos(id)
)''')
conn.commit()
conn.close()
10. Escribe un programa para insertar datos en tablas relacionadas en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO departamentos (nombre) VALUES ('Ventas')")
cursor.execute("INSERT INTO empleados (nombre, departamento_id) VALUES ('Ana', 1)")
conn.commit()
conn.close()
11. Escribe un programa en Python para realizar una consulta con JOIN en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute('''SELECT empleados.nombre, departamentos.nombre 
                  FROM empleados 
                  JOIN departamentos 
                  ON empleados.departamento_id = departamentos.id''')
registros = cursor.fetchall()
print(registros)
conn.close()
12. Escribe un programa en Python para agregar una columna nueva a una tabla existente en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute('ALTER TABLE empleados ADD COLUMN salario REAL')
conn.commit()
conn.close()
13. Escribe un programa para consultar registros ordenados en SQLite desde Python.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM empleados ORDER BY nombre ASC")
registros = cursor.fetchall()
print(registros)
conn.close()
14. Escribe un programa en Python para realizar una consulta con agrupación en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute('''SELECT departamento_id, COUNT(*) 
                  FROM empleados 
                  GROUP BY departamento_id''')
registros = cursor.fetchall()
print(registros)
conn.close()
15. Escribe un programa para eliminar una tabla en SQLite desde Python.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS empleados")
conn.commit()
conn.close()
16. Escribe un programa para crear un índice en una tabla SQLite desde Python.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("CREATE INDEX idx_nombre ON empleados(nombre)")
conn.commit()
conn.close()
17. Escribe un programa en Python para realizar una consulta con LIMIT en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM empleados LIMIT 5")
registros = cursor.fetchall()
print(registros)
conn.close()
18. Escribe un programa para hacer un respaldo de una base de datos en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
with open('backup.sql', 'w') as f:
    for linea in conn.iterdump():
        f.write('%s\n' % linea)
conn.close()
19. Escribe un programa en Python para habilitar las claves foráneas en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
conn.commit()
conn.close()
20. Escribe un programa para verificar si las claves foráneas están habilitadas en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys")
estado = cursor.fetchone()[0]
print(f"Claves foráneas habilitadas: {estado == 1}")
conn.close()
21. Escribe un programa para hacer una transacción en SQLite usando Python.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()

try:
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("INSERT INTO empleados (nombre) VALUES ('Luis')")
    cursor.execute("INSERT INTO empleados (nombre) VALUES ('Carlos')")
    conn.commit()
except sqlite3.Error as e:
    print("Error en la transacción:", e)
    conn.rollback()

conn.close()
22. Escribe un programa para revertir una transacción en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()

try:
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("INSERT INTO empleados (nombre) VALUES ('Ana')")
    raise Exception("Simulando un error")
    conn.commit()
except Exception as e:
    print("Error detectado, revirtiendo:", e)
    conn.rollback()

conn.close()
23. Escribe un programa para consultar el tamaño de una base de datos SQLite.
python

import os
tamaño = os.path.getsize('mi_base_datos.db')
print(f"Tamaño de la base de datos: {tamaño} bytes")
24. Escribe un programa en Python para importar un archivo CSV a una tabla SQLite.
python

import sqlite3
import csv

conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()

with open('archivo.csv', 'r') as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        cursor.execute("INSERT INTO empleados (nombre) VALUES (?)", (fila[0],))

conn.commit()
conn.close()
25. Escribe un programa para exportar una tabla SQLite a un archivo CSV desde Python.
python

import sqlite3
import csv

conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM empleados")

with open('empleados.csv', 'w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow([i[0] for i in cursor.description])  # Escribir encabezados
    writer.writerows(cursor)

conn.close()
26. Escribe un programa para calcular el promedio de una columna numérica en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT AVG(salario) FROM empleados")
promedio = cursor.fetchone()[0]
print(f"Promedio de salarios: {promedio}")
conn.close()
27. Escribe un programa para crear una tabla con una columna que tenga valores únicos en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS empleados_unicos (
    id INTEGER PRIMARY KEY, 
    nombre TEXT UNIQUE
)''')
conn.commit()
conn.close()
28. Escribe un programa para eliminar registros duplicados en una tabla SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()

cursor.execute('''DELETE FROM empleados 
                  WHERE rowid NOT IN 
                  (SELECT MIN(rowid) FROM empleados GROUP BY nombre)''')

conn.commit()
conn.close()
29. Escribe un programa para consultar los nombres de todas las tablas en una base de datos SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tablas = cursor.fetchall()
print(tablas)
conn.close()
30. Escribe un programa para consultar el esquema de una tabla en SQLite usando Python.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(empleados)")
esquema = cursor.fetchall()
for columna in esquema:
    print(columna)
conn.close()
31. Escribe un programa para calcular el máximo de una columna numérica en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT MAX(salario) FROM empleados")
maximo = cursor.fetchone()[0]
print(f"Salario máximo: {maximo}")
conn.close()
32. Escribe un programa para calcular el mínimo de una columna numérica en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT MIN(salario) FROM empleados")
minimo = cursor.fetchone()[0]
print(f"Salario mínimo: {minimo}")
conn.close()
33. Escribe un programa para calcular la suma de una columna numérica en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT SUM(salario) FROM empleados")
suma = cursor.fetchone()[0]
print(f"Suma de salarios: {suma}")
conn.close()
34. Escribe un programa en Python para generar informes usando SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute('''SELECT departamento_id, COUNT(*) AS total 
                  FROM empleados 
                  GROUP BY departamento_id 
                  ORDER BY total DESC''')
informe = cursor.fetchall()
print("Informe de empleados por departamento:")
for fila in informe:
    print(f"Departamento {fila[0]}: {fila[1]} empleados")
conn.close()
35. Escribe un programa para agregar datos masivos a una tabla SQLite usando un bucle.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()

empleados = [('Ana',), ('Pedro',), ('Luis',)]
cursor.executemany("INSERT INTO empleados (nombre) VALUES (?)", empleados)

conn.commit()
conn.close()
36. Escribe un programa para eliminar todas las filas de una tabla en SQLite desde Python.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("DELETE FROM empleados")
conn.commit()
conn.close()
37. Escribe un programa en Python para verificar si un registro existe en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT 1 FROM empleados WHERE nombre = 'Ana'")
existe = cursor.fetchone() is not None
print(f"El empleado existe: {existe}")
conn.close()
38. Escribe un programa para copiar una tabla en otra nueva en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS copia_empleados AS SELECT * FROM empleados")
conn.commit()
conn.close()
39. Escribe un programa para realizar un backup automático de una base de datos SQLite.
python

import sqlite3
import os
import shutil

def backup_database():
    src = 'mi_base_datos.db'
    dst = 'backup_' + src
    shutil.copyfile(src, dst)
    print(f"Backup realizado: {dst}")

backup_database()
40. Escribe un programa para eliminar una columna de una tabla SQLite (sin soporte directo).
python

import sqlite3

conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()

# 1. Crear una nueva tabla sin la columna
cursor.execute('''CREATE TABLE nueva_empleados (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT
                 )''')

# 2. Copiar datos a la nueva tabla
cursor.execute('''INSERT INTO nueva_empleados (id, nombre)
                  SELECT id, nombre FROM empleados''')

# 3. Eliminar la tabla anterior
cursor.execute("DROP TABLE empleados")

# 4. Renombrar la nueva tabla
cursor.execute("ALTER TABLE nueva_empleados RENAME TO empleados")

conn.commit()
conn.close()
41. Escribe un programa para realizar una búsqueda por palabra clave en una columna de texto en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM empleados WHERE nombre LIKE '%Ana%'")
resultados = cursor.fetchall()
print(resultados)
conn.close()
42. Escribe un programa para realizar una consulta con diferentes condiciones en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM empleados WHERE nombre = 'Ana' OR nombre = 'Luis'")
resultados = cursor.fetchall()
print(resultados)
conn.close()
43. Escribe un programa para manejar los errores de base de datos en SQLite.
python

import sqlite3

try:
    conn = sqlite3.connect('mi_base_datos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tabla_inexistente")
except sqlite3.Error as e:
    print(f"Error en la base de datos: {e}")
finally:
    conn.close()
44. Escribe un programa para verificar la existencia de una tabla en una base de datos SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='empleados'")
existe = cursor.fetchone() is not None
print(f"La tabla empleados existe: {existe}")
conn.close()
45. Escribe un programa en Python para generar un archivo JSON a partir de una consulta SQLite.
python

import sqlite3
import json

conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM empleados")
empleados = cursor.fetchall()

# Convertir a lista de diccionarios
empleados_dict = [{"id": fila[0], "nombre": fila[1]} for fila in empleados]

# Guardar como archivo JSON
with open('empleados.json', 'w') as archivo_json:
    json.dump(empleados_dict, archivo_json)

conn.close()
46. Escribe un programa para generar un informe en formato CSV con los datos de una tabla SQLite.
python

import sqlite3
import csv

conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM empleados")

with open('informe_empleados.csv', 'w', newline='') as archivo:
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerow([i[0] for i in cursor.description])  # Encabezados
    escritor_csv.writerows(cursor)

conn.close()
47. Escribe un programa para eliminar todas las filas duplicadas en una tabla SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()

cursor.execute('''DELETE FROM empleados 
                  WHERE rowid NOT IN 
                  (SELECT MIN(rowid) FROM empleados GROUP BY nombre)''')

conn.commit()
conn.close()
48. Escribe un programa en Python para realizar una consulta con UNION en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute('''SELECT nombre FROM empleados
                  UNION
                  SELECT nombre FROM copia_empleados''')
registros = cursor.fetchall()
print(registros)
conn.close()
49. Escribe un programa para realizar una consulta con subconsultas en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute('''SELECT nombre FROM empleados 
                  WHERE salario > (SELECT AVG(salario) FROM empleados)''')
registros = cursor.fetchall()
print(registros)
conn.close()
50. Escribe un programa para calcular la desviación estándar de una columna numérica en SQLite.
python

import sqlite3
conn = sqlite3.connect('mi_base_datos.db')
cursor = conn.cursor()
cursor.execute('''SELECT AVG(salario), 
                         SUM((salario - (SELECT AVG(salario))) * (salario - (SELECT AVG(salario)))) / COUNT(*)
                  FROM empleados''')
media, varianza = cursor.fetchone()
desviacion = varianza ** 0.5
print(f"Desviación estándar: {desviacion}")
conn.close()





