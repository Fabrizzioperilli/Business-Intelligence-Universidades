#
# @file util.py
# @brief Este archivo contiene funciones de utilidad para la aplicación.
# @details Se definen funciones para convertir listas en tuplas, generar colores aleatorios y cargar datos y modelos.
# @version 1.0
# @date 13/06/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

import random
import pandas as pd
import joblib
from datetime import datetime
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from data.queries import data_for_model

def list_to_tuple(value):
    """
    Convierte una lista en una tupla.
    Args:
        value: Lista a convertir.
    Returns:
        Tupla con los elementos de la lista.
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
    Genera una lista de colores aleatorios en formato hexadecimal.
    
    Args:
        size: Número de colores a generar.
    Returns:
        Lista de colores aleatorios.
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
    Carga los datos necesarios para entrenar el modelo.
    
    Returns:
        pd.DataFrame: Datos para entrenar el modelo.
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
        'nota_def_acceso': float,
        'nota_media': float,
        'abandona': str
    })
    
    return df


def load_model():
    """
    Carga el modelo entrenado.

    Returns:
        Modelo entrenado.
    """
    model_file = "src/trained_model.pkl"
    voting_clf = joblib.load(model_file)
    data = load_data_for_model()

    current_year = datetime.now().year
    data['edad_actual'] = current_year - data['anio_nac']

    # Codificar variable objetivo
    data['abandona'] = data['abandona'].map({'si': 1, 'no': 0})

    # Definir columnas
    columnas_categoricas = ['nacionalidad', 'sexo', 'titulacion']
    columnas_numericas = ['nota_def_acceso', 'nota_media', 'edad_actual']

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

    X_non_abandon = X[y == 0]
    data_non_abandon = data[y == 0].copy()

    X_non_abandon_preprocessed = preprocessor.fit_transform(X_non_abandon)

    poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
    X_non_abandon_poly = poly.fit_transform(X_non_abandon_preprocessed)

    # Predecir probabilidades de abandono
    probabilidades_abandono = voting_clf.predict_proba(X_non_abandon_poly)[:, 1]
    data_non_abandon['probabilidad_abandono'] = probabilidades_abandono

    return data_non_abandon