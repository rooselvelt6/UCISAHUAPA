# -*- coding: utf-8 -*-
""" 
	Agente inteligente basado en RNA modelo Perceptron Multicapa 
	con retropropagación de errores en Tensorflow 
"""
from odoo import models, fields, api
#import tensorflow as tf
class rna(models.Model):
    _inherit = "admision.admision"
    estadia = fields.Integer(
        string='Estadía en UCI',
        help='Estimación del tiempo de la estadía del paciente', 
    )
