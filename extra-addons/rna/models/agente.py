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
from odoo import models, fields, api
from sklearn.preprocessing import MinMaxScaler
import ast
import numpy as np
from .. import Deep
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class rna(models.Model):
    _inherit = "admision.admision"
    #*********************************************************************
    # Campos finales para la comunicación con el exterior.
    #*********************************************************************
    # Variable de salida.
    estadia = fields.Char(
        string='Estimación del tiempo en UCI',
        help='Estimación del tiempo de la estadía del paciente en la UCI', 
    )
    # Percepción del entorno de admisión.
    vector_entrada = fields.Text(
        string='Vector de atributos',
        calculate="_obtenerAtributos"
    )

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
    		entradas.append(float(attr.estadia_hospitalaria))
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
    		entradas.append(float(attr.datos_paciente.edad))
    		# SEXO
    		entradas.append(float(attr.datos_paciente.sexo))
    		
    		# TIPO DE ADMISION
    		entradas.append(float(attr.evaluacion_general.tipo_admision))	
    		
    		# igualar el vector de entrada a la lista de entradas procesadas		
    		attr.vector_entrada = entradas

    @api.onchange('vector_entrada')
    def percepciones(self):
        print("*********************************")
        print()
        print("Se perciben cambios en el entorno")
        print()
        print("*********************************")
        # Paso 1.
        for campo in self:
            lista_atributos = ast.literal_eval(campo.vector_entrada)
            matriz_prediccion = np.array(lista_atributos)
        # Paso 2.
        matriz_prediccion = np.reshape(matriz_prediccion,(-1,1));
        escala = MinMaxScaler(feature_range=(0,1));
        print(escala.fit(matriz_prediccion))
        final = escala.transform(matriz_prediccion)
        l2 = [x[0] for x in final]
        l3 = np.array([l2])
        print(l3)
        print(l3.shape, type(l3))
        #************************************************
        # Paso final...construcción
        #resultados_finales = _modelo_cargado.predict(l3)
        #print(resultados_finales)
        print("Fin del proyecto UDO SUCRE 2018...")
        