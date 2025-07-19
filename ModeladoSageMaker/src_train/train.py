# train.py
import os
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor

def model_fn(model_dir):
    return joblib.load(os.path.join(model_dir, "model.joblib"))

if __name__ == "__main__":
    # Carga de datos (ejemplo usando CSV locales)
    train_df = pd.read_csv(os.path.join("/opt/ml/input/data/train", "train.csv"))

    X = train_df.drop(columns=["precio"])
    y = train_df["precio"]

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['distrito', 'antiguedad_categoria']),
        ],
        remainder='passthrough'
    )

    modelo = XGBRegressor(tree_method="hist", random_state=42)

    parametros = {
        'n_estimators': [100, 150, 200, 250],
        'max_depth': [8, 10, 12, 14],
        'learning_rate': [0.01, 0.1, 0.2]
    }

    gs = GridSearchCV(
        modelo,
        parametros,
        cv=5,
        scoring='neg_mean_absolute_percentage_error',
        verbose=2,
        n_jobs=-1
    )

    pipeline = Pipeline([
        ('pre', preprocessor),
        ('model', gs)
    ])

    pipeline.fit(X, y)

    joblib.dump(pipeline, os.path.join("/opt/ml/model", "model.joblib"))
