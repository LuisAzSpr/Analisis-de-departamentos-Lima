import os
import io
import joblib
import pandas as pd
import numpy as np

def model_fn(model_dir):
    """Carga el modelo entrenado desde el directorio proporcionado por SageMaker."""
    model_path = os.path.join(model_dir, "model.joblib")
    return joblib.load(model_path)

def input_fn(request_body, content_type="text/csv"):
    """Convierte la entrada del request en un DataFrame."""
    if content_type == "text/csv":
        return pd.read_csv(io.StringIO(request_body))  # 👈 cambio aquí
    else:
        raise ValueError(f"Unsupported content type: {content_type}")

def predict_fn(input_data, model):
    """Usa el modelo cargado para hacer predicciones."""
    preds = model.predict(input_data)
    return preds

def output_fn(prediction, accept="text/csv"):
    """Devuelve la predicción en el formato adecuado."""
    if accept == "text/csv":
        return ",".join(map(str, prediction.tolist()))
    else:
        raise ValueError(f"Unsupported accept type: {accept}")
