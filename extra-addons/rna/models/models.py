# -*- coding: utf-8 -*-
"""
	Prueba de integración de RNA con Odoo.
"""
from datetime import datetime
from decimal import Decimal
from keras import backend as K
from keras import losses, metrics, optimizers
from keras.callbacks import EarlyStopping, TensorBoard
from keras.layers import Dense
from keras.models import Sequential, load_model, model_from_json
from keras.utils import plot_model
from odoo import models, fields, api
from pprint import pprint
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python import debug as tf_debug
import ast
import numpy as np
import os
import webbrowser

# Simulador de red neuronal artificial
class Agente():
	""" Perceptron multicapa para la predicción de la estadía de un paciente en la UCI del SAHUAPA """
	def __init__(self):
		try:
			#self.reporte = {} # Reporte de RNA
			np.random.seed(7) # Semilla de aleatoriedad
			self.modelo = self._construirModelo() # Llamado al método de construcción del modelo de RNA
			self._imprimirModelo() # Generar imagen de la instancia de la RNA
			self.conjuntoDatos = self._crearConjuntos() # Cargar conjunto de datos para RNA
			# Tensorboard
			self.tensorboard = TensorBoard(write_grads=True, # Pérdida y error
										   write_graph=True, # Mostrar modelo gráfico
										   histogram_freq=1, # Histograma
										   write_images=True, # Imagen del entrenamiento
										   log_dir="/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Tablero/{0}".format(datetime.now()) # Ruta
										   )
		except Exception as e:
			raise
		else:
			pass
		finally:
			print("___________________________________________________________________")
			print("                RED NEURONAL ARTIFICIAL DEFINIDA                   ")
			print("===================================================================")
			self.modelo.summary() # Mostrar el modelo creado
			pprint(self._obtenerModelo()) # Mostrar configuración del modelo creado

	def _construirModelo(self):
		""" Definir y compilar el modelo de la RNA """
		try:
			modelo = Sequential() # Definir tipo de modelo
			# Capa de entrada con 9 neuronas y función relu
			modelo.add(Dense(units=9, activation="relu", name="Capa_Entrada", input_dim=9))
			# Capa de entrada con 7 neuronas y función relu
			modelo.add(Dense(units=7, activation="relu", name="Capa_Oculta"))
			# Capa de salida con 1 neurona y función sigmoide
			modelo.add(Dense(units=1, activation="sigmoid", name="Capa_Salida"))
			# Compilación del modelo
			modelo.compile(loss=losses.mean_squared_error, # Pérdida
						   optimizer=optimizers.Adam(lr=0.01),  # Método de optimización con parámetro de la tasa de aprendizaje
						   metrics=[metrics.mae] # Lista de metricas a obtener
						   ) # Fin de la compilación
			return modelo 
		except Exception as e:
			raise
		else:
			pass
		finally:
			pass
		
	def _obtenerModelo(self):
		""" Obtener la configuración global de la RNA construida """
		return self.modelo.get_config()

	def _imprimirModelo(self):
		""" Generar una imagen de la instancia RNA """
		plot_model(self.modelo, to_file="/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Modelo/modelo.png")

	def _crearConjuntos(self):
		try:
			# Cargar el conjunto total.
			conjunto = np.loadtxt("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/DataSet/uci_sahuapa.csv", delimiter=",")
			# Dividir en partes las etiquetas y los atributos
			atributos = conjunto[:, 0:9] # Atributos
			etiqueta  = conjunto[:,9] # Etiquetas
			etiqueta = np.reshape(etiqueta,(-1,1)) # Transformar etiqueta
			escala = MinMaxScaler() # Aplicar escalado MinMax
			print(escala.fit(atributos), escala.fit(etiqueta))
			escalaAtributos = escala.transform(atributos)
			escalaEtiqueta = escala.transform(etiqueta)
			# División del conjunto de entrenamiento y prueba
			attrEntrenamiento, attrPrueba, etiquetaEntrenamiento, etiquetaPrueba = train_test_split(escalaAtributos, escalaEtiqueta)
			return (attrEntrenamiento, attrPrueba, etiquetaEntrenamiento, etiquetaPrueba)
		except Exception as e:
			raise
		else:
			pass
		finally:
			print("___________________________________________________________________")
			print("                  CONJUNTO DE DATOS CARGADO                        ")
			print("===================================================================")

	def _guardarModelo(self):
		""" Enviar los datos del modelo en formato JSON y los pesos en formato HDF5 """
		modeloJSON = self.modelo.to_json()
		# Construir el archivo en formato JSON
		with open("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Modelo/modelo.json","w") as archivoJSON:
			archivoJSON.write(modeloJSON) # Escribir datos del modelo al formato
		# Serializar pesos en formato HDF5
		self.modelo.save_weights("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Modelo/pesos.h5")

	def _cargarModelo(self):
		archivo_json = open("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Modelo/modelo.json","r");
		modelo_cargado_json = archivo_json.read()
		archivo_json.close();
		modelo_cargado = model_from_json(modelo_cargado_json)
		modelo_cargado.load_weights("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Modelo/pesos.h5")
		return modelo_cargado

	def _entrenarModelo(self):
		# Monitor de paciencia del modelo para el conjunto de validación
		earlyStop = EarlyStopping(monitor="val_loss", patience=50);
		self.modelo.fit(self.conjuntoDatos[0],
						self.conjuntoDatos[2],
						epochs=500,
						batch_size=32,
						verbose=1,
						validation_split=0.2,
						callbacks=[self.tensorboard, earlyStop]
						)
		# Guardar el modelo con los datos del entrenamiento y validación
		self._guardarModelo()

	def _probarModelo(self):
		cargado = self._cargarModelo()
		cargado.compile(loss=losses.mean_squared_error, optimizer=optimizers.Adam(lr=0.01), metrics=[metrics.mae])
		loss, mae = cargado.evaluate(self.conjuntoDatos[1], self.conjuntoDatos[3], batch_size=32, verbose=2)
		print("===================================================================")
		print("                   FASE DE PRUEBA DEL MODELO                       ")
		print("===================================================================")
		# Reducir a 4 decimales
		print("Loss: {0:.4f}, MAE: {1:.4f}".format(loss, mae))
		print("===================================================================")

	def _predecir(self, atributos, modelo):
		vector = np.array([atributos])
		pronostico = modelo.predict(vector).flatten()
		return pronostico

	def _cargarCompilar(self):
		modelo_cargado = self._cargarModelo();
		# Compilación del modelo 
		modelo_cargado.compile(loss=losses.mean_squared_error,
					   optimizer=optimizers.Adam(lr=0.01),
					   metrics=[metrics.mae]
					   )
		print("___________________________________________________________________")
		print("            RED NEURONAL ARTIFICIAL CARGARDA Y COMPILADA           ")
		print("===================================================================")
		return modelo_cargado

	def _postprocesar(self, minV, maxV, minimoNuevo, maximoNuevo, valor):
		return round(Decimal((((valor - minV) * (maximoNuevo - minimoNuevo)) / (maxV - minV)) + minimoNuevo),4)

	def _mostrarTablero(self):
		""" Obtener tablero TensorBoard en el navegador por defecto """
		webbrowser.open("http://robzombie6:6006", new=2, autoraise=True)
		os.system("tensorboard --logdir='/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Tablero'")

