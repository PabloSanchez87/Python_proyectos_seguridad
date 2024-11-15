# Extracción de metadatos con Python

## Objetivos

### Competencia
- Conocer los principales módulos disponibles en Python con el objetivo de automatizar la extracción de metadatos de documentos e imágenes.
- El proceso de extracción de información permite recoger metadatos de documentos y en ocasiones también es posible obtener la ubicación geográfica o el autor del documento.

### Resultados
- Obtener información geográfica acerca de la localización de un servidor a partir de la IP o nombre de dominio.
- Crear scripts en Puython para  automatizar el proceso de extracción de metadatos de documentos PDF con el módulo `PyPDF2`.
- Crear scrips en Python para automatizar el proceso de extración de metadatos de imágenes con el módulo EXIF.


### Índice

1. Obtener información geográfica acerca de la locaclización de un sercidor.
2. Utilizar el mñodulo PyPDF2 para extraer metadatos de documentos PDF.
3. Extración de metadatos de imágenes con el módulo EXIF.
4. Resumen

---

## 1. Obtener información geográfica acerca de la locaclización de un sercidor.

- Una forma de obtener la geolocalización a partir de una dirección IP o dominio es mediante un servicio que proporciona este tipo de información.

- Entre los servicios que brindan esta información podemos destacart:
    - https://hackertarget.com/geoip-ip-location-lookup/

- Este servicio también proporciona una API REST para obtener una geolocalización de una dirección IP.

    - https://api.hackertarget.com/geoip/?q=8.8.8.8
        ```json
        IP: 8.8.8.8
        Country: United States
        State: N/A
        City: None
        Latitude: 37.751
        Longitude: -97.822
        ```

### Servicio de geolocalización `freegeoip`
- Podríamos obtener la misma información en formato **JSON** con el servicio de `freegeoip` que proporciona una consulta a partir de una dirección IP.

    - https://ipbase.com/

    - https://freegeoip.app/json/8.8.8.8
        ```json
        {
            "ip": "8.8.8.8",
            "country_code": "US",
            "country_name": "United States",
            "region_code": "CA",
            "region_name": "California",
            "city": "Mountain View",
            "zip_code": "94043",
            "time_zone": "America/Los_Angeles",
            "latitude": 37.4056,
            "longitude": -122.0775,
            "metro_code": 807
        }
        ```

- En el siguiente script, estamos utilizando este servicio y el módulo `requests` para obtener una respuesta en formato JSON.

    - [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/2-ip_to_geo.py)

        - Resultado:
            ```json
            {
            "latitude":37.386051177978516,
            "longitude":-122.08384704589844,
            "country":"United States",
            "city":"Mountain View",
            "time_zone":"America/Los_Angeles",
            "ip_address":"8.8.8.8",
            "country_code":"US"
            }
            ```

- En el siguiente script, solicitamos al usuario introducir la dirección ip desde el teclado y devolvemos la geolocalización en formato JSON.

    - [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/3-ip_to_geo_input.py)

        - Resultado:
            ```json
            {
            "ip":"8.8.8.8",
            "country_code":"US",
            "country_name":"United States",
            "region_code":"US-CA",
            "region_name":"California",
            "city":"Mountain View",
            "zip_code":"94035",
            "time_zone":"America/Los_Angeles",
            "latitude":37.386051177978516,
            "longitude":-122.08384704589844,
            "metro_code":0
            }
            ```
    

### Método de geolocalización en Python

- `PyGeoIP` es uno de los módulos disponibles que le permite recuperar información geográfica a partir de una dirección IP.

- Se basa en bases de datos GeoIP, que se distribuyen en varios archivos según su tipo (ciudad, región, país, etc.).

