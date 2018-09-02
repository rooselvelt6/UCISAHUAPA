# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Evaluacion(models.Model):
	_name = "admision.evaluacion"

	# TIPO DE PACIENTE
	tipo_paciente = fields.Selection([(0,"Interno de UCI"), (1,"Externo de UCI")])

	# TIPO DE ADMISIÓN
	tipo_admision = fields.Selection([(0,"Electiva"), (1,"Urgente")])

	# COLOR DE PIEL.
	color_piel = fields.Selection([(0,"Morena"),(1,"Blanca")])

	# SERVICIO DE PROCEDENCIA
	procedencia = fields.Char(string="Servicio de procedencia")

	# PRESENCIA DE INTERVENCIONES QUIRURGICAS
	intervenciones_quirurgicas = fields.Selection([(0,"No"), (1,"Si")])
	
	# COMPLICACIONES POSTOPERATORIAS
	complicacion_postoperatoria = fields.Selection([(0,"No"),(1,"Si")])
	
	# COMPLICACIONES RESPIRATORIAS
	complicacion_respiratoria = fields.Selection([(0,"No"), (1,"Si")])
	
	# VENTILADOR MECANICO
	ventilacion_mecanica = fields.Selection([(0,"No"), (1,"Si")])
	
	# PRESENTA PROCESOS INVASIVOS
	procesos_invasivos = fields.Selection([(0,"No"), (1,"Si")])
	
	# MIGRACION
	migracion = fields.Selection([(0,"No"), (1,"Si")])
	
	# INFECCION INTRAHOSPITALARIA
	infecciones_intrahospitalarias = fields.Selection([(0,"No"), (1,"Si")])