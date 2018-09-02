# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Admision(models.Model):
	_name = "admision.admision"

	# FOTO DEL PACIENTE
	foto  = fields.Binary()
	
	# FECHA INGRESO A UCI
	fecha_ingreso_uci = fields.Date()
	
	# DATOS DEL PACIENTE.
	datos_paciente = fields.Many2one(
	    'admision.paciente',
	    'Paciente',
	)

	# RESUMEN DE INGRESO A UCI
	resumen_ingreso  = fields.Html(
	    string='Resumen general de ingreso',
	)

	# EXAMEN FISICO DE INGRESO A UCI
	examen_fisico_uci = fields.Many2one(
	    'admision.examenfisico',
	    'Examen físico de ingreso a UCI',
	)

	# EVALUACION GENERAL DE INGRESO
	evaluacion_general = fields.Many2one(
	    'admision.evaluacion',
	    'Evaluación',
	)
