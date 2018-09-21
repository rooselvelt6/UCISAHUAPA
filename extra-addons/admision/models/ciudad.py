# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ciudad(models.Model):
	_name = "admision.ciudad"
	_description = "Ciudades"
	_rec_name = "nombre"
	# PARENTESCO
	nombre = fields.Char(string="Ciudad", 
							translate=True,
							index=True,
							help='Ciudad')