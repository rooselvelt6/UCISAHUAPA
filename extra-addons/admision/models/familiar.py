# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Familiar(models.Model):
	_name = "admision.familiar"
	_description = "Familiares"
	_rec_name = "parentesco"
	# PARENTESCO
	parentesco = fields.Char(string="Parentesco con el paciente", 
							translate=True,
							index=True,
							help='Parentesco del familiar con el paciente')