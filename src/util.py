import random
import pandas as pd
import numpy as np
import xgboost as xgb
from datetime import datetime
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
from data.queries import data_for_model


# Función para convertir una lista en una tupla
def list_to_tuple(value):
    """
    Función para convertir una lista en una tupla
    
    Args:
        value: Lista o str a convertir en tupla

    Returns:
        Tupla con el valor de entrada
    """
    if isinstance(value, str):
        return (value,)
    elif isinstance(value, list):
        return tuple(value)
    else:
        return ValueError(
            "Tipo de dato no soportado, se esperaba un list o str. {}".format(
                type(value)
            )
        )


def random_color(size):
    """
    Función para generar colores aleatorios en formato hexadecimal
    
    Args:
        size: Cantidad de colores a generar

    Returns:
        Lista de colores en formato hexadecimal
    """
    return ["#%06X" % random.randint(0, 0xFFFFFF) for _ in range(size)]


# Configuración de los botones de la barra de herramientas de Plotly
config_mode_bar_buttons_gestor = {
    "displayModeBar": True,
    "displaylogo": False,
    "scrollZoom": True,
    "modeBarButtonsToRemove": ["zoom2d", "lasso2d", "resetScale2d"],
    "modeBarButtonsToAdd": [
        "drawline",
        "drawcircle",
        "drawrect",
        "eraseshape",
        "toggleSpikelines",
    ],
}


def load_data_for_model():
    """
    Función para cargar los datos del modelo
    
    Returns:
        pd.DataFrame: Datos del modelo
    """
    data = data_for_model()
    df = pd.DataFrame(data)
    
    # Ajustar los tipos de datos de las columnas
    df = df.astype({
        'id': str,
        'anio_nac': int,
        'nacionalidad': str,
        'sexo': str,
        'titulacion': str,
        'nota_def_ebau': float,
        'nota_media': float,
        'abandona': str
    })
    
    return df

def load_model():
    
    model_file = "src/voting_classifier_model_improved.pkl"
    voting_clf = joblib.load(model_file)
    data = load_data_for_model()

    current_year = datetime.now().year
    data['edad_actual'] = current_year - data['anio_nac']

    # Codificar variable objetivo
    data['abandona'] = data['abandona'].map({'si': 1, 'no': 0})

    # Definir columnas
    columnas_categoricas = ['nacionalidad', 'sexo', 'titulacion']
    columnas_numericas = ['nota_def_ebau', 'nota_media', 'edad_actual']

    # Imputación de datos
    num_imputer = SimpleImputer(strategy='mean')
    cat_imputer = SimpleImputer(strategy='constant', fill_value='Desconocido')

    # Preprocesamiento
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', Pipeline([('imputer', num_imputer), ('scaler', StandardScaler())]), columnas_numericas),
            ('cat', Pipeline([('imputer', cat_imputer), ('encoder', OneHotEncoder(handle_unknown='ignore'))]), columnas_categoricas)
        ]
    )

    # Dividir datos en características y variable objetivo
    X = data[columnas_categoricas + columnas_numericas]
    y = data['abandona']
    ids = data['id']

    # Filtrar los estudiantes que no han abandonado aún
    X_non_abandon = X[y == 0]
    data_non_abandon = data[y == 0].copy()  # Mantener una copia de los datos originales

    # Aplicar preprocesamiento
    X_non_abandon_preprocessed = preprocessor.fit_transform(X_non_abandon)

    # Feature engineering: polynomial features
    poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
    X_non_abandon_poly = poly.fit_transform(X_non_abandon_preprocessed)

    # Predecir probabilidades de abandono
    probabilidades_abandono = voting_clf.predict_proba(X_non_abandon_poly)[:, 1]

    # Añadir las probabilidades al DataFrame original de los estudiantes que no han abandonado
    data_non_abandon['probabilidad_abandono'] = probabilidades_abandono

    return data_non_abandon