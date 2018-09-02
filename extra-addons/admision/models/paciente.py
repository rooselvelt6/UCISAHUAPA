# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Paciente(models.Model):

	_name = "admision.paciente"

	# NUMERO DE HISTORIA CLINICA
	id_historia = fields.Many2one(
	    'admision.historia',
	    'Historia',
	)

	# FECHA DE NACIMIENTO
	fecha_nacimiento  = fields.Date(string='Fecha de nacimiento')
	
	# NOMBRE
	nombre = fields.Char(string='Nombre')

	# SEXO.
	sexo = fields.Selection([(0,"Femenino"),(1,"Masculino")])

	# CI
	ci = fields.Char(string='Cédula de identidad', size = 9)
	
	# LUGAR DE NACIMIENTO
	lugar_nacimiento = fields.Char(string="Lugar de nacimiento")

	# DIRECCIÓN ACTUAL
	direccion = fields.Text(string="Dirección actual")

	# FECHA DE INGRESO AL HOSPITAL
	fecha_ingreso_hospital  = fields.Date(string='Fecha de ingreso al HUAPA')

	# OCUPACIÓN
	ocupacion = fields.Char(string="Ocupación")

	# PESO CORPORAL
	peso_corporal = fields.Float(string='Peso corporal')

	# FAMILIAR ENCARGADO
	familiar_encargado = fields.Many2one('admision.familiar', 'Familiar')
	
	# DIAGNOSTICO DE INGRESO AL HOSPITAL.
	diagnostico_hospital = fields.Many2one(
	    'admision.diagnostico',
	    'Diagnóstico HUAPA',
	)

	# EXAMEN DE INGRESO AL HOSPITAL.
	examen_hospital = fields.Many2one(
	    'admision.examenfisico',
	    'Examen físico HUAPA',
	)

	# ANTECEDENTES DE INGRESO
	antecedentes = fields.Html()