# Analisis-de-departamentos-Lima

**Autor : Luis Angel Azaña Vega**


-> Report en Looker Studio : 
**https://goo.su/UeE4rZT**

Un análisis de los departamentos en alquiler en Lima de Febrero y Marzo.

El proyecto consta de 3 etapas principales :

1. Extracción de datos : Se realizó un bot de web scraping para poder extraer datos de las principales páginas web y se creó su respectiva imagen Docker para poder ejecutarlo de manera paralela, controlable y en segundo plano en una maquina local evitando bloqueos de IP.

2. Transformación de datos : Se usó python para todo la transformacion de datos que consta de un formateo de datos, un analisis exploratorio y una limpieza de datos.

3. Construcción del pipeline ETL : Se usó apache airflow integrado con gcp en donde se extrajeron los datos en formato .json de un bucket de gcs, para luego realizar la transformación de datos y por último cargarlos en un dataset de bigquery.

4. Explotación de datos : A partir de los datos limpios en bigquery se realizara su explotación de datos mediante 3 enfoques complementarios.

    4.1. Un reporte interactivo en looker studio con el objetivo de facilitar la comprensión de como varia el precio de alquiler segun las caracteristicas de departamentos, zonas y distritos.

    4.2. Un modelo de regresión con una técnica de Stacking para la implementación de un modelo predictivo robusto del precio de alquiler, combinando múltiples algoritmos base (como regresión lineal, random forest, knn, xgboost) con el fin de mejorar la capacidad de generalización y reducir el error de predicción.

    4.3. Aplicación de pruebas de hipótesis como ANOVA y t-Student, con el objetivo de validar patrones observados durante el EDA. Se evaluarán diferencias significativas en los precios de alquiler entre distintas categorías de distritos y dentro de una misma categoría, se analizarán correlaciones entre variables cuantitativas como precio, antiguedad y área, se explorará el efecto de variables como el número de dormitorios y baños sobre el precio, manteniendo el area constante.


![alt text](pipeline.PNG)

