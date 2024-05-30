# README

## Autores
* Daniel Alzate Arias
* Luis Miguel Giraldo

# ¿Para qué sirve?

Este código proporciona una herramienta para calcular la nómina de los empleados de una empresa en función de una serie de parámetros, como el salario básico, los días laborables, los días de licencia médica, las horas extras, entre otros. Al proporcionar estos datos, el programa calcula tanto los valores devengados como los valores deducidos de la nómina de cada empleado. Los valores devengados incluyen el salario base, el subsidio de transporte (si corresponde), y los pagos por horas extras, mientras que los valores deducidos abarcan las contribuciones a la seguridad social, el fondo de pensiones y las retenciones salariales.

Además de realizar cálculos básicos de nómina, el código también implementa una serie de validaciones para asegurarse de que los parámetros ingresados sean coherentes y cumplan con ciertas reglas establecidas, como por ejemplo, que el salario base sea mayor que el salario mínimo legal, que el porcentaje de seguro de salud no sea cero, y que el porcentaje de fondo de pensiones se ajuste según el rango salarial del empleado. Estas validaciones garantizan la integridad de los cálculos y ayudan a prevenir errores comunes en el procesamiento de la nómina.

# Propósito

Este código proporciona una herramienta completa y robusta para gestionar eficientemente la nómina de los empleados de una empresa, automatizando cálculos precisos y asegurando el cumplimiento de las regulaciones laborales pertinentes.

# Prerrequisitos

* **Instalación de Python**: "Python" es el lenguaje de programación utilizado en este programa, por lo que la persona que desee ejecutarlo deberá tener Python instalado en su sistema. Puede descargar Python desde el sitio web oficial de Python ([Instalador de Python](https://www.python.org/)) e instalarlo siguiendo las instrucciones proporcionadas.

* **Instalación de la libreria kivy**: Es un framework de código abierto en Python para desarrollar aplicaciones multitáctiles. Se utiliza principalmente para crear aplicaciones con interfaces de usuario (UI) atractivas y dinámicas que pueden funcionar en varias plataformas, incluyendo Windows, macOS, Linux, iOS y Android.

La instalación se puede llevar a cabo mediante el siguiente código en la terminal: `pip install kivy`

* **Instalacion de la extensión kivymd**: Esta es una extensión de Kivy que proporciona una implementación de los principios de Material Design de Google para el framework Kivy. Material Design es un sistema de diseño desarrollado por Google que se centra en la usabilidad y la estética, proporcionando una guía visual coherente para el diseño de interfaces de usuario.

La instalación se puede llevar a cabo mediante el siguiente código en la terminal: `pip install kivymd `

* **Datos de entrada relevantes**: Al ejecutar el programa se necesitará tener acceso a los datos necesarios para proporcionar los parámetros requeridos por el programa, como el salario básico, los días laborables, los días de licencia médica, entre otros.

* **Instalación de psycopg2**: Esa es una librería de Python que proporciona una interfaz para interactuar con bases de datos PostgreSQL.
La instalación se puede llevar a cabo mediante el siguiente código en la terminal:  `pip install psycopg2` 

# ¿Cómo está hecho?

El proyecto presenta una arquitectura modular y bien estructurada, diseñada para calcular la nómina de los empleados de una empresa de manera eficiente y precisa. El programa cuenta con 6 archivos, los cuales son:

1. MonthlyPaymentLogic.py
2. MonthlyPaymentTest.py
3. ExtraordinaryCasesTest.py
4. ErrorCaseTest.py
5. Console.py
6. interfaz.py
7. Controladortablas.py
8. TablesEmployer.py
9. securitydb.py
10. DatabaseTest.py
11. consoledb.py

La estructuras por carpetas es la siguiente

1. **sql**: 
   - Contiene scripts SQL para las operaciones de base de datos.

2. **src**:
   - **MonthlyPaymentLogic.py**: Contiene la lógica principal del cálculo de la nómina.
   - **Console.py**: Interfaz de consola para interactuar con el programa.
   - **interfaz.py**: Interfaz gráfica del usuario.
   - **Controladortablas.py**: Controladores de las tablas.
   - **TablesEmployer.py**: Definición de las tablas del empleador.
   - **securitydb.py**: Manejo de la seguridad de la base de datos.
   - **consoledb.py**: Interfaz de consola para la base de datos.

3. **test**:
   - **MonthlyPaymentTest.py**: Pruebas unitarias para casos normales.
   - **ExtraordinaryCasesTest.py**: Pruebas unitarias para casos extraordinarios.
   - **ErrorCaseTest.py**: Pruebas unitarias para casos de error.
   - **DatabaseTest.py**: Pruebas unitarias para la base de datos.

4. **.gitignore**: Archivos y carpetas a ignorar por Git.
5. **LICENSE**: Licencia MIT del proyecto.
6. **README.md**: Documentación del proyecto, explicación del propósito, instalación y ejecución.


El código utiliza la libreria estándar de Python, `math`, que proporciona funciones matemáticas básicas, como la función `trunc()` utilizada para truncar valores decimales. Esta biblioteca es fundamental para realizar cálculos precisos dentro del programa, como calcular porcentajes o redondear valores según sea necesario.

El código hace uso de la libreria `unittest`, que es un marco de pruebas unitarias integrado en Python. Las pruebas unitarias son esenciales para verificar la corrección del código y garantizar su funcionamiento esperado a medida que se realizan cambios o actualizaciones en el proyecto.

Además el código hace uso de la libreria `pytest` que es una librería de pruebas para Python que permite escribir pruebas simples y escalables.



# Estructura sugerida:

* Carpeta MonthlyPayment: Carpeta en la cual se guarda la lógica del proyecto.
* Carpeta test: Carpeta en la cual se guardan las pruebas unitarias.
* Carpeta console: Carpeta en la cual estará la interfaz de consola con la cual el usuario podrá manejar el código sin ver el código fuente.
* Carpeta GUI: Carpeta en la cual estará la interfaz gráfica, la cual proporcionará una mayor comodidad para el usuario.

# Como ejecutar la interfaz gráfica

1) Dirijase a la pantalla de escritorio y en ese lugar cree una carpeta con el nombre: <Calculadora_de_nomina>

2) Ahora copia  `git clone https://github.com/Tmurillo23/Liquidador_para_nomina.git`

