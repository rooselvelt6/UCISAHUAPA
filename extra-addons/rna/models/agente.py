# -*- coding: utf-8 -*-
""" 
	Agente inteligente basado en RNA modelo Perceptron Multicapa 
	con retropropagación de errores en Tensorflow.

	El sistema toma percepciones del entorno es decir del sistema de admisión actual
	y en base a las variables procesa las variables y obtiene un resultado capaz de 
	predecir el tiempo de estadía dentro de la UCI con funciones onchange.
	
"""
from odoo import models, fields, api
#import tensorflow as tf
class rna(models.Model):
    _inherit = "admision.admision"
    estadia = fields.Integer(
        string='Estimación del tiempo en UCI',
        help='Estimación del tiempo de la estadía del paciente en la UCI', 
    )

    vector_entrada = fields.Text(
        string='Vector de atributos',
        calculate="_obtenerAtributos"
    )

    @api.onchange('antecedentes',
    			  'estadia_hospitalaria',
    			  'datos_paciente',
    			  'evaluacion_general')

    def _obtenerAtributos(self):
        """ Función que genera el vector de entradas para la RNA tomando percepciones del entorno """
    	entradas = []
    	for attr in self:

    		# ESTADÍA HOSPITALARIA.
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
    		entradas.append(attr.preprocesar(minV=12,
                                             maxV=92,
                                             minimoNuevo=0,
                                             maximoNuevo=1,
                                             valor=int(attr.datos_paciente.edad)))
    		# SEXO
    		entradas.append(float(attr.datos_paciente.sexo))
    		
    		# TIPO DE ADMISION
    		entradas.append(float(attr.evaluacion_general.tipo_admision))	
    		
    		# igualar el vector de entrada a la lista de entradas procesadas		
    		attr.vector_entrada = entradas


    def preprocesar(self, minV, maxV, minimoNuevo, maximoNuevo, valor):
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