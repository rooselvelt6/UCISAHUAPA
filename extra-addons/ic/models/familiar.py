# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Familiar(models.Model):
	_name = "paciente.familiar"
	_description = "Familiar del paciente"
	_rec_name = "parentesco"
	# PARENTESCO
	parentesco = fields.Char(string="Parentesco con el paciente", 
							translate=True,
							index=True,
							help='Parentesco con el paciente', size=10, required=True)
	_sql_constraints = [
	    ('parentesco_uniq', 'unique (parentesco)', ('Ya se encuentra registrado intenta con otro !!!')),
	]