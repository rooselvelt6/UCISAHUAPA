# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OrdenMedica(models.Model):
	_name = "admision.orden"
	_description = "Ordenes médicas"
	_rec_name = "paciente_id"

	# Control de la orden medica
	paciente_id = fields.Many2one(
	    'admision.paciente',
	    string='Paciente',
	)
	medico_id = fields.Many2one(
	    'hr.employee',
	    string='Médico tratante',
	)
	fecha_inicio = fields.Datetime(
	    string='Fecha de inicio',
	    help='Fecha de inicio de la orden medica', 
	)

	fecha_final= fields.Datetime(
	    string='Fecha de culminación',
	    help='Fecha de finalización de la orden medica', 
	)

	orden = fields.Text(
	    string='Orden médica',
	    help='Descripción de la orden médica', 
	)

	actualizacion = fields.Html(
	    string='Actualización de la orden médica',
	    help='Actualización de la orden médica', 
	)



