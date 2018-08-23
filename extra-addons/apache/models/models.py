# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Apache(models.Model):

	# NOMBRE DEL MODELO
	_name = 'apache.apache'

	# FECHA ACTUAL PARA EL CÁLCULO DEL SISTEMA

	# 					CONTROL DE VARIABLES FISIOLÓGICAS SOLICITADAS AL USUARIO

	# TEMPERATURA CORPORAL (1)
	temperatura = fields.Float(string="Temperatura °C", required=True, translate=True)

	# PRESIÓN ARTERIAL MEDIA (2)
	pam = fields.Integer(string="Presión Arterial Media (PAM)", required=True, translate=True)
 
	# FRECUENCIA CARDIACA (3)
	fc = fields.Integer(string="Frecuencia cardíaca (respuesta ventricular)", required=True, translate=True)

	# FRECUENCIA RESPIRATORIA (4)
	fr = fields.Integer(string="Frecuencia respiratoria (no ventilado o ventilado)", required=True, translate=True)

	# PH ARTERIAL (5)
	ph =  fields.Float(string="pH arterial (Preferido)", required=True, translate=True)
	# HCO3 SERICO
	hco3serico = fields.Float(string="HCO3 SÉRICO (venoso mEq/l)", required=True, translate=True)

	# NA SERICO
	naserico = fields.Integer(string="Sodio Sérico (mEq/l)", required=True, translate=True)

	# K SERICO
	kserico = fields.Float(string="Potasio Sérico (mEq/l)", required=True, translate=True)

	# CREATININA SERICA
	creatinina = fields.Float(string="Creatinina sérica (mg/dl)", required=True, translate=True)

	# HEMATOCRITO
	hematocrito = fields.Float(string="Hematocrito (%)", required=True, translate=True)

	# LEUCOCITOS
	leucocitos = fields.Float(string="Leucocitos (Total/mm3 en miles)", required=True, translate=True)

	# OXIGENACIÓN
	oxigenacion = fields.Float(string="Oxigenación", required=True, translate=True)