<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`STEAM CASE`**</h1>

<p align="center">
<img src="images/Steam-background.jpg"  height=300>
</p>

<hr>  

# ***SISTEMA DE RECOMENDACIÓN DE VIDEOJUEGOS***

El presente caso es mi Proyecto Individual 01 de mi carrera de Data Science para la etapa de LABS de la plataforma educativa HENRY, en el cual implementaré, de forma práctica, sobre un caso real la mayoría de las habilidades obtenidas durante la etapa de aprendizaje del BOOTCAMP.
## DESCRIPCIÓN DEL PROYECTO

En este proyecto debo fungir el rol de Data Scientist de STEAM, la cual es una plataforma multinacional de videojuegos y me solicita que que te encargues de crear un sistema de recomendación de videojuegos para usuarios.
Este objetivo lo logré a través de  de 4 etapas bien definidas, las cuales detallo a continuación:

## 1. ETL - Data Engineer
En esta etapa de Ingeniería de Datos se realizó un proceso de ETL, extracción, transformación y carga de datos, donde se recibieron 3 archivos JSON comprimidos en formato GZ con datos de compra de los videojuegos, la interacción de los usuarios y las evaluaciones de ellos.
Al final de esta etapa, se crea un dataset en formato CSV que servirá en la siguiente etapa y se guardarán en la carpeta: Data2_ETL_out.
#### Notebook Link: https://github.com/jalcantara777/SteamCase/blob/main/1_ETL-Data_xform.ipynb
#### Data Source: https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj

## 2. EDA - Exploratory Data Analysis
En esta etapa de Análisis Exploratorio de Datos se realizó la conversión y completado de los datos, también se verificaron y eliminaron los datos nulos, duplicados, outliers y el formato de los datos para posteriormente realizar un análisis gráfico sobre estos datos depurados. Al igual que en la etapa anterior, al final se crea un dataset en formato CSV que servirá en la siguiente etapa y se guardarán en la carpeta: Data3_EDA_out.
#### Notebook Link: https://github.com/jalcantara777/SteamCase/blob/main/2_EDA.ipynb
#### Data Source: https://github.com/jalcantara777/SteamCase/blob/main/Data2_ETL_out.rar

## 3. ML - Machine Learning
Después de haber realizado eficaz y profesionalmente las etapas anteriores, los datos ya se encuentran preparados para realizar el entrenamiento del modelo establecido, para lo cual se diseñan e implementan las respectivas funciones. Al igual que en la etapa anterior, al final se crea un dataset en formato CSV que servirá eficientemente en la ejecución de la API y se guardarán en la carpeta: Data4_FuncReturn2API.
#### Notebook Link: https://github.com/jalcantara777/SteamCase/blob/main/3_ML_Functions.ipynb
#### Data Source: https://github.com/jalcantara777/SteamCase/blob/main/Data3_EDA_out.rar

## 4. FastAPI - RENDER
Una vez completadas las 3 etapas anteriores, los datos se encuentran optimizados en cuanto a tamaño para que puedan ser consultados sin problemas mediante el framework FastAPI en la web service de RENDER. Para lograr esto, se desarrolló el código principal en el módulo **main.py**. En el cual se encuentran las siguientes funciones:

    def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.

    def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

    def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)

    def UsersWorstDeveloper( año : int ): Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)

    def sentiment_analysis( empresa desarrolladora : str ): Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.

    def recomendacion_usuario( id de usuario ): Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.

#### Main.py Link: https://github.com/jalcantara777/SteamCase/blob/main/main.py
#### Render Link : https://proyecto-3-jflm.onrender.com/docs

## Video
En el siguiente link se encuentra el video que explica tanto el funcionamiento del web service como las 3 etapas anteriores del proyecto en forma resumida.
#### Youtube Link: https://www.youtube.com/channel/UCrR9T1nEFfQpWviNudpueBw

## Requisitos para la ejecución correcta en RENDER

Asegúrate de tener instaladas las siguientes bibliotecas antes de ejecutar el código:

- FastAPI
- pandas
- uvicorn

## Herramientas usadas
- Visual Studio Code: editor de código
- Python: lenguaje de programacion
- GitHub: repositorio del proyecto y fuente para la API
- FastAPI: web framework
- Render: servicio en la nube 
- Winrar: utilitario para comprimir y descomprimir archivos gz y rar

