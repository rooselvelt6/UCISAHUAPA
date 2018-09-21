# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Historia(models.Model):
	_name = "admision.historia"
	_description = "Historias"

	# CAMPO PARA MOSTRAR EN RELACIÓN
	_rec_name = "numero"
	
	# RESUMEN
	numero = fields.Char(string='Número de historia',
						   index=True, 
						   help='Número de la Historia Clínica')