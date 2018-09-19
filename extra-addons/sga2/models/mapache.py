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

			# CALCULO DEL PUNTAJE DE LAS VARIABLES
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

	mortalidad_max = fields.Integer(default=85)
	# FECHA DEL SISTEMA
	fecha_actual = fields.Date()

	# VARIABLES FISIOLOGICAS DEL PACIENTE SOLICITADAS AL USUARIO
	
	# TEMPERATURA
	temperatura = fields.Float(digits=(2,1), string="Temperatura °C", help='Temperatura rectal (Axial +0.5°C)')
	
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
	na = fields.Integer(string="Sodio Sérico", help='Na sérico (mEq/l)')

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
	oxigenacion = fields.Integer("Valor de Oxigenación", help='Oxigenación')

	# SISTEMA GLASGOW

	# APERTURA OCULAR
	apertura_ocular = fields.Selection([(1,"No responde"),
										(2,"Dolor"),
										(3,"Orden verbal"),
										(4,"Espontánea")])

	# RESPUESTA VERBAL.	
	respuesta_verbal = fields.Selection([(1,"Ninguna respuesta"),
										(2,"Sonidos incomprensibles"),
										(3,"Palabras inapropiadas"),
										(4,"Desorientado y hablando"),
										(5,"Orientado y conversando")
										])

	# RESPUESTA MOTORA.
	respuesta_motora = fields.Selection([(1,"Ninguna respuesta"),
										(2,"Extensión"),
										(3,"Flexión anormal"),
										(4,"Retirada y flexión"),
										(5,"Localiza el dolor"),
										(6,"Obedece ordenes verbales")
										])

	

	# EDAD DEL PACIENTE.
	edad = fields.Integer(string="Edad del paciente", help='Edad del paciente') # campo referencial por modelo

	# ENFERMEDAD CRONICA DOCUMENTACIÓN
	"""documentacion = [
		"CARDIOVASCULAR: NYHA IV",
		"RENAL: Hemodialisis",
		"RESPIRATORIO: EPOC, enfermedad restictiva o vascular que limita actividad funcional, Hipoxia cronica y/o hipercapnia; dependencia respiratoria, Policitemia o hipertension pulmonar severa (40>mmHg)",
		"HEPATICO: Cirrosis (por biopsia), Encefalopatia previa, Hipertension portal documentada Historia de hemorragia digestiva debida hipertension portal",
		"INMUNOSUPRESION: [Farmacologico:quimioterapia, radioterapia, esteroides, SIDA, linfoma, leucemias]",
	]"""

	# ENFERMEDADES CRONICAS.
	enfermedades = fields.Selection([(0,'NINGUNA'), 
									 (2,'ELECTIVA'), 
									 (5,"NO-QUIRURGICA"), 
									 (5,"URGENTE")], 
									 )
									
	# INDICADORES DE GRAVEDAD Y MORTALIDAD
	
	# APS
	aps = fields.Integer(string='APS')

	# APACHE
	apache = fields.Integer(string='APACHE')
	
	# MORTALIDAD
	mortalidad = fields.Integer(string='Mortalidad')

	# CONTROL DE BOTONES
	@api.multi
	def controlados(self):
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
			x.aps = 0
			x.apache = 0
			x.mortalidad = 0
			# INDIVIDUO SANO
			x.apertura_ocular = 4
			x.respuesta_verbal = 5
			x.respuesta_motora = 6
			x.edad = 1
		return True
	
	@api.onchange('temperatura','pam','fc','fr','ph','hco3','na','k','creatinina','fallo_renal','hematocrito','leucocitos','fio2','oxigenacion','apertura_ocular','respuesta_verbal','respuesta_motora','enfermedades','edad')
	def _calcular_resultados(self):
		# OBTENCIÓN DEL PUNTAJE POR VARIABLES FISIOLOGICAS
		self._temperatura(); 
		self._presionArterialMedia() 
		self._frecuenciaCardiaca() 
		self._frecuenciaRespiratoria()
		self._phArterial()
		self._hco3Serico()
		self._naSerico() 
		self._kSerico()
		self._creatininaSerica()
		self._hematocrito()
		self._leucocitos()
		self._oxigenacion()
		self._calcularGlasgow()
		# PUNTAJE CRONICO DE ENFERMEDADES PARA EL CÁLCULO DEL APACHE II
		self._puntajeCronico()
		self._puntajeEdad()
		# ESTIMACIÓN DEL PORCENTAJE DE MORTALIDAD.
		self._calcularMortalidad()
			
	# FUNCIONES DE CALCULO DEL SISTEMA	
	@api.depends('aps') # variables dependientes
	def _temperatura(self):
		datos = dict(); # MEMORIA DE DATOS 

		# RECORRER REGISTRO ACTUAL.
		for x in self:
			# NOMBRE DE LA VARIABLE ACTUAL
			datos["nombre"] = "Temperatura";

			# VALOR OBTENIDO DE LA INTERFAZ DE USUARIO EN EL REGISTRO ACTUAL
			datos["valor_actual"] = float(x.temperatura);

			# EVALUACION DEL RANGO Y PUNTAJE
			if(datos["valor_actual"] <= 29.9):
				# TIPO DE RANGO
				datos["rango"] = "BAJO";
				# PUNTAJE OBTENIDO POR EL VALOR ACTUAL
				datos["puntos"] = int(4);

			elif(datos["valor_actual"] >= 30.0 and datos["valor_actual"] <= 31.9):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(3);

			elif(datos["valor_actual"] >= 32.0 and datos["valor_actual"] <=33.9):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 34.0 and datos["valor_actual"] <=35.9):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(1)

			elif(datos["valor_actual"] >= 36.0 and datos["valor_actual"] <=38.4):
				datos["rango"] = "MEDIO"
				datos["puntos"] = int(0)

			elif(datos["valor_actual"] >= 38.5 and datos["valor_actual"] <=38.9):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(1)

			elif(datos["valor_actual"] >= 39.0 and datos["valor_actual"] <=40.9):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 41):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(4)

			else:
				datos["error"] = "Valor fuera del rango de valores"

			# GUARDAR DATOS EN LA VARIABLE APS SOLO EL PUNTAJE PARA ESTA VERSION
			x.aps = datos["puntos"]

	# PAM
	@api.depends('aps')
	def _presionArterialMedia(self):
		datos = dict()
		for x in self:
			datos["nombre"] = "Presion arterial media (mmHg)"
			datos["valor_actual"] = int(x.pam)
			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] <= 49):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(4)

			elif(datos["valor_actual"] >= 50 and datos["valor_actual"] <= 69):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 70 and datos["valor_actual"] <= 109):
				datos["rango"] = "MEDIO"
				datos["puntos"] = int(0)

			elif(datos["valor_actual"] >= 110 and datos["valor_actual"] <= 129):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 130 and datos["valor_actual"] <= 159):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 160):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(4)

			else:
				datos["error"] = "Valor fuera del rango de valores"

			x.aps += datos["puntos"]
	
	# FC
	@api.depends('aps')
	def _frecuenciaCardiaca(self):
		# Registro de variables
		datos = dict()
		for x in self:
			datos["nombre"] = "Frecuencia cardíaca (respuesta ventricular)"

			datos["valor_actual"] = int(x.fc)

			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] <= 39.9):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(4)

			elif(datos["valor_actual"] >= 40 and datos["valor_actual"] <= 54):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 55 and datos["valor_actual"] <= 69):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 70 and datos["valor_actual"] <= 109):
				datos["rango"] = "MEDIO"
				datos["puntos"] = int(0)

			elif(datos["valor_actual"] >= 110 and datos["valor_actual"] <= 139):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 140 and datos["valor_actual"] <= 179):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 180):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(4)
			else:
				datos["error"] = "Valor fuera del rango de valores"

			# AUMENTAR APS	
			x.aps += datos["puntos"]
			
	# FR
	@api.depends('aps')
	def _frecuenciaRespiratoria(self):
		# Registro de variables
		datos = dict()
		for x in self:
			datos["nombre"] = "Frecuencia respiratoria (no ventilado o ventilado)"

			datos["valor_actual"] = int(x.fr)

			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] <= 5):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(4)

			elif(datos["valor_actual"] >= 6 and datos["valor_actual"] <= 9):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 10 and datos["valor_actual"] <= 11):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(1)

			elif(datos["valor_actual"] >= 12 and datos["valor_actual"] <= 24):
				datos["rango"] = "MEDIO"
				datos["puntos"] = int(0)

			elif(datos["valor_actual"] >= 25 and datos["valor_actual"] <= 34):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(1)

			elif(datos["valor_actual"] >= 35 and datos["valor_actual"] <= 49):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 50):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(4)
			else:
				datos["error"] = "Valor fuera del rango de valores"

			# AUMENTAR APS	
			x.aps += datos["puntos"]

	# ph
	@api.depends('aps')
	def _phArterial(self):
		# Registro de variables
		datos = dict()
		for x in self:
			datos["nombre"] = "pH arterial (Preferido)"

			datos["valor_actual"] = float(x.ph)

			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] < 7.15):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(4)

			elif(datos["valor_actual"] >= 7.15 and datos["valor_actual"] <= 7.24):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 7.25 and datos["valor_actual"] <= 7.32):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 7.33 and datos["valor_actual"] <= 7.49):
				datos["rango"] = "MEDIO"
				datos["puntos"] = int(0)

			elif(datos["valor_actual"] >= 7.50 and datos["valor_actual"] <= 7.59):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(1)

			elif(datos["valor_actual"] >= 7.60 and datos["valor_actual"] <= 7.69):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 7.70):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(4)
			else:
				datos["error"] = "Valor fuera del rango de valores"

			# AUMENTAR APS	
			x.aps += datos["puntos"]

	# HC03
	@api.depends('aps')
	def _hco3Serico(self):
		# Registro de variables
		datos = dict()
		for x in self:
			datos["nombre"] = "HCO3 SERICO (venoso mEq/l)"

			datos["valor_actual"] = float(x.hco3)

			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] < 15.0):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(4)

			elif(datos["valor_actual"] >= 15.0 and datos["valor_actual"] <= 17.9):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 18.0 and datos["valor_actual"] <= 21.9):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 22.0 and datos["valor_actual"] <= 31.9):
				datos["rango"] = "MEDIO"
				datos["puntos"] = int(0)

			elif(datos["valor_actual"] >= 32.0 and datos["valor_actual"] <= 40.9):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(1)

			elif(datos["valor_actual"] >= 41.0 and datos["valor_actual"] <= 51.9):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 52):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(4)
			else:
				datos["error"] = "Valor fuera del rango de valores"
			# AUMENTAR APS	
			x.aps += datos["puntos"]

	# NA
	@api.depends('aps')
	def _naSerico(self):
			
		# Registro de variables
		datos = dict()
		for x in self:
			datos["nombre"] = "Sodio Serico (mEq/l)"

			datos["valor_actual"] = int(x.na)

			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] <= 110):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(4)

			elif(datos["valor_actual"] >= 111 and datos["valor_actual"] <= 119):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 120 and datos["valor_actual"] <= 129):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 130 and datos["valor_actual"] <= 149):
				datos["rango"] = "MEDIO"
				datos["puntos"] = int(0)

			elif(datos["valor_actual"] >= 150 and datos["valor_actual"] <= 154):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(1)

			elif(datos["valor_actual"] >= 155 and datos["valor_actual"] <= 159):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 160 and datos["valor_actual"] <= 179):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 180):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(4)
			else:
				datos["error"] = "Valor fuera del rango de valores"
			x.aps += datos["puntos"]
	# K
	@api.depends('aps')
	def _kSerico(self):
		
		# Registro de variables
		datos = dict()
		for x in self:
			datos["nombre"] = "Potasio Serico (mEq/l)"

			datos["valor_actual"] = float(x.k)

			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] < 2.5):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(4)

			elif(datos["valor_actual"] >= 2.5 and datos["valor_actual"] <= 2.9):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 3.0 and datos["valor_actual"] <= 3.4):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(1)

			elif(datos["valor_actual"] >= 3.5 and datos["valor_actual"] <= 5.4):
				datos["rango"] = "MEDIO"
				datos["puntos"] = int(0)

			elif(datos["valor_actual"] >= 5.5 and datos["valor_actual"] <= 5.9):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(1)

			elif(datos["valor_actual"] >= 6.0 and datos["valor_actual"] <= 6.9):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 7):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(4)
			else:
				datos["error"] = "Valor fuera del rango de valores"
			# AUMENTAR APS	
			x.aps += datos["puntos"]

	# CREATININA
	@api.depends('aps')
	def _creatininaSerica(self):
		# Registro de variables
		datos = dict()
		for x in self:
			datos["fallo_renal"] = x.fallo_renal

			datos["nombre"] = "Creatinina serica (mg/dl)"

			datos["valor_actual"] = float(x.creatinina)

			# Evaluar Rango y valor del rango
			if(datos["fallo_renal"] == False):
				if(datos["valor_actual"] < 0.6):
					datos["rango"] = "BAJO"
					datos["puntos"] = int(2)

				elif(datos["valor_actual"] >= 0.6 and datos["valor_actual"] <= 1.4):
					datos["rango"] = "MEDIO"
					datos["puntos"] = int(0)

				elif(datos["valor_actual"] >= 1.5 and datos["valor_actual"] <= 1.9):
					datos["rango"] = "ALTO"
					datos["puntos"] = int(2)

				elif(datos["valor_actual"] >= 2.0 and datos["valor_actual"] <= 3.4):
					datos["rango"] = "ALTO"
					datos["puntos"] = int(3)

				elif(datos["valor_actual"] >= 3.5):
					datos["rango"] = "ALTO"
					datos["puntos"] = int(4)
				else:
					datos["error"] = "Valor fuera del rango de valores"
				# AUMENTAR APS	
				x.aps += datos["puntos"]
			else:
				if(datos["valor_actual"] < 0.6):
					datos["rango"] = "BAJO"
					datos["puntos"] = int(4)

				elif(datos["valor_actual"] >= 0.6 and datos["valor_actual"] <= 1.4):
					datos["rango"] = "MEDIO"
					datos["puntos"] = int(0)

				elif(datos["valor_actual"] >= 1.5 and datos["valor_actual"] <= 1.9):
					datos["rango"] = "ALTO"
					datos["puntos"] = int(4)

				elif(datos["valor_actual"] >= 2.0 and datos["valor_actual"] <= 3.4):
					datos["rango"] = "ALTO"
					datos["puntos"] = int(6)

				elif(datos["valor_actual"] >= 3.5):
					datos["rango"] = "ALTO"
					datos["puntos"] = int(8)
				else:
					datos["error"] = "Valor fuera del rango de valores"
				# AUMENTAR APS	
				x.aps += datos["puntos"]
	# HEMATOCRITO
	@api.depends('aps')
	def _hematocrito(self):
		# Registro de variables
		datos = dict()
		for x in self:
			datos["nombre"] = "Hematocrito (%)"

			datos["valor_actual"] = float(x.hematocrito)

			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] < 20.0):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(4)

			elif(datos["valor_actual"] >= 20.0 and datos["valor_actual"] <= 29.9):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 30.0 and datos["valor_actual"] <= 45.9):
				datos["rango"] = "MEDIO"
				datos["puntos"] = int(0)

			elif(datos["valor_actual"] >= 46.0 and datos["valor_actual"] <= 49.9):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(1)

			elif(datos["valor_actual"] >= 50.0 and datos["valor_actual"] <= 50.9):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 60.0):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(4)
			else:
				datos["error"] = "Valor fuera del rango de valores"

			# AUMENTAR APS	
			x.aps += datos["puntos"]
	
	# LEUCOCITOS
	@api.depends('aps')
	def _leucocitos(self):
		# Registro de variables
		datos = dict()
		for x in self:
			datos["nombre"] = "Leucocitos (Total/mm3 en miles)"

			datos["valor_actual"] = float(x.leucocitos)

			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] < 1.0):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(4)

			elif(datos["valor_actual"] >= 1.0 and datos["valor_actual"] <= 2.9):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 3.0 and datos["valor_actual"] <= 14.9):
				datos["rango"] = "MEDIO"
				datos["puntos"] = int(0)

			elif(datos["valor_actual"] >= 15.0 and datos["valor_actual"] <= 19.9):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(1)

			elif(datos["valor_actual"] >= 20.0 and datos["valor_actual"] <= 39.9):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 40.0):
				datos["rango"] = "ALTO"
				datos["puntos"] = int(4)
			else:
				datos["error"] = "Valor fuera del rango de valores"
			# AUMENTAR APS	
			x.aps += datos["puntos"]
	
	# OXIGENACION
	@api.depends('aps')
	def _oxigenacion(self):
		
		# Registro de variables
		datos = dict()
		for x in self:
			datos["nombre"] = "Oxigenacion"

			datos["Fi02"] = float(x.fio2)
			datos["valor_actual"] = int(x.oxigenacion)

			if(datos["Fi02"] < 0.5):
				datos["valor_medido"] = "PaO2"

				# Evaluar Rango y valor del rango
				if(datos["valor_actual"] <= 55):
					datos["puntos"] = int(4)
					datos["rango"] = "BAJO"

				elif(datos["valor_actual"] > 55 and datos["valor_actual"] <= 60):
					datos["puntos"] = int(3)
					datos["rango"] = "BAJO"

				elif(datos["valor_actual"] >= 61 and datos["valor_actual"] <= 70):
					datos["puntos"] = int(1)
					datos["rango"] = "BAJO"

				elif(datos["valor_actual"] > 70):
					datos["puntos"] = int(0)
					datos["rango"] = "MEDIO"
				else:
					datos["error"] = "Valor fuera del rango de valores"
				# AUMENTAR APS	
				x.aps += datos["puntos"]
			else:
				datos["valor_medido"] = "A-aDO2"

				# Evaluar Rango y valor del rango
				if(datos["valor_actual"] < 200):
					datos["puntos"] = int(0)
					datos["rango"] = "MEDIO"

				elif(datos["valor_actual"] >= 200 and datos["valor_actual"] <= 349):
					datos["puntos"] = int(2)
					datos["rango"] = "ALTO"

				elif(datos["valor_actual"] >= 350 and datos["valor_actual"] <= 499):
					datos["puntos"] = int(3)
					datos["rango"] = "ALTO"

				elif(datos["valor_actual"] >= 500):
					datos["puntos"] = int(4)
					datos["rango"] = "ALTO"
				else:
					datos["error"] = "Valor fuera del rango de valores"
				# AUMENTAR APS	
				x.aps += datos["puntos"]
	
	# GLASGOW 
	@api.depends('aps')
	def _calcularGlasgow(self):
		glasgow = 0 # CONTADOR
		for x in self: # RECORRER EL FORMULARIO Y OBTENER LOS VALORES
			# SUMAR LAS VARIABLES DEL GLASGOW
			glasgow = int(15) - int(x.apertura_ocular + x.respuesta_verbal + x.respuesta_motora);
			# SUMAR AL APACHE EL RESULTADO DEL GLASGOW
			x.aps += glasgow;

	# PUNTAJE POR ENFERMEDAD 
	@api.depends('apache', 'aps')
	def _puntajeCronico(self):
		# REGISTRo
		datos = dict()
		for x in self:
			datos["nombre"] = "Enfermedad Cronica"
			#datos["opciones"] = {"NINGUNA":0, "ELECTIVA":2, "NO-QUIRURGICA":5, "URGENTE":5}
			datos["valor"] = x.enfermedades
			#datos["puntos"] = datos["opciones"][datos["valor"]]
			x.apache = (x.aps + datos["valor"])
	
	# PUNTAJE POR LA EDAD DEL PACIENTE
	@api.depends('apache','aps')
	def _puntajeEdad(self):
		""" Evaluar puntaje en base a la edad """

		# Registro de variables
		datos = dict()
		for x in self:
			datos["nombre"] = "Puntaje por edad"

			datos["valor_actual"] = int(x.edad)

			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] <= 44):
				datos["puntos"] = int(0)

			elif(datos["valor_actual"] >= 45 and datos["valor_actual"] <= 54):
				datos["puntos"] = int(2)

			elif(datos["valor_actual"] >= 55 and datos["valor_actual"] <= 64):
				datos["puntos"] = int(3)

			elif(datos["valor_actual"] >= 65 and datos["valor_actual"] <= 74):
				datos["puntos"] = int(5)

			elif(datos["valor_actual"] >= 75):
				datos["puntos"] = int(6)
			else:
				datos["error"] = "Valor fuera del rango de valores"
			# AUMENTO DEL APACHE EN BASE A LA EDAD DEL PACIENTE
			x.apache += datos["puntos"] 

	# ESTIMACIÓN DE LA MORTALIDAD
	@api.depends('apache')
	def _calcularMortalidad(self):
		""" Evaluar el porcentaje de mortalidad basado en la gravedad """
		# Registro de variables
		datos = dict()
		for x in self:
			datos["nombre"] = "Prediccion de mortalidad"

			datos["valor_actual"] = int(x.apache)

			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] >= 0 and datos["valor_actual"] <= 4):
				datos["puntos"] = int(4)

			elif(datos["valor_actual"] >= 5 and datos["valor_actual"] <= 9):
				datos["puntos"] = int(8)

			elif(datos["valor_actual"] >= 10 and datos["valor_actual"] <= 14):
				datos["puntos"] = int(15)

			elif(datos["valor_actual"] >= 15 and datos["valor_actual"] <= 19):
				datos["puntos"] = int(25)

			elif(datos["valor_actual"] >= 20 and datos["valor_actual"] <= 24):
				datos["puntos"] = int(40)

			elif(datos["valor_actual"] >= 25 and datos["valor_actual"] <= 29):
				datos["puntos"] = int(55)

			elif(datos["valor_actual"] >= 30 and datos["valor_actual"] <= 34):
				datos["puntos"] = int(75)

			elif(datos["valor_actual"] >= 34):
				datos["puntos"] = int(85)
			else:
				datos["error"] = "Valor fuera del rango de valores"
			
			x.mortalidad = datos["puntos"]