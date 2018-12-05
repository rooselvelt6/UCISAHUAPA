#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal
from keras import backend as K
from keras import losses, metrics, optimizers
from keras.callbacks import TensorBoard, EarlyStopping
from keras.layers import Dense
from keras.models import Sequential, model_from_json, load_model
from keras.utils import plot_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python import debug as tf_debug
import numpy as np
import os
import webbrowser

class Agente():
	def __init__(self):
		np.random.seed(7) # Semilla de aleatoriedad
		# Tensorboard
		self.tensorboard = TensorBoard(log_dir="/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Tablero/{0}".format(datetime.now()), write_grads=True, write_graph=True, histogram_freq=1, write_images=True)
		
		#self.hook = tf_debug.TensorBoardDebugHook("robzombie6:7000")
		
		# Construir modelo.
		self.modelo = self._construirModelo()

		# Obtener arquitectura de RNA
		self._getModelo()
		
		# Orden: (X_train, X_test, y_train, y_test)
		self.conjunto_datos = self._crearConjuntos();

	def _postprocesar(self, minV, maxV, minimoNuevo, maximoNuevo, valor):
		return round(Decimal((((valor - minV) * (maximoNuevo - minimoNuevo)) / (maxV - minV)) + minimoNuevo),4)
		
	def _construirModelo(self):
		
		modelo = Sequential()

		modelo.add(Dense(units=9, activation="relu", name="Capa_Entrada", input_dim=9))
		
		modelo.add(Dense(units=7, activation="relu", name="Capa_Oculta"))
		
		modelo.add(Dense(units=1, activation="sigmoid", name="Capa_Salida"))
		
		modelo.compile(loss=losses.mean_squared_error, 
					   optimizer=optimizers.Adam(lr=0.01),
					   metrics=[metrics.mae]
					   )
		return modelo;

	def _imprimirModelo(self):
		""" Crear imagen del modelo construido """
		plot_model(self.modelo, to_file="modelo.png", show_shapes=False, expand_nested=False, dpi=96, rankdir="LR")

	def _getTablero(self):
		# Abrir pestaña de navegador y ejecutar servicio tensorboard
		webbrowser.open("http://robzombie6:6006", new=2, autoraise=True);
		os.system("tensorboard --logdir='/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Tablero' --debugger_port=7000");

	def _getModelo(self):
		""" Mostrar arquitectura del modelo """
		self.modelo.summary();

	def _crearConjuntos(self):
		try:
			# Paso 1. Cargar 
			conjunto = np.loadtxt("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Data/todo/conjunto_total.csv", delimiter=",")
			# Paso 2. Dividir en pedazos con slicing.
			x = conjunto[:, 0:9];
			y = conjunto[:,9]
			# Paso3. Transformar Y.
			y = np.reshape(y,(-1,1))
			# Paso 4. Escala MinMax.
			escala = MinMaxScaler()
			print(escala.fit(x), escala.fit(y))
			escalaX = escala.transform(x)
			escalaY = escala.transform(y)
			print("Atributos:",escalaX.shape)
			print("Etiquetas:",escalaY.shape)
			# Paso 5. Retornar el modelo al constructor.
			X_train, X_test, y_train, y_test = train_test_split(escalaX, escalaY);
			print("************************")
			print("Tamaño de los conjuntos:")
			print("************************")
			print("Conjunto de Entrenamiento:", len(X_train))
			print("Conjunto de prueba:", len(X_test))
			print("************************")
			return (X_train, X_test, y_train, y_test)
		except Exception as e:
			print(e)
			raise

	def _guardarModelo(self):
		self.modelo_json = self.modelo.to_json();
		with open("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Modelo/modelo.json","w") as archivo_json:
			archivo_json.write(self.modelo_json);
		# Serializar pesos en formato HDF5.
		self.modelo.save_weights("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Modelo/pesos.h5")
	
	def _cargarModelo(self):
		archivo_json = open("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Modelo/modelo.json","r");
		modelo_cargado_json = archivo_json.read()
		archivo_json.close();
		modelo_cargado = model_from_json(modelo_cargado_json)
		modelo_cargado.load_weights("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Modelo/pesos.h5")
		print()
		print()
		print("El modelo se ha cargado.")
		print()
		print()
		return modelo_cargado

	def _entrenar(self):
		# Entrenar el modelo.
		early_stop = EarlyStopping(monitor='val_loss', patience=50) # Parada forzada
		self.modelo.fit(self.conjunto_datos[0], 
						self.conjunto_datos[2], 
						epochs=500, 
						batch_size=32, 
						verbose=1, 
						validation_split=0.2, 
						callbacks=[self.tensorboard, early_stop] 
						)
		self._guardarModelo();

	def _probar(self):
		modelo_cargado = self._cargarModelo();
		modelo_cargado.compile(loss=losses.mean_squared_error, 
					   optimizer=optimizers.Adam(lr=0.01),
					   metrics=[metrics.mae]
					   )
		print()
		print("Evaluación del modelo:")
		print()
		loss, mae = modelo_cargado.evaluate(self.conjunto_datos[1],
												 self.conjunto_datos[3],
												 batch_size=32,
												 verbose=1
												)
		print("Resultados:")
		print()
		print("Loss:", loss)
		print("MAE:", mae) # 100 ? es solo de prueba

	def _cargarCompilar(self):
		modelo_cargado = self._cargarModelo();
		modelo_cargado.compile(loss=losses.mean_squared_error, 
					   optimizer=optimizers.Adam(lr=0.01),
					   metrics=[metrics.mae]
					   )
		print()
		print("El modelo ha sido cargado y compilado con éxito...")
		print()
		return modelo_cargado

	def _estimar(self, atributos, modelo):
		vector = np.array([atributos])
		estimar = modelo.predict(vector).flatten()
		return estimar
