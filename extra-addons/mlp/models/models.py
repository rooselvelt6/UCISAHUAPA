# -*- coding: utf-8 -*-
from ..Deep.rna import RNA
from odoo import models, fields, api
from os import system
from sklearn.preprocessing import MinMaxScaler
import ast
import numpy as np

# Modo aprendizaje. (Fase 1)

_agente = RNA() # Nuevo agente...

def _modo():
    system("clear")
    while True:
        print("**************************")
        print("(1). Modo de Aprendizaje. ")
        #print()
        #print("(2). Modo de Predicción.  ")
        print("**************************")
        fase = input("Indicar el modo de la RNA:")
        try:
            valor = int(fase)
            if((valor > 0) and (valor <=1)):
                if(valor==1):
                    print("Iniciado el modo de Aprendizaje...")
                    print()
                    # Modo entrenamiento
                    _agente._entrenarModelo(); 
                    _agente._probarModelo(); 
                    _agente._mostrarTablero();
                    break;
            else:
                system("clear")
                print("Has cometido un error !!!")
                print("ATENCIÓN. Por favor revisar las opciones del menú...")
                continue;
        except ValueError:
            system("clear")
            print("ATENCIÓN: Debe ingresar un número entero")

# Fase de entrenamiento
#_modo();

# Fase de recuerdo
# Modo predicción (Fase 2)
_modelo = _agente._cargarCompilar(); # Cargar Modelo.
_modelo._make_predict_function();


class mlp(models.Model):
   
    _inherit = 'ingreso.ingreso'

    percepciones = fields.Text(
        string='Percepción del entorno',
    )

    prediccion = fields.Float(
        string='Predicción del tiempo en UCI',
        help='Tiempo estimado de estadía en la UCI', 
    )

    @api.onchange('edad','sexo','color_piel','estadia_hospitalaria','antecedentes','tipo_admision','migracion','ventilacion_mecanica','procesos_invasivos')
    def _onchange_entorno(self):
    	entorno = [];
    	for attr in self:

    		# ESTADÍA HOSPITAL
    		entorno.append(float(attr.estadia_hospitalaria));
    		
    		# ANTECEDENTES
    		if (attr.antecedentes != ""):
    			entorno.append(float(1));
    		if(attr.antecedentes == ""):
    			entorno.append(float(0));

    		# VM
    		entorno.append(float(attr.ventilacion_mecanica));
    		
    		# MIGRACIÓN
    		entorno.append(float(attr.migracion))
    		
    		# COLOR DE PIEL
    		entorno.append(float(attr.color_piel))
    		
    		# PROCESOS INVASIVOS
    		entorno.append(float(attr.procesos_invasivos))
    		
    		# EDAD Cruda entorno.append(float(attr.edad))
            # Edad preprocesada para la RNA
    		entorno.append(float(attr.edad))
    		# SEXO
    		entorno.append(float(attr.sexo))
    		
    		# TIPO DE ADMISION
    		entorno.append(float(attr.tipo_admision))	

    		attr.percepciones = entorno
    
    @api.onchange('percepciones')
    def _onchange_percepciones(self):
        for campo in self:
            lista_atributos = ast.literal_eval(campo.percepciones)
            matriz_prediccion = np.array(lista_atributos)
        matriz_prediccion = np.reshape(matriz_prediccion, (-1,1))
        escala = MinMaxScaler(feature_range=(0,1));
        print(escala.fit(matriz_prediccion))
        final = escala.transform(matriz_prediccion)
        l2 = [x[0] for x in final]
        print(l2)
        if(len(l2)==9):
            # Predicción de la estadía
            #resultado = _agente._estimar(atributos=l2, modelo=_modelo)
            # Prueba
            resultado = _agente._predecir(atributos=l2, modelo=_modelo)
            ##########
            del(l2)
            for attr in self:
                # Original: attr.prediccion = resultado
                # Postprocesar.
                attr.prediccion = _agente._postprocesar(minV=0, maxV=1, minimoNuevo=0, maximoNuevo=41, valor=resultado[0])