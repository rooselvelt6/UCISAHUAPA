#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime
from decimal import Decimal
from keras import backend as K
from keras import losses, metrics, optimizers
from keras.callbacks import EarlyStopping, TensorBoard
from keras.layers import Dense
from keras.models import Sequential, load_model, model_from_json
from keras.utils import plot_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python import debug as tf_debug
import numpy as np
import os
import webbrowser

class RNA():
	
	def __init__(self):
		""" Constructor """
		try:
			self.reporte = {} # Reporte básico
			np.random.seed(7) # Semilla de aleatoriedad
			self.modelo = self._construirModelo() # Construir modelo general
			self._imprimirModelo() # Generar imagen del modelo a construir
			self.conjuntoDatos = self._crearConjuntos() # Cargar el conjunto de datos a utilizar por el modelo
			# Tensorboard
			self.tensorboard = TensorBoard(write_grads=True, # Pérdida y error
										   write_graph=True, # Mostrar modelo gráfico
										   histogram_freq=1, # Histograma
										   write_images=True, # Imagen del entrenamiento
										   log_dir="/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Tablero/{0}".format(datetime.now()) # Ruta
										   )
		except Exception as e:
			print(e)
			raise
		finally:
			print("___________________________________________________________________")
			print("                RED NEURONAL ARTIFICIAL DEFINIDA                   ")
			print("===================================================================")
			self.modelo.summary() # Mostrar el modelo creado

	def _debug(self):
		""" En investigación """
		print("INICIO DEBUG")
		sess = K.get_session()
		sess = tf_debug.LocalCLIDebugWrapperSession(sess)
		K.set_session(sess)
		print("FINAL DEBUG")

	def _construirModelo(self, tasa=0.01):
		# Definir modelo
		modelo = Sequential()
		# Agregar capa de entrada con 9 neuronas
		modelo.add(Dense(units=9, activation="relu", name="Capa_Entrada", input_dim=9))
		# Agregar capa oculta con 7 neuronas
		modelo.add(Dense(units=7, activation="relu", name="Capa_Oculta"))
		# Agregar capa de salida con una neurona de salida
		modelo.add(Dense(units=1, activation="sigmoid", name="Capa_Salida"))
		# Compilar el modelo definido.
		modelo.compile(loss=losses.mean_squared_error, # Pérdida
					   optimizer=optimizers.Adam(lr=tasa),  # Método de optimización
					   metrics=[metrics.mae] # List de metricas a obtener
					   ) 
		# Retornar el modelo creado
		self.reporte["configuracion"] = modelo.get_config()
		return modelo

	def _imprimirModelo(self):
		""" Crear imagen del modelo construido """
		plot_model(self.modelo, to_file="/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Modelo/modelo.png")

	def _crearConjuntos(self):
		try:
			# Cargar el conjunto total.
			conjunto = np.loadtxt("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Data/todo/conjunto_total.csv", delimiter=",")
			# Dividir en partes las etiquetas y los atributos
			atributos = conjunto[:, 0:9] # Atributos
			etiqueta  = conjunto[:,9] # Etiquetas
			#print("___________________________________________________________________")
			#print("                        CONJUNTO DE ATRIBUTOS                      ")
			#print("===================================================================")
			#self.reporte["atributos"] = atributos
			#print(atributos,type(atributos))
			#print("===================================================================")
			#print("                        CONJUNTO DE ETIQUETAS                      ")
			#print("===================================================================")
			#print(etiqueta,type(etiqueta))
			#print("===================================================================")
			#self.reporte["etiquetas"] = etiqueta
			#print("                 ETIQUETA TRANSFORMADA EN MATRIZ                   ")
			#print("===================================================================")
			etiqueta = np.reshape(etiqueta,(-1,1)) # Transformar etiqueta
			escala = MinMaxScaler() # Aplicar escalado MinMax
			self.reporte["escalado"] = escala
			# Imprimir el escalado de los datos.
			#print("---------------------------PREPROCESAMIENTO MINMAXSCALER-----------------------")
			print(escala.fit(atributos), escala.fit(etiqueta))
			escalaAtributos = escala.transform(atributos)
			escalaEtiqueta = escala.transform(etiqueta)
			# Imprimir las transformaciones
			#print("===================================================================")
			#print("Cantidad total de ejemplos:",escalaAtributos.shape[0]);
			self.reporte["total_ejemplos"] = escalaAtributos.shape[0]
			#print("===================================================================")
			#print("Dimensión de los atributos:",escalaAtributos.shape[1]);
			#print("===================================================================")
			self.reporte["dimension_atributos"] = escalaAtributos.shape[1]
			#print("Dimensión de las etiquetas:",escalaEtiqueta.shape[1]);
			#print("===================================================================")
			self.reporte["dimension_etiquetas"] = escalaEtiqueta.shape[1]
			# Dividir conjuntos de aprendizaje y prueba
			attrEntrenamiento, attrPrueba, etiquetaEntrenamiento, etiquetaPrueba = train_test_split(escalaAtributos, escalaEtiqueta)
			#print("Tamaño del conjunto de entrenamiento:",len(attrEntrenamiento));
			#print("===================================================================")
			self.reporte["length_set_train"] = len(attrEntrenamiento)
			#print("Tamaño del conjunto de prueba:",len(attrPrueba));
			self.reporte["length_set_test"] = len(attrPrueba)
			# Dividir conjuntos de aprendizaje y prueba
			attrEntrenamiento, attrPrueba, etiquetaEntrenamiento, etiquetaPrueba = train_test_split(escalaAtributos, escalaEtiqueta)
			# Retornar datos en el orden de creación: (X_train, X_test, y_train, y_test)
			return (attrEntrenamiento, attrPrueba, etiquetaEntrenamiento, etiquetaPrueba)
		except Exception as e:
			print(e)
		finally:
			print("___________________________________________________________________")
			print("                  CONJUNTO DE DATOS CARGADO                        ")
			print("===================================================================")

	def _get_reporte(self):
		return self.reporte
		
	def _guardarModelo(self):
		""" Enviar los datos del modelo en formato JSON y los pesos en formato HDF5 """
		modeloJSON = self.modelo.to_json()
		# Construir el archivo en formato JSON
		with open("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Modelo/modelo.json","w") as archivoJSON:
			archivoJSON.write(modeloJSON) # Escribir datos del modelo al formato
		# Serializar pesos en formato HDF5
		self.modelo.save_weights("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Modelo/pesos.h5")

	def _cargarModelo(self):
		archivo_json = open("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Modelo/modelo.json","r");
		modelo_cargado_json = archivo_json.read()
		archivo_json.close();
		modelo_cargado = model_from_json(modelo_cargado_json)
		modelo_cargado.load_weights("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Modelo/pesos.h5")
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
		print(self.reporte)
		return modelo_cargado

	def _postprocesar(self, minV, maxV, minimoNuevo, maximoNuevo, valor):
		return round(Decimal((((valor - minV) * (maximoNuevo - minimoNuevo)) / (maxV - minV)) + minimoNuevo),4)

	def _mostrarTablero(self):
		""" Obtener tablero TensorBoard en el navegador por defecto """
		webbrowser.open("http://robzombie6:6006", new=2, autoraise=True)
		os.system("tensorboard --logdir='/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Tablero'")
