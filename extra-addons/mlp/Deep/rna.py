#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Debo actualizar el proyecto a rutas automáticas de python """
import numpy as np 
import os
import webbrowser
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

class RNA():
	""" Perceptron multicapa para la predicción de la estadía de un paciente en la UCI del SAHUAPA """
	def __init__(self):
		try:
			# Semilla de aleatoriedad 
			np.random.seed(7)
			# Construcción del modelo automáticamente al iniciar objeto.
			self.modelo = self._construirModelo()
			# Generar imagen del modelo construido
			self._imprimirModelo()
			# Obtener modelo desarrollado y mostrar en consola
			self._obtenerModelo()
			# Crear el conjunto de datos
			self.conjuntoDatos = self._crearConjuntos()
			# Tensorboard tablero para resultados de la RNA
			self.tensorboard = TensorBoard(log_dir="/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Tablero/{0}".format(datetime.now()), write_grads=True, write_graph=True, histogram_freq=1, write_images=True)
		except Exception as e:
			print(e)
			raise
		finally:
			print("---------------------------------")
			print("(RNA) HA SIDO DEFINIDA CON ÉXITO ")
			print("---------------------------------")
		
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
		modelo.compile(loss=losses.mean_squared_error, optimizer=optimizers.Adam(lr=tasa), metrics=[metrics.mae])
		# Retornar el modelo creado
		return modelo
			
	def _imprimirModelo(self):
		""" Crear imagen del modelo construido """
		plot_model(self.modelo, to_file="/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Modelo/modelo.png")

	def _obtenerModelo(self):
		""" Mostrar arquitectura del modelo """
		return self.modelo.summary()

	def _crearConjuntos(self):
		try:
			# Cargar el conjunto total.
			conjunto = np.loadtxt("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Data/todo/conjunto_total.csv", delimiter=",")
			# Dividir en partes las etiquetas y los atributos
			# Conjunto de atributos
			atributos = conjunto[:, 0:9]
			# Conjunto de etiquetas
			etiqueta  = conjunto[:,9]
			#print("---------------------------CONJUNTO DE ATRIBUTOS-------------------------------")
			#print(atributos);
			#print(type(atributos))
			#print("---------------------------CONJUNTO DE ETIQUETAS-------------------------------")
			#print(etiqueta)
			#print(type(etiqueta))
			# Transformar etiqueta
			etiqueta = np.reshape(etiqueta,(-1,1))
			# Aplicar escalado MinMax
			escala = MinMaxScaler()
			# Imprimir el escalado de los datos.
			#print("---------------------------PREPROCESAMIENTO MINMAXSCALER-----------------------")
			print(escala.fit(atributos), escala.fit(etiqueta))
			escalaAtributos = escala.transform(atributos)
			escalaEtiqueta = escala.transform(etiqueta)
			# Imprimir las transformaciones
			print("-------------------------------------------------------------------------------")
			print("---------------------------INFORMACIÓN ADICIONAL-------------------------------")
			print("Cantidad total de ejemplos:",escalaAtributos.shape[0]);
			print("Dimensión de los atributos:",escalaAtributos.shape[1]);
			print("Dimensión de las etiquetas:",escalaEtiqueta.shape[1]);
			# Dividir conjuntos de aprendizaje y prueba
			attrEntrenamiento, attrPrueba, etiquetaEntrenamiento, etiquetaPrueba = train_test_split(escalaAtributos, escalaEtiqueta)
			print("Tamaño del conjunto de entrenamiento:",len(attrEntrenamiento));
			print("Tamaño del conjunto de prueba:",len(attrPrueba));
			# Retornar datos en el orden de creación: (X_train, X_test, y_train, y_test)
			return (attrEntrenamiento, attrPrueba, etiquetaEntrenamiento, etiquetaPrueba)
		except Exception as e:
			print(e)
			raise
		finally:
			print("------------------------------------------")
			print("Conjuntos de datos transformados con éxito")
			print("------------------------------------------")

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
		print("---------------------------RESULTADOS DE LA PRUEBA DEL MODELO-------------------------------")
		print("PÉRDIDA:", loss)
		print("ERROR ABSOLUTO MEDIO (MAE):", mae)
		print("--------------------------------------------------------------------------------------------")

	def _predecir(self, atributos, modelo):
		vector = np.array([atributos])
		pronostico = modelo.predict(vector).flatten()
		return pronostico

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
		
	def _postprocesar(self, minV, maxV, minimoNuevo, maximoNuevo, valor):
		return round(Decimal((((valor - minV) * (maximoNuevo - minimoNuevo)) / (maxV - minV)) + minimoNuevo),4)
		
	def _mostrarTablero(self):
		""" Obtener tablero TensorBoard en el navegador por defecto """
		webbrowser.open("http://robzombie6:6006", new=2, autoraise=True)
		os.system("tensorboard --logdir='/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/mlp/Deep/Tablero'")

