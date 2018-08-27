#!/usr/bin/python3
# -*- coding: utf-8 -*-
# SISTEMA REALIZADO PARA FUNCIONAR EN PYTHON 3.X
# NO ES COMPATIBLE CON PYTHON 2.X PRESENTA ERRORES CON LA FUNCION SUPER
from datetime import datetime
import glasgow


class Apache(glasgow.Glasgow):
	"""
		Funcionamiento del  del sistema
			# INSTANCIAR EL MODELO
			#apache = Apache()

			# INGRESAR DATOS AL SISTEMA DE LAS VARIABLES FISIOLOGICAS SOLICITADAS AL USUARIO
			#apache.temperatura(42)
			#apache.glasgow()
			# REALIZAR CALCULOS
			#apache.calcularAPS()
			#apache.evaluarEdad(80)
			#apache.evaluarPuntajeCronico("NINGUNA")
			#apache.calcularApache()
			#apache.calcularMortalidad()

			# MOSTRAR RESULTADOS CON LAS FUNCIONES GET.
			#pprint(apache.getMemoria())
			#print("APS",apache.getAPS())
			#print("APACHE",apache.getAPACHE())
			#print("MORTALIDAD",apache.getMortalidad())
	"""

	def __init__(self):

		# CONSTRUCTOR DE GLASGOW
		super().__init__()

		# Fecha actual del calculo.
		self.fecha = datetime.now().strftime("%d/%b/%Y/%X/%p")

		# Memoria de variables
		self.memoria = list()

		# APS
		self.aps = int(0)

		# Puntos por edad.
		self.puntos_edad = None

		# Puntaje por enfermedad
		self.puntos_enfermedad = None

		# APACHE II (GRAVEDAD)
		self.apache = int(0)

		# Mortalidad (%)
		self.mortalidad = int(0)

	def getFecha(self):
		""" Obtener la fecha actual del sistema """
		return self.fecha

	def getMemoria(self):
		""" Obtener la memoria de las variables calculadas """
		return self.memoria

	def getAPS(self):
		""" Obtener la variable APS """
		return self.aps

	def getPuntajeEdad(self):
		""" Obtener Puntaje por edad """
		return self.puntos_edad

	def getPuntajeEnfermedad(self):
		""" Obtener Puntaje por enfermedad """
		return self.puntos_enfermedad

	def getAPACHE(self):
		""" Obtener la variable APACHE """
		return self.apache

	def getCantidadProcesadas(self):
		""" Obtener la cantidad de variables procesadas en la memoria """
		return len(self.memoria)

	def getMortalidad(self):
		""" Obtener la mortalidad estimada del paciente """
		return self.mortalidad["puntos"]

	# CALCULO DE VARIABLES FISIOLOGICAS DEL PACIENTE
	# ESTAS SOLICITAN UN VALOR PARA REALIZAR EL CALCULO Y OBTENER EL RESULTADO
	# EN LA MEMORIA PRINCIPAL QUE SERVIRA PARA OBTENER LOS DATOS NECESARIOS PARA EL USUARIO
	
	# TEMPERATURA 
	def temperatura(self, valor=37):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Temperatura"

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
		
		# Agregar datos a la memoria
		self.memoria.append(datos)
	# PAM
	def presionArterialMedia(self, valor=70):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Presion arterial media (mmHg)"

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
		
		# Agregar datos a memoria
		self.memoria.append(datos)
	# FC
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
		
		# Agregar datos al memoria
		self.memoria.append(datos)
	# FR
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
		
		# Agregar datos al memoria
		self.memoria.append(datos)
	# ph
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
		
		# Agregar datos al memoria
		self.memoria.append(datos)
	# HC03
	def hco3Serico(self, valor=22):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "HCO3 SERICO (venoso mEq/l)"

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
		
		# Agregar datos al memoria
		self.memoria.append(datos)
	# NA
	def naSerico(self, valor=130):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Sodio Serico (mEq/l)"

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
		
		# Agregar datos al memoria
		self.memoria.append(datos)
	# K
	def kSerico(self, valor=3.5):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Potasio Serico (mEq/l)"

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
		
		# Agregar datos al memoria
		self.memoria.append(datos)
	# CREATININA
	def creatininaSerica(self, valor=0.6, fallo_renal=False):
		try:
			# Registro de variables
			datos = dict()

			datos["fallo_renal"] = fallo_renal

			datos["nombre"] = "Creatinina serica (mg/dl)"

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
		
		# Agregar datos al memoria
		self.memoria.append(datos)
	# HEMATOCRITO
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
		
		# Agregar datos al memoria
		self.memoria.append(datos)
	# LEUCOCITOS
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
		
		# Agregar datos al memoria
		self.memoria.append(datos)
	# OXIGENACION
	def oxigenacion(self, Fi02=0.6, valor=71):
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Oxigenacion"

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

		# Agregar datos al memoria
		self.memoria.append(datos)
	# COMA GLASGOW
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
		
		self.memoria.append(datos)

	# CALCULAR INDICADORES
	
	# APS
	def calcularAPS(self):
		""" Sumatoria del puntaje de todas las variables medidas """
		total = 0
		for variable in self.memoria:
			total += variable["puntos"]
		self.aps = int(total)
	# PUNTAJE POR EDAD
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
	# PUNTAJE POR ENFERMEDAD
	def evaluarPuntajeCronico(self, tipo_cirugia="NINGUNA"):
			try:
				# registro
				self.datos = {}
			
				self.datos["nombre"] = "Enfermedad Cronica"
					
				self.datos["descripcion"] = {
													"Cardiovascular":"NYHA IV",
													"RENAL":"Hemodialisis",
													"RESPIRATORIO":["EPOC, enfermedad restictiva o vascular que limita actividad funcional",
																	"Hipoxia cronica y/o hipercapnia; dependencia respiratoria",
																	"Policitemia o hipertension pulmonar severa (40>mmHg)"
																	],
													"HEPATICO":["Cirrosis (por biopsia)",
																"Encefalopatia previa",
																"Hipertension portal documentada",
																"Historia de hemorragia digestiva debidaa hipertension portal",
																],
													"INMUNOSUPRESION":["Farmacologico:quimioterapia, radioterapia, esteroides", "SIDA, linfoma, leucemias"]
												}
				self.datos["opciones"] = {
												"NINGUNA":0,
											  	"ELECTIVA":2,
											  	"NO-QUIRURGICA":5,
											  	"URGENTE":5
											  }
				self.datos["valor"] = str(tipo_cirugia).upper()

				self.datos["puntos"] = self.datos["opciones"][self.datos["valor"]]

				self.puntos_enfermedad = self.datos

			except ValueError as e:
				return "El valor de la {} no es un número".format(self.datos["nombre"])
	# APACHE
	def calcularApache(self):
		
		a = self.getAPS() # PUNTAJE POR VARIABLES FISIOLOGICAS
		
		b = self.getPuntajeEdad()["puntos"] # PUNTAJE POR EDAD.

		c = self.getPuntajeEnfermedad()["puntos"] # PUNTAJE POR ENFERMEDAD CRONICA
		
		self.apache = int(a + b + c) # GRAVEDAD DEL PACIENTE
	# MORTALIDAD
	def calcularMortalidad(self):
		""" Evaluar el porcentaje de mortalidad basado en la gravedad """
		try:
			# Registro de variables
			datos = dict()

			datos["nombre"] = "Prediccion de mortalidad"

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