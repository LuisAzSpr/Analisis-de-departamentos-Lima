# Analisis-de-departamentos-Lima

**Autor : Luis Angel Azaña Vega**

-> Report en Looker Studio : 
**https://goo.su/UeE4rZT**

## Problematica

En los últimos años, el acceso a una vivienda en alquiler a un precio justo se ha vuelto una tarea cada vez más difícil para los ciudadanos de Lima, sobre todo en distritos céntricos. A pesar de los ingresos medios de la población, que rondan los 2,000 nuevos soles mensuales, los precios de alquiler presentan una tendencia inflacionaria, especialmente en distritos de clase alta. Esta situación se ve agravada por la desinformación de muchos jóvenes limeños, quienes suelen subestimar el costo real de alquilar un departamento en zonas céntricas y de alta demanda. Esta combinación de ingresos limitados, alzas sostenidas en los precios y desconocimiento del mercado implica que una gran parte de la población enfrente una toma de decisión compleja, entre optar por distritos periféricos o destinar una proporción desproporcionada de sus ingresos al alquiler, comprometiendo así su estabilidad económica.

## Objetivo

El presente proyecto tiene como objetivo principal analizar el mercado de departamentos en alquiler en Lima, con el propósito de proporcionar información clara, visual e interpretativa que permita al ciudadano comprender qué factores influyen en el precio. Mediante un reporte interactivo en Looker Studio, se busca facilitar la comparación entre zonas y distritos, evaluar la relación entre las características del inmueble (como área, número de dormitorios, baños y ubicación) y el costo del alquiler. Esta herramienta tiene como fin apoyar a los usuarios en la toma de decisiones informadas.


## Proceso

El proyecto consta de 3 etapas principales :

1. Extracción de datos : Se realizó un bot de web scraping para poder extraer datos de las principales páginas web y se creó su respectiva imagen Docker para poder ejecutarlo de manera paralela, controlable y en segundo plano en una maquina local evitando bloqueos de IP.

2. Transformación de datos : Se usó python para todo la transformacion de datos que consta de un formateo de datos, un analisis exploratorio y una limpieza de datos.

3. Construcción del pipeline ETL : Se usó apache airflow integrado con gcp en donde se extrajeron los datos en formato .json de un bucket de gcs, para luego realizar la transformación de datos y por último cargarlos en un dataset de bigquery.

4. Explotación de datos : A partir de los datos limpios en bigquery se realizara su explotación de datos mediante 3 enfoques complementarios.

    4.1. Un reporte interactivo en looker studio con el objetivo de facilitar la comprensión de como varia el precio de alquiler segun las caracteristicas de departamentos, zonas y distritos.

    4.2. Un modelo de regresión con una técnica de Stacking para la implementación de un modelo predictivo robusto del precio de alquiler, combinando múltiples algoritmos base (como regresión lineal, random forest, knn, xgboost) con el fin de mejorar la capacidad de generalización y reducir el error de predicción.

    4.3. Aplicación de pruebas de hipótesis como ANOVA y t-Student, con el objetivo de validar patrones observados durante el EDA. Se evaluarán diferencias significativas en los precios de alquiler entre distintas categorías de distritos y dentro de una misma categoría, se analizarán correlaciones entre variables cuantitativas como precio, antiguedad y área, se explorará el efecto de variables como el número de dormitorios y baños sobre el precio, manteniendo el area constante.


![alt text](pipeline.PNG)

