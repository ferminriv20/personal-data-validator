# 📊 Validador de Datos Personales

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://personal-data-validator-d7bwrgovxgadirhxj5gwcv.streamlit.app/)

 ## 📝 Descripción
Aplicación web desarrollada en ***Streamlit***  para validar  información de datos personales
a partir de archivos de ***Excel***. La app  identifica  los registros inválidos,
genera un resumen con métricas de calidad de los datos y permite la exportación a un archivo de excel con los errores resaltados en rojo
. Su objetivo principal es ***garantizar la precisión de
la información personal*** mediante reglas de validación adaptadas al contexto colombiano.

El proceso de uso es sencillo:

1. Sube tu propio archivo de Excel o utiliza un archivo de muestra incluido para probar la aplicación.

2. Selecciona una o varias columnas para validar.

3. El sistema genera métricas de calidad para los datos seleccionados.

4. Descarga un archivo Excel con los errores resaltados en rojo para una revisión sencilla.


## ⚡ Funcionalidades
- **Vista previa de datos:** Permite visualizar de inmediato las primeras 10  filas del archivo cargado.
- **Validación visual:** Muestra una tabla con las columnas seleccionadas y una casilla de verificación junto a cada registro indicando si la validación fue exitosa.
- **Recuento de errores por columna:**  Presenta una tabla con el nombre de cada columna seleccionada y la cantidad de errores encontrados en cada una.
- **Métricas de calidad de datos:**  Tarjetas resumen con el total de registros, errores, datos validados, porcentaje de calidad y valores nulos.
- **Descarga de resultados:**  Permite descargar un archivo Excel de una sola hoja con los resultados de validación y los errores resaltados.

## **⚙️ Reglas de Validación:**
 
- **Teléfono celular 📱:** Debe tener exactamente 10 dígitos, comenzar con `3` y contener un prefijo válido de operadores móviles colombianos.
 
- **Correo electrónico 📧:**   Se utilizan expresiones regulares, basadas en el formato RFC 5322.
  
- **Número de identificación 🆔:** Debe tener exactamente 10 dígitos y comenzar con `1`

- **Tipo de documento (CC / TI) 🪪:** 
   - Si la persona es mayor de edad (>= 18 años) → Tipo de documento ***CC***.

   - Si la persona es menor de edad (< 18 años) → Tipo de documento ***TI***.

- **Género 🚻:**  Valores aceptados: `M` (Masculino), `F` (Femenino) y `X` (Otro).

- **Fecha de nacimiento 🎂:** Debe ser una fecha válida (formato correcto) y no puede ser futura.

- **Estado civil 💍:** Valores comunes aceptados: `soltero`, `casado`, `divorciado`, `viudo`, `separado`.

- **Nombres y apellidos🧑 :** Solo letras (incluyendo acentos), con una longitud entre 3 y 12 caracteres.

- **Ubicación (Departamento y Ciudad)🌎:** La validación se basa en el archivo `colombia.json`, que contiene los departamentos y
 ciudades de Colombia. Primero, se verifica la validez del departamento  en colombia y luego  se determina si la ciudad pertenece a ese departamento.
  De acuerdo con esta lógica, si el departamento es incorrecto, la ciudad del mismo registro será marcada como error.

## 📂 Archivos del Proyecto

`App.py` → Interfaz principal desarrollada con ***Streamlit***.

`validator.py` → Contiene todas las funciones de validación.

`requirements.txt` → Muestra las dependencias con sus respectivas versiones (`pandas`, `pytest`, `openpyxl`).

`colombia.json` → Conjunto de datos de referencia con departamentos y ciudades de Colombia.


## 🚀 Uso

1. **Instalar los requisitos:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Ejecutar la aplicación:**
   ```bash
   streamlit run App.py
   ```
3. **Abrir en el navegador:**
   La app se abrirá automáticamente o puedes ir a `http://localhost:8501`.
4. **Cargar tu archivo o usa el de ejemplo:**
   - Haz clic en "Browse files" para subir tu archivo Excel, o
   - Marca "Usa un archivo de ejemplo" para probar la aplicación.
5. **Seleccionar columnas y validar**
   - Elige las columnas que deseas validar.
   - Haz clic en "🚀 validar datos" para ver los resultados y métricas.
6. **Descargar los resultados**
   - Haz clic en "Resultados validados" para descargar el archivo Excel validado.


## 👀 Vista Previa de la App

<img width="1324" height="614" alt="image" src="https://github.com/user-attachments/assets/91e1b43a-ef7d-4d03-8d78-f5018670daa0" />


## Limitaciones 
Durante el desarrollo de la aplicación se identificaron varias limitaciones que vale la pena destacar. 
En primer lugar, al tratarse de un validador de datos personales, el acceso a información real puede verse restringido por ***políticas de confidencialidad y protección de datos***,
lo que dificulta realizar pruebas con conjuntos de datos auténticos. Además, el uso exclusivo de archivos en formato Excel, si bien aporta ***practicidad*** por su amplia adopción, 
puede ralentizar el procesamiento de grandes volúmenes de información. En cuanto a las reglas de validación, algunas se mantienen en un nivel básico: por ejemplo, 
la validación de nombres podría fortalecerse para permitir espacios o verificar combinaciones más naturales; de igual forma, podría ampliarse el rango de géneros y 
tipos de documento aceptados. En lo referente a las fechas, una mejora futura sería restringir las edades a un máximo de 120 años. 
Finalmente, en la validación de ubicaciones (departamentos y ciudades), se da prioridad al departamento, ya que, si este no existe, resulta imposible 
determinar con certeza el departamento correspondiente incluso cuando el nombre de la ciudad sea válido.

## 👨‍💻 Autor
Este proyecto fue originalmente desarrollado por ***Fermín Antonio Rivero Sotelo***como parte del curso ***CS50P de Harvard***.
Posteriormente, realicé una adaptación completa al español para integrarlo a mi portafolio personal, con el objetivo de hacerlo accesible a un público hispanohablante y continuar mejorando sus funcionalidades.

Si encuentras alguna observación, deseas brindar retroalimentación o te interesa colaborar en el desarrollo del proyecto, puedes ponerte en contacto conmigo. 

📧 Contact: ferminriverosotelo@gmail.com

🌐 GitHub: @feminriv20

## 🙏 Agradecimientos

-El archivo `colombia.json` utilizado para la validación de departamentos y ciudades fue obtenido del repositorio:
https://github.com/marcovega/colombia-json
