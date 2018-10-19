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
from ..Deep.mlp import Agente
from os import system
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

_agente = Agente(); # Nuevo agente...
_modelo = _agente._cargarCompilar(); # Cargar Modelo.
_modelo._make_predict_function();

def _modo():
    system("clear")
    while True:
        print("**************************")
        print("(1). Modo de Aprendizaje. ")
        print()
        print("(2). Modo de Predicción.  ")
        print("**************************")
        fase = input("Indicar el modo de la RNA:")
        try:
            valor = int(fase)
            if((valor > 0) and (valor <=2)):
                if(valor==1):
                    print("Iniciado el modo de Aprendizaje...")
                    print()
                    # Modo entrenamiento
                    _bot._entrenar(); 
                    _bot._probar(); 
                    _bot._getTablero();
                    break;
                else:
                    # Fase 2: Predicciones
                    # Modo predicción
                    print("Iniciando Modo predicción...")
                    print()
                    _modelo_cargado = _bot._cargarCompilar();
                    print("La predicción es:")
                    print(_bot._predecir(_modelo_cargado, [0.1,0.2,0.3,0.4,1,1,1,1,1]))
                    break;
            else:
                system("clear")
                print("Has cometido un error !!!")
                print("ATENCIÓN. Por favor revisar las opciones del menú...")
                continue;
        except ValueError:
            system("clear")
            print("ATENCIÓN: Debe ingresar un número entero")
        

#***********************************************************************
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
        string='Percepciones',
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
    def percibir(self):
        # Paso 1 Generar una lista del entorno.
        lista = [0,0,0,0,0,0,0,0,0];
        # Evaluar condición de longitud de lista.
        if(len(lista)==9):
            resultado = _agente._estimar(atributos=lista, modelo=_modelo)
            del(lista)
            print("Resultado:",resultado)
        
    def razonar(self):
        for campo in self:
            lista_atributos = ast.literal_eval(campo.vector_entrada)
            matriz_prediccion = np.array(lista_atributos)                   
        # Paso 2.
        matriz_prediccion = np.reshape(matriz_prediccion,(-1,1));
        escala = MinMaxScaler(feature_range=(0,1));
        print(escala.fit(matriz_prediccion))
        final = escala.transform(matriz_prediccion)
        l2 = [x[0] for x in final]
        return l2