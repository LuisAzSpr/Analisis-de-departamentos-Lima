import pandas as pd
import numpy as np
import concurrent.futures
from datetime import datetime
from utils.manejador_bucket_gcp import upload_cs_file
from utils.configurar_logger import configurar_logger

logger = configurar_logger("../logs/datawrangling.log")


def comparar_valores(data_real,data_convertida,columnas):
    '''
    Compara los valores reales y los valores imputados para con conjunto de columnas
    sujetas a un error que puede ser:

    1. Error abosoluto ( val>=1 o val=0 ) : Diferencia entre el valor real y valor imputado
    2. Error relativo ( 0 < val < 1 ) : Diferencia entre el valor real y valor imputado sobre el valor total.

    Luego se calculan el porcentaje de valores que coinciden con la tolerancia del error para cada columna.
    '''

    # Filtramos aseguramos que tengan las misma filas que la convertida para poder comparar
    data_real_filtrada = data_real.loc[data_convertida.index,columnas.keys()]

    # tomamos la data convertida y le asociamos el sufijo _imp referen
    data_convertida_col = data_convertida.rename(columns=dict([(col,col+"_imp") for col in columnas.keys()]))

    # concatenamos los datsets
    data_comparacion = pd.concat([data_real_filtrada, data_convertida_col], axis=1)
    coincidencias = []

    # para cada columna y valor de error de tolerancia
    for col,val in columnas.items():

        # eliminamos los nulos para hacer la comparacion
        data_comparacion_col = data_comparacion.query(f"{col}.notna() and {col}_imp.notna()")

        # diferencia entre la columna real y la convertida
        data_comparacion_col[f'{col}_diff'] = np.abs(data_comparacion_col[col] - data_comparacion_col[f'{col}_imp'])

        # el total de elementos comparados
        total = data_comparacion_col.shape[0]

        # el total de elementos que cumplen con el error de tolerancia
        cumplen = 0
        if val<1 and val>0: # es una proporcion (el error es menor que el x% del valor)
            cumplen = data_comparacion_col.query(f'{col}_diff/{col} <= {val}').shape[0]
        elif val>=1 or val==0: # es un valor (el error es igual o menor que el valor)
            cumplen = data_comparacion_col.query(f'{col}_diff <= {val}').shape[0]
        else:
            logger.info('El valor de comparación debe ser un número mayor que 0.')

        # proporcion de los que cumplen con la tolerancia del error
        coincidencias_col = cumplen/total
        coincidencias.append(coincidencias_col)
        logger.info(f"El % de coincidencias para la columna '{col}': {coincidencias_col*100:.2f}% de {total}")

    return data_comparacion,coincidencias


def procesar_en_paralelo(func, items, workers=5):
    """Ejecuta consultas en paralelo usando múltiples hilos.

    Args:
        func: Función a ejecutar (obtener_coordenadas u obtener_precision)
        items: Lista de elementos a procesar
        workers: Número de hilos paralelos
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        resultados = executor.map(func, items)

    return list(resultados)


from datetime import datetime


def guardar_csv_en_gcp(bucket_name, df_format, ruta_local):
    """
    Guarda un DataFrame como archivo CSV localmente y lo sube a un bucket de Google Cloud Storage (GCP).

    Args:
        bucket_name: Nombre del bucket de GCP donde se almacenará el archivo.
        df_format: DataFrame que se desea guardar como CSV.
        ruta_local: Ruta local donde se guardará temporalmente el archivo CSV antes de subirlo.
    """

    # Guardar el DataFrame como CSV en la ruta local especificada
    df_format.to_csv(ruta_local, index=False)

    # Fecha y hora para tener un seguimiento de las transformaciones de los datos
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Construir la ruta destino en el bucket con timestamp
    ruta_folder_bucket = f"data/csv/data-formateada_{timestamp_str}.csv"

    # Subir el archivo local al bucket de GCP
    upload_cs_file(bucket_name, ruta_local, ruta_folder_bucket)

    # Retornar la ruta del archivo en el bucket
    return ruta_folder_bucket
