#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright YEAR(2018), AUTHOR(ROOSELVELT ANGULO)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

""" 
    Descripción:
            Agente inteligente basado en RNA modelo Perceptron Multicapa 
        con retropropagación de errores en Tensorflow.

        El sistema toma percepciones del entorno es decir del sistema de admisión actual
        y en base a las variables procesa las variables y obtiene un resultado capaz de 
        predecir el tiempo de estadía dentro de la UCI con funciones onchange.

        El problema de la estimación del tiempo de estadía se presenta como un
        modelo de regresión por medio de RNA con el objetivo de predecir la salida
        de un valor continuo, como el tiempo de estadía de un paciente admitido en
        la UCI del SAHUAPA en base al siguiente conjunto de variables.

        Orden de las variables del universo del conjunto de entrenamiento.
            1. Presencia de antecedentes.
            2. Color de piel del paciente.
            3. Edad del paciente.
            4. Estadía hospitalaria del paciente.
            5. Proviene de migración el paciente.
            6. Presencia de procesos invasivos.
            7. Sexo del paciente.
            8. Tipo de admisión realizada al paciente.
            9. Ventilador Mecánico.
            ----------------------------------------------------
            10. Etiqueta de salida. (Tiempo de estadía en UCI).
            ----------------------------------------------------
    Procesos:
        (0). Cargar y delimitar conjunto de datos en atributos y etiquetas.
        (1). Definir el modelo secuancial MLP.
        (2). Configurar el modelo para el proceso de regresión.
        (3). Dividir el conjunto total en tres subconjuntos (entrenamiento, validación, prueba)
        (4). Entrenar el modelo con los conjuntos muestreados.
        (5). Evaluar el modelo con datos de prueba.
        (6). Predecir nuevos resultados con el sistema de admisión.
    
"""
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from datetime import datetime
from decimal import Decimal
from keras import losses, metrics, optimizers
from keras.callbacks import TensorBoard, EarlyStopping
from keras.layers import Dense
from keras.models import Sequential, model_from_json, load_model
from keras.wrappers.scikit_learn import KerasRegressor
from odoo import models, fields, api
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import webbrowser
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class rna(models.Model):
    _inherit = "admision.admision"
    #*********************************************************************
    # Campos finales para la comunicación con el exterior.
    #*********************************************************************
    # Variable de salida.
    estadia = fields.Integer(
        string='Estimación del tiempo en UCI',
        help='Estimación del tiempo de la estadía del paciente en la UCI', 
    )
    # Percepción del entorno de admisión.
    vector_entrada = fields.Text(
        string='Vector de atributos',
        calculate="_obtenerAtributos"
    )

    #*********************************************************************
    # Métodos del sistema
    #*********************************************************************
    def guardarModelo(self, modelo):
        """ Guardar el modelo creado en el entrenamiento en formato JSON, YAML para la arquitectura y en formato HD5 para los pesos del sistema"""
        modelo_json = modelo.to_json()
        with open("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Memoria/modelo.json","w") as json_file:
            json_file.write(modelo_json) # Escribir modelo en archivo JSON.
        # Serializar pesos del entrenamiento en formato HDF5 para futuras predicciones del sistema
        modelo.save_weights("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Memoria/pesos.h5");

    def cargarModelo(self):
        """ El modelo es leido como archivo y cargado a memoria de nuevo para ser usado"""
        json_file = open('/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Memoria/modelo.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # Cargamos los pesos respectivos en el modelo
        loaded_model.load_weights("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Memoria/pesos.h5")
        return loaded_model

    def entrenamiento(self, modelo ,subconjuntos):
        """ Método de entrenamiento de la RNA configurado con los hiperparámetros """
        tensorboard = TensorBoard(log_dir="/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Tablero/{0}".format(datetime.now()), write_grads=True, write_graph=True, histogram_freq=1)   
        # Parar el entrenamiento si no se mejora el resultado de val_loss con paciencia de 50 ejemplos
        #early_stop = EarlyStopping(monitor='val_loss', patience=60) # Paradas forzado si no hay mejoras
        history = modelo.fit(subconjuntos[0], # Conjunto de atributos
                             subconjuntos[2], # Conjunto de etiquetas
                             epochs=500, # Epocas.
                             batch_size=32, # Tamaño del Lote.
                             verbose=1, # Información del proceso
                             # Conjunto de validación al 20% del entrenamiento
                             validation_split=0.2,
                             callbacks=[tensorboard] #early_stop# Filtrar información al tablero TensorBoard.
                            )
        self.guardarModelo(modelo) # Guardar el entrenamiento en el disco.
        # Fin del entrenamiento.

    def probar(self, subconjuntos):
        """ 
            (0). Cargar el modelo entrenado, compilarlo.
            (1). Llamar a la función evaluate(atributos_prueba, etiquetas_prueba).
        """
        modelo_cargado = self.cargarModelo(); # Cargar de disco el modelo.
        print("El modelo ha sido cargado para pruebas")
        # Configurar y compilar modelo
        modelo_cargado.compile(loss=losses.mean_squared_error, # Error Cuadrático medio
                            optimizer=optimizers.SGD(lr=0.01,  # SGD
                                                     decay=1e-6, 
                                                     momentum=0.9, 
                                                     nesterov=True),
                            metrics=[metrics.mae] # Mean Absolute Error.
                            )
        # Evaluar el modelo en el nuevo conjunto de pruebas definido anteriormente.
        scores = modelo_cargado.evaluate(subconjuntos[1], subconjuntos[3], batch_size=32, verbose=1)
        print("Resultados de la prueba final:",scores)
        # Fin de evaluación del modelo.

    def predecir(self, atributos=[]):
        modelo_cargado = cargarModelo(); # Cargar de disco el modelo.
        print("El modelo ha sido cargado para pruebas")
        # Configurar y compilar modelo
        modelo_cargado.compile(loss=losses.mean_squared_error, # Error Cuadrático medio
                            optimizer=optimizers.SGD(lr=0.01,  # SGD
                                                     decay=1e-6, 
                                                     momentum=0.9, 
                                                     nesterov=True),
                            metrics=[metrics.mae] # Mean Absolute Error.
                            )
        #***********************************************************************************
        # Preprocesamiento
        #***********************************************************************************
        # Transformar a en array cada caso de salida deseada
        atributos = np.array([atributos])
        # Transformación minMax a escala entre 0 y 1 de forma escalar datos
        escala1 = MinMaxScaler(feature_range=(0, 1))
        print(escala1.fit(atributos))
        preprocesar = scaler.transform(atributos)
        #***********************************************************************************
        estimacion = modelo_cargado.predict(preprocesar) # Estimación del tiempo
        #***********************************************************************************
        valor = float(estimacion)
        salida = postprocesar(minV=0, maxV=1, minimoNuevo=0, maximoNuevo=41, valor=valor)
        print("*************************************************")
        print("El tiempo estimado para el paciente en la UCI es:")
        print(estimacion," se representa como: {0} días".format(round(salida)))
        print("*************************************************")
    
    def construirModelo(self):
        modelo = Sequential();
        # Añadir capas
        modelo.add(Dense(units=9, activation="relu", name="Capa_Entrada", input_dim=9))
        modelo.add(Dense(units=7, activation="relu", name="Capa_Oculta"))
        modelo.add(Dense(units=1, activation="sigmoid", name="Capa_Salida"))
        # Configuración y compilación del modelo creado
        modelo.compile(loss=losses.mean_squared_error, optimizer=optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True), metrics=[metrics.mae])
        print("Arquitectura de la RNA:")
        modelo.summary()
        return modelo;

    def cargarDatos(self):
        # Cargar el conjunto de datos para entrenamiento y validación
        try:
            # Proceso de carga del conjunto
            conjunto = np.loadtxt("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Datasets/todo/conjunto_total.csv", delimiter=",");
            # División del conjunto
            x = conjunto[:,0:9]; # Atributos de entrada
            y = conjunto[:,9]; # Etiquetas o salidas deseadas 

            if(len(x) == len(y)):
                print("Conjunto de entrenamiento cargado correctamente...")
                # Transformar a en array cada caso de salida deseada
                y = np.reshape(y,(-1,1));
                # Transformación minMax a escala entre 0 y 1 de forma escalar datos
                scaler = MinMaxScaler()
                print(scaler.fit(x))
                print(scaler.fit(y))
                # Transformación escalar.
                xscale = scaler.transform(x)
                yscale = scaler.transform(y)
                # División de los conjuntos de validación y prueba.
                X_train, X_test, y_train, y_test = train_test_split(xscale, yscale);
                return (X_train, X_test, y_train, y_test) # Retornar subconjuntos para entrenamiento y prueba
        except Exception as e:
            print("Error en la carga del archivo")
            print("Ha ocurrido una falla al cargar el archivo del conjunto")
            print(e)

    def postprocesar(self, minV, maxV, minimoNuevo, maximoNuevo, valor):
        """ 
            Información:
                Función utilizada para el preprocesamiento y postproprecesamiento de las variables
                del sistema RNA para que las variables se adecuen al manejo del sistema.
            Argv:
                minv: minímo valor de la variable
                maxV: maximo valor de la variable
                minimoNuevo: mínimo valor esperado a obtener
                maximoNuevo: máximo valor esperado a obtener
                valor: valor actual del sistema
            Return: 
                Escalado de la variable en función de la siguiente expresión.
                (((valor - minV) * (maximoNuevo - minimoNuevo)) / (maxV - minV)) + minimoNuevo

        """
        return (((valor - minV) * (maximoNuevo - minimoNuevo)) / (maxV - minV)) + minimoNuevo

    def obtenerTablero(self):
        """ Capturar en TensorBoard toda la información y mostrarla en el navegador"""
        # Abrir el navegador en la siguiente dirección
        webbrowser.open("http://robzombie6:6006", new=2, autoraise=True)
        # Ejecutar el servicio de tensorboard
        os.system("tensorboard --logdir='Tablero'")
    
    def fase_Aprendizaje(self):
        modelo = self.construirModelo()
        print("Modelo construido con éxito!!!")
        # Orden de los datos cargados en la tupla es: (X_train, X_test, y_train, y_test)
        subconjuntos = self.cargarDatos()
        self.entrenamiento(modelo, subconjuntos)
        print("Entrenamiento finalizado !!!")
        print()
        print()
        print("Pruebas finales...")
        self.probar(subconjuntos)
    
    def fase_Prediccion(self):

    #*********************************************************************   
    # Métodos onchange
    #*********************************************************************
    @api.onchange('antecedentes',
    			  'estadia_hospitalaria',
    			  'datos_paciente',
    			  'evaluacion_general')
    def _obtenerAtributos(self):
    	entradas = []
    	for attr in self:

    		# ESTADÍA HOSPITALARIA.entradas.append(float(attr.estadia_hospitalaria))
    		entradas.append(attr.estadia_hospitalaria)
    		# ANTECEDENTES
    		if(attr.antecedentes != ""):
    			entradas.append(float(1))
    		
    		if(attr.antecedentes == ""):
    			entradas.append(float(0))
    		
    		# VENTILADOR MECANICO
    		entradas.append(float(attr.evaluacion_general.ventilacion_mecanica));
    		
    		# MIGRACIÓN
    		entradas.append(float(attr.evaluacion_general.migracion))
    		
    		# COLOR DE PIEL
    		entradas.append(float(attr.datos_paciente.color_piel))
    		
    		# PROCESOS INVASIVOS
    		entradas.append(float(attr.evaluacion_general.procesos_invasivos))
    		
    		# EDAD Cruda entradas.append(float(attr.datos_paciente.edad))
            # Edad preprocesada para la RNA
    		entradas.append(attr.datos_paciente.edad)
    		# SEXO
    		entradas.append(float(attr.datos_paciente.sexo))
    		
    		# TIPO DE ADMISION
    		entradas.append(float(attr.evaluacion_general.tipo_admision))	
    		
    		# igualar el vector de entrada a la lista de entradas procesadas		
    		attr.vector_entrada = entradas

    @api.onchange('vector_entrada')
    def _onchange_vector_entrada(self):
        print("Se detectan cambios en las entradas de la RNA")
        #self.fase_Aprendizaje()
        
            

    
    