#!/usr/bin/env python
# -*- coding: "utf-8" -*-
# Autor: Ranielt Angulo, Rooselvelt Angulo
# Fecha: 31/01/18 
# Versión: 1.1

""" Sistema APACHE II:
		El score: Acute Physiology and Chronic Health Evaluation II 
		(APACHE II), es un sistema de valoración pronostica de mortalidad, 
		que consiste en detectar los trastornos fisiológicos agudos 
		que atentan contra la vida del paciente y se fundamenta en la 
		determinación de las alteraciones de variables fisiológicas y de 
		parámetros de laboratorio, cuya puntuación es un factor 
		predictivo de mortalidad, siendo este índice válido para un amplio 
		rango de diagnósticos, fácil de usar y que puede sustentarse en datos 
		disponibles en la mayor parte de las UCI (Knaus et al., 1985).
		
		El índice APACHE II es calculado en el momento de ingreso o al final 
		del día de internación del paciente, por lo tanto la misma, brinda un 
		perfil momentáneo del estado del internado, no pudiendo 
		aportar información dinámica.
"""
import sys
import glasgow 
from datetime import datetime
from pprint import pprint

class Apache(glasgow.Glasgow):

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
	def __init__(self):
		""" Constructor """

		# Iniciar el constructor del glasgow
		super().__init__()

		# Nombre del sistema
		self.nombre = str("APACHE II")

		# Fecha actual de cálculo
		self.fecha_actual = datetime.now().strftime("%d/%b/%Y/%X/%p")

		# Historial de variables calculadas
		self.historial = list()

		# Reporte general
		self.reporte = dict()

		# INDICADORES DE GRAVEDAD Y MORTALIDAD

		# APS: Sumatoria de todas las variables fisiológicas
		self.APS = 0

		# Puntaje obtenido en base a la edad:
		self.puntos_edad = None 

		# Puntaje obtenido en base a la enfermedad:
		self.puntos_cronico = None 

		# APACHE II: Gravedad del paciente.
		self.APACHE = int(0)

		# Mortalidad
		self.mortalidad = int(0)

	# METODOS DEL OBJETO

	def __str__(self):
		return "{}".format(self.nombre)

	def getNombre(self):
		""" Obtener el nombre de la aplicación """
		return self.nombre

	def getFecha(self):
		""" Obtener la fecha de cálculo del sistema """
		return self.fecha_actual

	def getHistorial(self):
		""" Obtener el historial de variables fisiológicas calculadas """
		return self.historial

	def getCantidadVariables(self):
		""" Obtener la cantidad de variables medidas en una instancia de APACHE II """
		return len(self.historial)

	def getAPS(self):
		""" Obtener el APS """
		return self.APS

	def getPuntosEdad(self):
		""" Obtener el puntaje basado en la edad """
		return self.puntos_edad

	def getPuntajeCronico(self):
		return self.puntos_cronico

	def getAPACHE(self):
		""" Obtener la gravedad del paciente """
		return self.APACHE

	def getMortalidad(self):
		""" Obtener la mortalidad del paciente """
		return self.mortalidad

	def getReporte(self):
		""" Obtener reporte """
		return self.reporte

	# METODOS PARA CALCULO DE VARIABLES FISIOLÓGICAS
	def temperatura(self, valor=37):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Temperatura rectal (Axial +0.5°C)"

			datos["valor_actual"] = float(valor)

			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] <= 29.9):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(4)

			elif(datos["valor_actual"] >= 30.0 and datos["valor_actual"] <=31.9):
				datos["rango"] = "BAJO"
				datos["puntos"] = int(3)

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

		except ValueError as e:
			 print("No pude convertir el valor")
		
		# Agregar datos al historial
		self.historial.append(datos)
		#return datos

	def presionArterialMedia(self, valor=70):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Presión arterial media (mmHg)"

			datos["valor_actual"] = int(valor)

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

		except ValueError as e:
			 print("No pude convertir el valor ")
		
		# Agregar datos al historial
		self.historial.append(datos)
		#return datos

	def frecuenciaCardiaca(self, valor=70):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Frecuencia cardíaca (respuesta ventricular)"

			datos["valor_actual"] = int(valor)

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

		except ValueError as e:
			 print("No pude convertir el valor")
		
		# Agregar datos al historial
		self.historial.append(datos)

	def frecuenciaRespiratoria(self, valor=12):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Frecuencia respiratoria (no ventilado o ventilado)"

			datos["valor_actual"] = int(valor)

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

		except ValueError as e:
			 print("No pude convertir el valor")
		
		# Agregar datos al historial
		self.historial.append(datos)
	
	def phArterial(self, valor=7.33):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "pH arterial (Preferido)"

			datos["valor_actual"] = float(valor)

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

		except ValueError as e:
			 print("No pude convertir el valor")
		
		# Agregar datos al historial
		self.historial.append(datos)

	def hco3Serico(self, valor=22):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "HCO3 SÉRICO (venoso mEq/l)"

			datos["valor_actual"] = float(valor)

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

		except ValueError as e:
			 print("No pude convertir el valor")
		
		# Agregar datos al historial
		self.historial.append(datos)

	def naSerico(self, valor=130):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Sodio Sérico (mEq/l)"

			datos["valor_actual"] = int(valor)

			# Evaluar Rango y valor del rango
			if(datos["valor_actual"] < 110):
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

		except ValueError as e:
			 print("No pude convertir el valor")
		
		# Agregar datos al historial
		self.historial.append(datos)

	def kSerico(self, valor=3.5):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Potasio Sérico (mEq/l)"

			datos["valor_actual"] = float(valor)

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

		except ValueError as e:
			 print("No pude convertir el valor")
		
		# Agregar datos al historial
		self.historial.append(datos)

	def creatininaSerica(self, valor=0.6, fallo_renal=False):
		try:
			# Registro de variables
			datos = dict()

			datos["fallo_renal"] = fallo_renal

			datos["nombre"] = "Creatinina sérica (mg/dl)"

			datos["valor_actual"] = float(valor)

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


		except ValueError as e:
			 print("No pude convertir el valor")
		
		# Agregar datos al historial
		self.historial.append(datos)

	def hematocrito(self, valor=30.0):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Hematocrito (%)"

			datos["valor_actual"] = float(valor)

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

		except ValueError as e:
			 print("No pude convertir el valor")
		
		# Agregar datos al historial
		self.historial.append(datos)

	def leucocitos(self, valor=3):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Leucocitos (Total/mm3 en miles)"

			datos["valor_actual"] = float(valor)

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

		except ValueError as e:
			 print("No pude convertir el valor")
		
		# Agregar datos al historial
		self.historial.append(datos)

	def oxigenacion(self, Fi02=0.6, valor=71):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Oxigenación"

			datos["Fi02"] = float(Fi02)
			datos["valor_actual"] = int(valor)

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

				elif(datos["valor_actual"] > 500):
					datos["puntos"] = int(4)
					datos["rango"] = "ALTO"
				else:
					datos["error"] = "Valor fuera del rango de valores"
		except ValueError as e:
			 print("No pude convertir el valor")

		# Agregar datos al historial
		self.historial.append(datos)

	def glasgow(self, aperturaOcular=1, respuestaMotora=1, respuestaVerbal=1):
		""" Escala de coma Glasgow """

		datos = dict()
		datos["nombre"] = "Escala de coma Glasgow"
		datos["valor"] = aperturaOcular, respuestaMotora, respuestaVerbal
		
		self.apertura_ocular(datos["valor"][0])
		self.respuesta_motora(datos["valor"][1])
		self.respuesta_verbal(datos["valor"][2])

		datos["puntos"] = self.get_ecg()
		datos["estado"] = self.get_estado()
		
		self.historial.append(datos)

	# INDICADORES DEL SISTEMA

	def calcularAPS(self):
		""" Sumatoria del puntaje de todas las variables medidas """
		total = 0
		for variable in self.historial:
			total += variable["puntos"]
		self.APS = int(total)

	def evaluarEdad(self, valor=44):
		""" Evaluar puntaje en base a la edad """
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Puntaje por edad"

			datos["valor_actual"] = int(valor)

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

		except ValueError as e:
			 print("No pude convertir el valor")

		self.puntos_edad = datos
	
	def evaluarPuntajeCronico(self, tipo_cirugia="NINGUNA"):
			try:
				# registro
				self.datos = {}
			
				self.datos["nombre"] = "Enfermedad Crónica"
					
				self.datos["descripcion"] = {
													"Cardiovascular":"NYHA IV",
													"RENAL":"Hemodiálisis",
													"RESPIRATORIO":["EPOC, enfermedad restictiva o vascular que limita actividad funcional",
																	"Hipoxia crónica y/o hipercapnia; dependencia respiratoria",
																	"Policitemia o hipertensión pulmonar severa (40>mmHg)"
																	],
													"HEPATICO":["Cirrosis (por biopsia)",
																"Encefalopatía previa",
																"Hipertensión portal documentada",
																"Historia de hemorragía digestiva debidaa hipertensión portal",
																],
													"INMUNOSUPRESION":["Farmacológico:quimioterapia, radioterapia, esteroides", "SIDA, linfoma, leucemias"]
												}
				self.datos["opciones"] = {
												"NINGUNA":0,
											  	"ELECTIVA":2,
											  	"NO-QUIRURGICA":5,
											  	"URGENTE":5
											  }
				self.datos["valor"] = str(tipo_cirugia).upper()

				self.datos["puntos"] = self.datos["opciones"][self.datos["valor"]]

				self.puntos_cronico = self.datos

			except ValueError as e:
				return "El valor de la {} no es un número".format(self.datos["nombre"])

	def calcularApache(self):
		
		a = self.getAPS() # PUNTAJE POR VARIABLES FISIOLOGICAS
		
		b = self.getPuntosEdad()["puntos"] # PUNTAJE POR EDAD.

		c = self.getPuntajeCronico()["puntos"] # PUNTAJE POR ENFERMEDAD CRONICA
		
		self.APACHE = int(a + b + c) # GRAVEDAD DEL PACIENTE

	def calcularMortalidad(self):
		""" Evaluar el porcentaje de mortalidad basado en la gravedad """
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Predicción de mortalidad"

			datos["valor_actual"] = int(self.getAPACHE())

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

		except ValueError as e:
			 print("No pude convertir el valor")

		self.mortalidad= datos

	def generarReporte(self, detallado=False):
		""" Generar el reporte del sistema """

		if(detallado==False):

			# FECHA DE CALCULO
			self.reporte["FECHA"] = self.getFecha()

			# NOMBRE DEL SISTEMA
			self.reporte["SISTEMA"] = self.getNombre()

			# CANTIDAD DE VARIABLES MEDIDAS
			self.reporte["CANTIDAD_MEDICIONES"] = self.getCantidadVariables()

			# APS
			self.reporte["APS"] = self.getAPS()

			# GRAVEDAD APACHE II
			self.reporte["GRAVEDAD"] = self.getAPACHE()

			# MORTALIDAD
			self.reporte["MORTALIDAD"] = self.getMortalidad()

			# EDAD DEL PACIENTE
			self.reporte["EDAD"] = self.getPuntosEdad()["valor_actual"]

			# PUNTAJE POR ENFERMEDAD CRONICA
			self.reporte["PUNTOS_ENFERMEDAD_CRONICA"] = self.getPuntajeCronico()["puntos"]

		else:
	
			# FECHA DE CALCULO
			self.reporte["FECHA"] = self.getFecha()

			# NOMBRE DEL SISTEMA
			self.reporte["SISTEMA"] = self.getNombre()

			# CANTIDAD DE VARIABLES MEDIDAS
			self.reporte["CANTIDAD_MEDICIONES"] = self.getCantidadVariables()

			# APS
			self.reporte["APS"] = self.getAPS()

			# GRAVEDAD APACHE II
			self.reporte["GRAVEDAD"] = self.getAPACHE()

			# MORTALIDAD
			self.reporte["MORTALIDAD"] = self.getMortalidad()

			# EDAD DEL PACIENTE
			self.reporte["EDAD"] = self.getPuntosEdad()["valor_actual"]

			# PUNTAJE POR ENFERMEDAD CRONICA
			self.reporte["PUNTOS_ENFERMEDAD_CRONICA"] = self.getPuntajeCronico()["puntos"]

			# ESTADO FISIOLOGICO ACTUAL
			self.reporte["HISTORIAL"] = self.getHistorial()
