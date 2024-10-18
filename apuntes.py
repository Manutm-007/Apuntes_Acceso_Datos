
Preguntas y Respuestas sobre SQLite3 y sqlite3 en Python
¿Qué es SQLite?

Respuesta: SQLite es una biblioteca de software que implementa un sistema de gestión de bases de datos relacional. Es ligero y no requiere un servidor separado; almacena datos en un archivo en disco.
¿Cómo se conecta a una base de datos SQLite usando Python?

Respuesta: Se utiliza la librería sqlite3. El comando para conectar es:
python

import sqlite3
conn = sqlite3.connect('nombre_base_de_datos.db')
¿Qué función se utiliza para crear un cursor en SQLite3?

Respuesta: La función cursor() se usa para crear un cursor:
python

cursor = conn.cursor()
¿Cómo se ejecuta una consulta SQL para crear una tabla?

Respuesta: Se puede usar el método execute() del cursor. Por ejemplo:
python

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
)
''')
¿Qué método se utiliza para guardar los cambios en la base de datos?

Respuesta: Se utiliza el método commit() en la conexión:
python

conn.commit()
¿Cómo se cierra la conexión a la base de datos?

Respuesta: Se utiliza el método close():
python

conn.close()
¿Cómo se insertan datos en una tabla?

Respuesta: Se utiliza el método execute() con una consulta INSERT. Ejemplo:
python

cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Juan', 30))
¿Cómo se realizan consultas para obtener datos de una tabla?

Respuesta: Se utiliza SELECT con execute(). Por ejemplo:
python

cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()
¿Cómo manejar excepciones al trabajar con SQLite3 en Python?

Respuesta: Se pueden manejar excepciones usando try y except:
python

try:
    cursor.execute("...")  # consulta SQL
except sqlite3.Error as e:
    print(f"Error: {e}")
¿Qué significa ? en las consultas SQL de SQLite3?

Respuesta: El símbolo ? es un marcador de posición para los parámetros. Se utiliza para prevenir inyecciones SQL.
Consejos Generales
Practica escribiendo consultas SQL y el código de Python necesario para interactuar con SQLite.
Familiarízate con las funciones y métodos más comunes de la librería sqlite3.
Revisa la documentación oficial de Python y SQLite para aclarar dudas o conceptos que no entiendas completamente.
Espero que estas preguntas y respuestas te sean útiles para prepararte. ¡Buena suerte en tu examen!



Tú dijiste:
te voy a pasar el temario del tema 2 voy a pasarte varios mensajes hasta que no te diga tal cual VALE no me contestes
ChatGPT Plus
ChatGPT
Entendido, espero tus mensajes.



Tú dijiste:
1. Introducción
Conforme vamos creando programas más sofisticados, aparece la necesidad de almacenar
de forma persistente la información que manejan para poder utilizarla en otro momento.
Por ejemplo, en el disco duro del ordenador, el móvil, la nube, etc.
Tradicionalmente han existidos dos sistemas de almacenamiento de información: los
ficheros y las bases de datos.
Aprender a gestionar la información que almacenamos en ficheros es relativamente
sencilla y puede ser útil para almacenar información muy básica. Por ejemplo: lista de
credenciales, datos de un vuelo, aplicaciones web permitidas, etc.
Pero si necesitamos almacenar gran cantidad de información relacionada entre sí entonces
debemos aprender a trabajar con bases de datos, ya que ofrecen mayores prestaciones.
 2. Bases de datos
Una base de datos está formada por un conjunto de datos relacionados entre sí que
recoge las necesidades de información de una organización.
Ejemplos:
• La información que maneja la aplicación Ítaca de la Generalitat Valenciana:
profesorado, alumnado, calificaciones, horarios, expedientes, etc.
• Datos de una agenda electrónica: nombres, direcciones, correos electrónicos de los
contactos, etc.
• Gestión de reservas en una pista deportiva: usuarios, fechas, horas, pistas, etc.
Para facilitar la creación y gestión de las bases de datos existen los Sistemas gestores de
bases de datos (SGBD) que son conjuntos de programas que permiten crear la estructura
de las bases de datos y manipular la información que almacenan. Además, proporcionan
una capa de seguridad extra ya que se ocupan de mantener la integridad de los datos,
permitir el acceso simultáneo a los mismos, controlar los permisos de acceso a
determinada información, ofrecer sistemas de recuperación ante fallos, etc.
Existen distintos modelos de bases de datos (jerárquicos, transaccionales, documentales,
orientados a objetos, etc) pero nosotros nos centraremos en el modelo relacional cuya
característica principal es que almacena los datos y las relaciones entre los mismos en unas
estructuras de datos llamadas tablas.
2
Programación con Python Introducción a las bases de datos
 2.1. Tablas, columnas y filas
Una tabla permite almacenar datos de una entidad, objeto o concepto de la vida real y las
relaciones entre sí.
La representación gráfica de una tabla suele ser una rejilla formada por filas y columnas.
Las columnas se corresponden con el nombre de los atributos o campos de los que
queremos almacenar información (por ejemplo: ciudad, fecha de nacimiento, altura) y las
filas se corresponden con los registros o elementos de los que estamos almacenando
dicha información.
Ejemplo: Tabla PERSONA que almacena información de cinco campos (dni, nombre, edad,
ciudad, altura) de cada persona de una organización.
DNI Nombre Edad Ciudad Altura
111111111 Ana 15 Morella 165
222222222 Pepito 8 Elche 132
333333333 Mireia 8 Manises 170
444444444 Joan 82 Oliva 170
 2.2. Claves y relaciones
Una vez que tenemos claros los datos que queremos almacenar en una tabla de una
entidad necesitamos encontrar la manera de diferenciar unos registros de otros. Esta
función la realizan las claves candidatas.
Una clave candidata es un conjunto de atributos de una tabla (mínimo uno) que permiten
identificar unívoca y mínimamente un registro de otro. Dicho de otra forma, no habrá
varias filas de una tabla con el mismo valor en los mismos atributos. Por ejemplo: el DNI de
una persona sería una clave candidata del ejemplo anterior.
A veces, las claves candidatas aparecen de forma natural y otras veces hay que añadir un
campo extra a la tabla. Por ejemplo, un campo numérico secuencial.
De entre todas las claves candidatas que aparezcan en una tabla, elegiremos una como
clave primaria y el resto quedarán como claves alternativas.
3
Columnas: nombres de los atributos
Filas: cada fila se
corresponde con
una persona
Programación con Python Introducción a las bases de datos
Ya que las claves candidatas sirven para identificar un registro de una tabla, no se permite
almacenar valores nulos en ellas. Es decir, es obligatorio almacenar un valor en cada
campo perteneciente a una clave candidata.
Hasta ahora hemos visto cómo almacenar información de una entidad en una tabla, pero
¿cómo almacenamos las relaciones entre distintas entidades?
Veamos algunos ejemplos de relaciones entre distintas entidades.
Ejemplo 1: una persona tiene una lengua materna (aunque luego pueda hablar más de un
idioma) y una misma lengua materna puede ser hablada por muchas personas. Relación
1:N.
Ejemplo 2: las personas pueden afiliarse a distintas asociaciones por motivos diversos y
una asociación puede tener afiliadas muchas personas. Relación N:N.
Existen más tipos de relaciones entre entidades pero nos centraremos en estas dos por ser
las más comunes.
Ahora ya podemos dar respuesta a nuestra pregunta. Las relaciones entre entidades se
almacenan como claves ajenas entre tablas.
Una clave ajena en una entidad es un conjunto de atributos (mínimo uno) que se
corresponde con la clave primaria de otra entidad, o de la misma según el tipo de relación.
Veamos su aplicación a los ejemplos anteriores.
Ejemplo 1: Relación 1:N entre PERSONA y LENGUA MATERNA.
4
PERSONA ASOCIACIÓN
PERSONA LENGUA MATERNA
Añadimos la clave ajena lengua en
la tabla PERSONA para referenciar
a la clave primaria de la tabla
LENGUA MATERNA.
Programación con Python Introducción a las bases de datos
Tabla PERSONA Tabla LENGUA MATERNA
DNI nombre edad ciudad altura lengua Abreviatura Nombre Descripción
111111111 Ana 15 Morella 165 cs cs castellano España
222222222 Pepito 8 Elche 132 cs va valenciano C.Valenciana
333333333 Mireia 8 Manises 170 va en inglés Reino Unido
444444444 Joan 82 Oliva 170 fr fr francés Francia
Como se puede observar, un registro de la tabla PERSONA puede estar relacionada con un
registro de la tabla LENGUA MATERNA (por ejemplo: Ana y Pepito) pero un registro de la
tabla LENGUA MATERNA puede estar relacionada con varios registros de la tabla PERSONA
o con ninguno.
Ejemplo 2: Relación N:N entre PERSONA y ASOCIACIÓN.
En este caso, una persona puede estar afiliada a
muchas asociaciones y una asociación puede tener
muchas personas afiliadas.
La solución pasa por crear una nueva tabla
llamada AFILIACIONES que contendrá un clave
ajena hacia la tabla PERSONA y una clave ajena hacia la tabla ASOCIACION. Además,
podremos añadir nuevos campos como la fecha de alta de dicha persona en dicha
asociación.
Tabla PERSONA Tabla ASOCIACION
DNI nombre edad ciudad altura CIF Nombre
111111111 Ana 15 Morella 165 1 Asociación de vecinos
222222222 Pepito 8 Elche 132 2 Programando juntos
333333333 Mireia 8 Manises 170 3 Club de cocina
444444444 Joan 82 Oliva 170
Tabla AFILIACIONES
persona asociacion fecha alta
444444444 1 15/01/2020
111111111 1 30/04/2021
111111111 2 01/05/2021
5
Programación con Python Introducción a las bases de datos
 3. El SGBD integrado SQLite
SQLite es un SGBD contenido en una librería del lenguaje C que viene integrada en Python.
Así que no necesitamos realizar ninguna instalación extra para trabajar con bases de datos
SQLite en programas de Python. Simplemente habrá que importar la librería
correspondiente, como a continuación:
import sqlite3
No obstante, puede ser muy útil poder acceder al contenido de nuestras bases de datos
para hacer comprobaciones sin tener que crear un programa específico en Python y
también probar las instrucciones SQL que vamos a ir aprendiendo durante esta unidad. Así
que, instalaremos el terminal de comandos de SQLite.
 3.1. Instalar el terminal de SQLite
Existen versiones del terminal sqlite3 para varios sistemas operativos: Android, Linux, Mac
OS, Windows, etc. En los siguientes apartados se explica con detalle cómo instalar el
terminal para Windows y Lliurex.
 3.1.1. Instalar en Windows
Sigue los pasos que se indican a continuación:
• Accede a la página web https://www.sqlite.org/download.html
• Busca el apartado Precompiled Binaries for Windows.
Figura 1: Página web de descargas
• Descarga el fichero sqlite-tools-win32-x86-3370200.zip o similar.
• Descomprime el fichero .zip y copia el fichero ejecutable sqlite3.exe en la carpeta
que quieras. Te recomiendo ubicarlo dentro de tu carpeta de proyectos de Python.
6
Programación con Python Introducción a las bases de datos
 3.1.2. Instalar en Lliurex
En la página oficial aparece un fichero para Linux de 32 bits pero es posible que tu sistema
operativo sea de 64 bits y tengas problemas para hacerlo funcionar, así que una alternativa
es seguir estos pasos:
• Comprobamos los repositorios del sistema operativo:
◦ En Lliurex 16, asegúrate de tener marcados los dos primeros repositorios en la
opción de menú Parámetros/Repositorios de la aplicación Gestor de paquetes
Synaptic.
◦ En Lliurex 19, debes tener marcado el repositorio Ubuntu bionic en la pestaña
Repositoris por defecto de la aplicación RepoMan.

• Instalamos el paquete sqlite3 con el siguiente comando:
sudo apt install sqlite3
7
Programación con Python Introducción a las bases de datos
 3.2. Uso del terminal SQLite
Una vez que tenemos instalado el terminal SQLite en nuestro sistema operativo, podemos
abrirlo de varias formas:
a) Sin especificar una base de datos: en ese caso estaremos trabajando con una base
de datos temporal y sus efectos se perderán cuando cerremos el terminal. No
obstante, siempre podremos salvar el contenido de los datos temporales en una
base de datos con el comando .save que veremos más adelante.
sqlite3
b) Especificando la base de datos: si la base de datos existe entonces se abrirá, pero si
la base de datos no existe entonces se creará en ese momento.
sqlite3 nombre_fichero.db
Una vez estemos dentro del terminal de SQLite podremos ejecutar directamente
instrucciones SQL o comandos específicos de sqlite3. En la siguiente tabla se presentan
algunos de estos comandos.
Comando Descripción
.open Abre una base de datos existente o la crea si no existe.
Ejemplo 1: Abrir una base de datos que se encuentra en la misma carpeta que el
ejecutable sqlite3.
.open colegio.db
Ejemplo 2: Abrir una base de datos que se encuentra en otra carpeta.
.open C:/bbdd/colegio.db
.save Guarda en el fichero de base de datos la definición y contenido de la base de datos
actual. Hay que tener cuidado porque no pide confirmación para modificar una base
de datos ya existente.
Ejemplo 1: Guardar una base de datos en la misma carpeta que sqlite3.
.save colegio.db
ChatGPT Plus
ChatGPT
Entendido, continúa con el temario cuando estés listo.



Tú dijiste:
Ejemplo 2: Guardar una base de datos que se encuentra en otra carpeta.
.save C:/bbdd/colegio.db
.read Este comando ejecuta las instrucciones SQL que contenga un fichero de texto.
Ejemplo:
.open myscript.sql
.schema Muestra la definición de la base de datos
Ejemplo:
.tables Muestra el nombre de las tablas existentes
Ejemplo:
.mode column Visualiza los resultados de las consultas en formato columna.
.exit Cerrar el terminal de SQLite
.help Muestra ayuda sobre los comandos del terminal. Si escribimos el nombre de un
comando a continuación, muestra la información solamente de ese comando.
Ejemplo:
 4. Lenguaje SQL
El lenguaje SQL (Structured Query Language) es el lenguaje más popular para trabajar con
bases de datos relacionales. Se compone de varios sublenguajes.
Aunque SQL ofrece una gran variedad de instrucciones, en esta unidad nos centraremos en
las instrucciones básicas de estos sublenguajes:
• El Lenguaje de definición de datos o DDL que permite crear la estructura de la base
de datos.
• El Lenguaje de manipulación de datos o DML que permite insertar, modificar y borrar
datos en la base de datos.
• El Lenguaje de consultas o DQL que permite recuperar o seleccionar información de
la base de datos.
9
Programación con Python Introducción a las bases de datos
 4.1. DDL: Lenguaje de definición de datos
El DDL o Lenguaje de definición de datos ofrece instrucciones para crear, modificar y borrar
distintos elementos de las bases de datos. Nosotros nos centraremos en la creación y
borrado de tablas.
 4.1.1. Crear tablas
Para crear tablas de datos utilizaremos la instrucción CREATE con la que definiremos las
columnas que contendrá, el tipo de datos que se almacenarán en las columnas y las
restricciones necesarias (por ejemplo, la definición de las claves candidatas y ajenas).
La sintaxis es la siguiente:
CREATE TABLE [IF NOT EXISTS] nombre_tabla (
columna1 tipo_dato [NOT NULL],
...
columnan tipo_dato [NOT NULL],
PRIMARY KEY(lista_columnas) [,
FOREIGN KEY(lista_columnas)
 REFERENCES tabla_referenciada(campos_ref)]
);
En la cabecera debemos indicar el nombre de la tabla teniendo en cuenta que no pueden
existir varias tablas con el mismo nombre en la misma base de datos.
• Si utilizamos la expresión IF NOT EXISTS entonces la instrucción CREATE solamente
se ejecutará en caso de que no exista una tabla en la base de datos con dicho
nombre.
• Si no utiliza la expresión IF NOT EXISTS y existe una tabla con el mismo nombre, se
producirá un error.
En la parte de la definición de las columnas debemos indicar la siguiente información:
• columnax es el nombre de la columna que estamos creando. Dentro de una misma
tabla no puede haber dos columnas con el mismo nombre.
• tipo_dato indica el tipo de valores que vamos a poder almacenar en dicha columna.
Los tipos de datos que podremos utilizar dependerán del SGBD en el que vayamos
10
 Definición de las columnas
 Definición de las claves
Programación con Python Introducción a las bases de datos
a utilizar esta sentencia. Nosotros utilizaremos los siguientes: INTEGER (número
entero), REAL (número real o decimal), TEXT (cadena de texto).
• NOT NULL indica que no es un valor optativo. Si se indica en la definición de un
campo estamos indicando que no se pueden crear registros en esta tabla para los
que no se asignen valores a este campo.
En la parte de la definición de las claves debemos indicar la siguiente información:
• La clave primaria utilizando la expresión PRIMARY KEY(lista_columnas) donde
lista_columnas es la lista de nombres de columnas, separadas por comas, que
forman parte de la clave primaria.
Ejemplos:
PRIMARY KEY(DNI)
PRIMARY KEY(nombre, apellido1, apellido2)
• Si la tabla tiene campos que actúan como claves ajenas, entonces deberemos
utilizar una expresión FOREIGN KEY(lista_columnas) REFERENCES
tabla_referenciada(campos_ref) por cada clave ajena que contenga la tabla. La
lista_columnas es la lista de columnas de la tabla que forman parte de la clave
ajena y campos_ref son los campos de la tabla referenciada a la que hacen
referencia (normalmente coinciden con la clave primaria de la tabla referenciada).
Ejemplos:
FOREIGN KEY(lengua) REFERENCES LENGUA_MATERNA(abreviatura)
FOREIGN KEY(nom_inqui, ape1_inqui, ape2_inqui) REFERENCES
 INQUILINO(nombre, apellido1, apellido2)
Te recomiendo que abras el terminal sqlite3 y pruebes las sentencias de los ejemplos que
hay a continuación.
Ejemplo 1: Creamos la tabla LENGUA_MATERNA con la definición de los campos y la clave
primaria.
CREATE TABLE LENGUA_MATERNA (
abreviatura TEXT,
nombre TEXT,
descripcion TEXT,
PRIMARY KEY(abreviatura)
);
11
Programación con Python Introducción a las bases de datos
Ejemplo 2: Ahora creamos la tabla PERSONA con la definición de los campos y la definición
de todas las claves, tanto la primaria como la clave ajena.
CREATE TABLE PERSONA (
dni INTEGER,
nombre TEXT,
edad INTEGER,
ciudad TEXT,
altura INTEGER,
lengua TEXT,
PRIMARY KEY(dni),
FOREIGN KEY(lengua) REFERENCES LENGUA_MATERNA(abreviatura)
);
Para comprobar que se han creado correctamente las dos tablas en la base de datos,
puedes ejecutar los siguientes comandos: .tables, .schema nombre_tabla.

 4.1.2. Borrar tablas
Si queremos borrar una tabla de la base de datos, y no nos referimos a vaciarla de
contenido sino a borrar la estructura completa de la tabla, podemos utilizar la siguiente
sentencia:
DROP TABLE [IF EXISTS] nombre_tabla;
12
Programación con Python Introducción a las bases de datos
Donde nombre_tabla es el nombre de la tabla que queremos eliminar de la base de datos.
• Si la tabla no existe entonces dará un error.
• Podemos utilizar la expresión IF EXISTS para evitarnos este problema. De esta
forma, si existe entonces la borrará pero si no existe entonces no pasará nada.
La sentencia DROP TABLE borra una tabla cada vez, así que deberemos ejecutar tantas
sentencias de este tipo como tablas queramos eliminar y siempre en el orden inverso en el
que las hemos creado si contienen claves ajenas.
Ejemplo 1: Borramos una tabla sin la cláusula IF EXISTS.
DROP TABLE persona;
Ejemplo 2: Borramos una tabla con la cláusula IF EXISTS.
DROP TABLE IF EXISTS persona;

La tabla se borra cuando existe pero, si no existe, no da error la sentencia DROP TABLE.
 4.2. DML: Lenguaje de manipulación de datos
El DML o Lenguaje de manipulación de datos ofrece instrucciones para poblar las tablas de
registros. Las sentencias INSERT, UPDATE y DELETE nos permitirán añadir registros,
modificar los datos de los ya existentes o eliminar algunos de ellos.
13
La primera vez que ejecutamos DROP TABLE la
tabla existe, así que, se borra sin problemas.
La segunda vez, se produce un error porque
estamos intentando borrar una tabla inexistente.
Programación con Python Introducción a las bases de datos
 4.2.1. INSERT: inserción de registros
Cuando ya tenemos creadas las tablas de la base de datos, podemos utilizar la siguiente
instrucción para añadir registros a las mismas:
INSERT INTO nombre_tabla [(columna1, …, columnan)]
VALUES(valor1, …, valorn);
Donde nombre_tabla es el nombre de la tabla a la que queremos añadir un registro. A
continuación, entre paréntesis, podemos indicar la lista de columnas de la tabla en el
orden que queramos. Si no se indica, entonces se tomará el orden de las columnas
conforme aparecen en la definición de la tabla.
Y, por último, indicamos la lista de valores que tomarán las columnas del registro. El primer
valor se almacenará en la primera columna de la lista, el segundo valor en la segunda
columna y así sucesivamente.
Ejemplo 1: Omitimos la lista de columnas.
INSERT INTO LENGUA_MATERNA
VALUES(‘cs’, ‘castellano’, ‘España’);
Ejemplo 2: Indicamos la lista de columnas en otro orden distinto del que aparece en la
definición de la tabla y funciona sin problemas.
INSERT INTO LENGUA_MATERNA(descripcion, nombre, abreviatura)
VALUES(‘valenciano’, ‘C.Valenciana’, ‘va’);
 4.2.2. DELETE: borrado de registros
Si lo que queremos es borrar varios registros de una tabla o todos ellos, podemos utilizar
la sentencia DELETE.
Ésta es su sintaxis:
DELETE FROM nombre_tabla
[WHERE condición_de_búsqueda];
14
Programación con Python Introducción a las bases de datos
En la expresión WHERE debemos indicar la condición de búsqueda para seleccionar los
registros que queremos eliminar. La veremos con mayor profundidad en la sentencia de
selección SELECT.
Ejemplo 1: Borramos los registros cuya abreviatura sea igual a “cs”.
DELETE FROM LENGUA_MATERNA WHERE abreviatura = “cs”;
Ejemplo 2: Borramos aquellas personas que vivan en Manises y tengan menos de 50 años.
DELETE FROM PERSONA WHERE ciudad = “Manises” and edad < 50;
Si omitimos la parte del WHERE entonces se borrarán todos los registros de una tabla,
aunque no su estructura. Ésta es la diferencia con la instrucción DROP TABLE.
15
Programación con Python Introducción a las bases de datos
Ejemplo 3: Borramos todos los registros de la tabla LENGUA_MATERNA.
DELETE FROM LENGUA_MATERNA;

 4.2.3. UPDATE: modificación de registros
Podemos modificar todos los registros de una tabla o una selección de ellos. Y podemos
modificar el valor de varias columnas de un registro o solo de una de ellas.
Ésta es la sintaxis de la sentencia UPDATE:
UPDATE nombre_tabla
SET columna₁ = nueva_valor₁,
...
columnan = nueva_valorn
[WHERE condición_de_búsqueda];
La sintaxis de esta sentencia es parecida a la de la sentencia DELETE excepto por el
apartado SET. En él se deben indicar los valores nuevos de las columnas que queremos
modificar.
En este caso también se puede omitir el apartado WHERE si queremos actualizar todos los
registros de la tabla.
Ejemplo 1: Modificamos la edad de todas las personas.
UPDATE PERSONA
SET edad = edad + 1;
ChatGPT Plus
ChatGPT
Entendido, sigue cuando quieras.



Tú dijiste:
Ejemplo 2: Modificamos la altura de Joan porque debe ser 175 y no 170.
UPDATE PERSONA
SET altura = 175
WHERE nombre = “Joan”;
 4.3. DQL: Lenguaje de consulta de datos
El Lenguaje de consultas de datos o DQL permite realizar consultas de los registros de las
tablas de una base de datos. Para ello, se utiliza la instrucción más conocida de este
lenguaje: la sentencia SELECT.
Aunque esta instrucción ofrece muchas prestaciones y podemos construir una sentencia
SELECT muy sofisticada, en esta introducción a bases de datos, nos centraremos en una
versión más simple de la misma.
 4.3.1. Seleccionar registros de una tabla
Una primera aproximación a la sintaxis de la sentencia SELECT puede ser la siguiente:
SELECT lista_columnas
FROM nombre_tabla
17
Programación con Python Introducción a las bases de datos
[WHERE condición_búsqueda]
[ORDER BY nombre_columna [ASC|DESC]];
Donde:
• En la cláusula SELECT indicaremos el nombre de las columnas de la tabla que
queremos ver, separadas por comas.
• En la cláusula FROM indicaremos el nombre de la tabla que queremos consultar.
• En la cláusula WHERE escribiremos la condición de búsqueda que deberán cumplir
los registros que se mostrarán en el resultado de la consulta.
◦ Esta condición de búsqueda se forma con expresiones lógicas. Podemos
comparar valores con operadores relacionales (>, >=, <, >=, =, !=) y concatenar
expresiones lógicas con los operadores lógicos (and, or, not).
◦ Si no se utiliza esta cláusula entonces se mostrarán todos los registros de la
tabla.
• En la cláusula ORDER BY indicaremos la lista de columnas que se utilizarán para
ordenar los registros.
◦ Se ordenarán según la lista de campos especificada de izquierda a derecha. Por
defecto en orden ascendente (ASC) aunque podemos cambiar el orden a
descendente (DESC).
◦ Si no se utiliza esta cláusula entonces los registros se ordenarán por la lista de
campos especificada en la cláusula SELECT, de izquierda a derecha y
ascendentemente.
Ejemplo 1: Muestra todos los registros de la tabla PERSONA.
SELECT * FROM PERSONA;
18
Para conocer más de esta cláusula, consulta la web
https://www.sqlitetutorial.net/sqlite-where/
Programación con Python Introducción a las bases de datos
Ejemplo 2: Muestra los campos nombre y ciudad de todos los registros de la tabla
PERSONA.
SELECT nombre, ciudad FROM PERSONA;
Ejemplo 3: Muestra todos los registros de la tabla PERSONA ordenados descendentemente
por la altura y ascendentemente por el nombre.
SELECT * FROM PERSONA
ORDER BY altura DESC, nombre ASC;
Ejemplo 4: Muestra los registros de la tabla PERSONA con altura menor de 170.
SELECT * FROM PERSONA
WHERE altura < 170;
Ejemplo 5: Muestra los registros de la tabla PERSONA con altura menor de 170 y edad
igual a 8.
SELECT * FROM PERSONA
WHERE altura < 170 and edad = 8;
19
Programación con Python Introducción a las bases de datos
 4.3.2. Seleccionar registros de varias tablas
También podemos seleccionar registros de varias tablas que estén relacionados.
Normalmente los uniremos por alguna clave ajena. Podemos incluir en la cláusula WHERE
las condiciones de unión de los registros de dichas tablas.
SELECT lista_columnas
FROM tabla1 T1, tabla2 T2, …, tablan Tn
WHERE
Donde:
• En la cláusula FROM escribimos la lista de tablas implicadas.
• Para cada nombre de tabla podemos especificar un alias que utilizaremos delante
de sus campos para indicar la tabla y evitar ambigüedades.
Ejemplo 1: Mostrar los datos de aquellas personas cuya lengua materna sea la de España.
SELECT * FROM PERSONA P, LENGUA_MATERNA LM
WHERE P.lengua = LM.abreviatura and
 LM.descripcion = “España”;
Se pueden mezclar las condiciones de unión de tablas con las condiciones de búsqueda de
los registros.
Ejemplo 2: Mostrar los datos de aquellas personas cuya lengua materna sea la de España y
tengan 8 años.
SELECT * FROM PERSONA P, LENGUA_MATERNA LM
WHERE P.lengua = LM.abreviatura and
 LM.descripcion = “España” and P.edad = 8;
20
Programación con Python Introducción a las bases de datos
Para mostrar todos los campos de una tabla podemos indicarlo así: nombre_tabla.*
Ejemplo 3: Mostrar los datos de las personas afiliadas a la “Asociación de vecinos”.
SELECT P.*
FROM PERSONA P, AFILIACIONES AF, ASOCIACION ASO
WHERE P.dni = AF.persona and AF.asociacion = ASO.cif and
 ASO.nombre = 'Asociación de vecinos';
 5. Conclusiones
A lo largo de este documento hemos explicado qué es una base de datos, cuáles son los
elementos básicos para crear una (tablas y relaciones) y qué instrucciones SQL podemos
utilizar para gestionarlas.
El mundo de las bases de datos es mucho más amplio de lo que hemos podido ver aquí y
el lenguaje SQL ofrece muchas más instrucciones y cláusulas de las que hemos presentado.
Pero éste puede ser un buen punto de partida. Te invito a seguir conociendo más sobre
bases de datos a través de tutoriales en Internet, por ejemplo:
https://www.sqlitetutorial.net
En el aula virtual dispones de los siguientes ficheros para hacer pruebas:
Comando Descripción
ejemplos.sql Fichero de texto que contiene las instrucciones SQL necesarias para crear la base de
datos que hemos utilizado en los ejemplos de este documento y poblar las tablas
con registros. Puedes ejecutarlo en sqlite3 con .read ejemplos.sql
21
Programación con Python Introducción a las bases de datos
ejemplos.db Fichero de base de datos después de ejecutar las instrucciones SQL del fichero
anterior. Puedes abrirlo en sqlite3 y trabajar sobre él: .open ejemplos.db
ChatGPT Plus
ChatGPT
Perfecto, has cubierto una introducción completa a las bases de datos y a las instrucciones SQL. Si tienes alguna pregunta o quieres profundizar en algún tema específico, ¡dímelo!



Tú dijiste:
INTRODUCCIÓN
No se necesita ninguna instalación extra para que Python pueda trabajar con BDA SQLite ya que existe la librería
incorporada SQLite3. Así pues, solo hemos de importar esta librería par apoder hacer uso de las funciones y
elementos que incluye para crear BDA y manipular su información. La sintaxis de la importación:
CONEXIÓN Y DESCONEXIÓN DE UNA BDA
Lo primero que se hace para poder trabajar con una BDA es conectarnos a ella. Hay varios casos:
- Conexión a una BDA existente.
- Conexión a una BDA existente pero todavía no tiene creada su estructura.
- Conexión a una BDA temporal para hacer pruebas.
Las dos primeras residen en el disco duro de nuestra máquina, es decir, se crea un fichero con extensión .db que
contiene toda la información de la BDA. La última es una BDA que reside en RAM y cuando acabe el programa
desaparece.
import sqlite3
nombre_conexion = sqlite3.connect(nombre_fichero_db)
Variable Python que
representa la BDA.
Nombre del fichero de la BDA entre comillas
para almacenar todo | :memory: para BDA
temporal.
Para cerrar la conexión a la BDA utilizamos: nombre_conexion.close()
Variable Python que
representa la BDA.
Ejemplo 1: nos conectamos a la BDA "ejemplos.db". Dicho fichero está situado en la misma carpeta que el
programa Python.
import sqlite3
my_conn = sqlite3.connect("ejemplos.db") # fichero que guarda la BDA
# para BDA temporales ":memory:"
# código que utiliza la BDA
my_conn.close()
Ejemplo 2: nos conectamos a la BDA "ejemplos.db". Dicho fichero está situado en una carpeta diferente a la del
programa Python.
CONEXIÓN Y DESCONEXIÓN DE UNA BDA
Realiza actividad_sqlite_conn.py
Realiza actividad_sqlite_conn2.py
import sqlite3
my_conn = sqlite3.connect("datos/ejemplos.db") # fichero que
guarda la BDA
# para BDA temporales ":memory:"
# código que utiliza la BDA
my_conn.close()
Ejemplo 3: trabajamos con una BDA temporal, que no se almacena en un soporte físico de la máquina.
import sqlite3
my_conn = sqlite3.connect(":memory:") # para BDA temporales ":memory:"
# código que utiliza la BDA
my_conn.close()
En un programa Python se puede trabajar con varias BDA simultáneamente. Por ejemplo, para hacer una migración
de datos de una BDA a otra. Para hacer cosas de ese estilo, se abre una conexión por cada BDA que necesitamos y
ejecutamos las funciones de conexión correspondientes.
Ejemplo4: abrimos varias conexiones a diferentes BDA.
import sqlite3;
con_sec = sqlite3.connect("secundaria.db")
con_pri = sqlite3.connect("primaria.db")
con_inf = sqlite3.connect("infantil.db")
# Código que utiliza las BDA
con_sec.close()
con_pri.close()
con_inf.close()
CONEXIÓN Y DESCONEXIÓN DE UNA BDA
Realiza actividad_sqlite_conn3.py
Realiza actividad_sqlite_conn4.py
USO DE CURSORES
Un cursor es un objeto de la BDA que nos permite ejecutar instrucciones SQL en la BDA y recuperar registros de ésta.
Para poder utilizar las funciones de un cursor, primero se crea:
nombre_cursor = nombre_conexion.cursor()
Variable Python que contiene
el cursor de la BDA.
Conexión a la BDA
definida préviamente.
Ejemplo: definición de un cursor de una BDA
import sqlite3
my_conn = sqlite3.connect(":memory:") # BDA temporal
# un cursor es un objeto que permite ejecutar intrucciones SQL en una BDA
my_cur = my_conn.cursor() # creamos cursor
# instrucciones de uso del cursor
my_conn.close()
A continuación, veremos las operaciones que se pueden hacer en una BDA a través de un cursor.
Realiza actividad_sqlite_cursores.py
CREACIÓN Y BORRADO DE TABLAS
Podemos ejecutar senténcias SQL a través de un cursor de una BDA teniendo en cuenta que siempre que hagamos
cambios en la estructura ( y contenido) de la BDA, tendremos que ejecutar la función commit() para que estos
cambios sean permanentes. La sintaxis es la siguiente:
mi_cursor.execute(sentencia_SQL_sin_punto_y_coma)
mi_conexion.commit()
Variable cursor del programa. Sin ; al final. Escribimos el SQL entre " o podemos pasar variable str con el SQL.
NOTA: Si queremos escribir el SQL en varias líneas para estructurarlo bien tenemos que usar triple comilla.
Ejemplo: creación de la tabla LENGUA_MATERNA.
import sqlite3
my_conn = sqlite3.connect(":memory:") # BDA temporal
my_cur = my_conn.cursor() # creamos cursor
# DDL
sentencia_sql = '''create table if not exists LENGUA_MATERNA(
abreviatura TEXT,
nombre TEXT,
descripcion TEXT,
PRIMARY KEY(abreviatura)
)'''
my_cur.execute(sentencia_sql) # ejecutamos SQL
my_conn.commit() # hace permanentes los cambios en la BDA (transacción)
my_conn.close()
Realiza actividad_sqlite_cursores2.py
Ejemplo 2: borramos la tabla afiliaciones.
# antes de ejecutar este programa hacemos un backup de ejemplos.db
import sqlite3
my_conn = sqlite3.connect("ejemplos.db")
my_cur = my_conn.cursor()
sentencia_sql = "drop table if exists AFILIACIONES"
my_cur.execute(sentencia_sql)
my_conn.commit()
my_conn.close()
# ahora entramos en sqlite3: .open ejemplos.db .tables y comprobamos que AFILIACIONES
# se ha borrado. Salimos con .exit
INSERCIÓN, ACTUALIZACIÓN Y BORRADO DE REGISTROS
Podemos ejecutar sentencias para insertar, borrar y actualizar registros de la BDA. También hemos de utilizar la
función commit() para hacer permanentes los cambios en la BDA.
CREACIÓN Y BORRADO DE TABLAS
Realiza actividad_sqlite_cursores3.py
# antes de ejecutar este fichero restauramos la copia de ejemplos.db
import sqlite3
my_conn = sqlite3.connect("ejemplos.db")
my_cur = my_conn.cursor()
# sentencias
ins = '''insert into AFILIACIONES
values(555555555, "1", "15/01/2020")'''
mod = '''update AFILIACIONES
set persona = 333333333 where persona = 555555555'''
bor = '''delete from AFILIACIONES where persona = 333333333'''
# ejecución de sentencia
my_cur.execute(ins)
my_cur.execute(mod)
my_cur.execute(bor)
my_conn.commit() # solo un commit por transacción
my_conn.close()
También podemos utilizar parámetros a la hora de construir las sentencias SQL. Por ejemplo, podemos insertar
registros utilizando los valores almacenados en variables del programa. Para ello, usaremos el carácter ? por cada
parámetro de la sentencia.
INSERCIÓN, ACTUALIZACIÓN Y BORRADO DE REGISTROS
Realiza actividad_sqlite_cursores4.py
Ejemplo: ejecución de instrucciones de manipulación de registros.
INSERCIÓN, ACTUALIZACIÓN Y BORRADO DE REGISTROS
Ejemplo: insertamos un registro con dos parámetros que se pasan a la función en forma de tupla.
import sqlite3
my_conn = sqlite3.connect("ejemplos.db")
my_cur = my_conn.cursor()
# sentencias sql dinámico: utilizamos ? por cada parámetro de la sentencia
ins = '''insert into AFILIACIONES
values(?, ?, "15/01/2020")'''
persona = 555555555
my_cur.execute(ins, (persona, "1")) # pasamos una tupla con los valores de los parámetros
# si solo pasáramos un parámetro sería (persona,)
# y no (persona)
my_conn.commit() # solo un commit por transacción
my_conn.close()
Realiza actividad_sqlite_cursores5.py
Ejemplo: solo pasando un parámetro a la instrucción SQL.
...
ins = '''INSERT INTO AFILIACIONES
VALUES (?, "1", "15/01/2020")'''
dni = 55555555
mi_cursor.execute(ins, (dni, ))
...
Utilizando una técnica similar se pueden insertar un grupo de registros en una tabla con solo una instrucción. Para
esto, utilizamos la función executemany() a la cual se le pasa una lista de tuplas con los valores de los campos de
cada registro.
Ejemplo: insertamos tres registros enla tabla AFILIACIONES pasando una lista de tuplas a executemany().
...
# técnica para insertar un grupo de registros con una sola instrucción
# usamos una lista de tuplas
lista = [(333333333, '1', '15/01/2020'),
(333333333, '2', '02/01/2021'),
(444444444, '3', '09/04/2021')]
ins = '''insert into AFILIACIONES
values(?, ?, ?)'''
my_cur.executemany(ins, lista) # pasamos la lista de tuplas
...
Realiza actividad_sqlite_cursores6.py
INSERCIÓN, ACTUALIZACIÓN Y BORRADO DE REGISTROS
CONSULTA DE DATOS
Vamos a ejecutar consultas de datos en una BDA para poder usar los valores recuperados en nuestros programas.
En este caso, no hace falta ejecutar la función commit() porque no se hacen cambios en la BDA.
Continuamos utilizando la función execute() para ejecutar la sentencia SQL. Además, utilizaremos las funciones
fetchone() i fetchall() de los cursores para rcuperar los resultados de la consulta.
La función fetchone() retorna una tupla con los valores de las columnas correspondientes. Si no recupera ningún
registro retorna None.
Ejemplo: uso de fectchone() para recuperar un registro de la consulta.
...
my_cur.execute("select * from PERSONA")
# recuperamos el primer registro de la consulta
# retorna tupla con los valores de las columnas o None si no hay nada que retornar
reg = my_cur.fetchone()
if reg == None:
print("La consulta no ha devuelto ningún registro")
else:
print(reg)
...
Realiza actividad_sqlite_cursores_consultas.py
Podemos usar la funcion fetchone() dentro de un bucle para recuperar todos los registros de la consulta.
Ejemplo 2: uso de la función fetchone() con bucle.
# vamos a ejecutar concultas mediante un cursor
import sqlite3
my_conn = sqlite3.connect("ejemplos.db")
my_cur = my_conn.cursor()
# no se usa commit() ya no se hacen cambios sobre la BDA
# usaremos execute() para ejecutar la consulta y fechone() / fetchall() para recuperar los resultados
my_cur.execute("select * from PERSONA")
# recuperamos todos los registros mediante un bucle
reg = my_cur.fetchone() # primer registro
while reg != None:
print(reg)
reg = my_cur.fetchone() # siguiente registro
my_conn.close()
Realiza actividad_sqlite_cursores_consultas2.py
CONSULTA DE DATOS
CONSULTA DE DATOS
La función fetchall() retorna una lista de tuplas con los valores de todos los registros de la consulta. Si la consulta no
retorna ningún registro la función devuelve una lista vacía [].
Ejemplo 3: uso de la función fetchall() para recuperar todos los registros de una consulta.
# vamos a ejecutar consultas mediante un cursor
import sqlite3
my_conn = sqlite3.connect("ejemplos.db")
my_cur = my_conn.cursor()
my_cur.execute("select * from PERSONA")
# recuperamos todos los registros mediante el método fetchall()
# fetchall retorna lista de tuplas, donde cada tupla es un registro.
# Si la consulta no retorma ningún registro fetchall retorna una lista vacía []
registros = my_cur.fetchall()
for reg in registros:
print(reg)
my_conn.close()
Realiza actividad_sqlite_cursores_consultas3.py
CONCLUSIÓN
Hemos visto cómo conectarnos a una BDA SQLite desde un programa Python y cómo ejecutar diferentes
instrucciones SQL tanto para modificar la estructura de la BDA como para manipular o consultar los registros que
contiene.
A lo largo del módulo ADA volveremos de nuevo a SQLite, pero ya con más conocimientos de Python, y
entenderemos mejor todo esto.
ChatGPT Plus
ChatGPT
Has elaborado una introducción muy completa sobre cómo trabajar con bases de datos SQLite en Python. Aquí hay un resumen de los puntos clave:

Introducción
SQLite3: Librería incorporada en Python para manejar bases de datos SQLite sin necesidad de instalación adicional.
Conexión y Desconexión
Conexión: Se establece usando sqlite3.connect(nombre_fichero_db), donde el nombre del fichero puede ser una ruta a un archivo existente o ":memory:" para una base de datos temporal.
Desconexión: Se realiza con nombre_conexion.close().
Uso de Cursores
Cursor: Objeto que permite ejecutar instrucciones SQL y recuperar registros. Se crea con nombre_cursor = nombre_conexion.cursor().
Creación y Borrado de Tablas
Para crear o borrar tablas, se utiliza cursor.execute(sentencia_SQL) y se asegura de hacer commit con conexion.commit() para guardar los cambios.
Inserción, Actualización y Borrado de Registros
Se pueden realizar inserciones, actualizaciones y borrados utilizando sentencias SQL y commit() para hacer permanentes los cambios.
Se pueden usar parámetros en las consultas con ? para mayor seguridad y flexibilidad.
Consulta de Datos
Las consultas se realizan con execute() y se recuperan resultados usando fetchone() o fetchall().
Conclusión
Se ha cubierto el uso de SQLite en Python, desde la conexión a la base de datos hasta la ejecución de diferentes instrucciones SQL.
Si necesitas más detalles sobre algún aspecto o ejemplos prácticos, ¡házmelo saber!



Tú dijiste:
vale partiendo de lo que te enviado. me van hacer el examen que te digo y el titulo del examen dice tal cual: !6 preguntas sobre consola SQLite3 y librería sqite3 de Python.

El mejor de 2 intentos. No hay fedback hasta que todos se hayan examinado.

 se puede usar VSCode, apuntes y páginas web de Python.
ChatGPT Plus
ChatGPT
¡Perfecto! Dado que te examinarás sobre SQLite3 y la librería sqlite3 de Python, aquí tienes algunos conceptos clave y ejemplos que podrías encontrar útiles. Esto te permitirá repasar y estar listo para el examen.

Temas Clave para el Examen
Conexión a la Base de Datos

Cómo conectarse a una base de datos existente o crear una nueva.
Ejemplo:
python

import sqlite3
conn = sqlite3.connect("mi_base_de_datos.db")
Uso de Cursores

Creación de un cursor para ejecutar instrucciones SQL.
Ejemplo:
python

cursor = conn.cursor()
Creación de Tablas

Sentencia SQL para crear tablas y el uso de commit().
Ejemplo:
python

cursor.execute('''
CREATE TABLE IF NOT EXISTS Persona (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
)
''')
conn.commit()
Inserción de Registros

Cómo insertar datos en una tabla, utilizando parámetros.
Ejemplo:
python

cursor.execute('INSERT INTO Persona (nombre, edad) VALUES (?, ?)', ('Juan', 30))
conn.commit()
Consulta de Datos

Cómo realizar consultas y recuperar resultados con fetchone() y fetchall().
Ejemplo:
python

cursor.execute('SELECT * FROM Persona')
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
Actualización y Borrado de Registros

Cómo actualizar y eliminar registros de una tabla.
Ejemplo:
python

cursor.execute('UPDATE Persona SET edad = ? WHERE nombre = ?', (31, 'Juan'))
conn.commit()
cursor.execute('DELETE FROM Persona WHERE nombre = ?', ('Juan',))
conn.commit()
Cierre de Conexiones

Importancia de cerrar conexiones y cursores.
Ejemplo:
python

cursor.close()
conn.close()
Consejos para el Examen
Lee atentamente cada pregunta: Asegúrate de comprender lo que se pregunta antes de responder.
Prueba en VSCode: Si puedes usar VSCode, intenta ejecutar ejemplos similares a los que podrías ver en el examen.
Consulta tus apuntes: Si hay algo que no recuerdas, revisa tus notas o documentación en línea.
Si tienes preguntas específicas o necesitas aclarar algún concepto, ¡házmelo saber!



Tú dijiste:
haz todas las preguntas que se te ocurran partiendo todos los documentos que te envié
ChatGPT Plus
ChatGPT
Claro, aquí tienes una serie de preguntas que podrían surgir en tu examen sobre SQLite3 y la librería sqlite3 de Python, basadas en los documentos que compartiste:

Preguntas sobre SQLite3
Conexión a la Base de Datos:

¿Cuál es la función utilizada para conectar a una base de datos SQLite en Python? Proporciona un ejemplo.
¿Qué sucede si intentas conectarte a una base de datos que no existe?
Uso de Cursores:

¿Qué es un cursor en SQLite y para qué se utiliza?
¿Cómo se crea un cursor a partir de una conexión?
Creación de Tablas:

Explica la sintaxis básica para crear una tabla en SQLite.
¿Qué es una clave primaria y cómo se define en una tabla?
Inserción de Datos:

¿Cómo se inserta un nuevo registro en una tabla? Proporciona un ejemplo utilizando parámetros.
¿Qué función se utiliza para hacer permanentes los cambios realizados en la base de datos después de una inserción?
Consultas de Datos:

¿Cuál es la instrucción SQL para seleccionar todos los registros de una tabla?
Describe la diferencia entre fetchone() y fetchall(). Proporciona ejemplos de cómo usarlos.
Actualización y Borrado de Registros:

¿Cómo se actualiza un registro en una tabla? Proporciona un ejemplo.
¿Qué instrucción SQL se utiliza para eliminar registros de una tabla?
Manejo de Errores:

¿Cómo puedes manejar errores al trabajar con bases de datos en Python?
Cierre de Conexiones:

¿Por qué es importante cerrar la conexión a la base de datos y el cursor al finalizar?
¿Qué función se utiliza para cerrar una conexión?
Uso de Múltiples Conexiones:

¿Es posible tener múltiples conexiones a diferentes bases de datos al mismo tiempo? Explica cómo.
Ejecución de Múltiples Consultas:

¿Cómo se pueden ejecutar múltiples inserciones de datos en una tabla usando una sola instrucción?
Ejemplos Prácticos
Proporciona un ejemplo completo de un script Python que realice lo siguiente:
Conectarse a una base de datos.
Crear una tabla.
Insertar algunos registros.
Consultar los registros e imprimirlos.
Actualizar un registro.
Eliminar un registro.
Cerrar la conexión.
Estas preguntas abarcan los conceptos clave que discutiste en tus documentos y deberían ayudarte a prepararte bien para tu examen. Si deseas más detalles o aclaraciones sobre alguna pregunta, ¡dímelo!



Tú dijiste:
disculpa necesito tanto preguntas como respuestas
ChatGPT Plus
ChatGPT
¡Claro! Aquí tienes una lista de preguntas con sus respuestas correspondientes.

Preguntas y Respuestas sobre SQLite3 y la librería sqlite3 de Python
Pregunta: ¿Cuál es la función utilizada para conectar a una base de datos SQLite en Python? Proporciona un ejemplo.

Respuesta: La función utilizada es sqlite3.connect().
Ejemplo:
python

import sqlite3
my_conn = sqlite3.connect("ejemplos.db")
Pregunta: ¿Qué sucede si intentas conectarte a una base de datos que no existe?

Respuesta: Si la base de datos no existe, SQLite creará un nuevo archivo con el nombre especificado y una base de datos vacía.
Pregunta: ¿Qué es un cursor en SQLite y para qué se utiliza?

Respuesta: Un cursor es un objeto que permite ejecutar instrucciones SQL en la base de datos y recuperar registros.
Pregunta: ¿Cómo se crea un cursor a partir de una conexión?

Respuesta: Se crea utilizando el método cursor() de la conexión.
Ejemplo:
python

my_cur = my_conn.cursor()
Pregunta: Explica la sintaxis básica para crear una tabla en SQLite.

Respuesta: La sintaxis básica es:
sql

CREATE TABLE nombre_tabla (
    columna1 tipo_dato,
    columna2 tipo_dato,
    ...
    PRIMARY KEY(columna1)
);
Pregunta: ¿Qué es una clave primaria y cómo se define en una tabla?

Respuesta: Una clave primaria es un campo que identifica de manera única cada registro en la tabla. Se define utilizando la cláusula PRIMARY KEY al crear la tabla.
Pregunta: ¿Cómo se inserta un nuevo registro en una tabla? Proporciona un ejemplo utilizando parámetros.

Respuesta: Se utiliza la instrucción INSERT INTO.
Ejemplo:
python

my_cur.execute("INSERT INTO PERSONA (nombre, edad) VALUES (?, ?)", ("Juan", 30))
Pregunta: ¿Qué función se utiliza para hacer permanentes los cambios realizados en la base de datos después de una inserción?

Respuesta: La función commit() se utiliza para hacer permanentes los cambios.
Ejemplo:
python

my_conn.commit()
Pregunta: ¿Cuál es la instrucción SQL para seleccionar todos los registros de una tabla?

Respuesta: La instrucción es SELECT * FROM nombre_tabla;.
Pregunta: Describe la diferencia entre fetchone() y fetchall(). Proporciona ejemplos de cómo usarlos.

Respuesta: fetchone() retorna una tupla con el siguiente registro de la consulta, o None si no hay más registros. fetchall() retorna una lista de tuplas con todos los registros.
Ejemplo:
python

my_cur.execute("SELECT * FROM PERSONA")
reg = my_cur.fetchone()  # Retorna el primer registro
registros = my_cur.fetchall()  # Retorna todos los registros
Pregunta: ¿Cómo se actualiza un registro en una tabla? Proporciona un ejemplo.

Respuesta: Se utiliza la instrucción UPDATE.
Ejemplo:
python

my_cur.execute("UPDATE PERSONA SET edad = ? WHERE nombre = ?", (31, "Juan"))
Pregunta: ¿Qué instrucción SQL se utiliza para eliminar registros de una tabla?

Respuesta: La instrucción es DELETE FROM nombre_tabla WHERE condición;.
Pregunta: ¿Cómo puedes manejar errores al trabajar con bases de datos en Python?

Respuesta: Se pueden manejar errores utilizando bloques try y except.
Ejemplo:
python

try:
    my_cur.execute("SELECT * FROM PERSONA")
except sqlite3.Error as e:
    print(f"Ocurrió un error: {e}")
Pregunta: ¿Por qué es importante cerrar la conexión a la base de datos y el cursor al finalizar?

Respuesta: Es importante para liberar los recursos del sistema y evitar posibles bloqueos o errores en futuras conexiones.
Pregunta: ¿Qué función se utiliza para cerrar una conexión?

Respuesta: La función close() se utiliza para cerrar la conexión.
Ejemplo:
python

my_conn.close()
Pregunta: ¿Es posible tener múltiples conexiones a diferentes bases de datos al mismo tiempo? Explica cómo.

Respuesta: Sí, se pueden abrir múltiples conexiones a diferentes bases de datos utilizando múltiples instancias de sqlite3.connect().
Ejemplo:
python

con1 = sqlite3.connect("db1.db")
con2 = sqlite3.connect("db2.db")
Pregunta: ¿Cómo se pueden ejecutar múltiples inserciones de datos en una tabla usando una sola instrucción?

Respuesta: Se puede utilizar el método executemany() para insertar múltiples registros a la vez.
Ejemplo:
python

lista = [(1, "Juan"), (2, "Ana"), (3, "Luis")]
my_cur.executemany("INSERT INTO PERSONA (id, nombre) VALUES (?, ?)", lista)
Espero que estas preguntas y respuestas te ayuden a prepararte para tu examen. Si necesitas más detalles o ejemplos, ¡házmelo saber!



Tú dijiste:
en caso de que me hagan hacer programas... me puedes poner preguntas y respuestas? creo que el examen va ser 100% programacion y en donde dice 6 preguntas tengo la intuicion que sera todo atraves de visual code
ChatGPT Plus
ChatGPT
¡Entendido! Aquí tienes preguntas y respuestas centradas en programación con la librería sqlite3 de Python, que podrían ayudarte en un examen práctico.

Preguntas y Respuestas de Programación con SQLite3 en Python
Pregunta: Escribe un programa en Python que cree una base de datos llamada test.db y una tabla llamada usuarios con columnas id, nombre y edad.

Respuesta:
python

import sqlite3

# Conectar a la base de datos (la crea si no existe)
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Crear la tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
)
''')

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()
Pregunta: Escribe un programa que inserte tres usuarios en la tabla usuarios.

