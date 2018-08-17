# -*- coding: utf-8 -*-

from odoo import models, fields, api

class apache(models.Model):
	_name = 'apache.apache'
	name = fields.Char(string="Titulo", required=True)
	descripcion = fields.Text()