- El módulo contiene varias funciones para recuperar datos, como el código país, la zona horaria o el registro completo de toda la información relacionada con una dirección IP específica.

    - [Repositorio de PyGeoIP](https://github.com/appliedsec/pygeoip)

- Para construir el objeto con el cual realizar las consultas usaremos un constructr que acepta como parámetro un archivo como una base de datos. Estos ficheros se proporcionan de forma adjunta.

    ```python
    import pygeoip
    geolitecity = pygeoip.GeoIp('GeoLiteCity.dat')
    ```

- Este objeto tiene una serie de métodos para obtener información sobre la geolocalización de una dirección IP o un nombre de dominio.

- Para ejemplo, el método region_by_addr() devuelve la región geográfica de una dirección IP en forma de un diccionario.

    ```python
    >>> for key,value in geolitecity.record_by_addr('173.194.34.192').items():
    >>>    print(key + "-->" + str(value))
    ```

    - Resultado:
    ```bash
    dma_code -- >807
    area_code -- >650
    metro_code -- >San Francisco, CA
    postal_code -- >94043
    country_code -- >US
    country_code3 -- >USA
    country_name -- >United States
    continent -- >NA
    region_code -- >CA
    city -- >Mountain View
    latitude -- >37.41919999999999
    longitude -- >-122.0574
    time_zone -- >America/Los_Angeles
    ```

#### Métodos de PyGeoIP

- El siguiente ejemplo implementa una función que acepta como parámetros la dirección IP y el dominio. Realiza la consulta sobre el fichero GeoLiteCity.dat para obtener la información de geolocalización usando los mñetodos `record_by_addr()` y `record_by_name()`.

- Estos métodos nos permiten obtener, en forma de diccionarios, una estructura con datos sobre el país, la ciudad, la latitud y la longitud.

    - [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/4-PyGeoIP_test.py)

    - Instanciamos un objeto de la clase GeoIP con la ruta del archivo que contien la base de datos.
    - A continuación, consultaremos en la base de datos un registro específico, especificando la dirección IP o el nombre de dominio.
    - Esto devuelve un registro que contiene campos para ciudad, nombre_región, código postal, nombre_país, latitud y longitud

    - Posible resultado:
        ```json
        {
        "dma_code":0,
        "area_code":0,
        "metro_code":"None",
        "postal_code":"RH15",
        "country_code":"GB",
        "country_code3":"GBR",
        "country_name":"United Kingdom",
        "continent":"EU",
        "region_code":"P6",
        "city":"Burgess Hill",
        "latitude":50.9667,
        "longitude":-0.13329999999999131,
        "time_zone":"Europe/London"
        }
        ``` 
        
### Geolocalización con la base de datos MaxMind
- La base de datos MaxMind contiene una serie de ficheros con los cuales obtener información geográfica.

- Dicha base de datos se puede descargar desde la página web realizando un registro previo en el servicio de MaxMind.
    - [Sitio web de MaxMind](https://www.maxmind.com/en/home)
    - [BBDD de MaxMind](https://dev.maxmind.com/geoip/geolocate-an-ip/databases/)

- Dentro de los módulos de Pythn podemos encontrar los giuientes que están utilizando la base de datos MaxMind:
    - `geoip2`: proporciona acceso a los servicios web y bases de datos de GepIP2.
        - https://github.com/maxmind/GeoIP2-python
    - `maxminddb-geolite2`: proporciona acceso a la base de datos de MaxMind GeoLite2.
        - https://github.com/rr2do2/maxminddb-geolite2
    - `python-geoip-python3`: proporciona acceso a la base de datos de MaxMind GeoIP2.
        - https://pypi.org/project/python-geoip-python3/

### Geolocalización con `geoip2-python`

- Este módulo proporciona diferentes bases de datos dependiendo de los datos en los que estemos interesados, por ejemplo, para obtener información relativa a ciudad, país, latitud y longitud podríamos usar la base de datos GeoLite2-City.mmdb. qye se encuentra dentro del repositorio de MaxMind.

- Para obtener esta información usamos el método `Reader()` al cual le pasamos por parámetro el nombre de la base de datos
    ```python
    import geoip2.database
    >>> reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    >>> response = reader.city('8.8.8.8')
    >>> print(response)
    ```


### Geolocalización con `maxminddb-geolite2`

- maxminddb-geolite2 es una biblioteca de Python que permite acceder a la base de datos de MaxMind GeoLite2.

- Para instalar la biblioteca se debe ejecutar el siguiente comando:
    ```bash
    pip install maxminddb-geolite2
    ```

- Para usar este módulo necesitamos importar la clase `Geolite2` y crear una instancia utilizando el método `reader()`.

- Posteriormente, utilizamos el método `get()`, pasándole por parámetro la direccion IP.

- La principal ventaja de este módulo con restecto al anterior es que no necesitamos el fichero de base de datos en local para realizar consultas.

    ```python
    >>> from geolite2 import geolite2
    >>> reader = geolite2.reader()
    >>> reader.get('8.8.8.8')
    ```
    - Resultado:
        ```json
        {
        "continent":{
            "code":"NA",
            "geoname_id":6255149,
            "names":{
                "de":"Nordamerika",
                "en":"North America",
                "es":"Norteamérica",
                "fr":"Amérique du Nord",
                "ja":"北アメリカ",
                "pt-BR":"América do Norte",
                "ru":"Северная Америка",
                "zh-CN":"北美洲"
            }
        },
        "country":{
            "geoname_id":6252001,
            "iso_code":"US",
            "names":{
                "de":"USA",
                "en":"United States",
                "es":"Estados Unidos",
                "fr":"États-Unis",
                "ja":"アメリカ合衆国",
                "pt-BR":"Estados Unidos",
                "ru":"США",
                "zh-CN":"美国"
            }
        },
        "location":{
            "accuracy_radius":1000,
            "latitude":37.751,
            "longitude":-97.822
        },
        "registered_country":{
            "geoname_id":6252001,
            "iso_code":"US",
            "names":{
                "de":"USA",
                "en":"United States",
                "es":"Estados Unidos",
                "fr":"États-Unis",
                "ja":"アメリカ合衆国",
                "pt-BR":"Estados Unidos",
                "ru":"США",
                "zh-CN":"美国"
            }
        }
        }
        ```

- [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/5-maxminddb-geolite2_reader.py)

    - Opcional: `python3 script.py --hostname python.org`


### Geolocalización con `python-geoip-python3` y `pip install python-geoip-python3`

- `python-geoip-python3` es una biblioteca de Python que permite acceder a la base de datos de MaxMind GeoIP2.

- Para instalar la biblioteca se debe ejecutar el siguiente comando:
    ```bash
    pip install python-geoip-python3
    pip install python-geoip-geolite2
    ```

- Para usar este módulo necesitamos importar la clase `geolite2` y crear una instancia utilizando el método `lookup()` pasándole por parámetro la dirección IP.

- [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/6-python-geoip-python3.py)


### Obtener información geográfica acerca de la localización de un servidor a partir de la IP o nombre de dominio.

- [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/7-geoip.py)


## 2. Utilizar el mñodulo PyPDF2 para extraer metadatos de documentos PDF.

- Uno de los módulos disponibles en Python para extraer dottos de documentos PDF es `PyPDF2`.

- El módulo se puede descargar directamente con el siguiente comando:
    ```bash
    pip install PyPDF2  
    ```
    - [Documentación oficial](https://pypi.org/project/PyPDF2/)

    ```python
    import PyPDF2 as pdf
    dir(PyPDF2)
    ```

#### Obtención de metadatos con PdfFileReader

- El método que podríamos utilizar para obtener la información de un documento PDF es `getDocumentInfo()`, de devuelve un diccionario con los datos del documento.

- En el siguiente script nos permite obtener la información del documento PDF que se encuentra en la ruta `</document.pdf>`.

    - [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/8-PyPDF2_getDocumentInfo.py)
        
        ``` 
        [+] Metadatos de Unidad_5_Extración_de_metadatos_con_Python/TutorialPython3.pdf
        Metadatos del PDF:
        /Producer: PyFPDF 1.7.2 http://pyfpdf.googlecode.com/
        /Title: Tutorial Python 3
        /Subject: Demo PDF for Metadata Extraction
        /Author: John Doe
        /Creator: FPDF Library
        /CreationDate: D:20241115083959
        ```

#### Extraer información y metadatos XMP de documentos PDF

- Para almacenar los metadatos, los ficheros PDF usan Extensible Metadata Platform (XMP).

- **`XMP`** se crea em `XML`, lo que facilita el intercambio de metadatos entre diversas aplicaciones y la publicación de flujos de trabajo.

- Los metados en la mayoría de los demás formatos (como Exif, GPS o TIFF) se transfieren de manera automática a XMP para facilitar su visualización y gestión.

- En el módulo `pypdf2` proporciona un método `getXmpMetadata()` para obtener otra información relacionada con el documento, como los creadores, el editor y la versión del PDF.

- El siguiente script nos permitiría obtener la información de todos los documentos PDF que se encuentren en la carpeta `pdf`.

    - [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/9-PyPDF2_getXmpMetadata.py)

    - En la función get_metadatos_carpeta_pdf() usamos el método `walk()` dentro del módulo `os` que es útil para recorrer todos los ficheros y directorios que se encuentran en una ruta.

    - Extraemos los metadatos XMP del documento comprobando previamente con el mètodo `hasattr()` para comprobar si una determinada propiedad se encuentra dentro del objeto xmpinfo antes de poder acceder a dicha información.


#### Ejercicio: Obtener los metadatos del documento PDF que se encuentra en la ruta indicada: Unidad_5_Extración_de_metadatos_con_Python/TutorialPython3.pdf

- [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/10-PyPDF2_getXmpMetadata_ejercicio.py)

    ```
    [+] Pages number: 86
    [+] Author: Adobe Developer Technologies
    [+] Creator: FrameMaker 7.2
    [+] Producer: Acrobat Distiller 8.1.0 (Windows)
    [+] Contributor: []
    [+] Identifier: None
    [+] Date: []
    [+] Source: None
    [+] Subject: []
    [+] ModifyDate: 2008-09-16 15:43:43
    [+] MetadataDate: 2008-09-16 15:43:43
    [+] DocumentId: uuid:a2a0d182-7b1c-4801-a22c-d610115116bd
    [+] InstanceId: uuid:1a365cee-e070-4b52-8278-db5e46b20a4c
    [+] PDF-Keywords: XMP metadata  Exif IPTC PSIR  file I/O
    [+] PDF-Version: None
    ```

### Extraer imágenes de un documento PDF

- Para extraer imágenes de un documento PDF tenemos diferentes opciones:
    - Si usamos una distribución basada en `debian` como `ubuntu` podríamos instalar la aplicación `pdfimages` que nos permite extraer imágenes de un documento PDF.
        - https://manpages.ubuntu.com/manpages/focal/man1/pdfimages.1.html

        - Instalación:
            ```bash
            sudo apt install pdfimages
            apt install poppler-utils
            ```

        - `pdfimagens` permite extraer imágenes de documentos PDF en sistemas LINUX/UNIX y guarda imágenes en formatos como PPM, PBM o archivos JPEG.

        - Para cada imagen que detecta en el doccumento crea un fichero con el formato `nnn.xxx` donde `nnn` es el número de la página y `xxx` es el formato de la imagen (.pp,. pbm, jpg, etc.).

        - Para ejecutar la herramienta bastaría con pasarle como argumentos la ruta del PDF y el directorio donde se guardarán las imágenes.

            ```bash
            pdfimages documento.pdf /tmp/images
            ```

        - El siguiente script utiliza el comando anterior con el móduglo subprocess para realizar el proceso.
            - [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/11-PyPDF2_extract_images.py)

    - Otra alternativa es utilizar el módulo `pymupdf` que permite extraer imágenes de documentos PDF.
        - [Repositorio de PyMuPDF](https://github.com/pymupdf/PyMuPDF)
        - [Instalación](https://github.com/pymupdf/PyMuPDF/wiki/Ubuntu-Installation%20Experience)

            ```bash
            sudo apt install python3-pip
            sudo -H pip3 install --upgrade pip
            sudo -H python3 -m pip install -U pymupdf
            ```	
        - La forma de usar este módulo es usando la clase `fitz` que dispone de métodos para abrir el fichero y extrar las imágenes en formato PNG.

            - [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/12-PyMuPDF_extract_images.py)

### Otras herramientas

- `Peepdf` es una herramienta de Python que analiza archivos PDF y nos permite visualizar todos los objetos incrustados en el documento.

- También tiene la capacidad de analizar diferentes versiones de un archivo PDF, secuencias de objetos y archivos cifrados, así como notificar y ofuscar archivos PDF.

- [Documentación oficial](https://eternal-todo.com/tools/peepdf-pdf-analysis-tool)

- Para instalar `peepdf` se debe ejecutar el siguiente comando:
    ```bash
    pip install peepdf
    ``` 

- Para ejecutarlo bastaría con pasarle un parámetro un fichero pdf y nos devolvería toda la información relacionada con firmas hash, tamaño ficheros, encriptación y objetos que tenga el documento al respecto a imágenes y stream de datos.

    - [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/13-peepdf.py)


## 3. Extración de metadatos de imágenes con el módulo EXIF.

### Estracción de metadatos de imágenes

### Extracción de metadatos de imágenes con ExifTool

- Podemos utilizar ExifTool para extraer metadatos de imágenes.

- [Documentación oficial ExifTool](https://exiftool.org/)

- Se trata de una aplicación de código abierto que permite leer, escribir y manipular metadatos de imágenes.

- Se trata de una aplicacion que nos permite **visualizar los metadatos de una gran cantidad de formatos de imágenes** como AWR, ASF, SVG, TIFF, PDF, JPEG, PNG, GIF, etc.

- En cuanto a formatos de metadatos soportados podemos mencionar el EXIF, IPTC, XMP, ICC, etc.

- En caso de una distribuciión basada en `debian`, podriamos intalarla con el siguiente comando:
    ```bash
    sudo apt-get install libimage-exiftool-perl
    ```

- Una vez instalada, para su ejecución se debe pasar como parámetro el nombre del fichero a analizar.
    ```bash
    exiftool imagen.jpg
    ```
    - Resultado:
        ```bash
        ExifTool Version Number         : 12.52
        File Name                       : imagen.jpg
        Directory                       : .
        File Size                       : 1.1 kB
        File Modification Date/Time     : 2023:04:27 14:30:00-03:00
        File Access Date/Time           : 2023:04:27 14:30:00-03:00
        File Inode Change Date/Time     : 2023:04:27 14:30:00-03:00
        File Permissions                : rw-r--r--
        File Type                       : JPEG
        File Type Extension             : jpg
        MIME Type                       : image/jpeg
        JFIF Version                    : 1.01
        X Resolution                    : 300
        Y Resolution                    : 300
        Resolution Unit                 : inches
        Exif Byte Order                 : Little-endian (Intel, II)
        Image Description               : 
        Make                            : Canon
        Model                           : Canon EOS 100D
        Orientation                     : Horizontal (normal)
        XResolution                     : 300
        YResolution                     : 300
        Resolution Unit                 : inches
        Software                        : Adobe Photoshop Lightroom Classic 7.1 (Windows)
        Modify Date                     : 2023:04:27 14:30:00
        YCbCr Positioning               : Centered
        Exposure Time                   : 1/500
        ...
        ```

### Extracción de metadatos con el móduglo `PIL.ExifTags`

- Uno de los principales módulos que encontramos dentro de Python para el procesamiento y manipulación de imágenes es `PIL.ExifTags`.

- `Pil` permite extraer los metadatos de imagenes en formatos EXIF.

- EXIF(Exchangeable Image File Format) es una especificación que indica las reglas que deben seguirse cuando vamos a guardar imágenes.

- Esta especificación es aplcada hoy en día en la mayoría de  dispositivos móviles y cámaras digitales.

- El módulo `PIL.ExifTags` permite extraer la información de estas etiquetas.

- ExifTags contien una estructura de diccionario con constantes y nombres para muchas etiquetas de EXIF conocidas.

    - [Documentación oficial](https://pillow.readthedocs.io/en/latest/reference/ExifTags.html)

- Este módulo proporciona 2 clases principales:
    - `PIL.ExifTags.TAGS`: Permite extraer las etiquetas más comunes almacenadas en las imágenes.
    - `PIL.ExifTags.GPSTAGS`: Permite extraer las etiquetas de GPS almacenadas con información de ubicación.

### Obtener los metadatos de una imagen

- Primero importamos los módulos `PIL.Image` y `PIL.ExifTags`.

- `PIL` es un móduglo de procesamiento de imágenes en Python que soporta diferentes formatos de archivo y tiene un poderosa capacidad de procesamiento de imágenes.

- Para obtener la información EXIF tags de una imagen se puede utilizar el método `_getexif()` del objeto de la imagen.

- Este método nos devuelve un diccionario que podemos recorrer con el método items().

    - [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/14-PIL_getexif.py)


### Obteniendo geolocalización de una imagen

- En el ejemplo anterior, vemos que hemos obtenido también informacion en el objeto GPSInfo acerca de la geolocalización de la imagen.

- Esta información se puede mejorar descodificando la información que hemos obtenido en un formato de valores latitud/longitud, para ellos podemos hacer una función que dado un atributo exif tipo GPSInfo, nos descodifique esa información.

    ```python	
    def decode_gps_info2(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        for key in exif['GPSInfo'].keys():
            decode = GPSTAGS.get(key,key)
            gpsinfo[decode] = exif['GPSInfo'][key]
        print(gpsinfo)
        exif['GPSInfo'] = gpsinfo
    ```

- Otra forma de parsear la información correspondiente a la geolocalización es a través de este método:

    ```python
    def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        '''
        Raw Geo-references
        for key in exif['GPSInfo'].keys():
            decode = GPSTAGS.get(key,key)
            gpsinfo[decode] = exif['GPSInfo'][key]
        exif['GPSInfo'] = gpsinfo
        '''

        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2][0] / float(exif['GPSInfo'][2][2][1])
        Nmin = exif['GPSInfo'][2][1][0] / float(exif['GPSInfo'][2][1][1])
        Ndeg = exif['GPSInfo'][2][0][0] / float(exif['GPSInfo'][2][0][1])
        Wsec = exif['GPSInfo'][4][2][0] / float(exif['GPSInfo'][4][2][1])
        Wmin = exif['GPSInfo'][4][1][0] / float(exif['GPSInfo'][4][1][1])
        Wdeg = exif['GPSInfo'][4][0][0] / float(exif['GPSInfo'][4][0][1])
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}

    ```	

    - Resultado:
        ``` 
        # Output
        [+] Metadata for file: images/image.jpg
        {'GPSVersionID':b'\x00\x00\x02\x02','GPSLatitudeRef': 'N', 'GPSLatitude': ((32, 1), (4, 1), (4349,
        100)), 'GPSLongitudeRef': 'E', 'GPSLongitude': ((131, 1), (28, 1), (328, 100)), 'GPSAltitudeRef: b'\x00',
        'GPSAltitude': (0, 1)}
        Metadata: GPSInfo - Value: {'GPSVersionID': b'\x00\x00\x02\x02', 'GPSLatitudeRef': 'N',
        'GPSLatitude': ((32, 1), (4, 1), (4349, 100)), 'GPSLongitudeRef': 'E', 'GPSLongitude': ((131, 1), (28, 1),
        (328, 100)), 'GPSAltitudeRef': b'\x00', 'GPSAltitude': (0, 1)}
        Metadata: ResolutionUnit - Value: 2
        Metadata: ExifOffset - Value: 146
        Metadata: Make - Value: Canon

        Metadata: Model - Value: Canon EOS-5
        Metadata: Software - Value: Adobe Photoshop CS2 Windows
        Metadata: DateTime - Value: 2008:03:09 22:00:01
        Metadata: Artist - Value: Frank Noort
        Metadata: Copyright - Value: Frank Noort
        Metadata: XResolution - Value: (300, 1)
        Metadata: YResolution - Value: (300, 1)
        Metadata: ExifVersion - Value: b'0220'
        Metadata: ImageUniquelD - Value: 2BF3A9E97BC886678DE12E6EB8835720
        Metadata: DateTimeOriginal - Value: 2002:10:28 11:05:09
        ```


### Ejercicio: Obtener metadatos de todas las imagenes que se encuentren en una carpeta

- [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/15-PIL_getexif_carpeta.py)

```
GPSInfo = {0:b'x00\x00\x02\x02', 1:'N', 2: ((32, 1), (4, 1), (4349, 100)), 3: 'E', 4:
((131, 1), (28, 1), (328, 100)), 5: b'\x00', 6: (0, 1)}
ResolutionUnit = 2
ExifOffset = 146

Make = Canon
Model = Canon EOS-5
Software = Adobe Photoshop CS2 Windows
DateTime = 2008:03:09 22:00:01
Artist = Frank Noort

Copyright = Frank Noort
XResolution = (300, 1)
YResolution = (300, 1)
ExifVersion = b'0220'
ImageUniqueID = 2BF3A9E97BC886678DE12E6EB8835720
DateTimeOriginal = 2002:10:28 11:05:09
```

### Extraer metadatos de imágenes web

- Creamos un script para conectarse a un sitio web, descargar todas las imágenes en el sitio y luego verificar si hay metadatos EXIF:

- Para esta tarea, estamos tulizando el módulo `urllib` que proporciona los paquetes de parse y request.

    - https://docs.python.org/3.0/library/urllib.parse.html
    - https://docs.python.org/3.0/library/urllib.request.html

- [Código de ejemplo](/Unidad_5_Extración_de_metadatos_con_Python/16-PIL_getexif_web.py)

- Ejecución del script:
    ```bash
    python3 16-PIL_getexif_web.py --url https://www.python.org/
    ```

## 4. Resumen

- Extraer información de geolocalización de una dirección IP o dominio con los servicios **hackertarget.com** y **freegeoip**.
- Analizamos los diferentes módulos de geolocalización en Python como **pygeoip**, **geoip2**, **maxminddb-geolite2**, **python-geoip-python3**. Algunos de estos módulos usan la base de datos de **MaxMind** que contiene una serie de ficheros con los cuales obtener información de **geolocalización**.
- Extraer metadatos en documentos PDF con el módulo **PyPDF2**. El módulo **PyPDF2** proporciona la clase **PdfFileReader** y los métodos **getDocumentInfo()**, **getXmpMetadata()** para obtener otra información relacionada con el documento, como los creadores, el editor y la versión en pdf.
- Extraer imágenes de documentos PDF con herramientas como **Pdfimages** y el módulo **pymupdf**.
- Extraer metadatos de imágenes con la herramienta **exiftool** y el módulo de Python **PIL.ExifTags**. La clase **PIL.ExifTags.TAGS** permite extraer la etiquetas más comunes almacenadas en la imagen y **PIL.ExifTags.GPSTAGS** permite extraer las etiquetas relacionadas con información de geolocalización.
- Obtener información sobre geolocalización de imágenes gracias al uso del objeto **GPSInfo**.


### FAQ
- `¿Para qué sirve la herramienta exiftool?`

    ExifTool es un programa de software gratuito y de código abierto para leer, escribir y manipular metadatos de imagen, audio, video y PDF. Es independiente de la plataforma, disponible como una biblioteca Perl y una aplicación de línea de comandos.

### Enlaces de interés
- https://pypi.org/project/PyPDF2/

### Glosario

- `Geolocalización`
    
    Se refiere a la posibilidad de localizar, obtener y mostrar la ubicación de un dispositivo. Es una característica que ha tomado gran relevancia en la web, tanto para dispositivos móviles como también para PCs.
- `Metadatos`

    Metadatos son datos que describen otros datos. El metadato puede ser texto, voz o imagen. El metadato ayuda a clarificar y encontrar datos. Por ejemplo, el metadato podría documentar atributos (nombre, tamaño, tipo de dato, etc), las estructuras de los datos (longitud, columnas, campos, etc), y datos sobre datos (donde está localizado, cómo está asociado, etc.). Un ejemplo de metadato es lo que se guarda en los sistemas de archivo. Para cada archivo informático almacenado se puede llegar a guardar la siguiente información: fecha y hora de creación, fecha y hora de modificación, última vez que fue accedido. Los metadatos se usan para facilitar la gestión de datos, ofreciendo información adicional sobre el contenido.
- `PDF`

    Portable Document Format (Formato de Documento Portable), formato gráfico creado por la empresa Adobe el cual reproduce cualquier tipo de documento en forma digital idéntica, permitiendo así la distribución electrónica de los mismos a través de la red en forma de archivos PDF.




