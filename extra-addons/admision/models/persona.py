# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Persona(models.Model):
	_name = "admision.persona"

	# NOMBRE
	nombre = fields.Char(
	    string='Nombre',
	    size = 40
	)

	# CI
	ci = fields.Char(
	    string='Cédula de identidad',
	    size = 9
	)

	# SEXO.
	sexo = fields.Selection([(0,"Femenino"),
							 (1,"Masculino")])

	# FECHA DE NACIMIENTO
	fecha_nacimiento  = fields.Date(
	    string='Fecha de nacimiento'
	)

	# LUGAR DE NACIMIENTO
	lugar_nacimiento = fields.Char(string="Lugar de nacimiento")

	# DIRECCIÓN ACTUAL
	direccion = fields.Text()

	# OCUPACIÓN
	ocupacion = fiels.Char(string="Ocupación")
	# EDAD
	"""edad = fields.Integer(
				    string='Field Label',
				    computed="calcularEdad"
				)"""

	"""@api.multi
				def calcularEdad(self):
					for x in self:
						x.edad = 1 # fecha de nacimiento - fecha de ingreso a UCI"""
