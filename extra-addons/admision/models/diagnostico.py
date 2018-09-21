# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Diagnostico(models.Model):
	_name = "admision.diagnostico"
	_description = "Diagnósticos"
	_rec_name = "resumen"
	
	# RESUMEN
	resumen = fields.Html(
	    string='Resumen del diagnóstico',
	    help='Resumen del diagnóstico', 
	    translate=True
	)
	# DESCRIPCIÓN
	descripcion = fields.Html(
	    string='Descripción del diagnóstico',
	    help='Descripción del diagnóstico', 
	    translate=True
	)