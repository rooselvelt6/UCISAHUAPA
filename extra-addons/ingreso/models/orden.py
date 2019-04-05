# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OrdenMedica(models.Model):
	_name = "ingreso.orden"
	_description = "Ordenes médicas"
	_rec_name = "paciente_id"

	# Control de la orden medica
	paciente_id = fields.Many2one(
	    'ingreso.ingreso',
	    string='Paciente',
	    required=True,
	)

	fecha_inicio = fields.Datetime(
	    string='Fecha de inicio',
	    help='Fecha de inicio de la orden medica',
	    required=True, 
	)

	fecha_final= fields.Datetime(
	    string='Fecha de culminación',
	    help='Fecha de finalización de la orden medica',
	    required=True, 
	)

	estado = fields.Selection([(0,"Suspendida"),(1,"Ordenada")], string="Estado de la Orden", default=0)

	orden = fields.Html(
	    string='Orden médica',
	    help='Descripción de la orden médica',
	    required=True, 
	)

	actualizacion = fields.Html(
	    string='Actualización de la orden médica',
	    help='Actualización de la orden médica',
	    required=True, 
	)