3) Ahora en la terminal copia  `cd Calculadora_de_nomina`

4) ahora copia el siguiente codigo en la terminal `python ./Liquidador_para_nomina/src/Gui/Interfaz.py`

# Como ejecutar las pruebas unitarias
1) Dirijase a la pantalla de escritorio y en ese lugar cree una carpeta con el nombre: <Calculadora_de_nomina>

2) Ahora copia  `git clone https://github.com/Tmurillo23/Liquidador_para_nomina.git`

3) Ahora en la terminal copia  `cd Calculadora_de_nomina`

Dependiendo del caso de prueba se copia lo siguiente:
4) Casos normales: ahora copia el siguiente codigo en la terminal `python ./Liquidador_para_nomina/test/MonthlyPaymentTest.py`

5) Casos extraordinarios: ahora copia el siguiente codigo en la terminal `python ./Liquidador_para_nomina/test/ExtraordinaryCasesTest.py`

6) Casos de error: ahora copia el siguiente codigo en la terminal `python ./Liquidador_para_nomina/src/test/ErrorCaseTest.py`

# Como ejecutar la interfaz por consola

1) Dirijase a la pantalla de escritorio y en ese lugar cree una carpeta con el nombre: <Calculadora_de_nomina>

2) Ahora copia  `git clone https://github.com/Tmurillo23/Liquidador_para_nomina.git`

3) Ahora en la terminal copia  `cd Calculadora_de_nomina`

4) ahora copia el siguiente codigo en la terminal `python ./Liquidador_para_nomina/src/Console/Console.py`

# Como ejecutar la pruebas de la base de datos

1) Dirijase a la pantalla de escritorio y en ese lugar cree una carpeta con el nombre: <Calculadora_de_nomina>

2) Ahora copia  `git clone https://github.com/Tmurillo23/Liquidador_para_nomina.git`

3) Ahora en la terminal copia  `cd Calculadora_de_nomina`

4) Para poder ejecutar las pruebas se debe modificar el archivo `securitydb.py que se encuentra en ./Liquidador_para_nomina/src/Model/securitydb.py ` Este archivo debe
ser modificado usando un procesador de texto por consola como nano o usando el comando `notepad ./Liquidador_para_nomina/src/Model/securitydb.py `
En este archivo debe ingresar los datos de conexión a su base de datos.
5) ahora copia el siguiente codigo en la terminal `python ./Liquidador_para_nomina/src/test/DatabaseTest.py`

# Como ejecutar la interfaz por consola de la base de datos

1) Dirijase a la pantalla de escritorio y en ese lugar cree una carpeta con el nombre: <Calculadora_de_nomina>

2) Ahora copia  `git clone https://github.com/Tmurillo23/Liquidador_para_nomina.git`

3) Ahora en la terminal copia  `cd Calculadora_de_nomina`

4) Para poder ejecutar la interfaz se debe modificar el archivo `securitydb.py que se encuentra en ./Liquidador_para_nomina/src/Model/securitydb.py ` Este archivo debe
ser modificado usando un procesador de texto por consola como nano o usando el comando `notepad ./Liquidador_para_nomina/src/Model/securitydb.py `
En este archivo debe ingresar los datos de conexión a su base de datos.

5) ahora copia el siguiente codigo en la terminal `python ./Liquidador_para_nomina/src/view/consoledb.py`
