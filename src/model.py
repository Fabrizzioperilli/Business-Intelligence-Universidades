import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression  # Corrección en la importación
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score, roc_auc_score
from sklearn.pipeline import Pipeline
import joblib
from tqdm import tqdm
from imblearn.over_sampling import SMOTE
import xgboost as xgb
from util import load_data_for_model # Corrección en la importación

data = load_data_for_model()  # Corrección en la carga de datos

current_year = datetime.now().year
data['edad_actual'] = current_year - data['anio_nac']

# Codificar variable objetivo
data['abandona'] = data['abandona'].map({'si': 1, 'no': 0})

# Definir columnas
columnas_categoricas = ['nacionalidad', 'sexo', 'titulacion']
columnas_numericas = ['nota_def_ebau', 'nota_media', 'edad_actual']

# Preprocesamiento
preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline([('imputer', SimpleImputer(strategy='mean')), ('scaler', StandardScaler())]), columnas_numericas),
        ('cat', Pipeline([('imputer', SimpleImputer(strategy='constant', fill_value='Desconocido')), 
                          ('encoder', OneHotEncoder(handle_unknown='ignore'))]), columnas_categoricas)
    ])

# Dividir datos en características y variable objetivo
X = data[columnas_categoricas + columnas_numericas]
y = data['abandona']
ids = data['id']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test, id_train, id_test = train_test_split(X, y, ids, test_size=0.2, random_state=42, stratify=y)

# Aplicar preprocesamiento y SMOTE en el conjunto de entrenamiento
X_train = preprocessor.fit_transform(X_train)
X_test = preprocessor.transform(X_test)

smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

# Feature engineering: polynomial features
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_train = poly.fit_transform(X_train)
X_test = poly.transform(X_test)

# Crear pipelines para cada modelo
modelos = {
    'rf': RandomForestClassifier(random_state=42, n_jobs=-1),
    'lr': LogisticRegression(max_iter=1000, random_state=42),
    'gb': GradientBoostingClassifier(random_state=42),
    'ab': AdaBoostClassifier(random_state=42),
    'xgb': xgb.XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')
}

# Definir el rango de parámetros para la búsqueda
param_grids = {
    'rf': {
        'n_estimators': [100, 200, 300],
        'max_depth': [10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'bootstrap': [True, False]
    },
    'lr': {
        'C': [0.01, 0.1, 1.0, 10.0],
        'solver': ['liblinear', 'lbfgs']
    },
    'gb': {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.01, 0.05, 0.1],
        'max_depth': [3, 5, 7]
    },
    'ab': {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.05, 0.1]
    },
    'xgb': {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.01, 0.05, 0.1],
        'max_depth': [3, 5, 7]
    }
}

# Buscar los mejores hiperparámetros con GridSearchCV
best_estimators = {}
with tqdm(total=len(modelos), desc="Entrenando modelos") as pbar:
    for key, model in modelos.items():
        grid_search = GridSearchCV(model, param_grids[key], cv=StratifiedKFold(n_splits=5), scoring='accuracy', n_jobs=-1)
        grid_search.fit(X_train, y_train)
        best_estimators[key] = grid_search.best_estimator_
        pbar.update(1)

# Crear el VotingClassifier con los mejores estimadores
voting_clf = VotingClassifier(
    estimators=[(key, best_estimators[key]) for key in best_estimators],
    voting='soft',
    n_jobs=-1
)

# Entrenar el VotingClassifier
voting_clf.fit(X_train, y_train)

# Guardar el modelo entrenado
joblib_file = "trained_model.pkl"
joblib.dump(voting_clf, joblib_file)
print(f"Modelo guardado en {joblib_file}")

# Evaluar el modelo
y_pred_voting = voting_clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred_voting):.2f}")
print(f"Precision: {precision_score(y_test, y_pred_voting):.2f}")
print(f"Recall: {recall_score(y_test, y_pred_voting):.2f}")
print(f"F1 Score: {f1_score(y_test, y_pred_voting):.2f}")
print(f"ROC AUC: {roc_auc_score(y_test, y_pred_voting):.2f}")
print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred_voting))

# Crear DataFrame con predicciones y IDs
predicciones = pd.DataFrame({
    'id': id_test,
    'abandona_real': y_test,
    'abandona_predicho': y_pred_voting
})

# Mostrar las predicciones junto con los IDs
print(predicciones)

# Validación cruzada
cross_val_scores_voting = cross_val_score(voting_clf, poly.transform(preprocessor.transform(X)), y, cv=StratifiedKFold(n_splits=5), scoring='accuracy', n_jobs=-1)
print(f"Cross-Validation Accuracy: {cross_val_scores_voting.mean():.2f}")
