#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from keras import losses, metrics, optimizers
from keras.callbacks import TensorBoard, EarlyStopping
from keras.layers import Dense
from keras.models import Sequential, model_from_json, load_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import os
import webbrowser
from keras import backend as K
from decimal import Decimal

class Agente(object):
	def __init__(self):
		np.random.seed(7) # Semilla de aleatoriedad
		# Tensorboard
		self.tensorboard = TensorBoard(log_dir="/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Deep/Tablero/{0}".format(datetime.now()), write_grads=True, write_graph=True, histogram_freq=1)
		# Construir modelo.
		self.modelo = self._construirModelo()
		# Obtener arquitectura de RNA
		self._getModelo()
		# Orden: (X_train, X_test, y_train, y_test)
		self.conjunto_datos = self._crearConjuntos();

	def _crearConjuntos(self):
		try:
			# Paso 1. Cargar 
			conjunto = np.loadtxt("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Deep/Data/todo/conjunto_total.csv", delimiter=",")
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
			return (X_train, X_test, y_train, y_test)
		except Exception as e:
			print(e)
			raise

	def _getModelo(self):
		""" Mostrar arquitectura del modelo """
		self.modelo.summary();

	def _construirModelo(self):
		modelo = Sequential()

		modelo.add(Dense(units=9, activation="relu", name="Capa_Entrada", input_dim=9))
		
		modelo.add(Dense(units=7, activation="relu", name="Capa_Oculta"))
		
		modelo.add(Dense(units=1, activation="sigmoid", name="Capa_Salida"))
		
		modelo.compile(loss=losses.mean_squared_error, 
					   optimizer="adam",#optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True),
					   metrics=[metrics.mae]
					   )
		return modelo;

	def _getTablero(self):
		# Abrir pestaña de navegador y ejecutar servicio tensorboard
		webbrowser.open("http://robzombie6:6006", new=2, autoraise=True);
		os.system("tensorboard --logdir='/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Deep/Tablero'");

	def _guardarModelo(self):
		self.modelo_json = self.modelo.to_json();
		with open("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Deep/Modelo/modelo.json","w") as archivo_json:
			archivo_json.write(self.modelo_json);
		# Serializar pesos en HDF5.
		self.modelo.save_weights("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Deep/Modelo/pesos.h5")
	
	def _cargarModelo(self):
		archivo_json = open("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Deep/Modelo/modelo.json","r");
		modelo_cargado_json = archivo_json.read()
		archivo_json.close();
		modelo_cargado = model_from_json(modelo_cargado_json)
		modelo_cargado.load_weights("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/Deep/Modelo/pesos.h5")
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
		# Fin del entrenamiento del modelo.

	def _probar(self):
		modelo_cargado = self._cargarModelo();
		modelo_cargado.compile(loss=losses.mean_squared_error, 
					   optimizer="adam",#optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True),
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
		print("MAE:", mae*100)
		print()

	def _postprocesar(self, minV, maxV, minimoNuevo, maximoNuevo, valor):
		return round(Decimal((((valor - minV) * (maximoNuevo - minimoNuevo)) / (maxV - minV)) + minimoNuevo),4)

	def _cargarCompilar(self):
		modelo_cargado = self._cargarModelo();
		modelo_cargado.compile(loss=losses.mean_squared_error, 
					   optimizer="adam",#optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True),
					   metrics=[metrics.mae]
					   )
		print()
		print("El modelo ha sido cargado y compilado con éxito...")
		print()
		return modelo_cargado

	def _estimar(self, atributos, modelo):
		"""
			Errores:
				Negativos:
					1.) Si existen menos de 9 dimensiones en el array no predice nada
							bot._predecir([1])  dimensión 1: error
								ValueError: Error when checking input: expected Capa_Entrada_input to have shape (9,) but got array with shape (1,)

							bot._predecir([0,1,0,0,1,1,1,1]) dimensión 8: error
								ValueError: Error when checking input: expected Capa_Entrada_input to have shape (9,) but got array with shape (8,)
			Aprobaciones:
				Positivos:
					1) Si se cumplen las 9 dimensiones y es un array numpy
							bot._predecir([0,1,0,0,1,1,1,1,1]) 9 dimensiones: 
				     		[[0 1 0 0 1 1 1 1 1]] <class 'numpy.ndarray'>
					 			Resultados: [[0.43830487]]
			
			# Error Final.
				- Sucede cuando se ejecuta dos veces la carga de archivos se sobre carga la función y pasa lo siguiente:
					TypeError: Cannot interpret feed_dict key as Tensor: Tensor Tensor("Placeholder:0", shape=(9, 9), dtype=float32) is not an element of this graph.
				  -Solución sacar el método de carga de archivos de la función para evitar la sobrecarga de consultas a disco para cargar el modelo.

				alueError: Error when checking input: expected Capa_Entrada_input to have shape (9,) but got array with shape (1,)
				ValueError: 
					Tensor Tensor("Capa_Salida_1/Sigmoid:0", shape=(?, 1), dtype=float32) is not an element of this graph.
		"""
		vector = np.array([atributos])
		estimar = modelo.predict(vector).flatten()
		return estimar
		
		
		 
