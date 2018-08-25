class Glasgow(object):
	
	""" Escala de coma de glasgow (ECG), La peor en las primeras 24 horas de UCI, antes de sedación. """

	def __init__(self):
		""" Escala glasgow """

		self.puntaje = int(0)

		self.respuesta = None

		self.control = [];

	def get_ecg(self):
		""" Obtener el total del glasgow """
		for control in self.control:
			self.puntaje += control["valor"]
		return self.puntaje

	def get_estado(self):
		""" Obtener los estados observados del ecg"""
		estados = [];

		for control in self.control:
			estados.append(control["observacion"])
	
		self.respuesta = list(zip(["APERTURA OCULAR", "RESPUESTA MOTORA","RESPUESTA VERBAL"],estados))

		return self.respuesta;

	def apertura_ocular(self, valor=1):
		""" Sistema de respuesta ocular. """
		try:

			if((valor >= 1) and (valor <= 4)):

				self.datos = {} # registro del hash de información
				
				self.datos["nombre"] = "APERTURA OCULAR"

				self.datos["valor"] = int(valor) # valor actual observado
		
				# ANOTAR OBSERVACIÓN BASADA EN EL VALOR
				if(self.datos["valor"] == 1):

					self.datos["observacion"] = "Ninguna"

				elif(self.datos["valor"] == 2):

					self.datos["observacion"] = "Al dolor"

				elif(self.datos["valor"]== 3):
			
					self.datos["observacion"] = "Al llamado"

				elif(self.datos["valor"] == 4):
			
					self.datos["observacion"] = "Espontánea"

				else:
			
					self.datos["error"] = "Error en el valor de entrada"
				
				self.control.append(self.datos)
			else:
				print("Error en el valor de entrada")
		
		except ValueError:
			print("Error en el valor de entrada")

	def respuesta_motora(self, valor=1):

		""" Sistema 2: respuesta motora del paciente """
		try:

			if((valor >= 1) and (valor <= 6)):
		
				self.datos = {} # hash de datos

				self.datos["nombre"] = "RESPUESTA MOTORA"

				self.datos["valor"] = int(valor) # valor observado

			# ANOTACIÓN DE LA OBSERVACIÓN

				if(self.datos["valor"] == 1):

					self.datos["observacion"] = "Ninguna"

				elif(valor == 2):

					self.datos["observacion"] = "Postura en extensión"

				elif(valor == 3):

					self.datos["observacion"] = "Postura en flexión"

				elif(valor == 4):

					self.datos["observacion"] = "Retirada"

				elif(valor == 5):

					self.datos["observacion"] = "Localiza estímulos"

				elif(valor == 6):

					self.datos["observacion"] = "Obedece órdenes"
				
				else:
					print("Error en el valor de entrada")

				self.control.append(self.datos)
				
		except ValueError:
			print("Error en el valor de entrada")

	def respuesta_verbal(self, valor=1):
		""" Sistema 3: respuesta motora del paciente """

		try:

			if((valor >= 1) and (valor <= 5)):

				self.datos = {} # hash de información

				self.datos["nombre"] = "RESPUESTA VERBAL"

				self.datos["valor"] = int(valor) # valor actual

				# ANOTACIÓN DE LA OBSERVACIÓN

				if(self.datos["valor"] == 1):

					self.datos["observacion"] = "Ninguna respuesta verbal"

				elif(self.datos["valor"] == 2):
				
					self.datos["observacion"] = "Sonidos incomprensibles"

				elif(self.datos["valor"] == 3):
				
					self.datos["observacion"] = "Palabras inapropiadas"

				elif(self.datos["valor"] == 4):
				
					self.datos["observacion"] = "Confuso"

				elif(self.datos["valor"] == 5):
				
					self.datos["observacion"] = "Orientado"

				else:
					print("Error en el valor de entrada")
	
				self.control.append(self.datos)
		except ValueError:
			print("Error en el valor de entrada")
			