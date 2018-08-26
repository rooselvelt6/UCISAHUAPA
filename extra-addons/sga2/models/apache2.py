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
			# CALCULO DE VARIABLES
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




# class sga2(models.Model):
#     _name = 'sga2.sga2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100