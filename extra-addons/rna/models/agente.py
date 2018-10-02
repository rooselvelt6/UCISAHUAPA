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
    	entradas = []
    	for attr in self:

    		# ESTADÍA HOSPITALARIA.
    		entradas.append(float(attr.estadia_hospitalaria))
    		# ANTECEDENTES
    		
    		if(attr.antecedentes != ""):
    			entradas.append(float(1))
    		
    		if(attr.antecedentes == ""):
    			entradas.append(float(0))

    		# igualar el vector de entrada a la lista de entradas procesadas		
    		attr.vector_entrada = entradas
    		
   
    		"""
    		entradas.append(attr.evaluacion_general.ventilacion_mecanica);
    		entradas.append(attr.evaluacion_general.migracion)
    		entradas.append(attr.datos_paciente.color_piel)
    		entradas.append(attr.evaluacion_general.procesos_invasivos)
    		entradas.append(attr.datos_paciente.edad)
    		entradas.append(attr.datos_paciente.sexo)
    		entradas.append(attr.evaluacion_general.tipo_admision)
    		attr.vector_entrada = entradas;
    		"""