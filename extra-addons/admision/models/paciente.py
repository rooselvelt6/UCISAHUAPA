# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta

class Paciente(models.Model):

	_name = "admision.paciente"

	# NUMERO DE HISTORIA CLINICA
	id_historia = fields.Many2one('admision.historia', string='Historia', ondelete='cascade')

	# FECHA DE NACIMIENTO
	fecha_nacimiento  = fields.Date(string='Fecha de nacimiento', help='Fecha de nacimiento')
	
	# NOMBRE
	nombre = fields.Char(string='Nombre', translate=True, help='Nombre del paciente')

	# SEXO.
	sexo = fields.Selection([(0,"Femenino"),(1,"Masculino")])
	
	# COLOR DE PIEL.
	color_piel = fields.Selection([(0,"Morena"),(1,"Blanca")], string="Color de piel", default=0)
	
	# CI
	ci = fields.Char(string='Cédula de identidad', size=9, help='Cédula de identidad')
	
	# LUGAR DE NACIMIENTO
	lugar_nacimiento = fields.Char(string="Lugar de nacimiento", translate=True, help='Lugar de nacimiento')

	# DIRECCIÓN ACTUAL
	direccion = fields.Text(string="Dirección actual", translate=True, help='Dirección actual')

	# FECHA DE INGRESO AL HOSPITAL
	fecha_ingreso_hospital  = fields.Date(string='Fecha de ingreso al HUAPA', help='Fecha de ingreso al Hospital')
	
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



		else:
			return {
				"warning":{
					'title':"Ha ocurrido un error",
					'message':"{0}".format(self.edad)
				}
			}

	        
	# PESO CORPORAL
	peso_corporal = fields.Float(string='Peso corporal', help='Peso corporal del paciente')

	# FAMILIAR ENCARGADO
	familiar_encargado = fields.Many2one('admision.familiar', string='Familiar', ondelete='cascade')
	
	# DIAGNOSTICO DE INGRESO AL HOSPITAL.
	diagnostico_hospital = fields.Many2one('admision.diagnostico', string='Diagnóstico HUAPA', ondelete='cascade')

	# EXAMEN DE INGRESO AL HOSPITAL.
	examen_hospital = fields.Many2one('admision.examenfisico', string='Examen físico HUAPA', ondelete='cascade')

	