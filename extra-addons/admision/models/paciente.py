# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta

class Paciente(models.Model):

	_name = "admision.paciente"
	_rec_name = "nombre"
	# NUMERO DE HISTORIA CLINICA
	historia_id = fields.Many2one('admision.historia', string='Historia')

	# FECHA DE NACIMIENTO
	fecha_nacimiento  = fields.Date(string='Fecha de nacimiento', help='Fecha de nacimiento', required=True)
	
	# NOMBRE
	nombre = fields.Char(string='Nombre completo', translate=True, help='Nombre completo del paciente', required=True)

	# SEXO.
	sexo = fields.Selection([(0,"Femenino"),(1,"Masculino")], default=0, string="Sexo")
	
	# COLOR DE PIEL.
	color_piel = fields.Selection([(0,"Morena"),(1,"Blanca")], string="Color de piel", default=0)
	
	# CI
	ci = fields.Char(string='Cédula de identidad', size=9, help='Cédula de identidad')
	
	# Lugar de nacimiento
	lugar_nacimiento = fields.Text(string="Lugar de nacimiento", translate=True, help='Lugar de nacimiento')

	# DIRECCIÓN ACTUAL
	direccion1 = fields.Char("Dirección 1")
	direccion2 = fields.Char("Dirección 2")
	ciudad = fields.Many2one("admision.ciudad", string="Ciudad")
	pais_id = fields.Many2one('res.country','Pais')
	estado_id = fields.Many2one('res.country.state','Estado')

	

	# FECHA DE INGRESO AL HOSPITAL
	fecha_ingreso_hospital  = fields.Date(string='Fecha de ingreso al HUAPA', help='Fecha de ingreso al Hospital', required=True)
	
	edad = fields.Char(
	    string='Edad del paciente',
	    calculate="_calcularEdad",
	    store=True,
	)
	# CORREGIR ERRORES DEL CALCULO DE EDAD
	@api.onchange('fecha_nacimiento')
	def _calcularEdad(self):
		if self.fecha_nacimiento:
			# Error existe en el calculo de la edad
			fecha_nacimiento = fields.Date.from_string(self.fecha_nacimiento)
			fecha_actual = fields.Date.from_string(datetime.now().strftime("%Y-%m-%d"))
			total = int(abs(((fecha_nacimiento - fecha_actual).days) / 365))
			self.edad = total 

	# PESO CORPORAL
	peso_corporal = fields.Float(string='Peso corporal', help='Peso corporal del paciente')

	# FAMILIAR ENCARGADO
	familiar_id = fields.Many2many('admision.familiar', string='Familiares encargados')
	
	# DIAGNOSTICO DE INGRESO AL HOSPITAL.
	diagnostico_id = fields.Many2one('admision.diagnostico', string='Diagnóstico HUAPA', ondelete='cascade')

	# EXAMEN DE INGRESO AL HOSPITAL.
	examen_id = fields.Many2one('admision.examenfisico', string='Examen físico HUAPA', ondelete='cascade')

	