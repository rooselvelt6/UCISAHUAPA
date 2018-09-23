# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Evaluacion(models.Model):
	_name = "admision.evaluacion"
	_description = "Evaluaciones"
	_rec_name = "create_date"

	# SERVICIO DE PROCEDENCIA
	procedencia = fields.Many2one(
	    'hr.department',
	    string='Servicio de procedencia',
	    help='Servicio de procedencia'
	)
	
	# TIPO DE ADMISIÓN
	tipo_admision = fields.Selection([(0,"Electiva"), (1,"Urgente")], string="Tipo de admisión", default=0)

	# MIGRACION
	migracion = fields.Selection([(0,"No"), (1,"Si")], string="Proviene de migración", default=0)

	# VENTILADOR MECANICO
	ventilacion_mecanica = fields.Selection([(0,"No"), (1,"Si")], string="Ventilador Mecánico", default=0)
	
	# PRESENTA PROCESOS INVASIVOS
	procesos_invasivos = fields.Selection([(0,"No"), (1,"Si")], string="Procesos invasivos", default=0)
	
	
	
	