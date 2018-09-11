# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
class Paciente(models.Model):

	_name = "admision.paciente"

	# NUMERO DE HISTORIA CLINICA
	id_historia = fields.Many2one('admision.historia', 'Historia')

	# FECHA DE NACIMIENTO
	fecha_nacimiento  = fields.Date(string='Fecha de nacimiento', help='Fecha de nacimiento')
	
	# NOMBRE
	nombre = fields.Char(string='Nombre', translate=True, help='Nombre del paciente')

	# SEXO.
	sexo = fields.Selection([(0,"Femenino"),(1,"Masculino")])

	# CI
	ci = fields.Char(string='Cédula de identidad', size=9, help='Cédula de identidad')
	
	# LUGAR DE NACIMIENTO
	lugar_nacimiento = fields.Char(string="Lugar de nacimiento", translate=True, help='Lugar de nacimiento')

	# DIRECCIÓN ACTUAL
	direccion = fields.Text(string="Dirección actual", translate=True, help='Dirección actual')

	# FECHA DE INGRESO AL HOSPITAL
	fecha_ingreso_hospital  = fields.Date(string='Fecha de ingreso al HUAPA', help='Fecha de ingreso al Hospital')

	# DEF CALCULAR EDAD.
	# EDAD
	def calcularEdad(self):
		edad_actual = fecha_nacimiento - fecha_ingreso_hospital;
		return int(edad_actual/365)
	edad = fields.Integer(calculate=calcularEdad)

	# PESO CORPORAL
	peso_corporal = fields.Float(string='Peso corporal', help='Peso corporal del paciente')

	# FAMILIAR ENCARGADO
	familiar_encargado = fields.Many2one('admision.familiar', 'Familiar')
	
	# DIAGNOSTICO DE INGRESO AL HOSPITAL.
	diagnostico_hospital = fields.Many2one('admision.diagnostico', 'Diagnóstico HUAPA')

	# EXAMEN DE INGRESO AL HOSPITAL.
	examen_hospital = fields.Many2one('admision.examenfisico', 'Examen físico HUAPA')
