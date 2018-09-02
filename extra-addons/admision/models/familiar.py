# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Familiar(models.Model):
	_name = "admision.familiar"

	# PARENTESCO
	parentesco = fields.Char(string="Parentesco con el paciente")