# Prueba del agente RNA
mlp = Agente() # Cargar Agente inteligente basado en RNA
#******************************************************************************
#                 Fase 1: Entrenamiento y prueba                              *
#******************************************************************************
# Se utiliza una sola vez luego es desconectada                               *
#******************************************************************************
#mlp._entrenarModelo() # Entrenamiento 
#mlp._probarModelo() # Prueba
#******************************************************************************
# Fase 2: Recuerdo e inferencia se encuentra activa una vez entrenado la RNA  *
#******************************************************************************
modelo = mlp._cargarCompilar() # Carga y compila el modelo entrenado
modelo._make_predict_function() # Fase de recuerdo
#******************************************************************************
# Fin del simulador

# Modelo de Odoo
class RNA(models.Model):
	# Herencia del sistema de admisión del paciente a la UCI
	_inherit = 'paciente.paciente' 

	percepciones = fields.Text(
	    string='Percepciones captadas del entorno',
	    translate=True
	)

	tiempo_estadia = fields.Float(
	    string='Tiempo de estadía en la UCI',
	    help="Predicción del tiempo de estadía basado en Redes Neuronales Artificiales"
	)

	# Percepciones del entorno basado en los siguientes parámetros
	@api.onchange('edad','sexo','color_piel','estadia_hospitalaria','antecedentes','tipo_admision','migracion','ventilacion_mecanica','procesos_invasivos')
	def _onchange_entorno(self):
		entorno = [] # Lista encargada de recolectar los cambios del entorno
		for attr in self: # Capturar los atributos importantes para la RNA
			# Estadía hospitalaria
			entorno.append(float(attr.estadia_hospitalaria))
			# Antecedentes
			if(attr.antecedentes != ""):
				entorno.append(float(1))
			if(attr.antecedentes == ""):
				entorno.append(float(0))
			# Ventilación mecánica
			entorno.append(float(attr.ventilacion_mecanica))
			# Migración
			entorno.append(float(attr.migracion))
			# Color de piel
			entorno.append(float(attr.color_piel))
			# Procesos invasivos
			entorno.append(float(attr.procesos_invasivos))
			# Edad
			entorno.append(float(attr.edad))
			# Sexo
			entorno.append(float(attr.sexo))
			# Tipo de admisión
			entorno.append(float(attr.tipo_admision))
			# Retorno del cambio capturado por el entorno
			attr.percepciones = entorno      

	# Predicción del tiempo de estadía basado en RNA
	
	@api.onchange('percepciones')
	def _onchange_percepciones(self):
		for campo in self:
			lista_atributos = ast.literal_eval(campo.percepciones)
			#print(lista_atributos)
			matriz_prediccion = np.array(lista_atributos)
			#print(matriz_prediccion)

		matriz_prediccion = np.reshape(matriz_prediccion,(-1,1))
		#print(matriz_prediccion)
		escala = MinMaxScaler(feature_range=(0,1))
		print(escala.fit(matriz_prediccion))
		final = escala.transform(matriz_prediccion)

		#print(final) # Imprimir proceso
		l2 = [x[0] for x in final]
		print(l2)
		if(len(l2) ==9):
			resultado = mlp._predecir(atributos=l2, modelo=modelo)
			print("Resultado de la predicción de la estadía:", resultado)
			# del(l2)
			for attr in self:
				# Estadía cruda sin postprocesamiento de salida.
				attr.tiempo_estadia = resultado[0]
				# Postprocesamiento de salida
				# La pregunta acá es cual es el valor de la estadía ???
				print("Estadía por 10:", resultado[0]*10)
				print("Estadía por 100:", resultado[0]*100)
				print("Postprocesamiento MinMax:", mlp._postprocesar(minV=0, maxV=1, minimoNuevo=0, maximoNuevo=41, valor=resultado[0]))
				#________________________________________________________________________________________________________________________
	
	        

