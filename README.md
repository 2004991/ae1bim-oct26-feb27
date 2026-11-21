
# Sistema de Gestión de Clínicas Veterinarias

## Actividad B1 - Desarrollo de Plataformas Web

**Universidad:** Universidad Técnica Particular de Loja (UTPL)  
**Carrera:** Ingeniería en Tecnologías de la Información  
**Estudiante:** Dixon Delgado

## 1. Descripción del proyecto

El presente proyecto consiste en desarrollar una base de datos
para administrar una red de clínicas veterinarias ubicadas en
diferentes ciudades.

El sistema permite registrar clínicas, consultorios,
veterinarios e historias clínicas de las mascotas atendidas.

Para su desarrollo se utilizó Python, SQLite y el ORM
SQLAlchemy, permitiendo gestionar los datos mediante
clases y objetos de Python.

## 2. Tecnologías utilizadas

- Python 3.14.2
- SQLite
- SQLAlchemy 2.1.9
- Visual Studio Code
- Git y GitHub

## 3. Entidades de la base de datos

### Clínica
Almacena el identificador, nombre comercial, dirección
y veterinario responsable.

### Consultorio
Registra el identificador, nombre, especialidad y clínica
a la que pertenece.

### Veterinario
Almacena nombres, apellidos, correo electrónico,
licencia profesional y consultorio asignado.

### Historia Clínica
Registra la fecha de atención, mascota, diagnóstico,
tratamiento y veterinario responsable.

## 4. Relaciones entre entidades

- Una clínica puede tener varios consultorios.
- Cada consultorio pertenece a una sola clínica.
- Un consultorio puede tener varios veterinarios.
- Cada veterinario pertenece a un solo consultorio.
- Un veterinario puede registrar varias historias clínicas.
- Cada historia clínica pertenece a un veterinario.

## 5. Archivos principales

- configuracion.py: configura la conexión con SQLite.
- crear_base_entidades.py: define las cuatro entidades.
- poblar_base.py: registra información en la base de datos.
- consulta_all.py: muestra las clínicas y sus historias.
- consulta_filter.py: filtra historias por diagnóstico.
- consulta_order_by.py: ordena historias por fecha.
- consulta_or.py: aplica condiciones mediante OR.
- consulta_and.py: aplica condiciones mediante AND.

## 6. Instalación y ejecución

Clonar el repositorio:

git clone https://github.com/2004991/ae1bim-oct26-feb27.git

Ingresar al directorio:

cd ae1bim-oct26-feb27

Instalar SQLAlchemy:

python -m pip install SQLAlchemy

Crear las tablas:

python crear_base_entidades.py

Ingresar los registros:

python poblar_base.py

Ejecutar las consultas:

python consulta_all.py
python consulta_filter.py
python consulta_order_by.py
python consulta_or.py
python consulta_and.py

## 7. Resultados de las pruebas locales

Se verificaron los siguientes registros:

- 3 clínicas veterinarias.
- 6 consultorios.
- 6 veterinarios.
- 12 historias clínicas.

Resultados de las consultas:

- all(): 4 historias clínicas por cada clínica.
- filter(): 1 historia con diagnóstico Gastritis.
- order_by(): 12 historias ordenadas por fecha.
- or_(): 2 historias con Gastritis o Dermatitis.
- and_(): 1 historia con Gastritis y fecha 2026-10-01.

## 8. Conclusión

Mediante esta actividad se logró implementar una base de datos
relacional utilizando Python, SQLite y SQLAlchemy.

El desarrollo permitió comprender la creación de entidades,
las relaciones mediante claves foráneas, el registro de
información y la ejecución de consultas.

Además, se comprobó que el uso de un ORM facilita el trabajo
con bases de datos, ya que permite realizar operaciones
utilizando objetos de Python.
