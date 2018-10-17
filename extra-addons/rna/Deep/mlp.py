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

class Agente(object):
	def __init__(self):
		# Tensorboard
		self.tensorboard = TensorBoard(log_dir="Tablero/{0}".format(datetime.now()), write_grads=True, write_graph=True, histogram_freq=1)
		# Construir modelo.
		self.modelo = self._construirModelo()
		# Obtener arquitectura de RNA
		self._getModelo()
		# Orden: (X_train, X_test, y_train, y_test)
		self.conjunto_datos = self._crearConjuntos();

	def _crearConjuntos(self):
		try:
			# Paso 1. Cargar 
			conjunto = np.loadtxt("./Data/todo/conjunto_total.csv", delimiter=",")
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
					   optimizer=optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True),
					   metrics=[metrics.mae]
					   )
		return modelo;

	def _getTablero(self):
		# Abrir pestaña de navegador y ejecutar servicio tensorboard
		webbrowser.open("http://robzombie6:6006", new=2, autoraise=True);
		os.system("tensorboard --logdir='Tablero'");

	def _guardarModelo(self):
		self.modelo_json = self.modelo.to_json();
		with open("./Modelo/modelo.json","w") as archivo_json:
			archivo_json.write(self.modelo_json);
		# Serializar pesos en HDF5.
		self.modelo.save_weights("./Modelo/pesos.h5")
	
	def _cargarModelo(self):
		archivo_json = open("./Modelo/modelo.json","r");
		modelo_cargado_json = archivo_json.read()
		archivo_json.close();
		modelo_cargado = model_from_json(modelo_cargado_json)
		modelo_cargado.load_weights("./Modelo/pesos.h5")
		return modelo_cargado
	
	def _entrenar(self):
		# Entrenar el modelo.
		#early_stop = EarlyStopping(monitor='val_loss', patience=50) # Parada forzada
		self.modelo.fit(self.conjunto_datos[0], 
						self.conjunto_datos[2], 
						epochs=300, 
						batch_size=32, 
						verbose=1, 
						validation_split=0.2, 
						callbacks=[self.tensorboard] # early_stop
						)
		self._guardarModelo();
		# Fin del entrenamiento del modelo.

	def _probar(self):
		modelo_cargado = self._cargarModelo();
		modelo_cargado.compile(loss=losses.mean_squared_error, 
					   optimizer=optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True),
					   metrics=[metrics.mae]
					   )
		print()
		print("Evaluación del modelo:")
		print()
		puntaje_prueba = modelo_cargado.evaluate(self.conjunto_datos[1],
												 self.conjunto_datos[3],
												 batch_size=32,
												 verbose=1
												)
		print("Resultados:")
		print()
		print(puntaje_prueba)
		print()

	def _postprocesar(self, minV, maxV, minimoNuevo, maximoNuevo, valor):
		return round(Decimal((((valor - minV) * (maximoNuevo - minimoNuevo)) / (maxV - minV)) + minimoNuevo),4)

	def _predecir(self, atributos=[]):
		"""
			Descripción:
				La función recibe un conjunto similar al de prueba
				y entrenamiento en formato de array numpy con
				dimensión de 9 la cual debe estar preprocesada
				similarmente a la que es usada en casos anteriores
				También se debe aplicar el método: 
				estimacion = modelo_cargado.predict(atributos)
				Una vez que la estimación se realize se debe
				postprocesar adecuandose a la realidad de la 
				variable en escala del 0-41 y enviar el valor
				al formulario del sistema donde es evaluado
				y corregido tantas por las percepciones del entorno.
				Se debe estudiar la función desde distintos aspectos
				hasta encontrar dicha solución desde Odoo.
				Cada vez que sucedan cambios en el vector_entradas
				este sistema debe calcularse sin cargar a cada
				momento el modelo es decir sin realizar tantas 
				consultas al disco duro para cargar modelos y pesos.

			Llamado de la función:
				a.predecir(atributos=[[1,2,3,4,5,6,7,8,9]])

			Luego postprocesar para adecuar a la realidad en Días.
		"""
		modelo_cargado = self._cargarModelo();
		modelo_cargado.compile(loss=losses.mean_squared_error, 
					   optimizer=optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True),
					   metrics=[metrics.mae]
					   )
		vector = np.array([atributos])
		print(vector, type(vector))
		x = self.modelo.predict(vector)
		print(x)
