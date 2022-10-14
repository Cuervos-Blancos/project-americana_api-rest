## Indice de contenido
- [1. Introducción al proyecto](#1-introducción-al-proyecto)
- [2. Configuración de desarrollo](#2-configuración-de-desarrollo)
	- [2.1 Instalación de Python y Pip](#21-instalación-de-python-y-pip)
		- [2.1.1 Creación de entorno virtual e instalación de dependencias](#211-creación-de-entorno-virtual-e-instalación-de-dependencias)
	- [2.2 Configuración de variables de entorno](#22-configuración-de-variables-de-entorno)
- [3. Revision de rutas](#3-revision-de-rutas)
	- [3.1 Ruta alumnos](#31-ruta-alumnos)
	- [3.2 Ruta CxC](#32-ruta-cxc)
- [4. Notas](#4-notas)
- [Links de utilidad](#links-de-utilidad)
	- [Base de datos](#base-de-datos)
	- [Flask](#flask)
	- [Firebird](#firebird)
- [Commits](#commits)

# 1. Introducción al proyecto
Esta es la primera parte de tres de un proyecto general para la consulta y automatización de generación de correos electrónicos para la escuela americana. 

Siendo la segunda parte una aplicación de CLI mediante la cual se hará la creación y envío automático de correos electrónicos y siendo la tercera parte el desarrollo de una aplicación móvil.

Este modulo se centra en la obtención de datos de una base de datos en Firebird v1.5. Funcionando como una API REST para el consumo de los dos módulos adicionales.

# 2. Configuración de desarrollo
Una vez clonado el repositorio mediante :
> ``` git clone https://github.com/Cuervos-Blancos/project-americana_api-rest ```

## 2.1 Instalación de Python y Pip
Tenemos que comprobar si tenemos el entorno correcto, el proyecto funciona con [python 3.9🔗](https://www.python.org/downloads/).

Si deseamos saber que version de python tenemos instalada, podemos hacerlo mediante el comando:
> `` python --version ``

De igual manera es util tener una version actualizada de `pip`. En este proyecto se una pip 22.
Se puede comprobar la version de pip instalada mediante el comando: 
> ``` pip --version ```

Una vez que se ha clonado el repositorio y se ha revisado que se tiene una version reciente de python. Es de utilidad  revisar la integridad de la base de datos, es bastante probable que la base de datos se encuentre corrupta o dañada, para ello vaya a la sección [utilidad🔗](#links-de-utilidad) y revise el enlace que se refiere a la integridad de la base de datos.

### 2.1.1 Creación de entorno virtual e instalación de dependencias
Para evitar el conflicto entre distintos proyectos de python y distintas versiones en los módulos, es menester la creación de un entorno virtual.

Para ello, abrirá una consola de comandos en la carpeta raíz del proyecto.
Desde ahora se asumirá que se esta en un entorno ***Windows***, no obstante, si se en otro entorno, siempre puede [buscar la equivalencia de comandos🔗](https://www.google.com).

El primer paso es instalar el modulo que permite crear entornos virtuales, esto mediante el comando:
`pip install virtualenv`

Se puede comprobar si se instalo correctamente utilizando el comando 
`virtualenv --version`

En el cmd, ubicado en la carpeta raiz del proyecto usara el comando:
> `virtualenv env`

Esto creara un entorno virtual en la carpeta ``env`` (Puede personalizar el nombre de la carpeta modificando el comando).

Creando el siguiente árbol de carpetas:
```
root
 |
 |- env
 |- src
 |   |- app
 |   |- modules
 |   |- __main__.py
 |   |- requirements.txt
```
Si la creó correctamente el entorno virtual, lo activaremos mediante el siguiente comando:
> ` ./env/scripts/activate `

Y deberá notar que ahora su linea de comandos tiene el prefijo `(env)`

Ahora, instale las dependencias, para ello nos moveremos a la carpeta `src` mediante `` cd .\src `` y usaremos el comando:
>`` pip install -r requirements.txt ``

Y se deberán instalar todos los módulos correctamente.


## 2.2 Configuración de variables de entorno
Para este proyecto necesitamos instanciar cinco variables de entorno:
- ENV
- HOST
- DATABASE
- USER
- PASSWORD

Existen dos forma de hacerlo, desde *powershell* y desde *cmd*.

Ejemplificando desde powershell:

*Establecer*
```powershell
$env:ENTORNO='development'
```

*Ver*
```powershell
$env:ENTORNO
```

En este caso tenemos instalado el modulo [python-dotenv 0.21.0🔗](https://pypi.org/project/python-dotenv/). Asi que tendremos que crear un archivo `.env` a la altura de las carpetas `src` y `env`. Lo cual nos dejara el siguiente árbol de directorios:
```
root
 |- env
 |- src
 |- .env
```
En el archivo `.env` necesitamos instanciar las variables mencionadas anteriormente, para ello, podemos usar el siguiente formato, pero personalizado con sus datos(*Es importante que se mantengan los mismo nombres y las mayúsculas*):
``` dotenv
ENV=development
HOST=localhost
DATABASE=C:\databases\DATOS.GDB
USER=admin
PASSWORD=admin
```

# 3. Revision de rutas
Actualmente la API cuenta unicamente con dos rutas. Para verificar que estén funcionando primero iniciaremos la aplicación mediante el comando:
>` python __main__.py `

*Asumiendo que se encuentre en `root\src`*

Y deberá recibir un mensaje de [*Flask*🔗](https://flask-es.readthedocs.io/installation/) verificando que la aplicación de inicio de manera correcta.

Para revisar las rutas, puede hacerlo desde el navegador o mediante un cliente como [insomnia🔗](https://insomnia.rest/) el cual es que se utilizo en la realización de este proyecto.

## 3.1 Ruta alumnos
La primera ruta es `` http://localhost:5000/api/alumnosprepa ``.

Al realizar una petición *GET* deberá recibir datos como los siguientes:
```json
[
	{
		"EMAIL": "",
		"GRADO": 4,
		"MATERNO": "PEÑA",
		"MATRICULA": "000000",
		"NIVEL": "PREPA",
		"NOMBRE": "MARIA FERNANDA",
		"NUMEROALUMNO": 9999,
		"PATERNO": "VARGAS"
	},
	{
		"EMAIL": "",
		"GRADO": 4,
		"MATERNO": "RAMIREZ",
		"MATRICULA": "00000000",
		"NIVEL": "PREPA",
		"NOMBRE": "VIVIAN CITLALI",
		"NUMEROALUMNO": 9999,
		"PATERNO": "LOPEZ"
	},
	{
		"EMAIL": "",
		"GRADO": 4,
		"MATERNO": "SALMERON",
		"MATRICULA": "0000000",
		"NIVEL": "PREPA",
		"NOMBRE": "HECTOR JESÚS",
		"NUMEROALUMNO": 9999,
		"PATERNO": "VILLANUEVA"
	},
	{
		"EMAIL": "",
		"GRADO": 4,
		"MATERNO": "MEZA",
		"MATRICULA": "0000000",
		"NIVEL": "PREPA",
		"NOMBRE": "MALU",
		"NUMEROALUMNO": 9999,
		"PATERNO": "ZARATE"
	}
]
```

## 3.2 Ruta CxC
La segunda ruta es `` http://localhost:5000/api/cxc ``
en donde deberá recibir datos como los siguientes:

```json
[
	{
		"ANIO": 2010,
		"CANTIDADPROGRAMADA": 1335.0,
		"EMAIL": "",
		"FECHA_SP1": null,
		"FECHA_SP2": null,
		"FINAL": 2010,
		"GRADO": 5,
		"INICIAL": 2009,
		"MATERNO": "MORENO",
		"MATRICULA": "080901764",
		"MES": 10,
		"NIVEL": "PREPA",
		"NOMBRE": "DAVID",
		"NUMEROALUMNO": 9999,
		"PATERNO": "JIMENEZ",
		"PERIODO": 2,
		"REFERENCIA": null,
		"REFERENCIA2": null,
		"REFERENCIA3": null
	},
	{
		"ANIO": 2009,
		"CANTIDADPROGRAMADA": 1000.0,
		"EMAIL": "",
		"FECHA_SP1": "Mon, 01 Jun 2009 00:00:00 GMT",
		"FECHA_SP2": "Tue, 09 Jun 2009 00:00:00 GMT",
		"FINAL": 2010,
		"GRADO": 1,
		"INICIAL": 2009,
		"MATERNO": "DDD",
		"MATRICULA": "080912345",
		"MES": 10,
		"NIVEL": "PREPA",
		"NOMBRE": "DDD",
		"NUMEROALUMNO": 9999,
		"PATERNO": "DDD",
		"PERIODO": 2,
		"REFERENCIA": null,
		"REFERENCIA2": null,
		"REFERENCIA3": null
	}
]
```

# 4. Notas
Si desea saber que problemas existe o las futuras rutas puede ir al archivo [issues](isues.txt)

Si desea hacer un commit, tome en cuenta que usamos la metodología de [conventional commits🔗](https://www.conventionalcommits.org/en/v1.0.0/)

# Links de utilidad

## Base de datos
Errores de consistencia en la base de datos o base de datos corrupta [🔗](https://ib-aid.com/en/articles/internal-gds-software-consistency-check/)

Link a la base de datos en drive [PENDIENTE DE SUBIR🔗]()

## Flask
Documentación de Flask [🔗](https://flask-es.readthedocs.io/installation/)

Que hace el modo DEBUG en Flask [🔗](https://www.educba.com/flask-debug-mode/)


## Firebird
Documentación del Driver *pyfirebirdsql* [🔗](https://pyfirebirdsql.readthedocs.io/en/latest/tutorial.html)

Documentación de Firebird [🔗](https://firebirdsql.org/en/firebird-rdbms/)

Link de Firebird 1.5 [🔗](https://firebirdsql.org/en/firebird-1-5/)

# Commits
Documentación conventional commits [🔗](https://www.conventionalcommits.org/en/v1.0.0/)

Video explicativo en YT [🔗](https://youtu.be/Cp_SHttVTi0)

FreeCodeCamp ConventionalCommits [🔗](https://www.freecodecamp.org/espanol/news/como-escribir-un-buen-mensaje-de-commit/)