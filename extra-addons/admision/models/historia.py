# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Historia(models.Model):
	_name = "admision.historia"

	# RESUMEN
	numero = fields.Integer(string='Número de historia')