# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Apache(models.Model):

	""" Indice de gravedad APACHE II 

	Args:
		glasgow.Glasgow: El sistema de coma glasgow que requiere el paciente.
	
	Returns:
		Diccionario de información con el reporte del sistema.

	PROCESO A SEGUIR POR EL SISTEMA:

			# INSTANCIA
				ap = Apache()
			# SOLICITUD DE LAS VARIABLES

			# CALCULO DEL PUNTAJE DE LAS VARIABLES INGRESADAS
				ap.temperatura()
				ap.presionArterialMedia()
				ap.frecuenciaCardiaca()
				ap.frecuenciaRespiratoria()
				ap.phArterial()
				ap.hco3Serico()
				ap.naSerico()
				ap.kSerico()
				ap.creatininaSerica()
				ap.hematocrito()
				ap.leucocitos()
				ap.oxigenacion()
				# ESCALA DE COMA GLASGOW
				ap.glasgow()
			# GENERAR INDICADORES.
				ap.calcularAPS()
				ap.evaluarEdad(74)
				ap.evaluarPuntajeCronico()
				ap.calcularApache()
			# RESULTADOS
				ap.generarReporte(True)
				pprint(ap.getReporte())
	"""
	_name = 'apache.apache'

	# FECHA DEL SISTEMA
	fecha_actual = fields.Date()

	# VARIABLES FISIOLOGICAS DEL PACIENTE SOLICITADAS AL USUARIO
	
	# TEMPERATURA
	temperatura = fields.Float(string="Temperatura °C", help='Temperatura rectal (Axial +0.5°C)')
	
	# PRESION ARTERIAL MEDIA
	pam = fields.Integer(string="Presión arterial media (mmHg)")

	# FRECUENCIA CARDIACA
	fc = fields.Integer(string="Frecuencia cardíaca", help='Respuesta ventricular')

	# FRECUENCIA RESPIRATORIA
	fr = fields.Integer(string="Frecuencia respiratoria", help='No ventilado o ventilado')

	# PH ARTERIAL
	ph = fields.Float(string='pH arterial', help='Preferido')

	# HCO3 SERICO
	hco3 = fields.Float(string='HCO3 SÉRICO', help='Venoso mEq/l')

	# NA SERICO
	na = fields.Float(string="Sodio Sérico", help='Na sérico (mEq/l)')

	# K SERICO
	k = fields.Float(string="Potasio Sérico", help="K sérico (mEq/l)")

	# CREATININA SERICA DEPENDE DEL FALLO RENAL
	creatinina  = fields.Float(string='Creatinina sérica', help='(mg/dl)')

	# FALLO RENAL PARA LA CREATININA SERICA
	fallo_renal =  fields.Boolean(string='Fallo renal', help='¿El paciente tiene fallas renales ? (Creatinina sérica)', required=True)

	# HEMATOCRITO
	hematocrito = fields.Float(string="Hematocrito", help="(%)")

	# LEUCOCITOS
	leucocitos = fields.Float(string="Leucocitos", help='(Total/mm3 en miles)')

	# OXIGENACIÓN (VALOR DE FI02)
	fio2 = fields.Float("Fi02", help='Oxigenación')

	# OXIGENACIÓN
	oxigenacion = fields.Float("Valor de Oxigenación", help='Oxigenación')

	# SISTEMA GLASGOW

	# APERTURA OCULAR
	apertura_ocular = fields.Integer(string="Apertura Ocular", help='Valor de apertura ocular. Rango:(1-4)')

	# RESPUESTA MOTORA.
	respuesta_motora = fields.Integer(string="Respuesta Motora", help='Valor de la respuesta motora. Rango:(1-6)')

	# RESPUESTA VERBAL.
	respuesta_verbal = fields.Integer(string="Respuesta verbal", help='Valor de la respuesta verbal. Rango:(1-5)')

	# CONTROL DE INDICADORES
	
	# APS
	aps = fields.Integer(string='APS')
	
	# APACHE
	apache = fields.Integer(string='APACHE')
	
	# MORTALIDAD
	mortalidad = fields.Integer(string='Mortalidad')

	# CONTROL DE BOTONES DEL SIMULADOR APACHE II

	@api.multi
	def limpiar(self):
		for x in self:
			# PACIENTE EN PERFECTO ESTADO DE SALUD
			x.temperatura = 37
			x.pam = 70
			x.fc = 70
			x.fr = 12
			x.ph = 7.33
			x.hco3 = 22
			x.na = 130
			x.k = 3.5
			x.creatinina = 0.6
			x.fallo_renal = False
			x.hematocrito = 30.0
			x.leucocitos = 3
			x.fio2 = 0.6
			x.oxigenacion = 71
			# INDIVIDUO SANO
			x.apertura_ocular = 4
			x.respuesta_motora = 5
			x.respuesta_verbal = 6
		return True

	@api.multi
	def calcular(self):
		pass



# class sga2(models.Model):
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100