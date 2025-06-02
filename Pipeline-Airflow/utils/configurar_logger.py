import logging


def configurar_logger(archivo_log):
    '''
    Ayuda a configurar los logs a nivel de INFO para esconder los DEBUG
    ademas se configura el logger Handler para que solo se cree una vez.
    '''
    logger = logging.getLogger()
    if not logger.hasHandlers():# si no hay un loger
        # se crea un logger a nivel de INFO
        logging.basicConfig(
            level=logging.INFO, # nivel de logs, no aparece DEBUG
            format="%(asctime)s - %(levelname)s - %(message)s", # formato
            handlers=[
                logging.StreamHandler(),  # Salida estándar
                logging.FileHandler(archivo_log, mode="a")  # Archivo de logs
            ]
        )
    return logger