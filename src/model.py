#
# @file model.py
# @brief Este archivo contiene el código del modelo de aprendizaje automático.
# @version 1.0
# @date 13/06/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from datetime import datetime
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score, roc_auc_score
from sklearn.pipeline import Pipeline
import joblib
from tqdm import tqdm
from imblearn.over_sampling import SMOTE
import xgboost as xgb
import lightgbm as lgb
from util import load_data_for_model

data = load_data_for_model()

# Crear nueva característica 'edad_actual'
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

# Crear interacciones polinómicas
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_train = poly.fit_transform(X_train)
X_test = poly.transform(X_test)

# Pipelines para cada modelo
modelos = {
    'RandomForest': RandomForestClassifier(random_state=42, n_jobs=-1),
    'LogisticRegression': LogisticRegression(max_iter=1000, random_state=42),
    'KNeighbors': KNeighborsClassifier(n_jobs=-1),
    'AdaBoost': AdaBoostClassifier(random_state=42),
    'XGBoost': xgb.XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss'),
    'LightGBM': lgb.LGBMClassifier(random_state=42, verbose=-1, force_row_wise=True)
}

# Hiperparámetros para búsqueda
param_grids = {
    'RandomForest': {
        'n_estimators': [100, 200],
        'max_depth': [10, 20],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2]
    },
    'LogisticRegression': {
        'C': [0.01, 0.1, 1.0],
        'solver': ['liblinear', 'lbfgs']
    },
    'KNeighbors': {
        'n_neighbors': [3, 5, 7],
        'weights': ['uniform', 'distance']
    },
    'AdaBoost': {
        'n_estimators': [50, 100],
        'learning_rate': [0.01, 0.1]
    },
    'XGBoost': {
        'n_estimators': [100, 200],
        'learning_rate': [0.01, 0.1],
        'max_depth': [3, 5]
    },
    'LightGBM': {
        'n_estimators': [100, 200],
        'learning_rate': [0.01, 0.1],
        'max_depth': [3, 5]
    }
}

# Buscar los mejores hiperparámetros y entrenar modelos
best_estimators = {}
metrics = {}

with tqdm(total=len(modelos), desc="Entrenando modelos") as pbar:
    for key, model in modelos.items():
        grid_search = GridSearchCV(model, param_grids[key], cv=StratifiedKFold(n_splits=5), scoring='accuracy', n_jobs=-1)
        grid_search.fit(X_train, y_train)
        best_estimators[key] = grid_search.best_estimator_
        
        # Evaluar modelo
        y_pred = grid_search.predict(X_test)
        metrics[key] = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1_score': f1_score(y_test, y_pred),
            'roc_auc': roc_auc_score(y_test, y_pred)
        }
        print("")
        print(f"Resultados para {key}:")
        print(f"Accuracy: {metrics[key]['accuracy']:.2f}")
        print(f"Precision: {metrics[key]['precision']:.2f}")
        print(f"Recall: {metrics[key]['recall']:.2f}")
        print(f"F1 Score: {metrics[key]['f1_score']:.2f}")
        print(f"ROC AUC: {metrics[key]['roc_auc']:.2f}")
        print("Matriz de Confusión:")
        print(confusion_matrix(y_test, y_pred))
        print("")
        
        pbar.update(1)

# Seleccionar los mejores modelos basados en las métricas
# Vamos a seleccionar los 3 mejores modelos para el ensemble
mejores_modelos = sorted(metrics.items(), key=lambda item: item[1]['f1_score'], reverse=True)[:3]
mejores_estimadores = [(key, best_estimators[key]) for key, _ in mejores_modelos]

# Crear VotingClassifier con los mejores modelos
voting_clf = VotingClassifier(
    estimators=mejores_estimadores,
    voting='soft',
    n_jobs=-1
)

# Entrenar el VotingClassifier
voting_clf.fit(X_train, y_train)

# Guardar el modelo entrenado
joblib_file = "trained_model.pkl"
joblib.dump(voting_clf, joblib_file)
print(f"Modelo guardado en {joblib_file}")

# Métricas del ensemble
y_pred_voting = voting_clf.predict(X_test)
print("Resultados del VotingClassifier:")
print(f"Modelos utilizados: {[name for name, _ in mejores_estimadores]}")
print(f"Accuracy: {accuracy_score(y_test, y_pred_voting):.2f}")
print(f"Precision: {precision_score(y_test, y_pred_voting):.2f}")
print(f"Recall: {recall_score(y_test, y_pred_voting):.2f}")
print(f"F1 Score: {f1_score(y_test, y_pred_voting):.2f}")
print(f"ROC AUC: {roc_auc_score(y_test, y_pred_voting):.2f}")
print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred_voting))

# Validación cruzada del ensemble
cross_val_scores_voting = cross_val_score(voting_clf, poly.transform(preprocessor.transform(X)), y, cv=StratifiedKFold(n_splits=5), scoring='accuracy', n_jobs=-1)
print(f"Cross-Validation Accuracy: {cross_val_scores_voting.mean():.2f}")
