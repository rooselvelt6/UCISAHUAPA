# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Admision(models.Model):
	_name = "admision.admision"
	_description = "Admisiones"
	_rec_name = "datos_paciente"

	estadia_hospitalaria = fields.Integer(calculate="_calcularEstadiaH", store=True, string="Estadía Hospitalaría General")

	@api.onchange('fecha_ingreso_uci')
	def _calcularEstadiaH(self):
		if self.fecha_ingreso_uci:
			HUAPA = fields.Date.from_string(self.datos_paciente.fecha_ingreso_hospital)
			UCI = fields.Date.from_string(self.fecha_ingreso_uci)
			self.estadia_hospitalaria = int(abs(((HUAPA - UCI).days)))
			

	usuario_id = fields.Many2one('res.users', string='Responsable de la admisión', index=True, track_visibility='onchange', default=lambda self: self.env.user)

	# FOTO DEL PACIENTE
	foto  = fields.Binary(string="Imagen del paciente", help='Imagen del paciente admitido', attachment=True)

	# ANTECEDENTES DE INGRESO
	antecedentes = fields.Html(translate=True, help='Antecedentes del paciente')
	
	# FECHA INGRESO A UCI
	fecha_ingreso_uci = fields.Date(string="Fecha de ingreso a UCI", help='Fecha de Ingreso a UCI')
	
	# DATOS DEL PACIENTE.
	datos_paciente = fields.Many2one('admision.paciente', string='Paciente', ondelete='cascade', index=True, track_visibility='onchange', help="Datos del paciente")

	# RESUMEN DE INGRESO A UCI
	resumen_ingreso  = fields.Html(string='Resumen general de ingreso', translate=True, help='Resumen de ingreso del paciente')

	# EXAMEN FISICO DE INGRESO A UCI
	examen_fisico_uci = fields.Many2one('admision.examenfisico', 
										string='Examen de ingreso a UCI', 
										ondelete='cascade', 
										
										track_visibility='onchange', 
										help="Examen físico de ingreso a UCI")

	# DIAGNOSTICO DE INGRESO A UCI
	diagnostico_uci = fields.Many2one('admision.diagnostico', string='Diagnóstico de ingreso a UCI', ondelete='cascade', track_visibility='onchange', help="Diágnostico de ingreso a UCI")
	
	# EVALUACION GENERAL DE INGRESO
	evaluacion_general = fields.Many2one('admision.evaluacion', string='Evaluación', ondelete='cascade', track_visibility='onchange', help="Evaluación de ingreso a UCI")
