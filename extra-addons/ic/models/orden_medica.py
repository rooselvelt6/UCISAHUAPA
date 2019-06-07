# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OrdenMedica(models.Model):
	_name = "paciente.orden"
	_description = "Orden médica"
	_rec_name = "id_paciente"

	# Control de la orden medica

	id_paciente = fields.Many2one(
	    'paciente.paciente',
	    string='Paciente',
	    required=True,
	)

	fecha_inicio = fields.Datetime(
	    string='Fecha de inicio',
	    help='Fecha de inicio de la orden',
	    required=True, 
	)

	fecha_final= fields.Datetime(
	    string='Fecha de culminación de la orden',
	    help='Fecha de finalización de la orden medica',
	    required=True, 
	)

	estado = fields.Selection([(0,"Suspendida"),(1,"Ordenada")], string="Estado de la Orden", default=0)

	orden = fields.Html(
	    string='Orden médica',
	    help='Descripción de la orden médica',
	    required=True, 
	)

	"""actualizacion = fields.Html(
				    string='Actualización de la orden médica',
				    help='Actualización de la orden médica',
				    required=True, 
				)"""

