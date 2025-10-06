
#Pycaret:

#from pycaret.regression import *

#Pipeline de pycaret:

#1. Setup() : Definir el dataset y parametros
    #exp = setup(data=df, target='precio', session_id=12,normalize=True)

#2. Compare_models(): Compara multiples modelos y los rankea
    #mejor_modelo = compare_models()

#3. Create model() : Crea un modelo especifico
    #lr = create_model('lr') 

#4. Tune_model() :Ajuste automatico de hiperparametros
    #tuned_lr = tune_model(lr)

#5. plot_model(): visualiza (graficamente) el desempeño del modelo
    #plot_model(tuned_lr,plot='residuals')
    #plot_model(tuned_lr,plot='feature')

#6. evaluate_model(): UI de evaluación del modelo
    #evaluate_model(tuned_lr)

#7. predict_model(): Predicciones sobre nuevos datos en el DF
    #predicciones = predict_model(tuned_lr,data=nuevo_df)

#8. save_model()/load_model(): Guardar y cargar modelo.
    #save_model(tunel_lr,'modelo_final')