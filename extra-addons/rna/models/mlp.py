from datetime import datetime
from decimal import Decimal
from keras import losses, metrics, optimizers
from keras.callbacks import TensorBoard, EarlyStopping
from keras.layers import Dense
from keras.models import Sequential, model_from_json, load_model
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
#import ast
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import webbrowser

class Mlp():
	def __init__(self):
		print("*****************")
		print("Iniciando RNA....")
		print("*****************")
		self.modelo = Sequential();
		self.modelo.add(Dense(units=9, activation="relu", name="Capa_Entrada"))
		self.modelo.add(Dense(units=7, activation="relu", name="Capa_Oculta"))
		self.modelo.add(Dense(units=1, activation="sigmoid", name="Capa_Salida"))
		self.modelo.compile(loss=losses.mean_squared_error, optimizer=optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True), metrics=[metrics.mae])
		# Tupla del Conjunto de datos: orden (X_train, X_test, y_train, y_test)
		self.conjuntos = self.cargarDatos();
		# Tensorboard
		self.tensorboard = TensorBoard(log_dir="/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/models/Tablero/{0}".format(datetime.now()), write_grads=True, write_graph=True, histogram_freq=1)

	def cargarDatos(self):
		try:
			conjunto = np.loadtxt("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/models/Datasets/todo/conjunto_total.csv", delimiter=",")
			x, y = conjunto[:,0:9], conjunto[:,9];
			if(len(x) == len(y)):
				y = np.reshape(y, (-1,1))
				scaler = MinMaxScaler()
				print(scaler.fit(x))
				print(scaler.fit(y))
				xscale = scaler.transform(x)
				yscale = scaler.transform(y)
				X_train, X_test, y_train, y_test = train_test_split(xscale, yscale);
				return (X_train, X_test, y_train, y_test) # Retornar subconjuntos para entrenamiento y prueba
		except Exception as e:
			raise

	def cargarModelo(self):
		json_file = open("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/models/Modelo/modelo.json",'r')
		loaded_model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(loaded_model_json)
		loaded_model.load_weights("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/models/Modelo/pesos.h5")
		return loaded_model

	def guardarModelo(self):
		modelo_json = self.modelo.to_json()
		with open("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/models/Modelo/modelo.json","w") as json_file:
			json_file.write(modelo_json) # Escribir modelo en archivo JSON. Serializar pesos del entrenamiento en formato HDF5 para futuras predicciones del sistema
			self.modelo.save_weights("/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/models/Modelo/pesos.h5");

	def postprocesar(self, minV, maxV, minimoNuevo, maximoNuevo, valor): 
		return (((valor - minV) * (maximoNuevo - minimoNuevo)) / (maxV - minV)) + minimoNuevo

	def obtenerTablero(self):
		webbrowser.open("http://robzombie6:6006", new=2, autoraise=True)
		os.system("tensorboard --logdir='/home/rooselvelt/Escritorio/UDO/SAHUAPA/UCISAHUAPA/extra-addons/rna/models/Tablero/'")

	def entrenar(self):
		early_stop = EarlyStopping(monitor='val_loss', patience=60)
		history = self.modelo.fit(self.conjuntos[0], self.conjuntos[2], epochs=500, batch_size=32, verbose=1, validation_split=0.2, callbacks=[self.tensorboard, early_stop])
		self.guardarModelo()

	def probar(self):
		modelo_cargado = self.cargarModelo();
		modelo_cargado.compile(loss=losses.mean_squared_error, optimizer=optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True), metrics=[metrics.mae])
		scores = modelo_cargado.evaluate(self.conjuntos[1], self.conjuntos[3], batch_size=32, verbose=1)
		print("Resultados:", scores)

	def pruebas(self):
		print("FUncionando bien")