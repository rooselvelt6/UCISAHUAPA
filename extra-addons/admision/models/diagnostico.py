# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Diagnostico(models.Model):
	_name = "admision.diagnostico"

	# RESUMEN
	resumen = fields.Date(
	    string='Resumen'
	)
	# DESCRIPCIÓN
	descripcion = fields.Text(
	    string='Descripción del diagnóstico',
	)