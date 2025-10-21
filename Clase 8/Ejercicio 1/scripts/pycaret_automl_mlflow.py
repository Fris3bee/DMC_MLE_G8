# pycaret_automl_mlflow.py
import mlflow
from pycaret.classification import *
import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")

# Ruta absoluta al CSV
data = pd.read_csv("D:/02.DMC/00.Mis Cursos/23.Especialización ML Engineering/Pruebas/DMC_MLE_G8/Clase 8/Ejercicio 1/data/credit_data.csv")

# Configuración de MLflow
mlflow.set_tracking_uri("http://68.211.72.133:5000")
mlflow.set_experiment("Clase_MLE_S8_ArnaldoAlvarado")

with mlflow.start_run(run_name="AutoML_pycaret"):
    # Setup y entrenamiento
    s = setup(data, target='default', session_id=123, #pongan ids diferentes
              log_experiment=True, experiment_name='Clase_MLE_S8_ArnaldoAlvarado') ##idem al experimento
    
    best = compare_models()
    evaluate_model(best)
    
    # Registrar modelo
    mlflow.sklearn.log_model(best, "mejor_modelo_AA")
    
    # Extra logs si deseas
    mlflow.log_param("modelo_principal_AA", str(best))
    
    # Registrar matriz de confusión como imagen
    import matplotlib.pyplot as plt
    from pycaret.utils import check_metric
    from pycaret.classification import plot_model
    
    plot_model(best, plot='confusion_matrix', save=True)
    mlflow.log_artifact("Confusion Matrix.png")
