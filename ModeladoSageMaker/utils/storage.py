import boto3
from utils.utils import configurar_logger

s3 = boto3.client('s3')
bucket_name = 'proyecto-analisis-lima'

def listar_archivos_s3(folder_prefix):
    """
    Lista solo los archivos (no carpetas) en un 'folder' dentro de un bucket S3.
    El folder_prefix debe terminar con '/'.
    """
    archivos = []
    paginator = s3.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name, Prefix=folder_prefix)

    for page in pages:
        for obj in page.get('Contents', []):
            key = obj['Key']
            # Ignorar "carpetas" (claves que terminan en '/')
            if not key.endswith('/'):
                archivos.append({
                    'Key': key,
                    'LastModified': obj['LastModified'],
                    'Size': obj['Size']
                })
    return archivos

def upload_to_s3(local_path: str, s3_key: str) -> bool:
    """
    Sube un archivo .pkl ubicado en local_path al bucket S3 bajo la ruta s3_key.
    Ejemplo s3_key: "modelos/pipeline_20250702.pkl"
    """
    try:
        s3.upload_file(local_path, bucket_name, s3_key)
        return True
    except Exception as e:
        return False

def descargar_archivo_s3(s3_key, local_path):
    """
    Descarga un archivo específico desde S3.
    s3_key: la clave completa del objeto en el bucket.
    local_path: ruta local donde guardar el archivo.
    """
    s3.download_file(bucket_name, s3_key, local_path)
    print(f"Archivo descargado: s3://{bucket_name}/{s3_key} → {local_path}")
    return local_path


def crear_folder(timestamp):
    s3 = boto3.client('s3')
    prefix = f'ejecuciones/ejecucion_{timestamp}/'
    
    # Carpetas principales
    folders = [
        '',  # folder raíz de la ejecución
        'data/',
        'modelo/',
        'logs/',
    ]
    
    for folder in folders:
        key = prefix + folder
        s3.put_object(Bucket=bucket_name, Key=key)
    
    return prefix