Respuesta:
python

import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Insertar tres usuarios
usuarios = [
    (1, "Juan", 25),
    (2, "Ana", 30),
    (3, "Luis", 22)
]
cursor.executemany("INSERT INTO usuarios (id, nombre, edad) VALUES (?, ?, ?)", usuarios)

conn.commit()
conn.close()
Pregunta: Crea un programa que consulte todos los registros de la tabla usuarios y los imprima en la consola.

Respuesta:
python

import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")
registros = cursor.fetchall()

for reg in registros:
    print(reg)

conn.close()
Pregunta: Escribe un programa que actualice la edad de un usuario específico en la tabla usuarios.

Respuesta:
python

import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Actualizar la edad de 'Juan'
cursor.execute("UPDATE usuarios SET edad = ? WHERE nombre = ?", (26, "Juan"))

conn.commit()
conn.close()
Pregunta: Escribe un programa que elimine un usuario de la tabla usuarios dado su nombre.

Respuesta:
python

import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Eliminar usuario con nombre 'Ana'
cursor.execute("DELETE FROM usuarios WHERE nombre = ?", ("Ana",))

conn.commit()
conn.close()
Pregunta: Crea un programa que maneje errores al conectar a la base de datos y al ejecutar consultas.

Respuesta:
python

import sqlite3

try:
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    registros = cursor.fetchall()

    for reg in registros:
        print(reg)

except sqlite3.Error as e:
    print(f"Ocurrió un error: {e}")

finally:
    if conn:
        conn.close()
Pregunta: Escribe un programa que inserte un nuevo usuario utilizando parámetros y maneje la posibilidad de que ya exista.

Respuesta:
python

import sqlite3

def insertar_usuario(nombre, edad):
    try:
        conn = sqlite3.connect("test.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
        conn.commit()
    except sqlite3.IntegrityError:
        print("El usuario ya existe.")
    finally:
        conn.close()

# Llamada a la función
insertar_usuario("Juan", 25)
Pregunta: Crea un programa que muestre la cantidad total de usuarios en la tabla usuarios.

Respuesta:
python

import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM usuarios")
total_usuarios = cursor.fetchone()[0]
print(f"Total de usuarios: {total_usuarios}")

conn.close()
Estas preguntas están diseñadas para cubrir varios aspectos de la programación con SQLite3 en Python. Si necesitas más ejemplos o enfoques, ¡házmelo saber!