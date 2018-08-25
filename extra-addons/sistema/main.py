#!/usr/bin/env python
# -*- coding: "utf-8" -*-
# Autor: Ranielt Angulo, Rooselvelt Angulo
# Fecha: 31/01/18 
# Versión: 1.1
import apacheV2
import os
import time
from pprint import pprint 

def main():
	
	print("************************************".center(100))
	print("SISTEMA DE GRAVEDAD APACHE II       ".center(100))
	print("************************************".center(100))
	print()
	print("(1).CALCULAR GRAVEDAD DE UN PACIENTE".center(100))
	print("************************************".center(100))
	print("(2).SALIR                           ".center(100))
	print("************************************".center(100))
	opcion = int(input("INGRESA UNA OPCION:"))

	if(opcion >=1 and opcion <=2):

		if(opcion == 1):
			apache = apacheV2.Apache()
			bandera = True
			while bandera:
				os.system("cls")
				print(" CÁLCULO DE LA GRAVEDAD DE PACIENTES".center(100))
				try:
					os.system("cls")
					print("TEMPERATURA".center(100))
					print("***********************************************************")
					print("INGRESA UN VALOR DE TEMPERATURA EN EL RANGO DE (0.0 y 45.0)")
					print("***********************************************************")
					temperatura = float(input("TEMPERATURA:"))
					if(temperatura >= 0.0 and temperatura <= 45.0):
						apache.temperatura(temperatura)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("PRESIÓN ARTERIAL MEDIA".center(100))
					print("***********************************************************************")
					print("INGRESA UN VALOR DE PRESIÓN ARTERIAL MEDIA EN EL RANGO DE (0.0 y 200.0)")
					print("***********************************************************************")
					PAM = float(input("PRESIÓN ARTERIAL MEDIA:"))
					if(PAM >= 0.0 and PAM <= 200.0):
						apache.presionArterialMedia(PAM)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("FRECUENCIA CARDIACA".center(100))
					print("***********************************************************************")
					print("INGRESA UN VALOR DE FRECUENCIA CARDIACA EN EL RANGO DE (0.0 y 200.0)")
					print("***********************************************************************")
					FC = float(input("FRECUENCIA CARDIACA:"))
					if(FC >= 0.0 and FC <= 200.0):
						apache.frecuenciaCardiaca(FC)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("FRECUENCIA RESPIRATORIA".center(100))
					print("***********************************************************************")
					print("INGRESA UN VALOR DE FRECUENCIA RESPIRATORIA EN EL RANGO DE (0 y 55)")
					print("***********************************************************************")
					FR = int(input("FRECUENCIA RESPIRATORIA:"))
					if(FR >= 0 and FR <= 55):
						apache.frecuenciaRespiratoria(FR)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("PH ARTERIAL".center(100))
					print("**********************************************************")
					print("INGRESA UN VALOR DE PH ARTERIAL EN EL RANGO DE (0.0 y 8.0)")
					print("**********************************************************")
					PH = float(input("PH ARTERIAL:"))
					if(PH >= 0.0 and PH <= 8.0):
						apache.phArterial(PH)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("HCO3 SERICO".center(100))
					print("***********************************************************")
					print("INGRESA UN VALOR DE HCO3 SERICO EN EL RANGO DE (0.0 y 55.0)")
					print("***********************************************************")
					HCO3 = float(input("HCO3 SERICO:"))
					if(HCO3 >= 0.0 and HCO3 <= 55.0):
						apache.hco3Serico(HCO3)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("SODIO SERICO".center(100))
					print("***********************************************************")
					print("INGRESA UN VALOR DE (NA) SERICO EN EL RANGO DE (0 y 200)")
					print("***********************************************************")
					NA = float(input("(NA) SERICO:"))
					if(NA >= 0 and NA <= 200):
						apache.naSerico(NA)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("POTASIO SERICO".center(100))
					print("***********************************************************")
					print("INGRESA UN VALOR DE (K) SERICO EN EL RANGO DE (0.0 y 8.0)")
					print("***********************************************************")
					K = float(input("(K) SERICO:"))
					if(K >= 0.0 and K <= 8.0):
						apache.naSerico(K)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("CREATININA SERICA".center(100))
					print("*****************************************************************")
					print("INGRESA UN VALOR DE CREATININA SERICA EN EL RANGO DE (0.0 y 4.0)")
					print("*****************************************************************")
					CS = float(input("CREATININA SERICA:"))
					if(CS >= 0.0 and CS <= 4.0):
						apache.creatininaSerica(CS)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("HEMATOCRITO".center(100))
					print("*****************************************************************")
					print("INGRESA UN VALOR DE HEMATOCRITO EN EL RANGO DE (0.0 y 65.0)")
					print("*****************************************************************")
					H = float(input("HEMATOCRITO:"))
					if(H >= 0.0 and H <= 65.0):
						apache.hematocrito(H)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("LEUCOCITOS".center(100))
					print("*****************************************************************")
					print("INGRESA UN VALOR DE LEUCOCITOS EN EL RANGO DE (0.0 y 45.0)")
					print("*****************************************************************")
					L = float(input("LEUCOCITOS:"))
					if(L >= 0.0 and L <= 45.0):
						apache.leucocitos(L)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("OXIGENACIÓN".center(100))
					print("****************************************************************¨******")
					print("INGRESA UN VALOR DE FIO2 EN OXIGENACIÓN: MENOR A: 0.5  O MAYOR A 0.5")
					print("***********************************************************************")
					fi = float(input("VALOR DE FIO2:"))
					if(fi < 0.5):
						valor = int(input("VALOR ACTUAL DE PaO2 en oxigenación en el rango de (0 y 70):"))
						apache.oxigenacion(fi,valor)
						bandera = False
					else:
						valor = int(input("VALOR ACTUAL DE A-aDO2 en oxigenación en el rango de (0 y 500):"))
						apache.oxigenacion(fi,valor)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("SISTEMA COMA GLASGOW".center(100))
					print("****************************************************************¨******")
					print("APERTURA OCULAR DEL PACIENTE DEL COMA GLASGOW EN EL RANGO ENTRE (1 Y 4)")
					print("***********************************************************************")
					AO = int(input("VALOR DE APERTURA OCULAR DEL PACIENTE:"))
					if(AO >=1 and AO <=4):
						print("******************************************************************")
						print("VALOR DE RESPUESTA MOTORA DEL PACIENTE EN EL RANGO ENTRE (1 Y 6):")
						print("******************************************************************")
						RM = int(input("RESPUESTA MOTORA DEL PACIENTE:"))
						if(RM >=1 and RM <=6):
							print("******************************************************************")
							print("VALOR DE RESPUESTA VERBAL DEL PACIENTE EN EL RANGO ENTRE (1 Y 5):")
							print("******************************************************************")
							RV = int(input("RESPUESTA VERBAL DEL PACIENTE:"))
							if(RV >=1 and RV <=5):
								print("COMA GLASGOW COMPLETADO CON EXITO")
								apache.glasgow(AO,RM,RV);
								bandera = False
							else:
								print("ERROR EN VALOR DE LA RESPUESTA VERBAL")
						else:
							print("VALOR ERRONEO DE RESPUESTA MOTORA:")

					else:
						print("VALOR ERRONEO DE APERTURA OCULAR:")
					
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			time.sleep(1)
			os.system("cls")

			bandera = True
			while bandera:
				try:
					os.system("cls")	
					print("EDAD DEL PACIENTE".center(100))
					print("*****************************************************")
					print("INGRESA LA EDAD DEL PACIENTE EN EL RANGO DE (1 y 110)")
					print("*****************************************************")
					EDAD = int(input("EDAD DEL PACIENTE:"))
					if(EDAD >= 1 and EDAD <= 110):
						apache.evaluarEdad(EDAD)
						bandera = False
				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")

			bandera = True
			while bandera:
				try:
					os.system("cls")
					print("ENFERMEDADES CRÓNICAS DEL PACIENTE".center(100))
					print("******************".center(100))
					print("(1) NINGUNA       ".center(100))
					print("(2) ELECTIVA      ".center(100))
					print("(3) NO-QUIRURGICA ".center(100))
					print("(4) URGENTE       ".center(100))
					print("******************".center(100))
					opcion = int(input("OPCIÓN:"))
					if(opcion >= 1 and opcion <= 4):
						if(opcion == 1):
							apache.evaluarPuntajeCronico("NINGUNA")
							bandera = False

						elif(opcion == 2):
							apache.evaluarPuntajeCronico("ELECTIVA")
							bandera = False

						elif(opcion == 3):
							apache.evaluarPuntajeCronico("NO-QUIRURGICA")
							bandera = False

						elif(opcion == 4):
							apache.evaluarPuntajeCronico("URGENTE")
							bandera = False
						else:
							print("OPCIÓN INCORRECTA")
							continue
					else:
						print("OPCIÓN INCORRECTA")

				except ValueError as e:
					print("NO HA INGRESADO UN VALOR CORRECTO")
					print("VUELVE A INTENTARLO !!!")
			os.system("cls")
			apache.calcularAPS()
			apache.calcularApache()
			apache.calcularMortalidad()
			print("***************************************************".center(100))
			print("GENERANDO REPORTE GENERAL DEL PACIENTE:".center(100))
			print("***************************************************".center(100))
			time.sleep(1)
			os.system("cls")

			print("*********************************************************".center(100))
			print("REPORTE GENERAL".center(100))
			print("*********************************************************".center(100))
			print("FECHA ACTUAL DEL CÁLCULO DE GRAVEDAD:",apache.getFecha())
			print("CANTIDAD VARIABLES MEDIDAS:",apache.getCantidadVariables())
			print("APS:",apache.getAPS())
			print("APACHE II:",apache.getAPACHE())
			print("MORTALIDAD:",apache.getMortalidad())

			
			input("PRESIONE <ENTER> PARA SALIR:")



		else:
			os.system("cls")
			os.system("exit 0")
			
	else:
		print("OPCIÓN INCORRECTA")




if __name__ == '__main__':
	main()