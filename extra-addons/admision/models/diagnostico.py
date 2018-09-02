# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Diagnostico(models.Model):
	_name = "admision.diagnostico"

	# RESUMEN
	resumen = fields.Html(
	    string='Resumen del diagnóstico'
	)
	# DESCRIPCIÓN
	descripcion = fields.Html(
	    string='Descripción del diagnóstico',
	)