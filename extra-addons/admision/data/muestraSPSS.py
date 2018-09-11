""" DATA DE LA UCI 
	
	Lista de ingresos realizados en la UCI - SAHUAPA DESDE EL AÑO 2013 HASTA EL 2016.

"""

from datetime import datetime, timedelta

# LISTA DE INGRESOS REALIZADOS 

pacientes = [ # INICIO DE LISTA DE REGISTROS

	{
		
		"nombre": "Antonia María Rivas".upper(),
		"ci": "2.291.248",
		"sexo": "F".upper(),
		"fechaNacimiento": datetime(1931, 9, 29),
		"lugarNacimiento": "cumana estado sucre".upper(),
		"edad": 84,
		"dirección": "Cumanacoa calle pichincha numero 6".upper(),

		"fechaIngresoHUAPA": datetime(2016,5,16),	
			
		"fechaIngresoUCI": datetime(2016,5,16),	

		"resumenIngreso": '''Se trata de paciente femenino de 84 años de edad, 
		con antecedente de HTA de larga data, controlada con Nifedipino 30 mg OD, cardiopatía dilatada, 
		quien inicia enfermedad actual hace 3 meses aproximadamente, cuando presenta lesiones en piel generalizadas, 
		descamativas, en tratamiento por el servicio de infectología, el cual evoluciona tórpidamente, por lo que es 
		ingresada el día jueves 12/05/2016 centro privado con: diagnósticos: 
		1) Infección de piel y partes blandas. 2) HTA sistémica. Paciente permanece en área de hospitalización durante 
		72 horas, anexándose al cuadro clínico el día 15/05/2016 disnea en reposo, cianosis peri bucal y acrocianosis y 
		hipertensión arterial 170/100 mmhg por no contar con cupo en uci es trasladada a centro privado punta del Este,
		 donde se constata desaturación por monitor STO2 60 '%' además de alteración del estado de consciencia, por lo que 
		 se realiza maniobras de intubación endotraqueal y se conecta a mecánica. Permanece durante 24 horas en uci y por 
		 condiciones socioeconómicas es referida a nuestro centro asistencial y por disponibilidad de cupo se decide su 
		 ingreso.''',

		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, 
			intubado, recibiendo apoyo de Oxigeno húmedo a través de 
			ventilador de traslado, se conectado a ventilación mecánica con 
			parámetros en modo A/C; Vc: 480; Fl: 50; Fr: 12; TI: 1:4; FiO2: 60; PEEP: 0. 
			Con sonda nasogástrica y Foley funcionante sin gasto. Se conecta a monitor 
			cardiaco continuo que reporta signos vitales: 
			TA: 103/56(70) mmHg FC: 157 lpm FR: 25 rpm SaO2:100 %.''',

			"piel": '''Morena, normotérmica al tacto, se 
			evidencia lesiones en piel generalizada hipercrómicas, 
			descamativas con bordes irregulares y escasa secreción purulenta, 
			llenado capilar menor de 3s.''',

			"cardiopulmonar": '''Tórax simétrico normoexpansible, ruidos respiratorios presentes en ambos hemitorax, con agregados crepitantes hasta 1/3 medio bilateral, ruidos cardiacos arrítmicos regulares sin presencia de soplo ni galope. ''',

			"abdomen": '''RsHs presentes, plano, no impresiona dolor a la palpación superficial y profunda.''',

			"neurologico": '''No evaluable por efectos de sedación farmacológica. A su ingreso se realiza vía venosa central yugular interna derecha sin complicaciones.''',
		},

		"diagnosticoIngresoUCI": ["Insuficiencia respiratoria aguda.", 
								  "Emergencia hipertensiva expresada en edema agudo de pulmón.", 
								  "Infección de piel y partes blandas", 
								  "Hipertensión arterial sistemática"]
	}, # 1

	{ 
		"nombre": "Aracelys Mata".upper(),

		"edad": "40",
		
		"sexo": "F".upper(),	 		
		
		"lugarNacimiento": "cumana estado sucre".upper(), 		
		
		"ci": "13.631.742", 		
		
		"dirección": "san Lorenzo, municipio montes, Cumanacoa, estado sucre.".upper(), 		
		
		"fechaIngresoHUAPA": datetime(2016,5,20),	
		
		"fechaIngresoUCI": datetime(2016,5,20),
		
		"antecedentes": '''linfoma no hodgkin estadio IIBE (tumor mediastinico superior) quien recibe quimioterapia con esquema CHOP (sin rituximab) último ciclo 05/05/2016.''',  

		"resumenIngreso": '''Se trata de paciente femenino de 40 años de edad, cuyos familiares refieren inicio de enfermedad actual 05/05/16 cuando presenta disnea de grandes esfuerzos, persiste sintomática 13/05/16 persiste sintomática y se asocia aumento de la temperatura corporal no cuantificada que atenua con antipiréticos orales, 15/05/16 por exacerbación del patrón de disnea a pequeños esfuerzos y asociarse tos seca , acude a  centro clínico privado, donde se ingresa con los diagnosticos de neumonía severa, derrame pleural, y sepsis respiratoria. permanece por 24 horas. En vista de encontrarse en malas condiones generales, disneica, con crepitantes universales y dependiente de oxigeno, es evaluado por especialista quien decide su traslado e ingreso a UCI con ventilación mecánica no invasiva.''', 
		
		"examenFisicoIngresoUCI": {

				"resumen": '''Se recibe y evalúa paciente proveniente de centro clínico privado, en malas condiciones generales, disneica, recibiendo oxigeno por bigote nasal, afebril, taquicardica, hemodinamicamente estable, se conecta a monitor cardiovascular continuo que reporta TA: 171/83mmhg TAM: 117mmhg FC: 146 LPM FR: 64 RPM SATO2: 82%.''',

				"piel": '''blanca, normotermica, turgor y elasticidad disminuida, llenado capilar menor de 3seg. Se evidencia moderada palidez cutáneo mucosa y multiples equimosis generalizadas.''',

				"cardiopulmonar": '''Tórax simétrico hipoexpansible, ruidos respiratorios presentes en ambos hemitorax, crepitantes universales abundantes, se evidencia tiraje subcostal, intercostal ruidos cardiacos hipofoneticos sin presencia de soplo ni galope.''',

				"abdomen": 	'''RsHs presentes, plano, no impresiona dolor a la palpación superficial ni profunda.''',

				"neurologico": '''consciente, vigil, orientado en tiempo, espacio y persona, lenguaje coherente, pupilas centrales, isocóricas, reactivas a la luz, sin déficit motor ni sensitivo, Glasgow 15/15 ptos.''',
		}, 

		"diagnosticoIngresoUCI": [
									"Insuficiencia respiratoria aguda", 
									"Neumonía severa", 
									"Sepsis respiratoria", 
									"Linfoma No hodgkin estadio IIB-E", 
									{
										"resumen": '''Paciente permanece durante dos días en UCI, recibiendo oxigeno a través de BIPAP, el 19/05/16 en vista de persistencia dificultad respiratoria, y trabajo respiratorio dado por respiración abdominal, aleteo nasal, tiraje subcostal e intercostal se conecta a ventilación con parámetros modo A/C VC: 420 FIO2: 60 FL: 50 FR: 18 PEEP: 7, permanece hemodinamicamente estable y por petición de familiares se decide su traslado a HUAPA.''',
									},
								], 

		"examenFisicoIngresoHUAPA": {

			"resumen":  '''Se recibe paciente en camilla de traslado, recibiendo oxigeno húmedo con sistema de ambú a través de TET, se conecta a ventilación mecánica modo: A/C VC: 550 FIO2: 60 FL:50 FR:14 PEEP: 7 Y monitoreo cardiaco continuo que reporta TA:137/92 Mmhg TAM:101 Mmhg FC:126 LPM FR:12 RPM SATO2:88%. ''',
			
			"piel": '''Blanca, normotérmica, turgor y elasticidad conservado, llenado capilar menor de 3seg. Se evidencia moderada palidez cutáneo mucosa y múltiples equimosis generalizadas en tórax anterior.''',

			"cardiopulmonar": '''Tórax simétrico normoexpansible sin tirajes, ruidos respiratorios presentes en ambos hemitorax, con crepitantes basales escasos  ruidos cardiacos rítmicos  y regulares sin presencia de  soplo ni galope.''',

			"abdomen": '''RsHs presentes, plano, no impresiona dolor a la palpación superficial ni profunda.''',

			"urogenital": '''Se evidencia secrecion blanquecina moderada en labios menores y cavidad vaginal.''',
			
			"neurologico": '''No evaluable por efecto de sedoanalgesia''',


		}, 

		"diagnosticoIngresoHUAPA":[
			
				"INSUFICIENCIA RESPIRATORIA AGUDA",
				"SDRA", 
				"SEPSIS PUNTO DE PARTIDA RESPIRATORIO",
				"NEUMONIA BILATERAL SEVERA",
				"LINFOMA NO HODGKIN ESTADIO IIB-E",
				"MICOSIS VAGINAL A/D",
				"TRAUMATISMO HOMBRO DERECHO",
				"TRASTORNO HEMATOLOGICO: ANEMIA MODERADA",
		], 

	}, # 2

	{
		"nombre": "Carmen Guerra".upper(), 		
		
		"edad": "89",
		
		"sexo": "F",	
		
		"fechaNacimiento": datetime(1938,11,15),	
		
		"lugarNacimiento": "cumana estado sucre".upper(), 		
		
		"ci": "3.339.905", 		
		
		"dirección": "urb 3 picos calle los girasoles N 14".upper(), 		
		
		"fechaIngresoHUAPA": datetime(2016,5,11), 		
		
		"fechaIngresoUCI": datetime(2016,5,11),  		 

		"resumenIngreso": '''Se trata de paciente femenino de 89 años de edad, con antecedente de HTA de larga data, controlada con valsartan 160mg BID y bisoprolol HTC quien inicia enfermedad actual 09/05/16 cuando es llevada a mesa operatoria para realización de artroscopia en rodilla derecha, posterior a acto quirúrgico presenta elevación de cifras tensionales 180/100mmhg y deterioro neurológico dado por Glasgow de 7/15ptos RM: 4 ptos RO: 2 ptos RV: 1pto, sin signos de focalidad neurológica ni meníngeos. Se ingresa a UCI de centro privado con los diagnosticos: Emergencia hipertensiva expresada en EVC de etiología a precisar, POI de artroscopia derecha, HTA sistémica. Paciente permanece en UCI, por estado neurológico se decide intubación endotraqueal y conectar a ventilación mecánica sin complicación descrita, se realiza TAC de cráneo simple donde se evidencia: hematoma intraparenquimatoso agudo en región de ganglios basales izquierdos con extensión a la corona radiada y región fronto temporo parietal izquierda con edema periférico asociado y borramiento de surcos, comprensión ventricular y desplazamiento de la línea media a la derecha en 14 mm. Por requerimiento del familiar y disponibilidad de cupo se refiere a la UCI de este centro con los diagnosticos: Emergencia hipertensiva expresada en EVC hemorrágico en ganglios basales C/C edema perilesional, POM de artroscopia de rodilla derecha, HTA sistémica.''', 

		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, intubado, recibiendo apoyo de Oxigeno húmedo a través de Ambu, por lo que es conectado a ventilación mecánica con parámetros en modo A/C; Vc: 560; Fl: 50; Fr: 12; TI: 1:4; FiO2: 50; PEEP: 0. Con sonda nasogástrica y Foley funcionante sin gasto. Se conecta a monitor cardiaco continuo que reporta signos vitales: TA: 160/67(88) mmHg FC: 77 lpm FR: 12 rpm SaO2:100 %''',
			
			"piel": '''Morena, normotérmica al tacto, normoelástica, llenado capilar menor de 3s.''',

			"cardiopulmonar": '''Tórax simétrico normoexpansible, ruidos respiratorios presentes en ambos hemitorax, sin agregados , ruidos cardiacos rítmicos regulares sin presencia de  soplo ni galope.''',
			
			"abdomen": '''RsHs presentes, plano, no impresiona dolor a la palpación superficial y profunda.''',

			"neurologico": '''No evaluable por efectos de sedación farmacológica.''',
		}, 

		"diagnosticoIngresoUCI": [
									"Emergencia hipertensiva expresada en EVC hemorrágico, en ganglios basales C/C edema perilesional.",
									"POM de artroscopia de rodilla derecha.",
									"HTA sistémica.",
								],  
		
	},# 3

	{ 
		
		"nombre": "ynes mercedes Sánchez Mariña".upper(), 		
		
		"edad": "64",
		
		"sexo": "F",	
		
		"fechaNacimiento": datetime(1953,1,20), 		
		
		"lugarNacimiento": "cumanacoa estado sucre".upper(), 		
		
		"ci": "4.689.075", 		
		
		"dirección": "cantarrana 3era calle casa número 76, Cumaná-Estado Sucre.".upper(), 		
		
		"fechaIngresoHUAPA": datetime(2016,3,18),		
		
		"fechaIngresoUCI": datetime(2016,5,24),		 

		"resumenIngreso": '''Se trata de paciente masculino de 64 años de edad, natural y procedente de la localidad, con antecedentes personales de hipertensión arterial controlada con Valsartan y diabetes mellitus tipo 2, quien inicia enfermedad actual el día 17/05/2016 cuando presenta pérdida de la fuerza muscular en hemicuerpo izquierdo, con desviación de la comisura labial hacia la izquierda, por tal motivo es trasladada a centro privado donde es evaluado, evidenciándose cifras tensionales elevadas, ingresa en UCI durante un periodo de 24 horas, en vista de condiciones socioeconómicas y por deterioro del estado neurológico  es referida a este centro asistencial donde es evaluada e ingresada por el servicio de emergenciologia.''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, intubado, recibiendo oxígeno por ambú, en condiciones clínicas de cuidado, taquicárdica, hipotensa se traslada a cama de UCI, se conecta a ventilación mecánica en modo A/C VC560  FiO2 70  FR 12   FL50  PEEP 0,  y se conecta a monitor cardíaco contínuo que reporta: TA: 75 /55 mmHg TAM 60mmHg FC: 110  lpm FR: 12 rpm SatO2: 94%. ''',
			
			"piel": '''blanca fría al tacto, llenado capilar < 3 segundos. Temp: 36ºC, se evidencia moderada palidez cutánea mucosa.''',

			"cardiopulmonar":  '''torax asimétrico, hipoexpansible, RsRsPs en ambos hemitorax con crepitantes universales bilaterales. RsCs taquicárdicos, no se auscultan soplos.''',
			
			"abdomen": ''' globoso a expensas de panalículo adiposo, blando depresible no impresiona doloroso a la palpación, no megalias.''',

			"neurologico": '''px  Bajo efectos de sedación farmacológica, Glasgow no evaluable. Pupilas isocóricas hiporreactivas.''',

			"extremidades": '''simétricas , sin edema.''',

		}, 

		"diagnosticoIngresoUCI": ["Crisis hipertensiva"],  

		"examenFisicoIngresoHUAPA": {

			"resumen": '''T/A 160/100 mmHg  FC94lpm Fr 12rpm. A su ingreso presenta deterioro del estado de consciencia dado por Glasgow de 7/15 pts RM 4 pts RO 2 pt RV 1 pt, por lo que se decide maniobras de intubación endotraqueal y se conecta a ventilación mecánica en modo AC VC 450 FIO2 60 FL 50 FR 12 PEEp 0, posteriormente se realiza TAC de cráneo donde se evidencia lesión isquémica en región parietal derecha. Permanece durante  6 días en área de emergencia, intubada y conectada a ventilación mecánica, con evolución clínica tórpida. En vista de las condiciones clínicas del paciente y de disponibilidad de cupo se decide su ingreso en la unidad de cuidados intensivos.''',

			"piel": '''blanca, normotérmica, normoelástica, llenado capilar < de 3 segundos. ''',

			"cardiopulmonar": '''Torax simétrico, normoexpansible, RsRsPs en ambos hemitorax , se auscultan crepitantes bibasales. RsCsRsRs sin soplo ni galope.''',

			"abdomen": '''Globoso a expensas de panalículo adiposo, Blando, depresible, no impresiona doloroso a la palpación, no megálico.''',

			"extremidades": '''simétricas, sin edema.''',

			"neurologico": '''Px inconsciente, Glasgow 7 ptos /15ptos dado por RO2ptos, RV1pto, RM4ptos.''',

		},  

		"diagnosticoIngresoHUAPA": [
				"EVC de etiología a precisar.",
				"Broncoaspiracion.",
				"HTA.",
				"Diabetes mellitus tipo 2.",
		], 
		
	}, # 4

	{
		"IdHistoria": "54-13-38", 
		"nombre": "Sael José Astudillo Lara".upper(), 		
		"edad": "60",
		"sexo": "M",	
		"fechaNacimiento": datetime(1955,1,16), 		
		"lugarNacimiento": "San Antonio del golfo", 		
		"ci": "5.084.783", 		
		"dirección": "urbanización los chaimas bloque 3B apartamento 2 planta baja", 		
		"fechaIngresoHUAPA":datetime(2015,12,30), 		
		"fechaIngresoUCI": datetime(2016,1,1),

		"resumenIngreso": '''Se trata de paciente masculino de 60 años d edad con antecedentes de Hipertensión Arterial controlada con Nifedipino LP 60 mg OD, diabetes mellitus tipo en tratamiento con glibenclamida 5 mg OD, glucofage 500 mg OD, quien inicia enfermedad actual el día 27/12/2015 cuando presenta cefalea intensa acompañado de vómitos en 2 oportunidades, el día 28/12/2015 se anexa al cuadro parestesia de extremidad superior derecha por lo que acude a centro privado donde constatan cifras de tensión arterial elevadas (230/110 mmhg), anexándose posteriormente hemiparesia derecha, lenguaje disartrico y cefalea intensa, siendo ingresado durante 48 horas en centro privado, presentando posteriormente somnolencia y por persistencia de síntomas es trasladado a nuestro centro asistencial siendo valorado por el servicio de medicina interna e ingresado.''', 

		"examenFisicoIngresoUCI": {
			
			"piel": '''morena, normotérmica, a febril al tacto, llenado capilar <3segundos.''',

			"cardiopulmonar":  '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, se auscultan estertores tipo roncos en ambos campos pulmonares y crepitantes a predominio derecho. Ruidos cardíacos arrítmicos, irregulares, no se auscultan soplos ni galope.''',
			
			"abdomen": ''' globoso a expensa de panículo adiposo, blando, no doloroso a la palpación, sin megalias.''',

			"neurologico": ''' No evaluable por efectos de sedación farmacológica. Pupilas mióticas. Previa asepsia y antisepsia de región lateral derecha del cuello, infiltración de anestesia local se realiza cateterización de vía venosa yugular interna derecha, se realiza xifonaje positivo y se solicita RX de tórax para comprobar su correcta colocación.''',
		}, 

		"diagnosticoIngresoUCI": [
									"Insuficiencia respiratoria aguda",
									"Infección Respiratoria Baja: Neumonía por Broncoaspiración",
									"Evc isquémico en región occipital izquierda",
									"Trastorno del ritmo fibrilación auricular con respuesta ventricular rápida",
									"Diabetes mellitus tipo 2",
									"Hipertensión arterial sistémica",
								],  

		"examenFisicoIngresoHUAPA": {

			"resumen": ''' Signos vitales: Fr: 23 rpm Fc: 110 lpm TA 190/120 () mmHg ''',

			"piel": ''' Morena, normotermica, normohídrica, llene capilar < 3 seg. ''',

			"cabeza": 	''' Se evidencia herida en pirámide nasal. ''',

			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos ni galope.''',

			"abdomen": '''globoso, a expensa de panículo adiposo, blando, no doloroso a la palpación, ruidos hidroaéreos presentes, sin megalias. ''',

			"neurologico": '''somnolienta, con desviación de la comisura labial hacia la derecha, lenguaje disartrico, parestesia del lado derecho. ''',
		},  

		"diagnosticoIngresoHUAPA": [
					"Crisis hipertensiva tipo emergencia expresada en evc de etiología a precisar",
					"Fibrilación auricular con respuesta ventricular rápida",
					"Diabetes mellitus tipo 2 compensada",
					"Hipertensión arterial sistémica.",
					{"resumen": '''El paciente permanece durante 72 horas en área de observación adulto  recibiendo tratamiento con múltiples antipertensivo, Nitroprusiato de sodio durante 24 horas, posteriormente se realiza procedimiento de colocación de sonda nasogástrica siendo dirigida hacia vías respiratorias y utilizada para la administración de alimentación, presentando cuadro de dificultad respiratoria el día 31/12/2015 persistiendo sintomático, anexándose el día 01/01/2016 deterioro del estado neurológico por lo que solicitan valoración por el servicio de UCI quien acude al llamado, evaluando paciente en condiciones clínicas de cuidado, taquipneico, conectado a monitor cardiaco que reporta STO2 82 '%' con agregados pulmonares tipos crepitantes bilaterales abundantes, por lo que se realiza maniobras de intubación endotraqueal y se conecta a ventilación mecánica en modo A/C fr 12 fio2 60 '%' fl 50 vc 640 peep 0, por disponibilidad de cupo se decide su ingreso a uci. Se recibe paciente en camilla de traslado intubado, recibiendo oxigeno húmedo por ambu, se traslada a cama UCI y se conecta a monitor cardiaco que reporta Fr: 14 rpm Fc: 123 lpm TA 98/66 (78) mmHg SATO2: 100% y a ventilador mecánico evita 4 modo AC Vc: 640 Fr: 12 Fl: 50 TI 1:4 FiO2: 60 PEEP: 0. '''}
		], 
		
	},# 5

	{
		"IdHistoria": "38-08-99", 
		"nombre": "José gózalez".upper(), 		
		"edad": "68",
		"sexo": "M",	
		"fechaNacimiento": datetime(1947,7,8), 				
		"ci": "2.929.542", 		
		"dirección": "Urb. San José Edificio Mochima Piso 3 Apto 15  ", 		
		"fechaIngresoHUAPA": datetime(2016,2,10),	
		"fechaIngresoUCI":datetime(2016,2,10),		 
		"resumenIngreso": '''Se trata de paciente masculino de 68 años de edad, natural y procedente de la localidad, con antecedente de hipertensión arterial sistémica desde hace 20 años aproximadamente, controlada, cuyo familiar refiere inicio de enfermedad actual el día  06/01/ 2016 cuando  presenta dolor típico coronario irradiado a región escapular izquierda, que cede espontáneamente, manteniéndose asintomático hasta el día 06/02/2016, para este mismo día presenta nuevamente dolor típico coronario, acompañado de sudoración profusa, nauseas, concomitantemente dificultad respiratoria a mediados y pequeños esfuerzos, motivo por el cual es llevado a centro clínico privado donde es evaluado por intensivista de guardia quien en vista de compromiso respiratorio  y riesgo cardiovascular se decide su ingreso a UCI, donde permaneció hospitalizado por 5 días, por razones económicas se plantea su traslado para la unidad de cuidados intensivos del HUAPA. Previa valoración se decide su ingreso.''', 

		"examenFisicoIngresoUCI": {

			"resumen": '''Paciente es trasladado en camilla de transporte recibiendo oxigeno húmedo a través de tubo endotraqueal a razón de 10 litros por minuto; se traslada a cama UCI, conectándose a monitor cardiaco externo que reporta signos vitales: TA: 74/54 mmHg FC: 41  lpm  FR: 15 rpm  SPO2: 90% ''',
			
			"piel" : 	'''Morena normotérmica al tacto, hidratada llenado capilar < 3 seg.''',

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares estertores roncus difuso bilaterales,  Ruidos cardiacos bradicardico rítmicos no soplos.''',
			
			"abdomen": '''plano blando depresible no dolorosos a la palpación sin visceromegalias.''',

			"neurologico": '''no evaluable por efecto de sedación y relajación farmacológica. ''',
			
			"extremidades": '''eutróficas, asimétricas sin edema''',

		}, 

		"diagnosticoIngresoUCI": [
									"SHOCK CARDIOGENICO",
									"SINDROME CORONARIO AGUDO",
									"EDEMA AGUDO DE PULMON",
									"INSUFICIENCIA RESPIRATORIA AGUDA",
									"CARDIOPATIA ISQUEMICA",
									"HIPERTENCION ARTERIAL SISTEMICA",
									"DIABETES MELLITUS TIPO 2",
								],  


		"examenFisicoIngresoPrivado": {

			"resumen": '''TA: 97/44 mmHg FC: 157 lpm FR: 46  rpm. Se recibe paciente proveniente del área de emergencia en camilla de transporte, en malas condiciones generales, sudoroso, facie abotagada, con oxígeno por cánula nasal, cianosis bucal y peribucal, y en vista de  presentar franco trabajo respiratorio, con desaturación por monitoreo, se procede a intubación y conexión a ventilación mecánica modo: A/C  VC: 450, FiO2: 60, F1: 40, FR: 16, PEEP: 10;  bajo sedación y analgesia, permanece 3 días hospitalizado en unidad de cuidados intensivo, en condiciones de cuidados, contaje de leucocitos en ascenso, afebril, ameritando de Dobutamina (30cc/hora), Trangorex a través de bomba de infusión continua a 21 cc/hora, Imipenem ajustado a ClCr (43,7 ml/min), lasix 40 mg VEV cada 6 horas, Aspirina, Clexane, Plavix y Atorvastatina. Siendo evaluado por Cardiólogo quien indica Dopamina durante 24 horas. Para el día 10/02/2016 se reportan elevación de azoados (Urea: 157 mg/dl y Creatinina: 1.8 mg/dl), transaminasas: TGO: 1049 U/I  TGP: 880 U/I y LDH: 1845 U/I. ''',

			"piel": '''ligera palidez cutáneo-mucosa, hidratada turgor y elasticidad propia de la edad llenado capilar < 3 seg. ''',

			"cardiopulmonar": '''Tórax simétrico, hipoexpansible ruidos respiratorios presentes en ambos hemitorax, se auscultan crepitantes y roncus ruidos cardiacos rítmicos y regulares normofonéticos taquicardicos, sin soplo ni galope.''',

			"abdomen": '''Ruidos hidroaéreos presentes, blando depresible no dolorosos a la palpación sin visceromegalias.''',

			"extremidades": '''Simétrica eutrófica, sin edema.''',

			"neurologico": '''Consiente, orientado, pupilas isocóricas, normorreactivas a la luz, Glasgow 15/15.''',

		},  
		"diagnosticoIngresoHUAPA": [
				"INSUFICIENCIA RESPIRATORIA AGUDA",
				"SINDROME CORONARIO AGUDO",
				"CARDIOPATIA ISQUEMICA", 
				"EDEMA AGUDO DE PULMON",
		], 
		
	}, # 6

	{
		"IdHistoria": "54-54-35", 
		
		"nombre": "Eudis José López tachou".upper(), 		
		
		"edad": "41",
		
		"sexo": "F",	
		
		"fechaNacimiento": datetime(1977,11,6), 		
		
		"lugarNacimiento": "Guiria estado sucre", 		
		
		"ci": "12.215.863", 		
		
		"dirección": "Guiria calle principal", 		
		
		"fechaIngresoHUAPA": datetime(2016,5,11),

		"fechaIngresoUCI": datetime(2016,5,12),

		"resumenIngreso": '''Se trata de paciente femenino de 41 años de edad, con antecedente de lupues eritematoso sistémico en tratamiento con prednisona 10 mg OD, epilepsia en tratamiento valcote, litiasis vesicular, antecedente quirúrgico de tu quístico en el año 2014, quien inicia enfermedad actual el día sábado 07/05/2016 cuando posterior a ingesta copiosa presenta dolor abdominal difuso y nauseas, motivo por el cual acude a ambulatorio de la localidad donde administran tratamiento con analgésico permaneciendo bajo observación médica, en vista de persistir sintomática es referida a hospital de Carúpano el día lunes 09/05/2016 siendo evaluada por el servicio de cirugía realizando eco abdominal  que reporta Pancreatitis aguda, Litiasis Vesicular, ascitis leve y esteatosis hepática, por lo que deciden referir a nuestro centro asistencial el día miércoles 11/05/2016 por no contar con servicio de ambulancias, es evaluada por el servicio de cirugía el cual decide su ingreso con los diagnósticos: PANCREATITIS AGUDA NECROTIZANTE, LES, SINDROME CONVULSIVO, HTA''', 

		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, intubado, recibiendo apoyo de Oxigeno húmedo a través de Ambu, por lo que es conectado a ventilación mecánica con parámetros en modo A/C; Vc: 560; Fl: 50; Fr: 12; TI: 1:4; FiO2: 60; PEEP: 0. Con sonda nasogástrica y Foley funcionante sin gasto. Se conecta a monitor cardiaco continuo que reporta signos vitales: TA: 98/67(88) mmHg FC: 88 lpm FR: 15 rpm SaO2:100 %''',
			
			"piel" : 	'''Morena, normotérmica al tacto, deshidratada, llenado capilar menor de 3s.''',

			"cardiopulmonar":  ''' Tórax simétrico normoexpansible, ruidos respiratorios presentes en ambos hemitorax, sin agregados, ruidos cardiacos rítmicos regulares sin presencia de soplo ni galope.''',
			
			"abdomen": '''RsHs presentes, globoso a expensa de panículo adiposo, blando, depresible, se evidencia herida quirúrgica limpio y seco con presencia de drenes conectados a bolsas recolectoras con moderado gasto hemático.''',

			"neurologico": ''' No evaluable por efectos de sedación farmacológica.''',
		}, 

		"diagnosticoIngresoUCI": [
									"POM de laparotomía debido a pancreatitis aguda necrotizante", 
									"PANCREATITIS AGUDA NECROTIZANTE",
									"Insuficiencia renal aguda de origen pre-renal",
									"Litiasis vesicular", 
									"LES",
									"SINDROME CONVULSIVO",
									"Trastorno hematológico:", 
									"Anemia severa",
									"Trombocitopenia severa",
								],  

		"examenFisicoIngresoHUAPA": {

			"resumen": '''El paciente es llevado a mesa operatoria, donde bajo anestesia general realizan laparotomía media supra umbilical, con hallazgos de 100 cc de líquido seropurulento libre, parche de fibrina en curvatura mayor de estómago que involucra cabeza de páncreas, páncreas saponificado con aumento de tamaño de 15x 10  aproximadamente con necrosis de la cabeza y cuerpo de 5 cm aproximadamente, tomando como conducta, toma de muestra para cultivo, adherenciolisis en curvatura menor de estómago, necrosectomia en cabeza y cuerpo páncreas, sin evidencias de conductos pancreáticos, rafia con seda 2-0 y se deja 3 drenes extraídos por contra abertura dirigidos a lecho quirúrgico, y correderas parietocólicas, se realiza cierre por planos asepsia final, siendo trasladada posteriormente a área de recuperación de quirófano, donde se conecta a ventilación mecánica por parte del servicio de Terapia intensiva con parámetros establecidos y se realizan sugerencias. Permanece durante 24 horas en área de recuperación, intubada y conectada a ventilación mecánica, por disponibilidad de cupo se decide su ingreso a unidad de cuidados intensivos.''',
			
			"piel": '''Morena, normotérmica al tacto, deshidratada, se evidencia tinte ictérico en piel y mucosa llenado capilar menor de  3s.''',

			"cardiopulmonar": '''Tórax simétrico normoexpansible, ruidos respiratorios presentes en ambos hemitorax,  sin agregados, ruidos cardiacos rítmicos regulares sin presencia de  soplo ni galope.''',

			"abdomen": '''globoso a expensa de panículo adiposo, blando, depresible, doloroso a la palpación en toda su extensión, a predominio de hemiabdomen superior con signos de irritación peritoneal.''',

			"neurologico": '''conservado.''',
		},  
		
	}, # 7

	{
		"IdHistoria": "54-52-79", 
		"nombre": "Carmen Guerra", 		
		"edad": "89",
		"sexo": "F",	
		"fechaNacimiento": datetime(1938,11,15), 		
		"lugarNacimiento": "cumana estado sucre, ", 		
		"ci": "3.339.905", 		
		"dirección": "urb 3 picos calle los girasoles N 14", 		
		"fechaIngresoHUAPA": datetime(2016,5,11), 		
		"fechaIngresoUCI": datetime(2016,5,11),	

		"resumenIngreso": '''Se trata de paciente femenino de 89 años de edad, con antecedente de HTA de larga data, controlada con valsartan 160mg BID y bisoprolol HTC quien inicia enfermedad actual 09/05/16 cuando es llevada a mesa operatoria para realización de artroscopia en rodilla derecha, posterior a acto quirúrgico presenta elevación de cifras tensionales 180/100mmhg y deterioro neurológico dado por Glasgow de 7/15ptos RM: 4 ptos RO: 2 ptos RV: 1pto, sin signos de focalidad neurológica ni meníngeos. Se ingresa a UCI de centro privado con los diagnosticos: Emergencia hipertensiva expresada en EVC de etiología a precisar, POI de artroscopia derecha, HTA sistémica. Paciente permanece en UCI, por estado neurológico se decide intubación endotraqueal y conectar a ventilación mecánica sin complicación descrita, se realiza TAC de cráneo simple donde se evidencia: hematoma intraparenquimatoso agudo en región de ganglios basales izquierdos con extensión a la corona radiada y región fronto temporo parietal izquierda con edema periférico asociado y borramiento de surcos, comprensión ventricular y desplazamiento de la línea media a la derecha en 14 mm.''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, intubado, recibiendo apoyo de Oxigeno húmedo a través de Ambu, por lo que es conectado a ventilación mecánica con parámetros en modo A/C; Vc: 560; Fl: 50; Fr: 12; TI: 1:4; FiO2: 50; PEEP: 0. Se conecta a monitor cardiaco continuo que reporta signos vitales: TA: 114/85 (101) mmHg FC: 113 lpm  FR: 24 rpm SaO2: 96%''',
			
			"piel" : 	'''Morena, normotérmica al tacto, normoelástica, llenado capilar > 3s.''',

			"cardiopulmonar":  '''Tórax simétrico normoexpansible, ruidos respiratorios presentes en ambos hemitorax,  sin agregados , ruidos cardiacos rítmicos regulares sin presencia de  soplo ni galope.''',
			
			"abdomen": '''RsHs presentes, plano, no impresiona dolor a la palpación superficial y profunda.''',

			"neurologico": ''' No evaluable por efectos de sedación farmacológica.''',

		}, 

		"diagnosticoIngresoUCI": [
									"Emergencia hipertensiva expresada en EVC hemorrágico en ganglios basales C/C edema perilesional",
									"POM de artroscopia de rodilla derecha",
									"HTA sistémica ",
								],  		
	}, # 8

	{
		"IdHistoria": "54-10-94", 
		"nombre": "Víctor Antonio Castillejo Díaz", 		
		"edad": "45",
		"sexo": "M",	
		"fechaNacimiento": datetime(1970,11,27), 		
		"lugarNacimiento": "Cumana", 		
		"ci": "10.948.792", 		
		"dirección": "Urb. Gran Mariscal", 		
		"fechaIngresoHUAPA": datetime(2016,1,25), 		
		"fechaIngresoUCI": datetime(2016,1,29), 		
		"resumenIngreso": '''Paciente masculino de 45 años de edad, natural de la localidad y procedente de El Callao Estado Bolívar, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual desde el 9 de noviembre del 2015, cuando comienza a presentar dificultada respiratoria a mediados y pequeños esfuerzo acompañado con vómitos en múltiples ocasiones, motivo por el cual acude a medico  de su localidad donde es evaluado por especialista (NEFROLOGO) quien en vista de constatar cifras de tensión arterial elevadas indica tratamiento con Adalat Oro (no precisan dosis);  por persistencia de cifras de tensión arterial elevadas acude a cardiólogo quien evalúa y por resultados de paraclínicos refiere nuevamente a Nefrologia, acude a este centro donde es evaluado por especialista la Dra. Navas quien indica laboratorio control que evidencia cifras de HB 9.8 g/dl y retención de azoados; refiere al servicio de medicina interna para su hospitalización. El día 20/12/15 es trasladado al servicio de nefrología donde colocan catéter de hemodiálisis e inician tratamiento dialítico, por mejoría clínica el paciente egresa el 02/01/2016 continuando en plan de diálisis (Martes y Jueves). El día 24/01/2016 es traído a este centro por presentar sangrado activo a través de catéter por lo que es evaluado por residente de nefrología quien realiza cura compresiva e indica tratamiento con Vitamina k, Dicynone y egresa.  El paciente regresa ese mismo día por persistir el sangrado, por lo que se decide su ingreso. El día siguiente 25/01/2016 se decide retirar catéter por  mala posición del mismo, presentando sangrado activo, aumento de cifras de tensión arterial concomitantemente perdida del estado de consciencia, por lo que es llevado a observación adulto, donde se evalúa, se indica TAC de cráneo que reporta lesión isquémica en región occipital izquierda y edema cerebral en hemisferio derecho; debido a que el paciente presenta convulsiones y deterioro del estado neurológico, se decide intubación endotraqueal y conectar a ventilación mecánica. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente es trasladado en camilla de transporte intubado recibiendo oxígeno a través de ambu; se traslada a cama UCI, conectándose a ventilación mecánica modo A/C FiO2: 60 Fr: 12  Vc: 560, Fi: 50, PEEP: 0 y a monitor cardiaco externo que reporta signos vitales: TA: 146/112 mmHg FC: 109 lpm FR: 21 rpm SPO2: 99 %''',
			
			"piel" : 	'''Morena normotérmica al tacto llenado capilar < 3 seg''',

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares sin agregados Ruidos cardiacos taquicardicos no soplos.''',

			"abdomen": '''Plano, ruidos hidroaéreos presentes blando depresible no doloroso a la palpación no visceromegalias.''',

			"neurologico": '''Inconsciente, Glasgow 7/15 pts. RV: 1pts limitado por tubo endotraqueal, RO: 1 pts. RM: 5 pts. Pupilas isocóricas, hiporreactiva a la luz''',

			"extremidades": '''eutróficas, simétrica sin edema, con hemiparesia en hemicuerpo izquierdo.''',

		}, 

		"diagnosticoIngresoUCI": [

									"E.V.C Isquémico en Región Occipital Izquierda.",
									"Crisis hipertensiva tipo emergencia expresada en EVC isquémico",
									"IRB neumonía asociada a ventilación mecánica ", 
									"Enfermedad Renal Crónica  estadio V.",
									"Infección del tracto urinario micotica.",
									"Trastorno Hematológico: Anemia Severa.",
								],  

		"examenFisicoIngresoHUAPA": {

			"resumen": '''TA: 120/80  mmHg FC: 70 lpmFR: 20  rpm''',

			"piel": '''morena normotérmica normoelástica ''',

			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares sin agregados Ruidos cardiacos rítmicos no soplos.''',
			
			"abdomen": '''blando depresible no dolorosos a la palpación superficial ni profunda ruidos hidroaéreos positivos.''',
			
			"extremidades": '''eutróficas, simétrica sin edema. ''',

			"neurologico": '''consiente orientado en tiempo espacio y persona''',

		},  

		"diagnosticoIngresoHUAPA": [
			"Sangrado a través de catéter de diálisis",
			"Hipertensión arterial sistémica",
			{"resumen": '''El paciente permanece en observación adulto hasta el día de hoy 29/01/2016 cuando por disponibilidad de cupo en UCI se decide su ingreso. '''}			

		], 
		
	}, # 9

	{
		"IdHistoria": "54-52-78", 
		"nombre": "José Luis Martínez", 		
		"edad": "58",
		"sexo": "M",	
		"fechaNacimiento": datetime(1958,6,18), 		
		"lugarNacimiento": "Cumaná, Sucre ", 		
		"ci": "5.693.268", 		
		"dirección": "La trinidad vereda # 5 casa Nro 25. Cumaná, Estado Sucre", 		
		"fechaIngresoHUAPA": datetime(2016,5,9), 	
		"fechaIngresoUCI": datetime(2016,5,9),	

		"resumenIngreso": '''Se trata de paciente masculino de 58 años de edad, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual el 03/05/16 cuando posterior a esfuerzo físico presenta dolor en región lumbar derecha de severa intensidad, motivo por el cual acude a centro asistencial el día después donde previa evaluación clínica y paraclínica se indica tratamiento. Por persistencia de sintomatología acude nuevamente a facultativo quien realiza Eco abdominopelvico n hallazgos significativos. Para el día 05/05/16 se anexa al cuadro clínico aumento de la temperatura corporal cuantificada en 39 ºC; acompañada de escalofríos, por lo que familiar en varias ocasiones le administra  paracetamol endovenoso. El 08/05/16 en horas de la madrugada persiste aumento de temperatura cuantificada en 40ºC concomitante vómitos en número de 5 precedidos de nauseas de contenido alimentario, por lo que familiar administra Dipirona endovenosa; Para el día 09/05/16 en horas de la mañana es encontrado por familiar presentando movimientos tónico clónicos de aproximadamente 3 minutos de duración con relajación de esfínter vesical, motivo por el cual es trasladado a este centro donde previa evaluación clínica se  evidencian varios episodios de movimientos tónico clónicos y  rigidez de nuca, por lo que se realiza punción lumbar  que reporta:  2 ml de líquido ligeramente turbio, de color amarillo claro; contaje celular de 150 cel/mm3 ; Pandy positivo; proteínas 200mg/dl; hematíes de 1 a 3 XC  y leucocitos  de 2 a 3 XC con 70'%' de Segmentados, 21'% 'de Linfocitos y 01'% 'de Eosinófilos; en vista de resultados patológicos se ingresa con diagnósticos: Infección de Sistema Nervioso Central: Meningoencefalitis Bacteriana, Trastorno Hematológico: Anemia Moderada (7,6 mg/dl).''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente que luce en malas condiciones generales conectado a ventilación mecánica a través de TET con parámetros en modo A/C; Vc: 560; F: 50; F:12; TI: 1; FiO2: 50; PEEP: 0.  Conectado a monitor cardiaco continuo que reporta los siguientes parámetros: FC: 83  lpm FR: 12 rpm SaO2: 97% TA: 137/75mmHg  (111)''',
			
			"piel" : 	'''Morena, normotérmica al tacto, normoelástica, llenado capilar > 3s.''',

			"cardiopulmonar":  '''Tórax simétrico normoexpansible, ruidos respiratorios presentes en ambos hemitorax, se auscultan agregados tipo roncus dispersos, ruidos cardiacos rítmicos regulares sin presencia de  soplo ni galope.''',
			
			"abdomen": '''RsHs (Positivo), plano, no impresiona dolor a la palpación superficial y profunda.''',

			"neurologico": '''Glasgow 8/15 ptos; (AO: 1 punto;  RV: 1 Pto, limitado por TET; RM: 6 Ptos); pupilas anisocóricas con miosis derecha; hiporreactivas a la luz. ''',
		}, 

		"diagnosticoIngresoUCI": [
									"Infección de Sistema Nervioso Central: Meningoencefalitis Bacteriana",
									"Trastorno Hematológico: Anemia Moderada (7,6 mg/dl)",
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": '''Se evalúa paciente en AsRsCsGs, Afebril, disneico y sudoroso; Signos vitales al ingreso: TA: 110/70mmHg  Fr: 26 rpm  FC: 98 lpm  T: 37 ºC. En vista de trabajo respiratorio; se decide intubar al paciente y por condición clínica del paciente se expide interconsulta a la Unidad de Cuidados Intensivos, quien por disponibilidad de cupo decide ingresar. ''',

			"piel": '''Morena N/T, N/H;  llenado capilar < 3 segundos.''',

			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos hemitorax sin agregados adventicios a la auscultación. ''',

			"abdomen": '''Blando, depresible, no doloroso a la palpación profunda y superficial. ''',

			"extremidades": '''Simétricas, eutróficas, sin edemas.''',

			"neurologico": '''Inconsciente; con respuesta al dolor, rigidez de nuca; pupilas iscóricas con tendencia a la midriasis.''',
		},  
		
	},  # 10

	# OTROS MÁS

	{
		"nombre": "Carmen Verónica Hernandez", 		
		"edad": "80",
		"sexo": "F",	
		"fechaNacimiento": datetime(1926,1,26),		
		"lugarNacimiento": "Cumaná-Estado Sucre ", 		
		"ci": "2647334", 		 		
		"fechaIngresoHUAPA": datetime(2016,5,12),  		
		"fechaIngresoUCI":datetime(2016,5,12),
		"fechaEgreso": "13/05/2016", 		

		"resumenIngreso": '''Se trata de paciente femenino de 80  años de edad, natural y procedente de la localidad, conocida de hipertensión arterial en tratamiento con Diovan 80mg OD y diabetes Mellitus no controlada, antecedente de Tu de Cabeza de Páncreas para lo cual requirió derivación bilio-digestiva en agosto 2015, quien inicia enfermedad actual el día 12/05/2016 en horas de la mañana cuando presento disminución de fuerza muscular de hemicuerpo derecho, desviación de la comisura labial y lengua disartrico, motivo por el cual acude a centro clínico privado donde es evaluado por médico de guardia quien decide su ingreso.''', 

		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de transporte, tolerando aire ambiente, se traslada a cama de UCI, se conecta a monitor cardiaco que reporta: TA: 106/66(82) mmHg FC: 66 lpm FR: 14 rpm SPO2: 100 %''',
			
			"piel" : 	'''Morena, normotérmica y normohidratada, llenado capilar <3 segundo.''',

			"cardiopulmonar":  '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos normofonéticos regulares,  sin soplos ni galope. ''',
			
			"abdomen": '''globoso, no impresiona doloroso a la palpación, ruidos hidroaéreos presentes, no megalias. ''',

			"neurologico": '''Consciente con tendencia a la somnolencia, pupilas isocóricas, normorreactivas a la luz, Glasgow 15/15 ptos. Se evidencia monoplejía braquial derecha y monoparesia crural derecha. FM en Miembro superior derecho I/V, Miembro Inferior Derecho III/V, ROT II/IV.''',

			"extremidades": '''simétricas, eutróficas, sin edemas.''',
		}, 

		"diagnosticoIngresoUCI": [
									"EVC Isquémico Occipital Bilateral y Parietal Izquierdo.",
									"Tu de Cabeza de Páncreas.",
									"Hipertensión Arterial Sistémica.",
									"Diabetes mellitus tipo 2.",
									"Trastorno Hematológico: Anemia Leve.",
								],  
		
		"examenFisicoIngresoPrivado": {

			"resumen": '''TA: 120/70 mmHg FC: 72 lpm FR: 12 rpm SPO2: %''',

			"neurologico": '''consciente con tendencia a la somnolencia, orientada en persona, fluctuante en espacio y tiempo, lenguaje hipofluente, bradilálico, hemiparesia desproporcionada derecha, FM de miembro superior derecho I/V, miembro inferior derecho II/V, ROT II/IV. Sin alteraciones, VII par craneal directo central leve dado por la desviación de la comisura labial hacia la izquierda, sin signos meníngeos.Se realiza estudio tomografico cerebral que reporta Imágenes hipodensa occipital bilateral a predominio izquierdo y parietal alta izquierda subjetivo de EVC Isquémico reciente, cambios involutivos corticales y subcorticales propios de la edad; paciente permanece con evolución clínica tórpida; el día 13/05/2016 se realiza EEG que concluye anormal lento desorganizado. En vista de condiciones socioeconómicas el 13/05/2016 se decide su traslado a UCI Adultos del HUAPA''',

		},  
		
		"diagnosticoIngresoPrivado": [
					"Síndrome de Déficit de Conciencia.",
					"EVC  de etiología a precisar",
					"Tu. de Cabeza de Páncreas con MT hepática por antecedentes",
		], 
		
	},  # 11

	{
		"IdHistoria": "54-30-11", 
		"nombre": "Eleazar Malavé Amaya", 		
		"edad": "40",
		"sexo": "M",	
		"fechaNacimiento": datetime(1976,5,27),  		
		"lugarNacimiento": "Cumaná - Estado Sucre", 		
		"ci": "12.276.985", 		
		"dirección": "Brasil, Sector III, Calle 13", 		
		"fechaIngresoHUAPA": datetime(2016,2,21), 		
		"fechaIngresoUCI":datetime(2016,2,26), 

		"resumenIngreso": '''Se trata de paciente masculino de 40 años de edad, natural y procedente de la localidad, sin antecedentes conocidos, cuyo familiar refiere inicio de enfermedad actual el 18/02/2016 aproximadamente cuando presenta debilidad generalizada, vómitos en varias oportunidades, temperatura corporal cuantificada en 39º, concomitantemente cefalea de moderada intensidad, mialgias y artralgias. El día 21/02/2016 presenta disminución de la fuerza muscular en ambos miembros inferiores, motivos por los cuales acude a este centro donde es evaluado e ingresado por el Servicio de Medicina Interna.''', 

		"diagnosticoIngresoHUAPA": [
				
			"Síndrome Viral Agudo (ZIKA)",
			"Síndrome de  Guillain Barre.",
			{"resumen": ''' El paciente permanece en el Área de Emergencia durante 5 días, con evolución clínica tórpida caracterizada por disminución simétrica y progresiva de fuerza muscular en extremidades inferiores, El día 22/02/2016 se realiza punción lumbar donde se reporta: Celularidad: 0cels/mm3, Proteínas: 10mg/dl. Solicitan valoración por el Servicio de Hematología quien decide iniciar sesiones de Plasmaféresis y para ello realizan colocación de Catéter Bilumen en Vena Femoral Izquierda. El día 24/02/2016 el paciente presenta fuerza muscular valorada en 0/5, arreflexia, apnea, sialorrea, motivos por lo que se realiza maniobra de intubación endotraqueal y se conecta a ventilación mecánica. Solicitan valoración por el servicio de terapia intensiva quien acude al llamado evaluando al paciente y  por disponibilidad de cupo se decide su ingreso a UCI. Actualmente cursa con 52 días ingresado en la Unidad de Cuidados Intensivos, hemodinamicamente estable, ventilando espontáneamente con oxígeno húmedo a través de T de Ayres conectado a traqueostomo, tolerando vía oral, recibiendo tratamiento médico y sesiones de Fisiatría, por lo que se agradece su colaboración para continuar resto de manejo.'''}

		], 
		
		
	}, # 12

	{
		"IdHistoria": "54-42-51", 
		"nombre": "Eudimar José Guapa Torrivilla", 		
		"edad": "18",
		"sexo": "F",	
		"fechaNacimiento": datetime(1998,6,28), 		
		"lugarNacimiento": "Santa María de Cariaco", 		
		"ci": "27.871.715", 		
		"dirección": "Santa María de Cariaco, Edo. Sucre", 		
		"fechaIngresoHUAPA": datetime(2016,3,31),  		
		"fechaIngresoUCI": datetime(2016,4,2),  		
		"resumenIngreso": '''Se trata de paciente femenina de 18 años de edad, sin antecedentes patológicos conocidos, quien inicia enfermedad actual hace tres semanas aproximadamente cuando presenta hiporexia, mialgias localizadas en región cervical y miembros inferiores, que fueron aumentando en intensidad, inyección conjuntival sin secreción y vómitos de contenido alimentario, en una oportunidad, precedido de náuseas, motivo por el cual acude a centro de salud de su localidad donde evalúan y egresan con tratamiento ambulatorio a base de suplementos vitamínicos vía oral. Permanece asintomática durante una semana aproximadamente. El día 29/03/2016 presenta mialgias en miembros inferiores de severa intensidad que imposibilitan la marcha. El día 31/03/2016 se anexa al cuadro lesiones en piel hipercrómicas, de bordes irregulares, violáceas, no pruriginosas en miembros inferiores motivo por el cual acude a este centro hospitalario donde se evalúa e ingresa con los diagnósticos: Síndrome doloroso poliarticular, Amenorrea. La paciente es trasladada a sala de hospitalización a cargo del Servicio Medicina Interna. El día 01/04/2016 se solicita evaluación por UCI por alteración del estado general, se acude al llamado, se evalúa a la paciente y se realizan sugerencias. El día de 02/04/2016 por disponibilidad de cupo se decide su ingreso al Servicio.''', 

		"diagnosticoIngresoUCI": [
									"Leptospirosis", 
									{"resumen": ''' Actualmente la paciente en la Unidad de Cuidados Intensivos, intubada conectada a ventilación mecánica, con evolución clínica tórpida, con diagnósticos actuales de VASCULITIS, INFECCION RESPIRATORIA BAJA NEUMONIA ASOCIADA A VENTILILACION MECANICA, INFECCION DEL TRATO URINARIO DE ETIOLOGIA MICOTICA Y BACTERIANA, SHOCK SEPTICO,  se recibe Urocultivo que reporta PSEUDOMONA AERUGINOSA  sensible a COLISTIN, Klebsiella pneumoniae sensible IMIPENEM, además reporta presencia de CÁNDIDA resistente a FLUCONAZOL, sensible a ECALTA Y CANCIDAS, por lo que en revista médica se decide solicita. Al servicio de farmacia dichos fármacos. '''},
							
								], 
	}, # 13

	{
		"IdHistoria": "54-48-53", 
		"nombre": "Gayne Miguelina Figueroa Cortez", 		
		"edad": "34",
		"sexo": "F",	
		"fechaNacimiento": datetime(1982,3,29),	
		"lugarNacimiento": "caracas", 		
		"ci": "17.242.305", 		
		"dirección": "Carizal-Arenas", 		
		"fechaIngresoHUAPA": datetime(2016,4,20), 		
		"fechaIngresoUCI":datetime(2016,4,24), 		
		"resumenIngreso": '''''',
		"examenFisicoIngresoUCI": {

			"resumen": '''Se trata de paciente femenina de 34 años de edad natural del distrito capital y procedente del municipio montes, familiar refiere inicio de enfermedad actual el día 20/04/16, cuando posterior a ingesta de INSECTICIDA DE CARBAMATO, presenta dificultad respiratoria con cianosis peribucal y distal, acompañada con pérdida del estado de conciencia y movimientos tónico clónicos generalizado, el cual es llevada a centro ambulatorio de su localidad y en vista de persistencia de cuadro clínico y dos episodios de parada cardiorrespiratorio, es trasladad a este centro hospitalario, recibida por el servicio de emergenciologia quien evalúa e ingresa con los siguientes diagnósticos:1.	INTENTO DE AUTOLISIS POR INGESTA DE CARBAMATO (MECABINIL S.A) 2. ESTADO POST RCP El paciente permanece en el servicio de UCI durante 11 días recibiendo tratamiento endovenoso con ciprofloxacina y clindamicina desde su ingreso y en vista de resultado de Urocultivo que reportó klebsiella pneumoniae se rota antibioticoterapia a meropenem (5 días) y clindamicina (10 días); recibe oxigeno espontáneamente conectada a VM a través de TET hasta el día 03/05/16 donde se realiza traqueostomía en vista de intubación prologada (13 días). Se realiza TAC Cerebral el día 27/04/16 que reporta edema cerebral por lo que se anexa diagnóstico de encefalopatía post hipóxica, se indica tratamiento anti edema cerebral el cual no se inicia por trastorno hidroelectrolítico tipo hipernatremia, el cual se corrige en un periodo de 72 horas a base de solución dextrosa. El día 02/05/16 se inicia tratamiento anti edema cerebral a base de Manitol en vista de corrección del THE. Actualmente permanece en condiciones clínicas de cuidados.''',
		}, 

		"diagnosticoIngresoUCI": [

									"ENCEFALOPATIA POST HIPOXICA.",
									"ESTADO POST RCP.",
									"INTENTO DE AUTOLISIS POR INGESTA DE CARBAMATO (MECABINIL S.A)",
									"IRB: NEUMONIA POR BRONCOASPIRACION.",
									"INFECCION DEL TRACTO URINARIO DE ORIGEN BACTERIANO.",
									"TRASTORNO HEMATOLÓGICO: ANEMIA MODERADA.",
									"POM DE TRAQUEOSTOMIA",
								],  
		
	}, # 14

	{
		"IdHistoria": "54-46-15", 
		"nombre": "Giovanny José Blanco Flores", 		
		"edad": "21",
		"sexo": "M",	
		"fechaNacimiento": datetime(1994,3,8),		
		"lugarNacimiento": "Sucre.", 			
		"dirección": "Caigüiré de Cumanacoa", 		
		"fechaIngresoHUAPA": datetime(2016,4,13), 		
		"fechaIngresoUCI":datetime(2016,4,15), 		

		"resumenIngreso": '''Paciente masculino de 21 años de edad, natural y procedente de Sucre, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual el día 13/04/2016 en horas de la madrugada cuando posterior a accidente de tránsito tipo colisión moto auto, es encontrado con pérdida del estado de consciencia, sin recuperación espontánea de la misma, motivos por los cuales es trasladado a este centro hospitalario, donde  se ingresa por el servicio de Neurocirugía con los diagnósticos de: 1)	Politraumatismo: Traumatismo Craneoencefálico Severo Traumatismo Toracoabdominal cerrado. El paciente permanece a cargo del Servicio de Neurocirugía quien solicita valoración por UCI y  por no contar con cupo se mantiene en observación a cargo del servicio de emergencia. El 13/04/16 por deterioro neurológico se realiza intubación endotraqueal y se conecta a ventilación mecánica. Se solicita TAC de Cráneo la cual se realiza el día 14/04/16 donde se evidencia presencia de hemoventrículo más contusión hemorrágica parietal derecha, amerita colocación de derivación ventricular externa (catéter tipo Becker, solicitado por el servicio de neurocirugía). Para  el 15/04/16 se solicita nuevamente valoración por UCI y por contar con cupo se decide su ingreso al servicio.''', 

		"diagnosticoIngresoUCI": [
									"Traumatismo craneoencefálico severo complicado con  contusión hemorrágica parietal derecha y hemoventrículo",
									"Politraumatizado",
									"Traumatismo  toracoabdominal cerrado",
									"Infección respiratoria baja neumonía por broncoaspiracion",
									{"resumen": '''Actualmente permanece ingresado en la Unidad de Cuidados Intensivos de este centro hospitalario, en malas condiciones generales, hemodinamicamente estable, conectado a ventilación mecánica, se realiza TAC de cráneo que reporta contusión hemorrágica parietal derecha con hemoventrículo por lo que se requiere la colocación de derivación ventricular externa con catéter tipo Becker. Informe que se expide a petición de la parte interesada.'''},
								],  
		
	}, # 15

	{ 
		"nombre": "Martha Josefina Yendez Henríquez", 		
		"edad": "53",
		"sexo": "M",	
		"fechaNacimiento": datetime(1962,7,9), 		
		"lugarNacimiento": "CUMANA", 		
		"ci": "6.161.817", 		
		"dirección": "U.B. Brasil Sector 03 casa 4", 		
		"fechaIngresoHUAPA": datetime(2016,2,12), 		
		"fechaIngresoUCI":datetime(2016,2,12), 	

		"resumenIngreso": '''Se trata de paciente femenina de 53 años de edad natural y procedente de la localidad, sin antecedente de patológicos, cuyo familiar refiere inicio de enfermedad actual a partir de diciembre del 2015, cuando presenta deterioro neurológico caracterizado por disartria, hemiparesia de hemicuerpo derecho, para el día 12/01/2016 acude a consulta médica con especialista quien evalúa e indica estudio tomografico que evidencia LOE peri-trigonal izquierda sugestiva de malignidad, motivo por el cual es planificada para el día de hoy (12/02/16)para realización de biopsia.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' TA: mmHg FC lpm FR: rpm SPO2: % ''',
			
			"piel" : 	'''Blanca Normotérmica normo hidratada turgor acorde a la edad, llenado capilar menor a 3 Seg ''',

			"abdomen": '''Globoso a expensa de panículo adiposo, RsHsPs, blando, depresible no impresiona doloroso a la palpación.''',

			"neurologico": '''consiente, vigil, orientada, pupilas isocóricas normorreactivas a la luz, Glasgow 15/15 pts.''',
			
			"torax": '''Simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares sin agregados, ruidos cardiacos rítmicos y regulares sin soplo ni galope.''',
			
			"extremidades": '''simétrica, eutrófica sin edema.''',

		}, 

		"diagnosticoIngresoUCI": [ "LOE cerebral", "POI BIOPSIA ESTEREOTAXICA DEBIDO A LOE QUISTICO PARIETAL IZQUIERDO (PERI-TRIGONAL)",],  

		"examenFisicoIngresoHUAPA": {
			"resumen": '''Se recibe paciente en camilla de transporte, tolerando aire ambiente, trasladándose a cama de UCI comentándose a monitoreo cardiaco continuo que reporta los siguientes parámetros FC: 82 lpm, FR: 16 rpm, TA: 113/93 mmHg, TAM: 82 mmHg, SaTO2: 97 %.  ''',
			
			"piel": '''blanca normotérmica, hidratada llenado capilar <3 seg''',
		
			"extremidades": '''eutrófica fuerza muscular, sensibilidad conservada''',
			
			"torax": '''Simétrico, normoexpansible ruidos respiratorios presentes en ambos hemitorax sin agregados, ruidos cardiacos rítmicos.''',
			
			"neurologico": '''Consiente, orientada en tres plano Glasgow: 15 pts. Sin signos meníngeos.''',

		},  
		
	}, # 16
	
	{
		"nombre": "Luis Miguel Mata", 		
		"edad": "60",
		"sexo": "M",	
		"fechaNacimiento":datetime(1955,8,6),  		
		"lugarNacimiento": "Cumaná-Estado Sucre.", 		
		"ci": "4.684.390", 		
		"dirección": "Brasil Sector  3, Cumaná-Estado Sucre", 		
		"fechaIngresoHUAPA":datetime(2016,3,16),  		
		"fechaIngresoUCI":datetime(2016,3,16), 	
		"resumenIngreso": ''' ''',	

		"examenFisicoIngresoUCI": {

			"resumen": '''Se trata de paciente masculino de 60 años de edad, natural y procedente de la localidad, con antecedentes tabáquicos acentuados, cuyo familiar refiere inicio de enfermedad actual hace 1 mes caracterizada por dificultad respiratoria de medianos a pequeños esfuerzos y posteriormente se anexa dolor torácico derecho, por lo que acude a centro privado donde ingresan con los diagnósticos de Infección Respiratoria Baja: Neumonía derecha complicada con derrame pleural ipsilateral, ameritando de la colocación de sistema de drenaje con tubo de tórax y permanece hospitalizado durante dos semanas con aparente evolución satisfactoria, egresando al hogar. Permanece asintomático hasta hace una semana cuando presenta nuevamente cuadro de dificultad respiratoria evidenciándose derrame pleural derecho y escaso liquido izquierdo, que amerito drenaje torácico (derecho), se solicita TAC de Tórax observándose derrame pleural tabicado ameritando de fibrinólisis y toraconcentesis terapéutica derecha, para el día  de hoy 16/03/2016 el paciente acude a consulta privada con Dr. Sotillet quien en vista de que el paciente cursa con distrés respiratorio decide referir a este centro para realizar Toracotomía derecha +  Decorticación Pulmonar y drenaje pleural izquierdo.''',
		}, 

		"diagnosticoIngresoUCI": [
										"Postoperatorio Inmediato de Toracostomía posterolateral derecha +  Decorticación pulmonar ipsilateral y drenaje pleural izquierdo.",
										"Inestabilidad Hemodinámica: Shock Hipovolémico.",
										"Tu Pulmonar izquierdo A/D.",
										"Trastorno Hematológico: Anemia por clínica.",
										{"resumen":''' Actualmente el paciente permanece ingresado en la unidad de cuidados intensivos, traqueostomisado, con evolución clínica tórpida, imposibilitando destete de la ventilación mecánica, recibiendo múltiples cultivos de secreción bronquial con gérmenes multi resistente, se solicita en revista médica iniciar tratamiento antibiótgico a base tazopril 4.5 gramos VEV cada 6 horas. '''}
							
								],  

		
		"diagnosticoIngresoHUAPA": [
				
			"Derrame pleural bilateral.",

			"Tu Pulmonar izquierdo A/D.",

			{"resumen": ''' Paciente que es evaluado por Dr. Sotillet Cirujano de Tórax, encontrando paciente en condiciones de cuidado con trabajo respiratorio y taquicardico, decide llevar a mesa operatoria bajo anestesia general donde realizan toracotomía posterolateral derecha de emergencia encontrándose los siguientes hallazgos corteza pleural engrosada de1,5 a 2,5 cm aproximadamente, derrame pleural derecho e izquierdo, tomándose como conducta Decorticación pulmonar derecha y colocación de tubo de tórax en 6to EIC con línea Axilar anterior derecha y 6to EIC con Línea axilar media  izquierda, obteniéndose un estimado de sangrado de 1500 a 2000 cc aproximadamente. Posterior a acto quirúrgico se solicita valoración por el servicio de terapia intensiva en vista de que el paciente durante acto operatorio se mantiene taquicárdico, con oliguria, cifras tensionales en descenso, ameritando de trasfusión de 2 unidades de concentrado globular, en vista de las condiciones clínicas del paciente y de disponibilidad de cupo se decide su ingreso en la unidad de cuidados intensivos.'''}


		], 
		
	}, # 17

	{
		"IdHistoria": "54-52-78", 
		"nombre": "José Luis Martínez", 		
		"edad": "58",
		"sexo": "M",	
		"fechaNacimiento": datetime(1958,6,18),  		
		"lugarNacimiento": "Cumaná, Sucre ", 		
		"ci": "5.693.268", 		
		"dirección": "La trinidad vereda # 5 casa Nro 25. Cumaná, Estado Sucre", 		
		"fechaIngresoHUAPA":datetime(2016,5,9),   		
		"fechaIngresoUCI":datetime(2016,5,9),  		

		"resumenIngreso": '''Se trata de paciente masculino de 58 años de edad, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual el 03/05/16 cuando posterior a esfuerzo físico presenta dolor en región lumbar derecha de severa intensidad, motivo por el cual acude a centro asistencial donde previa evaluación clínica y paraclínica se indica tratamiento. Por persistencia de sintomatología acude nuevamente a facultativo quien realiza Eco abdominopelvico sin hallazgos significativos. Para el día 05/05/16 se anexa al cuadro clínico aumento de la temperatura corporal cuantificada en 39 ºC; acompañada de escalofríos, atenuada  con tratamiento endovenoso Paracetamol. Persiste sintomático, concomitante vómitos en número de 5 precedidos de nauseas de contenido alimentario.  Para el día 09/05/16 en horas de la mañana es encontrado por familiar presentando movimientos tónico clónicos de aproximadamente 3 minutos de duración con relajación de esfínter vesical, motivo por el cual es trasladado a este centro donde es evaluado por el servicio de Medicina Interna se  constatan episodios convulsivos y se ingresa. Paciente que permanece en el área de Observación adultos, donde se realiza punción lumbar que reporta los siguientes hallazgos:Aspecto: ligeramente turbio, color: amarillo claro; contaje celular de 150 cel/mm3; Pandy: positivo; proteínas 200mg/dl; hematíes: 1 a 3 XC  y leucocitos: 2 a 3 XC con 70'%' de Segmentados, 21'%' de Linfocitos y 01'%' de Eosinófilos. Por lo que se ingresa con los siguientes diagnósticos: 1. Infección de Sistema Nervioso Central: Meningoencefalitis Bacteriana. 2.Trastorno Hematológico: BicitopeniaEl paciente presenta deterioro neurológico dado por Glasgow de 7/15 puntos (no discriminado) y cuadro de dificultad respiratoria; por lo que el servicio de Emergenciología decide intubar y solicitan Interconsulta a la Unidad de Cuidados Intensivos, quien por disponibilidad de cupo decide ingresar.''', 

		"diagnosticoIngresoUCI": [

									"Infección de Sistema Nervioso Central: Meningoencefalitis Bacteriana",
									"Trastorno Hematológico: Anemia Severa (7,6 mg/dl)",
									"Shock séptico",
									"Sepsis punto de partida sistema nervioso central",
									"Meningoencefalitis bacteriana.",
									{"resumen": '''Actualmente permanece en la unidad de cuidados intensivos. En malas condiciones generales, inestable hemodinamicamente, intubado y conectado a ventilación mecánica, con diagnósticos actuales de:'''},

							
								], 
		
	}, # 18

	{
		"IdHistoria": "54-33-96", 
		"nombre": "Ismael José Gómez Martínez", 		
		"edad": "31",
		"sexo": "M",	
		"fechaNacimiento": datetime(1984,6,5), 		
		"lugarNacimiento": "Cumana", 				
		"dirección": "El peñón", 		
		"fechaIngresoHUAPA": datetime(2016,3,3), 	
		"fechaIngresoUCI":datetime(2016,3,7),		 
		"resumenIngreso": '''Se trata de paciente masculino de 31 años de edad natural y procedente de la localidad, cuyo familiar refiere inicio de enfermedad actual el día 03/03/2016 cuando posterior a recibir herida por proyectil de arma de fuego en región cigomática derecha, es trasladado a nuestro centro asistencial donde es evaluado por el servicio de cirugía quien decide su ingreso. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado conectada  a monitor cardiaco, conectado a ventilador de transporte se traslada a cama de UCI SIGNOS VITALES: FC 66 LPM  TA 112/64 (84) MMHG  FR 26  SAT O2 98%. Se conecta a VM EVITA 4 parámetros VC 480 FIO2 60 FL 50 FR 14 PEEP 10  ''',
			
			"piel" : 	'''Normotérmica, palidez cutáneo mucosa moderada, llenado capilar <3segundos. Se evidencia apósitos que cubre heridas quirúrgicas y orifico de entrada de proyectil de arma de fuego. Edema facial, edema bipalpebral que limita la apertura ocular con equimosis palpebral izquierda. ''',

			"cardiopulmonar":  '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos hemitorax con agregados pulmonares crepitantes bibasales.  Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos. ''',
			"abdomen": '''Blando, globoso a expensas de panículo adiposo  no  doloroso a la palpación superficial y  profunda, no visceromegalias.''',

			"neurologico": '''Glasgow no evaluable por efectos de sedantes, pupilas no evaluables por limitación para la apertura por edema palpebral''',

		}, 

		"diagnosticoIngresoUCI": [
									"Post operatorio mediato para control de daño debido a traumatismo facial por herida por proyectil de arma de fuego.",
									"traumatismo facial por herida por proyectil de arma de fuego complicado con fractura malar derecha, malar izquierda y maxilar superior.",
									"Crisis hipertensiva tipo emergencia complicada con edema agudo de pulmón",
									"Trastorno hematológico: anemia moderada",
								],  

		"examenFisicoIngresoHUAPA": {
			"piel": ''' piel morena, llenado capilar < 3seg. ''',

			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax, sin agregados pulmonares.  Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos ni galope. ''',
			
			"abdomen": '''Blando, globoso ruidos hidroaéreos presentes, no  doloroso a la palpación superficial y  profunda, no visceromegalias.''',
			
			"neurologico": '''vigil, orientado en los 3 planos, FM V/V ROT II/IV''',

		},  
		"diagnosticoIngresoHUAPA": [
			"Traumatismo facial por proyectil de arma de fuego complicado con fractura de rama derecha de maxilar superior y malar derecho",
			"VARICES ESOFAGICAS SANGRANTES", 
			"ILCERA GASTRODUODENAL",
			{"resumen":''' Posterior  a su egreso en se solicita valoración por terapia intensiva, quien acude al llamado realizando sugerencias en vista de no contar con cupo en la unidad de cuidados intensivos, complicándose cuadro con edema facial generalizado la cual dificulta la ventilación, por lo que se decide llevar a quirófano para permeabilización de la vía área a través de tubo endotraqueal 7.5 fr sin complicaciones, es trasladado a área de recuperación de quirófano donde se conecta a ventilación mecánica con parámetros AC fr 12 Vc 560 Fl 50 fio2 60 peep 0, se comunica caso especialista DR Nassa quien decide llevar a mesa operatoria donde bajo anestesia general realiza incisión supra mandibular con hallazgos, Hematoma en región malar izquierda, edema bipalpebral, edema facial, hemorragia subconjuntival, con conducta,  drenaje de hematoma aspiración de orificios nasales, colocación de dren de latex en malarizquierdo, síntesis por planos con nailon 5.0, rafia de mucosa oral y asepsia y cura final.  Siendo trasladado nuevamente a área de recuperación de quirófano, el día 05/03/2016 presenta cifras elevadas de tensión arterial 220/100 mmhg con salida de secreción asalmonada a través de tubo endotraqueal, desaturación por monitor cardiaco, or lo que se realiza reajuste del ventilador mecánico AC fr 14 fio2 95% fl 50 VC 400 PEEP 7, se realizan nuevamente sugerencias, el paciente presenta evolución clínica tórpida, el día 07/03/2016 se realiza estudio tomografico de macizo facial con reconstrucción 3D, y por disponibilidad de cupo se decide su ingreso a UCI.'''},
		], 
		
	},# 19

	{
		"nombre": "Jaime José Bermudez", 		
		"edad": "33",
		"sexo": "M",	
		"fechaNacimiento": datetime(1983,12,7),  		
		"lugarNacimiento": "Cumana", 		
		"ci": "18.777.868", 		
		"dirección": "Miramar calle Nueva N 10, Cumaná", 		
		"fechaIngresoHUAPA": datetime(2016,2,29), 		
		"fechaIngresoUCI":datetime(2016,2,29), 		

		"resumenIngreso": '''Se trata de paciente masculino de 33 años de edad, sin antecedentes patológicos personales quien inicia enfermedad actual el día de hoy 29/2/16 cuando posterior a accidente de tránsito tipo colisión en moto, es encontrado en la vía pública y trasladado a este centro asistencial donde es evaluado e ingresado por servicio de neurocirugía.''', 


		"examenFisicoIngresoUCI": {

			"piel" : 	'''Normotérmica al tacto, llenado capilar <3 Seg, escoriaciones en cara, hombro derecho''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax, se auscultan agregados tipo roncos en ambos campos pulmonares. Ruidos cardiacos rítmicos, regulares, sin soplos ni galope. ''',
			
			"abdomen": '''Ruidos hidroaéreos presentes, depresible, no doloroso a la palpación, no megálico.''',

			"neurologico": ''' No evaluable por efectos de sedación farmacológica''',
			"extremidades": '''Eutróficas, sin edema.''',

		}, 

		"diagnosticoIngresoUCI": [
							"Politraumatismos.",
							"Traumatismo Craneoencefálico Severo",
							"Traumatismo tóraco abdominal cerrado.",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' SIGNOS VITALES: TA:   mmHg    FC:  LPM FR:  RPM ''',
			"piel": '''Normotérmica al tacto, llenado capilar <3 Seg, escoriaciones en cara, hombro derecho''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax, sin agregados. Ruidos cardiacos rítmicos, regulares, sin soplos ni galope. ''',
			"abdomen": '''ruidos hidroaéreos presentes, depresible, no doloroso a la palpación, no megálico.''',
			"extremidades": ''' eutróficas, sin edema.''',
			"neurologico": '''Paciente bajo efectos del alcohol ''',

		},  
		"diagnosticoIngresoHUAPA": [
				"Intoxicación Etílica",
				"Traumatismo Cranoencefalico Leve a Moderado",
				"Traumatismo Facial.",
				{"resumen": ''' El paciente permanece en emergencia, se solicita evaluación por UCI y por disponibilidad de cupo se decide su ingreso. Recibo paciente en camilla de traslado, intubado, recibiendo oxigeno húmedo por ambu se traslada a cama UCI y se conecta a monitor cardiaco que reporta TA: 128/68 (97) mmHg Fc: 109 lpm Fr:19 rpm SATO2: 96% y  a ventilación mecánica modo A/C Vc:560 Fr:12 FiO2:60 Fl:50 TI: 1:4 PEEP:0 '''}
		], 
		
	},# 20

	{
		
		"nombre": "Jesús Rafael Guerrero León", 		
		"edad": "13",
		"sexo": "M",	
		"fechaNacimiento": datetime(2002,6,11), 	
		"lugarNacimiento": "Carúpano", 		
		"ci": "28.383.264", 		
		"dirección": "Irapa, Estado Sucre", 		
		"fechaIngresoHUAPA": datetime(2016,5,4), 		
		"fechaIngresoUCI":datetime(2016,5,4), 		
		"resumenIngreso": ''' Paciente masculino de 13 años de edad, natural y procedente de Irapa, con antecedente de Diábetes Mellitus tipo 1, en tratamiento regular con Levemir® 10 UDS 8:00am y Novorapid® según glicemia capilar, cuya madre refiere inicio de enfermedad actual el día 27/04/16 caracterizado por evacuaciones liquidas en Nª de 10, concomitante epigastralgia y vómitos en incontables oportunidades, permanece sintomático hasta el día 02/05/16 cuando, por exacerbación de los síntomas acude a CDI de su localidad donde recibe tratamiento a base de  antieméticos, fluidoterapia y egresa con mejoría parcial, el día 03/05/16 por reaparición de los síntomas y asociarse disnea acuden a hospital de Carúpano donde permanece 24 horas y refieren a este centro por no contar con cupo en UCI. Es recibido en este centro asistencial por el servicio de medicina interna quien evalúa e ingresa con los diagnósticos de:1) Diabetes mellitus tipo 1 descompensada en cetoacidosis diabética2) Sepsis punto de partida enteral3) Alergia al ketorolac ''', 


		"examenFisicoIngresoUCI": {

			"piel" : 	'''	blanca, hipertérmica al tacto, turgor y elasticidad disminuido, llenado capilar < 3 segundos,  mucosa oral seca''',

			"cardiopulmonar":  ''' Tórax simétrico, patrón respiratorio tipo Kussmaul, ruidos respiratorios presentes en ambos campos pulmonares, no se auscultan agregados. Ruidos cardíacos rítmicos, regulares, taquicardicos, no se auscultan soplos ni galope.''',
			
			"abdomen": ''' blando, depresible, no impresiona doloroso a la palpación profunda, ruidos hidroaéreos presentes, sin megalias. ''',

			"neurologico": '''estuporoso, pupilas isocóricas, reactivas a la luz, Glasgow  11/15ptos (RM: 6ptos, RO: 3 ptos, RV: 2 ptos).''',

			"extremidades": '''simétricas, eutróficas, sin edemas.''',

		}, 

		"diagnosticoIngresoUCI": [
									"DIABETES MELLITUS TIPO 1 DESCOMPENSADA EN CETOACIDOSIS DIABÉTICA",
									"IRB: NEUMONÍA ADQUIRIDA EN LA COMUNIDAD",
									"TRASTORNO HIDROELECTROLÍTICO: HIPOKALEMIA.",

								],  

		"examenFisicoIngresoHUAPA": {

			"resumen": ''' Paciente en aparentes regulares condiciones generales, afebril, disneico, deshidratado.En vista de condiciones clínicas del paciente solicitan valoración por  UCI, se evalúa paciente en área de emergencia, en vista de condiciones clínicas y  disponibilidad de cupo, previa autorización de Dra. Roa, se decide su ingreso a la UCI.Se recibe paciente en camilla de traslado, hemodinamicamente estable, ventilando espontáneamente, se traslada a cama de UCI, se conecta a monitor cardíaco externo que reporta:TA: 119/93mmHg	FC: 135 lpm	FR: 28rpm SatO2: 96 %''',

			"piel": ''' blanca, normotérmica, normoelástica,  llenado capilar < 3 segundos. ''',

			"cardiopulmonar": ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes  sin agregados, ruidos cardiacos rítmicos y regulares, sin soplos ni galope. ''',

			"abdomen": ''' plano, blando, depresible, no doloroso, ruidos hidroaéreos presentes. ''',
			
			"neurologico": '''Consciente, orientado en tiempo, espacio y persona. ''',
		},  
		
	}, # 21

	{
		"IdHistoria": "54-48-53", 
		"nombre": "Gayne Miguelina Figueroa Cortez", 		
		"edad": "34",
		"sexo": "F",	
		"fechaNacimiento": datetime(1982,3,29),  		
		"lugarNacimiento": "caracas", 		
		"ci": "17.242.305", 		
		"dirección": "Carrizal-Arenas", 		
		"fechaIngresoHUAPA": datetime(2016,4,20), 		
		"fechaIngresoUCI":datetime(2016,4,24), 		

		"resumenIngreso": ''' Se trata de paciente femenina de 34 años de edad natural del Distrito Capital y procedente del municipio Montes, familiar refiere inicio de enfermedad actual el día 20/04/16, cuando posterior a ingesta de INSECTICIDA DE CARBAMATO, presenta dificultad respiratoria con cianosis peribucal y distal, acompañada de  pérdida del estado de conciencia y movimientos tónico clónicos generalizado, el cual es llevada a centro ambulatorio de su localidad y en vista de persistencia de cuadro clínico y dos episodios de parada cardiorrespiratorio, es trasladada a este centro hospitalario, recibida por el servicio de emergenciologia quien evalúa e ingresa con los siguientes diagnósticos: 1. INTENTO DE AUTOLISIS POR INGESTA DE CARBAMATO (MECABINIL S.A) 2. ESTADO POST RCP ''', 

		"diagnosticoIngresoUCI": ["INTENTO DE AUTOLISIS POR INGESTA DE CARBAMATO (MECABINIL S.A)", "ESTADO POST RCP"],  

		"examenFisicoIngresoHUAPA": {

			"resumen": ''' FC: 122 lpm FR: 18 rpm SATO2: 98% TA: 100/60 mmHg. Paciente que permanece en área de emergencia conectada a ventilación mecánica modo AC con parámetros VC 560 FR 12 FL 50 PEEP 0 FIO2 60 siendo evaluada por servicio de toxicología quien indica tratamiento con Atropina, y es evaluada por terapia intensiva diariamente, para el día de hoy debido a disponibilidad de cupo se decide ingreso a UCI.''',

			"piel": ''' Morena, normotérmica, normoelástica, llenado capilar < 3 segundos.''',
			
			"cardiopulmonar": '''toras simétrico normoexpansible, ruidos respiratorios presentes en ambos hemitorax, no se auscultan agregados, ruidos cardiacos rítmicos y regulares no soplo no galope''',
			"abdomen": '''blando, depresible, no doloroso, ruidos hidroaéreos presentes, sin signos de irritación peritoneal.''',
			"neurologico": '''inconsciente, pupilas mióticas, no reactivas a la luz, Glasgow 3/15 ptos (RO: 1 pt0, RV: 1 pto, RM: I pto) ''',
		},  
		
	}, # 22


	{
		
		"nombre": "Roxanne Foucault", 		
		"edad": "62",
		"sexo": "F",	
		"fechaNacimiento": datetime(1953,10,8), 		
		"lugarNacimiento": "Cumaná-Estado Sucre.", 		
		"ci": "4.687.151", 		
		"dirección": "Urb. La Trinidad, vereda 1, casa No. 1, Cumaná-Estado Sucre.", 		
		"fechaIngresoHUAPA": datetime(2016,5,16), 		
		"fechaIngresoUCI":datetime(2016,5,20), 	

		"resumenIngreso": ''' Se trata de paciente femenina de 62 años de edad, natural y procedente de la localidad, con antecedentes de Hipertensión Arterial Sistémica tratada con amlodipina 5 mg/día y Miocardiopatía dilatada, quien inicia enfermedad actual el día 09-05-2016 caracterizada por tos productiva con expectoración amarillenta, y disnea a moderados esfuerzos, concomitantemente fiebre cuantificada en 38,5 ºC, motivo por el cual es llevada a consulta privada con neumonólogo quien diagnóstica infección respiratoria baja e indica tratamiento ambulatorio con cefixima. El día 14-05-2016 se anexa al cuadro ortopnea, cianosis distal y diaforesis profusa por lo que acude a centro privado donde es evaluada e ingresada a UCI con diagnóstico de:1. Insuficiencia Respiratoria Aguda2. Insuficiencia Cardíaca Congestiva descompensada en Edema Agudo de Pulmón3. Sepsis punto de partida Respiratorio4. IRB: Neumonía Bilateral5. Hipotensión arterial6. Miocardiopatía Dilatada7. Alergia a NovalcinaPermanece durante 48 horas en UCI de centro privado donde es evaluada por cirujano de tórax (Dr. Sotillet) quien realiza toracocéntesis diagnóstica sin obtención de líquido pleural, posteriormente es evaluada por cardióloga (Dra. Elianca Vivas) quien realiza ecocardiograma evidenciando leve hipocinesia septal y anterolateral, FE: 55%, pericardio engrosado planteando diagnóstico de miopericarditis. El día 16-05-2016 por motivos socioeconómicos y petición de familiares deciden referir a este centro hospitalario, donde se evalúa e ingresa.''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, que luce en regulares condiciones generales, intubada y conectada a ventilador mecánico de traslado con parámetros en modo A/C, Vc: 480, Fl: 50; Fr: 14; TI: 1:4; FiO2: 60; PEEP: 10, se traslada a cama de UCI y se conecta a ventilador mecánico Evita 4 con mismos parámetros y se conecta a monitor cardiovascular continuo que reporta signos vitales: TA: 84/46mmHg TAM: 58mmHg FC: 63  lpm FR: 16 rpm SaO2: 90%. ''',
			
			"piel" : 	'''Blanca, normotérmica, normohidratada, llenado capilar menor de 3 segundos. Se evidencia ligera palidez cutáneo-mucosa.''',

			"cardiopulmonar":  '''  Tórax simétrico hipoexpansible, ruidos respiratorios presentes en ambos hemitorax, disminuidos en base pulmonar derecha, se auscultan roncus dispersos y crepitantes en base pulmonar izquierda, ruidos cardíacos rítmicos, regulares sin presencia de  soplo ni galope.''',
			
			"abdomen": ''' Ruidos hidroaéreos positivos, globoso a expensas de tejido adiposo, blando, no impresiona dolor a la palpación superficial y ni profunda, sin visceromegalias. ''',

			"neurologico": '''No evaluable por efectos de sedación y relajación farmacológica.''',

			"extremidades": '''Simétricas, eutróficas, sin edema.''',

		}, 

		"diagnosticoIngresoUCI": [
									"Síndrome de Distrés Respiratorio del Adulto",
									"Insuficiencia Respiratoria Aguda",
									"IRB: Neumonía Bilateral",
									"Hipertensión Arterial Sistémica",
									"Miocardiopatía Dilatada",
									"Alergia a Novalcina",
									"Trastorno hematológico: Anemia leve",
									"Trastorno ácido base: acidosis metabólica compensada con alcalosis respiratoria + hiperoxemia.",
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se evalúa paciente en AsRsCsGs, Afebril, hidratada. Signos vitales: TA: 100/60mmHg  FR: 34 rpm   FC: 90 lpm.Paciente que permanece en el Área de Observación Adultos durante 4 días, recibiendo antibioticoterapia con moxifloxacina, piperacilina-tazobactam y clindamicina. El día 20-05-2016 por disponibilidad de cupo se decide su ingreso a UCI.''',
			"piel": ''' Morena N/T, N/H;  llenado capilar < 3 segundos. ''',
			"cardiopulmonar": ''' Tórax simétrico, hipoexpansible, tiraje supraesternal, RsRsPs, se auscultan crepitantes bibasales. RsCsRsRs sin soplo ni galope.''',
			"abdomen": '''Globoso a expensas de panículo adiposo, RsHs (+), depresible, no doloroso a la palpación, no megalia. ''',
			"extremidades": '''Simétricas, eutróficas, sin edemas. ''',
			"neurologico": '''consciente, orientada en tiempo, espacio y persona, lenguaje claro y coherente. ''',

		},  		
	}, # 23


	{
		"IdHistoria": "46-48-40", 
		"nombre": "Pedro Pablo Rojas", 		
		"edad": "62",
		"sexo": "M",	
		"fechaNacimiento": datetime(1953,6,29), 		
		"lugarNacimiento": "Cumana", 		
		"ci": "5.690.640", 		
		"dirección": "Brasil sector 2, calle 9 No 21", 		
		"fechaIngresoHUAPA": datetime(2016,3,26),  		
		"fechaIngresoUCI":datetime(2016,4,5),		
		"resumenIngreso": ''' Paciente masculino de 62 años de edad, natural y procedente de la localidad, con antecedentes de Diabetes Mellitus tipo 2 no controlada e Hipertensión Arterial no controlada y Cardiopatía Isquémica crónica desde 2008. Quien inicia enfermedad actual el día 24/03/2016 en horas de la tarde cuando presenta pérdida de fuerza muscular en miembro inferior derecho, motivo por el cual acude a centro asistencial donde es evaluado y se constatan cifras de tensión elevadas (160/110 mmHg) y cifras de glicemia elevadas (298 mg/dl), en EKG se reporta FARVR, por lo que se decide su ingreso a UCI. El paciente permanece por 48 horas en UCI, con progresión de perdida de la fuerza muscular evolucionando a la cuadriparesia, lenguaje disartrico, arreflexia se decide referir a este centro asistencial con los diagnósticos de : 1. Síndrome de Guillain Barre.2. Crisis hipertensiva tipo emergencia.3. Trastorno del Ritmo FARVR.4. Diabetes Mellitus tipo 2 descompensada en hiperglicemia.5. Cardiopatía isquémica Crónica.6. Hipertensión Arterial.''', 


		"examenFisicoIngresoHUAPA": {
			
			"piel" : 	''' hidratado, palidez cutáneo mucosa. ''',

			"cardiopulmonar":  ''' 	tórax simétrico, expandible, ruidos respiratorios presentes sin agregados; ruidos cardiacos arrítmicos, taquicardicos. ''',
			"abdomen": ''' globoso a expensa de panículo adiposo, ruidos hidroaéreos presentes, blando, depresible, no doloroso, no megalias.''',

			"neurologico": '''consciente, orientado en tiempo, persona y espacio, pupilas isocóricas reactivas a la luz; FM II/V en los 4 miembros, arreflexia ''',
		}, 

		"diagnosticoIngresoUCI": [
									"SINDROME DE GUILLAIN BARRE",
									"INFECCION RESPIRATORIA BAJA: NEUMONIA ASICIADA A VENTILACION MECANICA",
									"DIABETES MELLITUS TIPO 2",
									"CARDIOPATIA ISQUEMICA CRONICA",
									"HIPERTENSION ARTERIAL SISTEMICA",
								],  

		"examenFisicoIngresoUCI": {
			"piel": ''' blanca, normotérmica al tacto, llenado capilar < 3 segundos.''',

			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios disminuidos en hemitorax izquierdo, se auscultan roncus bilaterales. Ruidos cardíacos rítmicos y regulares, taquicárdicos,  no se auscultan soplos ni galope. ''',
			
			"abdomen": '''globoso a expensa de panículo adiposo, ruidos hidroaéreos presentes, blando, depresible, no doloroso, no megalias.''',

			"neurologico": '''Consciente, fuerza muscular II/V en miembros inferiores, 0/V en miembros superiores, ROT ausentes, pupilas isocóricas y reactivas a la luz''',
		},  

		"diagnosticoIngresoHUAPA": [
				"Síndrome de Guillain Barre.",
				"Crisis hipertensiva tipo emergencia.",
				"Trastorno del Ritmo FARVR.",
				"Diabetes Mellitus tipo 2 descompensada en hiperglicemia.",
				"Cardiopatía isquémica Crónica.",
				"Hipertensión Arterial.",
				{"resumen": ''' El paciente es evaluado e ingresado en Emergencia, 27/03/16 presenta hipoventilación por lo que se decide intubar y conectar a ventilación mecánica con parámetros establecidos VC:640 FIO2: 60 FL:50 Fr: 12 El 28/03/16 se realiza punción lumbar que reporta: CITOQUIMICO contaje celular leuc: 0 cel; bact no se obs; levad no se obs; parásitos ausentes; glucosa 112 mg/dl; prot 42 mg/dl Pandy neg y en vista de resultados y los síntomas se comienza sesiones de Plasmaféresis, recibiendo 3 sesiones. El paciente es evaluado por UCI diariamente, hasta el día de hoy 5/04/16 cuando por disponibilidad de cupo se decide su ingreso. Se recibe paciente en camilla de traslado, intubado, recibiendo oxigeno por ambu, se traslada a cama UCI y se conecta a ventilación mecánica y a monitor cardiaco que reporta. TA: 98/81(93) mmHg, FC: 123 lpm,  FR: 23 rpm, SATO2: 76%. '''},
		], 
		
	},# 24

	{
		"IdHistoria": "38-33-04", 
		"nombre": "Pascual Antonio Acuña", 		
		"edad": "55",
		"sexo": "M",	
		"fechaNacimiento": datetime(1960,5,15),  		
		"lugarNacimiento": "Tataracual - Edo. Sucre", 		
		"ci": "10.955.446", 		
		"dirección": "Cumanacoa Sector San Agustín", 		
		"fechaIngresoHUAPA": datetime(2016,1,7), 		
		"fechaIngresoUCI":datetime(2016,1,12), 	

		"resumenIngreso": ''' Se trata de paciente Masculino de 55 años natural de Tataracual y procedente de Cumanacoa,  sin antecedentes patológicos conocidos; quien inicia enfermedad actual el día 06/01/2016 en horas de la noche  cuando posterior a  esfuerzo físico, presenta cefalea de fuerte intensidad  por lo que se automédica con atamel, sin mejoría, concomitantemente presenta vómitos en una oportunidad de contenido alimentario, además perdida del estado de conciencia, motivo por el cual es llevado a centro asistencial de la localidad, donde administran tratamiento que no precisa, en vista de persistir el cuadro clínico es traído a este centro asistencial donde es evaluado e ingresado por Servicio de Medicina Interna .''', 


		"examenFisicoIngresoUCI": {

			"piel" : 	'''piel morena  hidratada,  llenado capilar <3segundos.''',

			"cardiopulmonar":  '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax, se auscultan crepitantes en base izquierda. Ruidos cardíacos rítmicos, regulares,  taquicárdicos, no se auscultan soplos ni galope. ''',
			
			"abdomen": '''RsHsPs, plano, depresible no doloroso a la palpación, no megalias. ''',

			"neurologico": '''Inconsciente, pupilas isocórica mióticas hiporreactiva a la luz.  Glasgow 3/15 ptos (RO 1  RV 1 RM 1). ''',

		}, 

		"diagnosticoIngresoUCI": [
									"Crisis hipertensiva tipo emergencia, expresada en ECV de etiología a precisar.",
									"Infección respiratoria baja: Neumonía por broncoaspiracion.",
									"Trastorno hidroelectrolítico: Hipokalemia, Hipernatremia.",
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 220/130 mmHg FC: 78 lpm FR: 18 rpm. ''',
			
			"piel": ''' morena, normotérmica, normoelástica, llenado capilar < 3 seg ''',
			
			"cardiopulmonar": '''Tórax simétrico hipoexpansible, ruidos respiratorios presentes en ambos hemitorax, se auscultan crepitantes bilaterales. RsCSRsRS sin soplo.''',
			
			"abdomen": '''plano, depresible  blando, no doloroso a la palpación, ruidos hidroaéreos presentes, no megalias ''',
			
			"extremidades": '''simétricas, no edemas, eutróficas ''',

			"neurologico": '''inconsciente, pupilas puntiforme  Glasgow 3/15 ptos (RO .1 RV. 1 RM. 1)''',

		},  

		"diagnosticoIngresoHUAPA": [
				"CRISISI HIPERTENSIVA TIPO EMERGENCIA EXPRESADA EN EVC DE PROBABLE ETIOLOGIA  HEMORRAGICA", 
				"ESTADO POST RCP",
				"INFECCION RESPIRATORIA BAJA: NEUMONIA POR BRONCOASPIRACION.",
				{"resumen":''' Se solicita valoración por UCI quien acude al llamado, evaluando paciente en sala de choque intubado, recibiendo oxigeno por ambu; inconsciente, con Glasgow de 3/15 ptos; se conecta a ventilación mecánica y por no disponer de cupo en UCI se hacen sugerencias. El paciente permanece en sala de choque durante 8 días y el día de hoy 12/1/16 por disponer de cupo se decide su ingreso a UCI. Se recibe  paciente en camilla de traslado intubado, recibiendo oxigeno por ambu, se traslada  a cama UCI y se conecta a ventilador mecánico modo A/C VC: 560 Fr: 12 FiO2: 60 Fl: 50 TI: 1:4 PEEP: 0 y a monitor cardiaco continuo que reporta: TA: 91/55 (62) mmHg FC: 92 lpm FR: 12 rpm SPO2: 98%'''},

		], 
		
	}, # 25

	{
		"nombre": "Germán Rafael Lanza.", 		
		"edad": "80",
		"sexo": "M",	
		"fechaNacimiento": datetime(1936,3,1),  		
		"lugarNacimiento": "Estado Sucre", 		
		"ci": "521.508", 		
		"dirección": "Urbanización Fe y Alegría, Bloque 26. Cumaná, Estado Sucre.", 		
		"fechaIngresoHUAPA": datetime(2016,5,7), 		
		"fechaIngresoUCI": datetime(2016,5,7), 		
		"resumenIngreso": '''Se trata de paciente masculino  de 80 años de edad, natural y procedente de la localidad, con antecedentes de hipertensión arterial en tratamiento con Amlodipina 5mg, Ramipril 2,5mg, Cardiopatía Hipertensiva en tratamiento con Digoxina 0,25mg, Diabetes Mellitus tipo 2 sin tratamiento, quien inicia enfermedad actual el día 06/05/2016 en horas de la mañana cuando presenta disminución de la fuerza muscular en hemicuerpo derecho, concomitantemente lenguaje disartrico, motivo por el cual es trasladado a centro clínico privado donde es hospitalizado, administran  oxígeno, se conecta a  monitoreo cardiaco continuo constatando  cifras de tensión arterial elevadas iniciando tratamiento no precisado. Posteriormente el 07/05/2016 se anexa al cuadro clínico disnea progresiva de moderados a leves esfuerzos y cianosis distal, por lo que es evaluado por especialista de guardia quien decide referir a nuestra institución, donde ingresa en unidad de cuidados intensivos. ''', 

		"diagnosticoIngresoHUAPA": [
						"Insuficiencia Respiratoria Aguda.",
						"Crisis Hipertensiva tipo Emergencia expresada en EVC de etiología a precisar.",
						"Insuficiencia Cardiaca descompensada en Edema Agudo de Pulmón.",
						"Hipertensión arterial sistémica.",
						"Diabetes Mellitus tipo 2.",
						"Cardiopatía Dilatada.",
						{"resumen": ''' Permaneció en la unidad de cuidados intensivos en malas condiciones generales, traqueostomisado y conectado a ventilación mecánica con evolución clínica tórpida, posteriormente se anexa al cuadro cambios electrocardiográficos subjetivos de síndrome coronario en cara anterior, que imposibilita el destete de la ventilación mecánica, el día 19/05/2016 realiza evento de bradicardia severa que evoluciona a la asistolia, se realiza maniobras de RCP básico y avanzado siendo infructuosa dichas maniobras, requiriendo en múltiples oportunidades colocación de atropina y epinefrina sin respuesta satisfactoria, por lo que se realiza electrocardiograma declarando fallecimiento a las 3:45 pm  durante su estancia en UCI requirió cuidados diarios por parte de familiar.'''},

		], 

		"diagnosticoEgresoPRIVADO": [
			"Insuficiencia Cardíaca descompensada en edema agudo de pulmón.",
			"Evc de etiología a precisar.",
			"Hipertensión arterial sistémica",
			"Diabetes Mellitus tipo 2.",
			"Cardiopatía Dilatada..",
			{"resumen": ''' Se recibe paciente en camilla de traslado, recibiendo oxigeno húmedo por mascarilla facial, se traslada a cama de UCI, se conecta a monitor cardíaco externo que reporta: TA: 88/45(55) mmHg	FC: 105pm	FR: 33rpm	SPO2: 45%A su ingreso se realiza intubación Endotraqueal, se conecta a VM evita 4, modo A/C con parámetros: Fio2: 100, Vc 420, Fl 50, Fr: 14, PEEP: 9, se procede a cateterización de vía venosa central derecha, sin complicaciones; se indica exámenes complementarios y RX de tórax. '''},

		],
		
	},# 26

	{
		"IdHistoria": "24-42-12", 
		"nombre": "Oscar José chirino Velásquez", 		
		"edad": "37",
		"sexo": "M",	
		"fechaNacimiento": datetime(1978,6,15), 		
		"lugarNacimiento": "Cumaná- Estado Sucre", 		
		"ci": "19.392.382", 		
		"dirección": "parcelamiento miranda calle manicuare", 		
		"fechaIngresoHUAPA": datetime(2016,1,16),  		
		"fechaIngresoUCI":datetime(2016,1,19),  		
		"resumenIngreso": ''' Se trata de paciente masculino de 37 años de edad natura y procedente l de la localidad, con antecedentes de epilepsia desde la infancia, en tratamiento actual con Rivotril 2 mg BID, Diazepam 10 mg BID,  kepra  500 mg TID, Tegretol 400 mg TID, quien inicia enfermedad actual hace 20 días aproximadamente cuando presenta tos seca permaneciendo sintomático hasta el día 15/01/2016 se hace productiva, con expectoración mucopurulenta, aumento de la temperatura corporal cuantificada en 39 ºC, por lo que acude a médico especialista, Neumónologo quien indica tratamiento médico ambulatorio, sin mejoría clínica, anexándose horas de la noche movimiento tónico clónico generalizado, que yugula de manera espontánea, por lo que es traído a nuestro centro asistencial siendo evaluada por el servicio de medicina interna quien vista de no evidenciar episodio convulsivo decide egreso con tratamiento médico ambulatorio. El día sábado 16/01/2016 persiste episodio convulsivos con episodios de más de 5 minutos de duración, en múltiples oportunidades, por lo que es trasladado nuevamente a nuestro centro asistencial  donde en vista de no yugular convulsiones con la administración de Diazepam VEV deciden intubación endotraqueal siendo conectado a T de Ayres y la administración de fenobarbital y es ingresado por el servicio de medicina interna. 1) Estatus  convulsivo 2) Infección respiratoria baja neumonía por broncoaspiracion 3) Retardo mental moderado a severo 4) Síndrome epiléptico''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente procedente de área de emergencia recibiendo oxigeno húmedo por ambu.  Se traslada a cama de UCI y se conecta a monitor cardíaco externo que reporta:TA: 103/78 (97) mmHg FC: 108 lpm FR: 18 rpm	SPO2: 100%Al ingreso previa asepsia y antisepsia de región lumbar se realiza punción lumbar extrayendo muestras para citoquímico el cual reporta normal por lo que se descarta infección del sistema nervioso central ''',
			
			"piel" : 	'''	morena, Normotérmica, normo elástica, con moderada palidez cutáneo-mucosa, llenado capilar > 3 segundos.''',

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax, se auscultan agregados roncus bilaterales abundantes a predominio derecho, ruidos cardíacos rítmicos, taquicardicos, sin soplos ni galopes.''',
			
			"abdomen": '''plano, ruidos hidroaéreos presentes, no doloroso a la palpación, sin megalias.''',

			"neurologico": '''somnolienta alternado con agitación psicomotriz, Glasgow: 6/15pts, Respuesta Motora: 4pts, Apertura Ocular: 1pt, Respuesta Verbal: 1pt limitado por TET, Pupilas isocóricas normorreactivas a la luz, sin signos meníngeo. ''',
			
			"extremidades": '''simétricas, eutróficas, sin edema.''',

		},  

		"examenFisicoIngresoHUAPA": {
			
			"resumen": ''' TA: 100/80 () mmHg	FC: 110 lpm	FR: 32 rpm	SPO2: %Paciente que luce en aparentes malas condiciones generales, pálido, estuporoso.El  paciente permanece en el Área de Emergencia durante 72 horas, el día 17/01/2016 recibe dosis de impregnación de Epamin 1200 mg, presentando múltiples episodios  convulsivos por lo que solicitan valoración por el servicio de terapia intensiva, quien acude al llamado evaluando paciente en condiciones clínicas de cuidado en vista de no contar con ventilación mecánica ni cupo en UCI se realizan sugerencias. Permanece recibiendo tratamiento a base de tazopril 48 horas y clindamicina. El día 18/01/2016 es llevado a estudio tomografico que reporta TAC de cráneo normal. Se plantea e revista médica por continuar febril, persistir cuadro convulsivo además anexarse al cuadro rigidez de nuca el diagnostico de infección del sistema nervioso central. El día 19/01/2016 se decide ingreso a UCI por disponibilidad de cupo.''',
			
			"piel": ''' Morena, hipertérmica al tacto, normo elástica, llenado capilar < 3 segundos.''',
			
			"cardiopulmonar": '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos hemitorax, se auscultan crepitantes bilaterales, ruidos cardíacos rítmicos, regulares taquicardicos sin soplos. ''',
			
			"abdomen": '''plano, blando, depresible, ruidos hidroaéreos presentes, no doloroso a la palpación, sin megalias. Sonda vesical conectada a bolsa recolectora con escasa salida de orina. ''',
			
			"extremidades": '''simétricas, sin edema.''',

			"neurologico": ''' estuporoso, no responde al dolor, Glasgow 8/15 pts.RM 4 pts. RO 2 pts: RV 1 pt. ''',

		},  
		"diagnosticoIngresoHUAPA": [
				"ESTATUS CONVULSIVO(R)  ",
				"INFECCION RESPIRATORIA BAJA :NEUMONIA POR BRONCOASPIRCION", 
				"EPILEPSIA GENERALIZADA ",
				"RETARDO MENTAL MODERADP",
				"TRASTORNO ACIDO BASICO ACIDOSIS METABOLICA+ALCALOSIS RESPIRATORIA DESCOMPENSADA", 
		], 
		
	}, # 27

	{
		"nombre": "Milagro Guanchez", 		
		"edad": "54",
		"sexo": "F",		
		"ci": "8.440.934", 				
		"fechaIngresoHUAPA": datetime(2016,5,11),  		
		"fechaIngresoUCI":datetime(2016,5,11),  		
		"antecedentes": ''' Hipertensión Arterial Sistémica, Cardiopatía Isquémica, Dislocación en columna cervical a nivel de C3 y C4, Rodilla de lavandera.''', 

		"resumenIngreso": ''' Cesareas (2) Se trata de paciente femenina, blanca de 53 años de edad con antecedentes patológicospersonales de Hipertensión Arterial Sistémica y Cardiopatia Hipertensiva, controlada con Vastarel, Cozaar 50 mg OD, Clopid 75 mg OD, Natrilix LP; antecedentes de traumatismo cervical C3-C4 porlo que presenta cervicalgia constante ameritando el uso de Collarin de Filadelphia permanente y AINES para alivio del dolor y cambios degenerativos en rodilla derecha, degeneración de menisco interno y externo grado II, osteoartrosis regional, cambios de tipo inflamatorio en región prerotuliana ( rodilla de lavandera) por lo que requiere del uso de baston de un solo apoyo para facilitar la deambulación imposibilitando cumplir con sus actividades diarias; discapacidad grado I/IV. Informe que se expide a solicitud de la parte interesada en Cumana Estado Sucre a los 11 días de Mayo de 2016.''', 
		
	}, # 28

	{
		"nombre": "Milenny Margarita Guerra Tineo", 		
		"edad": "16",
		"sexo": "F",	
		"fechaNacimiento": datetime(1999,12,31), 
		"lugarNacimiento": "Municipio Cajigal, Edo. Sucre", 		
		"ci": "28.753.022", 		
		"dirección": "Yaguaraparo, Edo. Sucre", 		
		"fechaIngresoHUAPA": datetime(2016,5,4),  		
		"fechaIngresoUCI":datetime(2016,5,4),  		

		"resumenIngreso": ''' Paciente femenina de 16 años de edad, I Gesta, quien el día  03/05/16 es llevada a mesa operatoria para realización de cesárea segmentaria por feto voluminoso, posteriormente se evidencia elevación de cifras tensionales, movimientos tónico-clónicos, se indica terapia anticonvulsivante con epamin y sulfato de magnesio, además antihipertensiva sin mejoría de la clínica, motivo por el cual refieren a este centro asistencial, donde es valorada e ingresada por el servicio de ginecología-obstetricia con diagnóstico de:1)	Puerperio quirúrgico inmediato de cesárea segmentaria por feto macrosómico complicado con THE: eclampsia.TA: 145/100mmHg FC: 78lpm. ''', 


		"examenFisicoIngresoHUAPA": {

			"resumen": ''' Se mantiene en unidad de cuidados intermedios evidenciándose movimientos tónico-clónicos generalizados, sin recuperación del estado de consciencia, a pesar de terapia anticonvulsivante con diazepam en varias oportunidades, se solicita valoración por servicio de UCI quien valora y por condiciones clínicas y disponibilidad de cupo decide su ingreso a la UCI.Se recibe paciente, en camilla de traslado, hemodinamicamente estable, respirando aire ambiente, se pasa a cama UCI y se conectada a monitor cardiaco continuo que reporta:TA: 136/115 mmHg FC: 127 lpm SatO2: 96'%' FR: 18 rpm ''',
			
			"piel" : 	'''Morena, normotérmica, hidratada, llenado capilar < 3 segundos ''',

			"cardiopulmonar":  '''Tórax simétrico, expansible, ruidos respiratorios presentes, con roncus bilaterales. Ruidos cardíacos rítmicos, regulares, sin soplos ni galope.''',
			
			"abdomen": ''' ruidos hidroaéreos presentes, blando, depresible, útero tónico, infraumbilical, incisión quirúrgica limpia y seca, genitales externos de aspecto y configuración normal, sonda vesical conectada a bolsa recolectora, con orinas claras en su interior, loquios escasos, no fétidos.''',

			"neurologico": '''en estado post-ictal, desorientada, no responde al llamado ROT III/IV  ''',

			"extremidades": '''simétricas, edema grado II/IV.''',

		}, 

		"diagnosticoIngresoUCI": [

									"STATUS CONVULSIVO",
									"TRASTORNO HIPERTENSIVO DEL EMBARAZO: ECLAMPSIA",
									"POST-OPERATORIO INMEDIATO DE CESAREA SEGMENTARIA POR FETO MACROSOMICO",
									"IRB: NEUMONÍA POR BRONCOASPIRACION ",
									"TRASTORNO HEMATOLÓGICO: ANEMIA MODERADA",
		
								],  

		"examenFisicoIngresoUCI": {
			"piel": ''' Morena, normotérmica, llenado capilar < 3 segundos.''',
			"cardiopulmonar": '''Tórax simétrico, expansible, ruidos respiratorios presentes, con roncus basales derecho. Ruidos cardíacos rítmicos, regulares, taquicardicos, sin soplos ni galope.''',

			"abdomen": '''globoso, útero tónico infraumbilical, apósito en herida quirúrgica limpio y seco, blando, depresible, sin signos de irritación peritoneal. ''',

			"extremidades": '''simétricas, eutróficas, edema grado II/IV''',

			"neurologico": '''estuporosa, pupilas isocóricas, reactivas a la luz, ROT III/IV, Glasgow 7/15 ptos (RM: 4 ptos, RO: 1 pto, RV: 2 ptos).  ''',

			"genitales": '''de aspecto y configuración normal, loquios escasos, no fétidos.  ''',
		},  	
	}, # 29

	{
		"IdHistoria": "40-01-93", 
		"nombre": "Frank José Martínez Evaristo ", 		
		"edad": "45",
		"sexo": "M",	
		"fechaNacimiento": datetime(1969,10,25), 	
		"lugarNacimiento": "Cumaná- Estado Sucre.", 		
		"ci": "10.469.107", 		
		"dirección": "barrio el dique 3era calle número 39", 		
		"fechaIngresoHUAPA":datetime(2016,1,14),  		
		"fechaIngresoUCI":datetime(2016,1,18), 		
		"resumenIngreso": ''' Paciente masculino de 45 años de edad, natural y procedente de la localidad, con antecedentes de diabetes mellitus tipo II en tratamiento con metformina y glibenclamida, hipertensión arterial en tratamiento con enalapril 20 mg OD, quien inicia enfermedad actual el día 12/01/2016 en horas de la mañana cuando presenta dolor en región abdominal de fuerte intensidad localizado en fosa iliaca derecha. por lo que acude a nuestro centro asistencial, siendo evaluado por el servicio de cirugía blanda, quien realiza paraclínicos, eco abdominal sin evidenciar alteración, siendo egresado con tratamiento médico ambulatorio(no precisado), sin mejoría clínica, el día 14/01/2016 se anexa al cuadro evacuaciones liquidas e intensificación del dolor abdominal, por lo que acude a nuestro centro asistencial siendo evaluado por el servicio de cirugía quien decide su ingreso.''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''TA: 37/20 (30) mmHg, FC: 154 lpm, FR: 34 rpm, SATO2: ?%. Se recibe  paciente en camilla de traslado, en malas condiciones generales, sin monitor cardíaco, intubada y recibiendo O2 por ambú®, se traslada a cama de UCI, se conecta a ventilación mecánica modo A/C, Vc: 640, FR: 12, FiO2: 60, Fl: 50, PEEP: 0 y se conecta monitor cardiaco continuo que reporta  signos vitales: Al momento del ingreso, requiere la administración de vasoactivos en vista de inestabilidad hemodinámica. Levophed a 40 cc/ hora. ''',
			
			"piel" : 	'''Morena, hipertérmica al tacto, con marcada palidez cutáneo mucosa, llenado capilar < 3 segundos. Diaforesis ''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, taquicárdicos,  sin soplos ni galope.  ''',
			
			"abdomen": '''globoso, ruidos hidroaéreos ausentes,  blando, depresible, impresiona doloroso a la palpación profunda, con drenes rígidos en fosa ilíaca derecha conectada a bolsa recolectora con escaso gasto purulento, se evidencia sonda nasogástrica conectada a bolsa recolectora con salida de 2000 cc de secreción bilioso aproximadamente  no megálico.''',

			"neurologico": ''' estuporoso, pupilas con tendencia a la midriasis, hiporreactivas a la luz. Glasgow 6/15 pst RM 4 pts RO 1 pt RV 1 pt.''',
		}, 

		"diagnosticoIngresoUCI": [
								
								"SHOCK SEPTICO",
								"SEPSIS PUNTO DE PARTIDA ABDOMINAL",
								"PERITONITIS PUNTO DE PARTIDA APENDICULAR ",
								"POST-OPERATORIO MEDIATO LAPAROTOMIA EXPLORADORA DEBIDO A PERITONITIS PUNTO DE PARTIDA APENDICULAR",
								"INSUFICIENCIA RENAL AGUDA PRE RENAL",
								"HIPERTENSION ARTERIAL SISTEMICA",
								"DIABETES MELLITUS TIPO II",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: / () mmHg, FC:  lpm, FR:  rpm, SATO2: %. El paciente es llevado a mesa operatoria donde bajo anestesia general se realiza laparotomía media supra, para e infra umbilical, con hallazgos de 1000 cc de secreción purulenta fétida, apéndice cecal en fase perforada en su base, conglomerado de epiplón, colon transverso, y asas delgadas. Tomando como conducta evacuación de secreción purulenta, toma de cultivo, apendicectomia apicobasal, confección de cecostomia, lavado y evacuación de cavidad abdominal con 5000 cc de solución 0,9%, dejando 2 drenes rígidos en corredera parietocólica, y fondo de saco, comprobación de hemostasia, cierre de piel y cura final. Durante acto quirúrgico el paciente permanece con hipotensión severa, imposibilitando la reversión de anestesia y su descontinuación de la ventilación mecánica, por lo que solicitan valoración por el servicio de terapia intensiva, quien acude al llamado, siendo conectado a ventilación mecánica en el área de recuperación de quirófano en modo A/C FR 12 VC 640 FL 50 FIO2 60 PEEP 0, y se realizan sugerencias en vista de no contar con disponibilidad de cupo. El paciente permanece durante 48 horas en el área de recuperación  de quirófano y el día 18/01/2016 por disponibilidad de cupo se decide su ingreso a UCI. ''',
			
			"piel": ''' Morena, normotérmica al tacto, llenado capilar < 3 segundos.''',
			
			"abdomen": '''globoso, a expensa de panículo adiposo, ruidos hidroaéreos presentes,  blando, depresible, impresiona dolor a la palpación superficial y  profunda en hipogastrio y fosa iliaca derecha, con signos de irritación peritoneal.''',
			
			"neurologico": '''conservado.''',

		},  

		"diagnosticoIngresoHUAPA": ["Peritonitis punto de partida apendicular"], 
		
	}, # 30

	{
		"IdHistoria": "54-46-15", 
		"nombre": "Giovanny José Blanco Flores", 		
		"edad": "21",
		"sexo": "M",		
		"lugarNacimiento": "Sucre", 				
		"dirección": "Cumanacoa", 		
		"fechaIngresoHUAPA": datetime(2016,4,13), 		
		"fechaIngresoUCI":datetime(2016,4,15),		
		"resumenIngreso": '''Paciente masculino de 21 años de edad, natural y procedente de Sucre, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual el día 13/04/2016 en horas de la madrugada cuando posterior a accidente de tránsito tipo colisión moto auto, es encontrado con pérdida del estado de consciencia, sin recuperación espontánea de la misma, motivos por los cuales es trasladado a este centro hospitalario, donde  se ingresa por el servicio de Neurocirugía con los diagnósticos de: Politraumatismo:Traumatismo Craneoencefálico Severo.Traumatismo Toracoabdominal cerrado.''', 


		"examenFisicoIngresoUCI": {
			"oidos": "Se evidencia restos de sangrado a través de conducto auditivo externo derecho.",
			
			"piel" : 	'''Morena, normotérmica al tacto, turgor conservado, con edema palpebral izquierdo con equimosis que limita la apertura ocular, llenado capilar < 3 segundos, con edema en hemicara izquierda.''',

			"cardiopulmonar":  '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, escasos roncus bilaterales; ruidos cardíacos, bradicardico, sin soplos ni galope.''',
			
			"abdomen": ''' plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación profunda, no megálico.''',

			"neurologico": '''Inconsciente, Glasgow: 7/15pts (Respuesta Motora: 5pts, Respuesta Verbal: 1pt, Apertura Ocular: 1pt). Pupilas isocóricas, hiporreactivas a la luz, reflejo corneal y tusígeno presentes. ''',
			
			"extremidades": '''eutróficas, sin edema ni deformidades. ''',

		}, 

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 115/61mmHg, FC: 56 lpm, FR: 11rpm, SatO2: 99'%'El paciente permanece a cargo del Servicio de Neurocirugía quien solicita valoración por UCI y  por no contar con cupo se mantiene en observación a cargo del servicio de emergencia. El 13/04/16 por deterioro neurológico se realiza intubación endotraqueal y se conecta a ventilación mecánica. Se solicita TAC de Cráneo la cual se realiza el día 14/04/16 donde se evidencia presencia de hemoventrículo más contusión hemorrágica parietal derecha, amerita colocación de derivación ventricular externa (catéter tipo Becker, solicitado por el servicio de neurocirugía). Para  el 15/04/16 se solicita nuevamente valoración por UCI y por contar con cupo se decide su ingreso al servicio. Se recibe paciente en camilla de traslado, con intubado, recibiendo oxigeno por dispositivo tipo Ambu, se pasa a cama de UCI,  se conecta a VM con los parámetros: Modo: A/C, VC: 560, FR: 12, FiO2: 60, Fl: 50, PEEP: 0, además a monitor cardíaco continuo que reporta:''',
			
			"piel": ''' Ligera palidez cutáneo mucosa, frìo.''',
			
			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos hemitórax, con agregados crepitantes en ambos hemitorax, ruidos cardíacos rítmicos, regulares, sin soplos.''',
			"abdomen": '''blando, depresible, no impresiona dolor a la palpación, no megalias.''',
			
			"extremidades": '''sin varices ni edema.''',

			"neurologico": '''paciente inconsciente. Glasgow 8/15pts (RM: 5pts, RO: 2pto, RV: 1pto). Pupila derecha con tendencia a la miosis, pupila izquierda no evaluable por equimosis bipalpebral.''',
			"cabeza": ''' Normocéfalo, tumoración en región temporal.''',

		},  
		"diagnosticoIngresoHUAPA": [
				
				"Traumatismo craneoencefálico severo complicado con contusión hemorrágica parietal derecha y hemoventrículo",
				"Politraumatizado",
				"Traumatismo  toracoabdominal cerrado",
				"Infección respiratoria baja neumonía por broncoaspiracion ",

		], 
		
	}, # 31

	{
		"IdHistoria": "54-42-51", 
		"nombre": "Eudimar José Guapa Torrivilla ", 		
		"edad": "18",
		"sexo": "F",	
		"fechaNacimiento": datetime(1998,6,28), 		
		"lugarNacimiento": "Santa María de Cariaco", 		
		"ci": "27.871.715", 		
		"dirección": "Santa María de Cariaco, Edo. Sucre", 		
		"fechaIngresoHUAPA": datetime(2016,3,31),  		
		"fechaIngresoUCI":datetime(2016,4,2),  		
		"resumenIngreso": ''' Se trata de paciente femenina de 18 años de edad, sin antecedentes patológicos conocidos, quien inicia enfermedad actual hace tres semanas aproximadamente cuando presenta hiporexia, mialgias localizadas en región cervical y miembros inferiores, que fueron aumentando en intensidad, inyección conjuntival sin secreción y vómitos de contenido alimentario, en una oportunidad, precedido de náuseas, motivo por el cual acude a centro de salud de su localidad donde evalúan y egresan con tratamiento ambulatorio a base de suplementos vitamínicos vía oral. Permanece asintomática durante una semana aproximadamente. El día 29/03/2016 presenta mialgias en miembros inferiores de severa intensidad que imposibilitan la marcha. El día 31/03/2016 se anexa al cuadro lesiones en piel hipercrómicas, de bordes irregulares, violáceas, no pruriginosas en miembros inferiores motivo por el cual acude a este centro hospitalario donde se evalúa e ingresa con los diagnósticos:1) Síndrome doloroso poliarticular2) Amenorrea ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, hemodinámicamente estable, ventilando espontáneamente, se traslada a cama de UCI, se conecta a monitor cardíaco externo que reporta: TA: 124/79 (93) mmHg FC: 113 lpm FR: 19 rpm	SPO2: 100%. ''',
			
			"piel" : 	'''	morena, normotérmica, normohidratada, turgor y elasticidad conservados, llenado capilar < 3 segundos, se evidencia pálidez cutáneo-mucosa y lesiones violáceas, de bordes irregulares, no pruriginosas en miembros inferiores, superiores y tórax.''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, se auscultan crepitantes bibasales, ruidos cardíacos rítmicos, regulares, no se auscultan soplos.''',
			
			"abdomen": ''' blando, depresible, no doloroso a la palpación, ruidos hidroaéreos presentes, sin megalias.''',

			"neurologico": ''' consciente, orientada, lenguaje coherente, pupilas isocóricas, normorreactivas, fuerza muscular 5/5, ROT II/IV, Glasgow 15/15 ptos..''',
			
			"extremidades": '''simétricas, eutróficas, edema grado II.''',

		}, 

		"diagnosticoIngresoUCI": ["Leptospirosis",],  

		"examenFisicoIngresoHUAPA": {
			
			"resumen": ''' La paciente es trasladada a sala de hospitalización a cargo del Servicio Medicina Interna. El día 01/04/2016 se solicita evaluación por UCI por alteración del estado general, se acude al llamado, se evalúa a la paciente y se realizan sugerencias. El día de hoy por disponibilidad de cupo se decide su ingreso al Servicio. Signos vitales: TA: 130/80 mmHg FC: 82 lpm FR: 16 rpm. Paciente en aparentes regulares condiciones generales, afebril, eupneica, e hidratada.''',
			
			"piel": '''Morena, normotérmica, normoelástica, llenado capilar < 3 segundos. Se evidencia equimosis en cara anterior y lateral. ''',
			
			"cardiopulmonar": '''tórax simétrico, hipoexpansible, sin tiraje, ruidos respiratorios presentes  sin agregados, ruidos cardíacos presentes sin soplo ni galope. ''',
			
			"abdomen": '''plano, ruidos hidroaéreos presentes, blando, depresible, no doloroso, sin visceromegalias. ''',

			"extremidades": '''simétrica, sin deformidades, ni edema, reflejo patelar ausente, con limitación funcional para la marcha.''',
			
			"neurologico": '''Consciente, orientada en los tres planos, arreflexia, limitación para la marcha.''',

		},  
		
	}, # 32

	{
		"IdHistoria": "52-94-68", 
		"nombre": "franklin Jesús Marval Vásquez", 		
		"edad": "35",
		"sexo": "M",	
		"fechaNacimiento": datetime(1980,10,15),  				
		"ci": "16.313.017", 		
		"dirección": "san Antonio del golfo.", 		
		"fechaIngresoHUAPA": datetime(2016,2,23), 		
		"fechaIngresoUCI":datetime(2016,4,28), 		

		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubado, conectado a ventilador de traslado, se traslada a cama de UCI y se conecta a monitor cardíaco externo que reporta:TA: 177/127 (143) mmHg FC: 104 lpm FR: 13 rpm SatO2: 97 % Se trata de paciente masculino de 35 años de edad, natural y procedente de la localidad, con antecedentes de hipertensión arterial sistémica diagnosticado en 2014 en tratamiento con amlodipino 10 mg OD, aprovel 300 mg OD (ibersartan), Clonidina 0,150 mg cada 8 horas, carvedilol 2,5 mg OD, Lupus Eritematoso Sistémico diagnosticado en enero  del 2015 en tratamiento con prednisona 25 mg OD, cloroquina 200 mg BID, Enfermedad Renal Crónica marzo del 2015 actualmente en hemodiálisis, quien inicia enfermedad actual en el mes de febrero, cuando presenta disnea a moderados esfuerzos que evoluciona a pequeños esfuerzos, tos con expectoración muco purulenta, por tal motivo acude a nuestro centro asistencial donde es evaluado e ingresado por el servicio de medicina interna. ''',
			
			"piel" : 	'''	morena, fría al tacto, llenado capilar > 3 segundos. Temp: 35ºC, se evidencia acentuada palidez cutánea mucosa.''',

			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, Se evidencia herida quirúrgica limpia y seca con dos tubos de  tórax ubicados en 6 to EIC con línea Axilar anterior izquierda y 6 to EIC con Línea axilar media  izquierda, ambos conectados a trampa de agua, con escasa secreción hemática clara. Ruidos cardíacos rítmicos, taquicárdicos, regulares, sin soplos sin galope. ''',
			
			"abdomen": ''' Rs Hs Ps, plano, no doloroso a la palpación, no megálico. ''',

			"neurologico": ''' Bajo efectos de sedación farmacológica, Glasgow no evaluable. Pupilas isocóricas mióticas, hiporreactivas a la luz.''',
			
			"extremidades": '''Simétricas, sin edema.''',

		}, 

		"diagnosticoIngresoUCI": [
									"Postoperatorio Inmediato de Toracotomía ",
									"postero lateral izquierda para drenaje de derrame pericárdico masivo y pericardiectomía anterior.",
									"Derrame pericárdico",
									"Enfermedad Renal Crónica estadio V en hemodiálisis.",
									"LES",
									"Hipertensión arterial sistémica ",
									"Trastorno hematológico: anemia moderada", 
								],  

		"examenFisicoIngresoHUAPA": {
			"Signos Vitales": '''FR: 22 rpm    FC: 115 rpm   TA: 160/110 mmhg   T 37 ºC ''',
			
			"resumen": ''' El día 29/02/2016 se realiza tomografía de tórax que reporta  Derrame pericárdico importante, Derrame pleural izquierdo escaso,  Cisuritis izquierda, calcificación pulmonar en vértice izquierdo.Por tal motivo se solicita valoración por el servicio de cirugía vascular el cual solicita preparar preoperatorios para resolución quirúrgica (pericardiectomía). Permaneciendo en el área de observación, el día 28/04/2016 es llevado a mesa operatoria donde bajo anestesia general, se realiza toracotomíaanterior izquierda, con hallazgos,  derrame pericárdico masivo 800 cc aproximadamente, derrame pleural izquierdo de 300 cc aproximadamente, pericardio engrosado,  tomando como conducta,  punción y aspiración de líquido pericárdico 60 cc para estudio, drenaje del líquido, pericardiectomía, anterior de 8 cm aproximadamente, comprobación de hemostasia, colocación de tubo de drenaje torácico numero 34 dirigido a pericardio y otro 34 FR a cavidad pleural izquierdo fijado a piel, conexión de los mismos a trampa de agua  cierre de pared torácica, se envía muestra de pericardio, y liquido pericárdico para estudio de BK, cultivo, citología y citoquímico.se decide su ingreso en la unidad de cuidados intensivos para cuidados post quirúrgico.''',
			
			"piel": ''' morena normotérmica, normohidratada, llenado capilar < 3 seg.''',
			
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes con agregados tipo crepitantes en bases pulmonares,. Rs Cs Rs Rs sin soplos, sin galope. ''',
			
			"abdomen": '''Blando, depresible, no impresiona doloroso a la palpación, no megálico.''',
			
			"extremidades": '''Simétricas con edema grado III. ''',

			"neurologico": '''Consciente, vigil, orientado en 3 planos.''',

		},  
		"diagnosticoIngresoHUAPA": [
			"Infección respiratoria baja neumonía bilateral",
			"Derrame pericárdico AD.",
			"Enfermedad Renal Crónica estadio V en Hemodiálisis.",
			"Hipertensión arterial sistémica", 
			"LES",
			"TBC AD",
		], 
		
	}, # 33

	{
		"IdHistoria": "54-34-80", 
		"nombre": "Esteban Daniel Guevara Sacarías", 		
		"edad": "21",
		"sexo": "M",	
		"fechaNacimiento": datetime(1994,7,8), 		
		"lugarNacimiento": "Cumana", 		
		"ci": "23.347.231", 		
		"dirección": "Mariguitar", 		
		"fechaIngresoHUAPA": datetime(2016,3,6), 		
		"fechaIngresoUCI":datetime(2016,3,7), 		 
		"resumenIngreso": ''' Se trata de paciente masculino de 21 años de edad natural procedente de Mariguitar sin antecedentes patológicos conocidos quien inicia enfermedad actual el día 05/03/2016 cuando posterior a accidente vial tipo caída de vehículo en movimiento tipo moto presenta múltiples traumatismos y perdida del estado de consciencia de 1 hora aproximadamente,  por lo que es traído a centro asistencial (HUAPA) evaluado y egresan ,para el día 06/03/2016,  Presenta cefalea holocraneana, diplopía y vómitos, posteriormente se anexa al cuadro clínico   deterioro del estado de consciencia acompañado de movimientos tónico clónicos generalizados con relajación de esfínter vesical y retroversión ocular,  por lo que es llevado a centro privado de la localidad donde se brindan los primeros auxilios y se refiere a este centro asistencial. ''', 


		"examenFisicoIngresoHUAPA": {

			"resumen": '''TA 110/70 MMHG FC 76 LPM FR 16 RPM ''',
			
			"piel" : 	'''piel morena, llenado capilar < 3seg''',

			"cabeza": ''' escoriaciones múltiples, estigmas traumáticos en región frontal ''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax, sin agregados pulmonares.  Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos ni galope. ''',
			
			"abdomen": '''Blando, globoso ruidos hidroaéreos presentes, no  doloroso a la palpación superficial y profunda, no visceromegalias.''',

			"neurologico": '''Estuporoso ECG 4/15 puntos RM 2 RV 1 RO 1, pupilas anisocóricas midriasis izquierda. ''',
		}, 

		"diagnosticoIngresoUCI": [
									"POST OPERATORIO INMEDIATO DE CRANIECTOMIA DESCOMPRESIVA SUB FRONTAL + DRENAJE DE HEMATOMA EPIDURAL TEMPORAL IZQUIERDO + DRENAJE DE HEMATOMA SUBDURAL FRONTOPARIETAL DERECHO ",
									"POLITRAUMATIZADO ",
									"TCE SEVERO CERRADO ",
									"TRAUMATISMO TORACO ABDOMINAL CERRADO",
								],  

		"examenFisicoIngresoUCI": {
			
			"resumen": ''' Se recibe paciente en camilla de traslado conectada  a monitor cardiaco, conectado a ventilador de transporte se traslada a cama de UCI SIGNOS VITALES:  FC 66 LPM TA 122/64 (84) MMHG FR 16 SAT O2 98%. Se conecta a VM EVITA 4 parámetros VC 560 FIO2 60 FL 50 FR 12  PEEP 0''',
			
			"piel": ''' Normotérmica, palidez cutáneo mucosa moderada, llenado capilar <3segundos. Se evidencia apósitos que cubre herida quirúrgica en cráneo ''',

			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos hemitorax sin  agregados pulmonares.  Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos. ''',

			"abdomen": '''Blando, no  doloroso a la palpación superficial y  profunda, no visceromegalias.''',

			"neurologico": '''Glasgow no evaluable por efectos de sedantes, pupilas isocóricas mióticas.''',

		},  
		"diagnosticoIngresoHUAPA": [
				
			"TCE SEVERO SIMPLE CERRADO", 
			"HEMATOMA EPIDURAL IZQUIERDO POR CLINICA ",
			{"resumen": ''' Se realiza TAC de cráneo evidenciándose Hematoma epidural temporal izquierdo y hematoma subdural frontoparietal derecho por lo que para el día de hoy 07/03/16 es evaluado por servicio de Neurocirugía y llevado a mesa operatoria para resolución quirúrgica realizándose craniectomía descompresiva sub frontal + drenaje de hematoma epidural temporal izquierdo y drenaje de hematoma subdural frontoparietal derecho, trasladándose a UCI para manejo post quirúrgico '''},

		], 
		
	}, # 34

	{
		"IdHistoria": "54-49-16", 
		"nombre": "Lennys José Patiño Cova ", 		
		"edad": "20",
		"sexo": "M",	
		"fechaNacimiento": datetime(1995,10,8),  		
		"dirección": "Araya Calle Palmira", 		
		"fechaIngresoHUAPA": datetime(2016,4,24), 		
		"fechaIngresoUCI":datetime(2016,4,24), 		
		"resumenIngreso": ''' Se trata de paciente femenina de 20 años de edad natural y procedente de Araya, familiar refiere inicio de enfermedad actual el día 24/04/16 en horas de la madrugada aproximadamente 2:00 am, cuando posterior a herida por proyectil de arma de fuego con orificio de entrada en región frontal de aproximadamente 0.5 cm,sin orificio de salida  presenta perdida del estado de conciencia y pérdida de masa encefálica, motivo por el cual es traslada a este centro donde se evalúa por el servicio de emergenciologia e ingresa.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, con intubación endotraqueal y apoyo de ambu, se traslada a cama de UCI, se conecta a ventilador mecánico modo A/C a través de TET; FIO2: 60, Vc: 560, Ti: 0.95, FLUJO: 50, FR: 12, PEEP: 0, con parámetros de monitor cardíaco externo que reporta:TA: 111/70 mmHg FC: 66 lpm	FR: 17 rpm	SPO2: 93%.''',
			
			"piel" : 	'''	blanca, normotermicatérmica al tacto, llenado capilar > 3 Seg. ''',
			
			"cabeza":''' normocefalica, se evidencia apósito quirúrgico limpio y seco cubriendo herida en región frontal derecha.''',

			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible ruidos respiratorios presentes en ambos hemitorax sin agregados, Ruidos cardiacos rítmicos y regulares, sin  soplo ni galope.''',
			
			"abdomen": ''' plano, Blando, no doloroso a la palpación, ruidos hidroaéreos presentes, no megalias.''',

			"neurologico": ''' Paciente inconsciente en estado de estupor, pupilas anisocóricas (derecha de más de 3 mm con tendencia a la midriasis e izquierda <2 mm con tendencia a la miosis), sin respuesta a la  luz, Glasgow 7/15 ptos. (RV: 1 pts, RO: 1 pto, RM: 4 ptos)  ''',
			
			"extremidades": '''Simétricas, sin edema.''',
		}, 

		"diagnosticoIngresoUCI": ["Herida por proyectil de arma de fuego en cráneo", ],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 120/80 mmHg; FC:76 lpm FR: 21 rpm SPO2:? ''',

			"cabeza": ''' se evidencia orificio de más o menos 0,5 cm con pérdida de masa encefálica''',

			"piel": ''' blanca hidratada llenado capilar < 3 seg.''',
			"cardiopulmonar": '''tórax simétrico normoexpansible ruidos respiratorios presentes en ambos hemitorax no se auscultan agregados ruidos cardiacos rítmicos y regulares sin soplo ni galope ''',
			"abdomen": '''plano blando no impresiona dolor, no se palpa megalia.''',
			"extremidades": '''simétrica sin edema''',
			"neurologico": '''paciente estuporosa con estímulo al dolor, Glasgow: RO: 1 ptos, RV: 2 ptos, RM: 2 ptos. Pupilas anisocóricas midriática derecha. ''',

		},  
		"diagnosticoIngresoHUAPA": [
			"TRAUMATISMO CEFÁLICO SEVERO ABIERTO DEBIDO A",
			"H.P.P.A.F  EN REGIÓN FRONTAL DERECHO.",
		], 
		
	}, # 35

	{
		"IdHistoria": "54-42-83", 
		"nombre": "Joskar David Soto Alfonzo", 		
		"edad": "30",
		"sexo": "M",	
		"fechaNacimiento": datetime(1985, 2, 27),  		
		"lugarNacimiento": "Mérida", 		
		"ci": "16.934.040", 		
		"dirección": "Urb. Gran Mariscal, Cumaná.", 		
		"fechaIngresoHUAPA": datetime(2016,4,2),  		
		"fechaIngresoUCI":datetime(2016,4,2),  		

		"resumenIngreso": ''' Se trata de paciente masculino de 30 años de edad, sin antecedentes patológicos conocidos, quien inicia enfermedad actual el día 01/04/2016 cuando presenta disnea a pequeños esfuerzos, mucosas secas, poliuria, polidipsia, polifagia, motivos por los cuales es evaluado, se realiza glicemia capilar que reporta: 576mg/dl, motivos por los cuales es ingresado con el diagnóstico:1) Cetoacidosis Diabética2)Diabetes Mellitus tipo 1 en estudio''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, hemodinamicamente estable, ventilando espontáneamente, se traslada a cama de UCI, se conecta a monitor cardíaco externo que reporta:TA: 95/58mmHg FC: 90lpm	FR:14rpm SPO2: 100%''',
			
			"piel" : 	'''blanca, normotérmica, turgor disminuido, llenado capilar < 3 segundos, con leve pálidez cutáneo-mucosa, mucosas secas.''',

			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, no se auscultan agregados, ruidos cardíacos rítmicos, regulares, no se auscultan soplos.''',
			
			"abdomen": ''' blando, depresible, no doloroso a la palpación, ruidos hidroaéreos presentes, sin megalias. ''',

			"neurologico": '''consciente, orientada en 3 planos, lenguaje coherente, fuerza muscular 5/5, ROT II/IV.''',
			
			"extremidades": '''simétricas, eutróficas, sin edemas.''',

		}, 

		"diagnosticoIngresoUCI": [
									"Diabetes Mellitus tipo 2 Descompensada en Cetoacidosis Diabética",
									"Trastorno Hidroelectrolítico: Hipokalemia.",
									"Trastorno Acido/Base: Acidosis Metabólica compensada con Alcalosis Respiratoria más Hiperoxemia.",
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente en aparentes malas condiciones generales, afebril, disneico, deshidratado. En vista de condiciones clínicas del paciente solicitan valoración por Residente de UCI, quien realiza sugerencias, realizan además Cateterización de Vía Venosa Central Yugular Interna con prueba de xifonaje positivo, se verifica correcta colocación de la misma con Rx de Tórax.El día de hoy por disponibilidad de cupo se decide su ingreso.''',

			"piel": ''' Morena, fría al tacto, sudoroso, llenado capilar < 3 segundos.''',
			"cardiopulmonar": '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes  sin agregados, se evidencia tiraje intercostal y respiración de Kussmaul. ''',
			"abdomen": '''blando, depresible, no doloroso,ruidos hidroaéreos presentes, sin signos de irritación peritoneal.''',
			"neurologico": '''Consciente, Desorientado.''',

		},  
		
	}, # 36

	{ 
		"nombre": "Germán Rafael Lanza.", 		
		"edad": "80",
		"sexo": "M",	
		"fechaNacimiento": datetime(1936,3,1), 		
		"lugarNacimiento": "Cumaná - Estado Sucre", 		
		"ci": "521.508 ", 		
		"dirección": "Urbanización Fe y Alegría, Bloque 26. Cumaná, Estado Sucre.", 		
		"fechaIngresoHUAPA": datetime(2016,7,5),		
		"fechaIngresoUCI":datetime(2016,7,5),		
		"resumenIngreso": ''' Se trata de paciente masculino  de 80 años de edad, natural y procedente de la localidad, con antecedentes de hipertensión arterial en tratamiento con Amlodipina 5mg, Ramipril 2,5mg, Cardiopatía Hipertensiva en tratamiento con Digoxina 0,25mg, Diabetes Mellitus tipo 2 sin tratamiento, quien inicia enfermedad actual el día 06/05/2016 en horas de la mañana cuando presenta disminución de la fuerza muscular en hemicuerpo derecho, concomitantemente lenguaje disartrico, motivo por el cual es trasladado acentro clínico privado donde es hospitalizado, administran  oxígeno, se conecta a  monitoreo cardiaco continuo constatando  cifras de tensión arterial elevadas iniciando tratamiento no precisado. Posteriormente el 07/05/2016 se anexa al cuadro clínico disnea progresiva de moderados a leves esfuerzos y cianosis distal, por lo que es evaluado por especialista de guardia quien decide referir a nuestra institución, donde ingresa en unidad de cuidados intensivos. ''', 

		"diagnosticoIngresoPrivado": [
									"Insuficiencia Cardíaca descompensada en edema agudo de pulmón.",
									"Evc de etiología a precisar.",
									"Hipertensión arterial sistémica",
									"Diabetes Mellitus tipo 2.",
									"Cardiopatía Dilatada.",
								],  
		"diagnosticoIngresoHUAPA": [
				"Insuficiencia Respiratoria Aguda.",
				"Crisis Hipertensiva tipo Emergencia expresada en EVC de etiología a precisar. ",
				"Insuficiencia Cardiaca descompensada en Edema Agudo de Pulmón.",
				"Hipertensión arterial sistémica.",
				"Diabetes Mellitus tipo 2.",
				"Cardiopatía Dilatada.",

		], 
		
	}, #37

	{
		"IdHistoria": "54-30-11", 

		"nombre": "Eleazar Malavé Amaya", 		

		"edad": "40",

		"sexo": "M",	

		"fechaNacimiento": datetime(1976,5,27), 		

		"lugarNacimiento": "Cumaná - Estado Sucre", 		

		"ci": "12.276.985 ", 		

		"dirección": "Brasil, Sector III, Calle 13", 		

		"fechaIngresoHUAPA": datetime(2016,2,21), 		

		"fechaIngresoUCI":datetime(2016,2,26), 		

		"resumenIngreso": ''' Se trata de paciente masculino de 40 años de edad, natural y procedente de la localidad, sin antecedentes conocidos, cuyo familiar refiere inicio de enfermedad actual el 18/02/2016 aproximadamente cuando presenta debilidad generalizada, vómitos en varias oportunidades, temperatura corporal cuantificada en 39º, concomitantemente cefalea de moderada intensidad, mialgias y artralgias. El día 21/02/2016 presenta disminución de la fuerza muscular en ambos miembros inferiores, motivos por los cuales acude a este centro donde es evaluado e ingresado por el Servicio de Medicina Interna.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' TA: 84/55 mmHg FC: 149 lpm FR: 20 rpm SPO2: 83%''',
			
			"piel" : 	'''	Morena, normotérmica, normoelástica, turgor disminuido, mucosas secas, con leve pálidez cutáneo mucosa,  llenado capilar < 3 Seg.  ''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes, sin agregados, disminuidos en base pulmonar izquierda. Ruidos cardiacos rítmicos, regulares, sin soplos.''',
			
			"abdomen": ''' Plano, depresible, ruidos hidroaéreos presentes, no doloroso a la palpación no megalias''',

			"neurologico": '''  No evaluable por sedación farmacológica. Pupilas mióticas no reactivas a la luz.''',
			
			"extremidades": '''Simétricas, eutróficas, sin edemas.''',

		}, 

		"diagnosticoIngresoUCI": [
								"Síndrome de Guillain Barre",
								"Insuficiencia respiratoria aguda",
								"Infección Respiratoria Baja: Neumonía Nosocomial ",
								{"resumen": ''' Paciente permanece durante 52 días en la Unidad de cuidados Intensivos, con diagnósticos de síndrome de Guillain Barre,Insuficiencia respiratoria aguda, infección respiratoria baja neumonía nosocomial, recibió 5 sesiones de Plasmaféresis, conevolución clínica tórpida progresando disminución de fuerza hasta 0/V, permanece  recibiendo tratamiento con múltiples antibióticosindicados de acuerdo a cultivos (secreción bronquial, Urocultivo, hemocultivo), recibiendo como primer antibiótico meropenem (24) díasel día 8/03/2016 por intubación prolongada se realiza traqueostomía sin complicaciones, el día 11/03/2016 se recibe Urocultivo que reportapresencia de Cándida sp por lo que se (24 días), posteriormente se recibe nuevo Urocultivo que reporta levaduras gemantes por lo que se realizanuevo ciclo de fluconazol el cual recibió por (15 días), actualmente se evidencia mejoría clínica desde el punto de vista neurológico y ventilatorio,lográndose destete de la ventilación mecánica el día 19/04/2016 recibiendo oxigeno húmedo por T de Ayres. Por lo que se solicita cupo en CDI para manejo derehabilitación física.'''},
							
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": '''TA: 130/80 mmHg	FC: 68 lpm  FR: 18 rpm El paciente permanece en el Área de Emergencia durante 5 días, con evolución clínica tórpida caracterizada por disminución simétrica y progresiva de fuerza muscular en extremidades inferiores, El día 22/02/2016 se realiza punción lumbar donde se reporta: Celularidad: 0cels/mm3, Proteínas: 10mg/dl. Solicitan valoración por el Servicio de Hematología quien decide iniciar sesiones de Plasmaféresis y para ello realizan colocación de Catéter Bilumen en Vena Femoral Izquierda. El día 24/02/2016 el paciente presenta fuerza muscular valorada en 0/5, arreflexia, apnea, sialorrea, motivos por lo que se realiza maniobra de intubación endotraqueal y se conecta a ventilación mecánica. Solicitan valoración por el servicio de terapia intensiva quien acude al llamado evaluando al paciente y  por disponibilidad de cupo se decide su ingreso a UCI.''',
			"piel": ''' Morena, Normotérmica, normoelástica, con llenado capilar < 3 Seg.''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes, sin agregados. Ruidos cardiacos rítmicos, sin soplos''',
			"abdomen": '''Plano, depresible, ruidos hidroaéreos presentes, no doloroso a la palpación no megalias''',
			"extremidades": '''Simétricas, eutróficas, sin edemas.''',
			"neurologico": '''Consiente, orientado en tres planos, con disminución de la fuerza muscular. ''',

		},

		"examenFisicoActual": {
			"resumen": ''' TA: 155/78 (99) mmHg	FC: 121 lpm FR: 21 rpm 	SPO2: 96%''',
			"piel": ''' Morena, normotérmica, normoelástica, turgor disminuido, mucosas secas, con leve pálidez cutáneo mucosa,  llenado capilar < 3 Seg. ''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes, con  agregados roncus bilaterales escasos. Ruidos cardiacos rítmicos, regulares, sin soplos.''',
			"abdomen": '''Plano, depresible, ruidos hidroaéreos presentes, no doloroso a la palpación no megalias''',
			"extremidades": '''Simétricas, eutróficas, sin edemas.''',
			"neurologico": '''consciente, orientado, pupilas isocóricas normorreactivas a la luz, Glasgow 11/15 pts RM 6 pts RO 4 pts RV 1 pt limitado por traqueostomo fuerza muscular II/V.''',

		}, 
		"diagnosticoIngresoHUAPA": [
				
			"Síndrome Viral Agudo (ZIKA)",
			"Síndrome de  Guillain Barre.",

		], 
		
	}, # 38

	{ 
		"nombre": "CRUZ RODRIGUEZ", 		
		"edad": "80",
		"sexo": "F",	
		"fechaNacimiento": datetime(1936,10,14),  		
		"lugarNacimiento": "Cumaná", 		
		"ci": "2.332.696", 		
		"dirección": "Cumanacoa, Estado Sucre.", 		
		"fechaIngresoHUAPA": datetime(2016,5,5), 		
		"fechaIngresoUCI":datetime(2016,5,6), 		
		"resumenIngreso": ''' Se trata de paciente femenina de 80 años de edad natural de Cumaná y procedente de Cumacacoa, con antecedentes de Hipertensión Arterial mal controlada, Cardiopatía Hipertensiva  e Isquémica crónica, y taquiarritmia tratada con Concor® 2,5 mg OD. Cursa con antecedente quirúrgico reciente del día 01/05/2016 por hernia inguinal izquierda atascada en centro clínico privado, donde realizan Hernioplastia con resección y anastomosis del segmento afectado aparentemente sin complicaciones, permaneciendo 24 horas en la Unidad de Cuidados Intensivos en el postoperatorio inmediato, hemodinamicamente estable; posteriormente es trasladada a sala de hospitalización durante 72 horas con evolución clínica satisfactoria, recibiendo Ciprofloxacina y Metronidazol, Nutrición parenteral parcial, hasta el día 05 del presente mes cuando en horas de la madrugada presenta distención abdominal, vómitos de contenido entérico y ausencia de ruidos hidroaéreos, motivo por el cual es reevaluada por Cirujano tratante quien en vista de motivos socioeconómicos de la paciente decide referir a este centroasistencial donde se ingresa por el Servicio de Cirugía blanda.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, procedente de recuperación de quirófano. Se traslada a cama de UCI y se conecta a monitor cardiaco continuo que reporta signos vitales:FR: 18 rpm FC: 144 lpm TA: 97/33 mmHg TAM: 46mmHg SATO2: 90%.''',
			
			"piel" : 	'''	Leve palidez cutáneo mucosa, afebril al tacto, deshidratada,  llenado capilar <3 seg. ''',

			"cardiopulmonar":  ''' Tórax simétrico normoexpansible Ruidos respiratorios presentes en ambos hemitorax, no se auscultan agregados. Ruidos cardiacos arrítmicos, sin soplos sin galope. ''',
			"abdomen": ''' Blando, depresible, Rs Hs Ps,  doloroso a la palpación profunda en hemiabdomen izquierdo. Se evidencian heridas quirúrgicas correspondientes a Hernioplastia inguinal izquierda y laparotomía exploradora con apósitos estériles limpios y secos sin drenajes. ''',

			"neurologico": ''' Somnolienta con episodios de agitación psicomotriz, Glasgow: 9/15 ptos dado por RO: 3 ptos RV: 1 ptos RM: 5 ptos. Pupilas isocóricas con tendencia a la miosis hiporreactivas a la luz.''',
			"extremidades": '''Simétricas sin edema.''',

		}, 

		"diagnosticoIngresoUCI": [

									"Shock Séptico.",
									"Post-operatorio Inmediato de relaparotomia exploradora por Obstrucción Intestinal por estenosis de anastomosis + Apendicectomía.",
									"Postoperatorio Mediato de Hernioplastia inguinal izquierda.",
									"Trastorno hematológico",
									"Anemia Leve.",
									"Trastorno hidroelectrolítico",
									"Deshidratación leve.",
							
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' No se reportan signos vitales de ingreso. ''',
			"piel": ''' Morena, normotérmica, normohidratada, turgor y elasticidad conservados, llenado capilar < 3 seg.  ''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, Rs Rs Ps sin agregados. Rs Cs Rs Rs S/S.''',
			"abdomen": '''Globoso a expensas de panículo adiposo, Rs Hs Presentes, distendido, timpánico, blando, doloroso a la palpación. Herida quirúrgica en fosa ilíaca izquierda limpia y seca, dolorosa a la palpación.''',
			"extremidades": '''Simétricas sin edema.''',
			"neurologico": '''Conservado. ''',

		},  

		"diagnosticoIngresoHUAPA": [
			"Postoperatorio Mediato de Hernioplastia Inguinal Izquierda.",
			"Obstrucción Intestinal.",
			"Hipertensión Arterial Sistémica.",
			{"resumen": ''' La paciente es llevada a mesa operatoria en donde bajo anestesia general se realiza relaparotomia media-infraumbilical,encontrándose los siguientes hallazgos: 100 cc de hemoperitoneo, entero-enteroanastomosis a 100 cm de asa fija estenótica,Tu quístico 2x2 cm en base apendicular, tomándose como conducta desmontaje y re-confección de anastomosis T-T en dos planos,apendicectomía, lavado de cavidad abdominal comprobación de hemostasias y cierre por planos. Permanece en área de recuperación durante 2 horas y en vista de que la paciente presenta cuadro de dificultad respiratoria con cianosis distal, es evaluada por elServicio de Anestesia, realizando Intubación endotraqueal y apoyo de oxígeno con Ambú a 10 litros, motivo por el cual solicitanvaloración por el servicio de Terapia Intensiva, se acude al llamado y se evalúa en conjunto a Intensivista de GuardiaDra. Begglia Roa quien en vista de disponibilidad de cupo se decide su ingreso. '''}

		], 
		
	}, # 39

	{
		"IdHistoria": "53-00-39", 
		"nombre": "Luis José Silva", 		
		"edad": "49",
		"sexo": "M",	
		"fechaNacimiento": datetime(1964,2,12), 	
		"lugarNacimiento": "Cumaná", 		
		"ci": "9.973.046", 		
		"dirección": "san Fernando de tataracual", 		
		"fechaIngresoHUAPA": datetime(2016,3,1), 		
		"fechaIngresoUCI":datetime(2016,3,2), 		
	
		"resumenIngreso": ''' Paciente masculino de 49 años de edad, natural de la localidad, procedente de Tataracual, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual el día 01/03/16 cuando posterior a caída de altura de 3 metros aproximadamente presenta traumatismos múltiples, por tal motivo es trasladado a  nuestro centro asistencial donde se evidencia  herida en región parietal con defecto cutáneo, paraplejia, con nivel sensitivo T3, por tal motivo es  ingresado por el servicio de Neurocirugía con los diagnósticos de:1) Politraumatizado 2) Traumatismo raquiomedular cerrado cervicodorsal frankel A3) TEC leve simple cerrado''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente, en camilla de traslado, tolerando aire ambiente, se pasa a cama UCI, se conecta a monitor cardíaco continuo que reporta: TA: 90/49(68) mmHg, FC: 65 lpm, FR: 10 rpm, SatO2: 96% ''',
			
			"piel" : 	'''	Morena, normotérmica, deshidratada. Llenado capilar menor de 3 segundos. ''',

			"cabeza": '''Normocéfalo se evidencia en región frontal apósito estéril que cubre herida limpia y seca''', 
			"cuello": '''Se evidencia en región anterolateral derecha apósito estéril que cubre herida quirúrgica limpio y seco''',
			"torax": '''Simétrico normoexpansible, ruidos respiratorios presentes sin agregados, ruidos cardiacos rítmicos sin soplo ni galope.''',

			"abdomen": '''Plano, ruidos hidroaéreos presentes, no doloroso a la palpación, no se palpan visceromegalias.''',

			"neurologico": ''' Consciente orientado en los 3 planos, Glasgow 15/15 pts .Paraplejia en extremidades inferiores, nivel sensitivo T3 reflejo aquiliano disminuido, rotuliano abolido, fuerza muscular IV/V en extremidades superiores sin signos meníngeos ni de hipertensión endocraneana. ''',
			"extremidades": '''simétricas eutróficas ''',

		}, 

		"diagnosticoIngresoUCI": [
							"POST-OPERATORIO INMEDIATO DE DISECTOMIA DE  C6- C7 + COLOCACIÓN DE DISPOSITIVO INTERSOMATICO + ARTRODESIS ",
							"TRAUMATISMO RAQUIMEDULAR COMPLICADO CON FRACTURA C6 FRANKEL A + ANTEROLISTESIS DE C6 SOBRE C7 ",
							"TEC LEVE SIMPLE CERRADO",
							{"resumen": ''' El paciente permanece durante 5 días en Unidad de Cuidados Intensivos, recibiendo tratamiento a base de ceftazidima (3 dias),vancomicina (4 dias), epamin (4 dias), el día 3/03/2016 se anexa al cuadro clínico bradicardia severa que requiere la administraciónde atropina e hipotensión arterial que requiere el uso de vasoactivos tipo levophed, permaneciendo inestable hemodinamicamente durante48 horas se anexa al diagnóstico shock medular, el día 07/03/2016 se logra destete satisfactorio de vasoactivos en vista de mejoría decifras tensionales. Sin nuevo episodio de bradicardia, se anexa al tratamiento el uso de esteroide solumedrol 500 mg cada 8 horas por 24 horas,realizándose rotación del mismo a hidrocortisona 100 mg cada 8 horas, se plantea en revista médica  continuar con esteroide hasta completar los 7días con el mismo, en vista de mejoría clínica y paraclínicos se decide alta médica a cargo del servicio de neurocirugía. '''},

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 120/70 mmHg FC: 76 lpm FR: 16 rpm SPO2: %. Posteriormente es trasladado a estudio por imágenes TAC de columna cervicodorsal el cual reporta  fractura del cuerpo vertebral C7, anterolistesis de C6 sobre C7, disminución del calibre del canal medular  nivel de C6-C7,  por lo que se comunica caso con especialista de guardia por parte de Neurocirugía quien indica planificar para quirófano.. El día 02/03/2016 es llevado a mesa operatoria donde bajo anestesia general se realiza disectomia de  C6- C7 más colocación de dispositivo intersomatico más artrodesis. Siendo trasladado posteriormente a Unidad de Cuidados Intensivos para cuidados post operatorios. ''',
			"piel": ''' morena, normotermica, normohidratada.''',

			"torax": ''' simétrico normoexpansible, ruidos respiratorios presentes sin agregados, ruidos cardiacos rítmicos sin soplo ni galope.''',
			"extremidades": '''simétricas eutróficas ''',
			"neurologico": '''consciente orientado en los 3 planos, Glasgow 15/15 pts paraplejia en extremidades inferiores, nivel sensitivo T3 ASIA MOTOR 50 puntos reflejo aquiliano disminuido, rotuliano abolido, fuerza muscular III/V en extremidades superiores sin signos meníngeos ni de hipertensión endocraneana. ''',

		},  
		
	}, # 40


	{
		"nombre": "Raúl José Malavé", 		
		"edad": "63",
		"sexo": "M",	
		"fechaNacimiento": datetime(1952,9,16),  		
		"lugarNacimiento": "Cumaná", 		
		"ci": "3.872.452", 		
		"dirección": "Boca De Sabana", 		
		"fechaIngresoHUAPA": datetime(2016,1,12),  		
		"fechaIngresoUCI":datetime(2016,1,12),  		

		"resumenEgreso": ''' Se trata de paciente masculino de 63 años de edad, natural y procedente de la localidad, con antecedentes de Hipertensión Arterial de larga data tratada con Cozaar 50 mg OD, inicia enfermedad actual hace 13 días (31-12-2015), cuando presenta cefalea holocraneana de fuerte intensidad y perdida brusca del estado de conciencia,  motivo por el cual es llevado a ambulatorio de la localidad donde recibe los primeros auxilios constatan cifras tensionales elevadas y por no disponer de un área adecuada refieren a otro centro asistencial. Es llevado por familiares a centro privado donde evalúan y por constatar cifras tensionales normales, egresan. Por persistencia de sintomatología es llevado nuevamente a centro privado el día 01-01-2016, donde es valora por especialista de guardia quien decide su ingreso a UCI. Durante su estancia se realiza TAC Cerebral que reporta Hemorragia Subaracnoidea con Drenaje a Ventrículo Fischer IV. Posteriormente se realiza Angio TAC que reporta Aneurisma Cerebral en Arteria Cerebral Media, ameritando valoración por Servicio de Neurocirugía (Dr. Montaño), quien plantea resolución quirúrgica al mejorar condiciones. Asimismo, desde su ingreso se evidencia aumento de niveles de amilasa, con lipasa normales, actualmente se mantiene con lipasa y amilasa elevadas. En vista de su evolución tórpida y a petición de familiares se decide su traslado a este centro asistencial, donde previa valoración se ingresa.''',


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe Paciente trasladado en camilla de transporte recibiendo oxigeno por mascarilla facial; se traslada a cama UCI, conectándose a monitor cardíaco continuo externo que reporta signos vitales: TA: 193/94 mmHg TAM: 119 mmHg FC: 100 lpm FR: 29 rpm  Sat O2: 95 %. Paciente es valorado por residente de UCI quien procede a realizar VVC yugular derecha sin complicaciones, xifonaje positivo. Se realiza Rx de tórax control.''',
			
			"piel" : '''Morena, afebril, normohidratada, turgor acorde a la edad, llenado capilar menor a 3 Segundos.''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax, sin agregados, Ruidos cardíacos taquicardicos e irregulares, normofonéticos, sin soplo, ni galope.''',
			"abdomen": ''' Globoso a expensa de panículo adiposo, RsHs presentes, blando, depresible no dolorosos a la palpación, sin visceromegalias. ''',

			"neurologico": ''' Somnoliento, Glasgow 11/15 puntos dados por RM 6, RV 1, RO 4, se evidencia hemiparesia izquierda. Pupilas isocóricas normorreactivas a la luz. ''',
		
			"genitales_externos": '''Aspecto y configuración normal, se evidencia sonda vesical conectada a bolsa de recolección con aproximadamente 200 cc de orinas claras sin sedimento.''',

		}, 

		"diagnosticoIngresoUCI": [

						"EVC DE ETIOLOGÍA HEMORRÁGICA",
						"HEMORRAGIA SUBARACNOIDEA CON DRENAJE A VENTRÍCULO FISCHER IV ",
						"ANEURISMA CEREBRAL EN ARTERIA CEREBRAL MEDIA",
						"PANCREATITIS AGUDA",
						"HIPERTENSIÓN ARTERIAL SISTÉMICA",

							
								],  

	
		
	}, # 41

	{
		"nombre": "Miguel Marcano", 		
		"edad": "17",
		"sexo": "M",	
		"fechaNacimiento": datetime(1998,8,18), 		
		"lugarNacimiento": "Cumana ", 		
		"ci": "26.419.763", 		
		"dirección": "El dique", 		
		"fechaIngresoHUAPA": datetime(2016,4,17), 		
		"fechaIngresoUCI":datetime(2016,4,21), 		

		"resumenIngreso": ''' Se trata de paciente masculino de 17 años de edad con antecedente de obstrucción intestinal a los 2 años de edad, quien inicia enfermedad actual el día 17/04/16 cuando presenta dolor abdominal difuso de moderada intensidad, concomitantemente vómitos biliosos precedidos de nauseas, abundante cantidad, en varias  oportunidades, motivo por el cual acude a ambulatorio de localidad quien indica tratamiento médico y estudio ecosonografico que reporta dilatación de asas intestinales, persiste sintomático, 22/04/16 acude a este centro, es evaluado por el servicio de cirugía blanda y se decide su ingreso. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Obstrucción intestinal parcial: síndrome adherencial En vista de persistir clínica, es llevado a mesa operatoria donde se realiza laparotomía exploratoria supra, para e infraumbilical con los siguientes hallazgos: 2000cc de pus. Lesión grado IIA 30cm de asa fija, a 100cm de válvula ileocecal. Conducta: vaciado de secreción y apendicectomia apicobasal, colocación de 3 drenes, en ambas correderas parietocólicas y fondo de saco. En post operatorio se imposibilita destete de ventilador mecánico, se solicita valoración por UCI, quien valora y por disponibilidad de cupo se ingresa. Se recibe paciente en camilla de traslado, hemodinamicamente estable, respirando oxigeno ambiente, con SNG con gasto bilioso, sonda de Foley funcionante, orinas claras, sistema de dren en ambas correderas parietocólicas y fondo de saco con gasto hemático. Vía central. Se conecta a monitor cardiovascular que reporta: TA:113/72 mmHg FC:95LPM SATo2:98%  FR:19RPM''',
			
			"piel" : 	'''	Morena, normotérmica, llenado capilar < 3 segundos. ''',

			"cardiopulmonar":  ''' Tórax simétrico, expansible, ruidos respiratorios presentes, sin agregados respiratorios, ruidos cardíacos rítmicos, regulares, sin soplos ni galope ''',
			
			"abdomen": ''' plano, ruidos hidroaéreos presentes, blando, depresible, se evidencia apósito supra-para-infraumbilical limpio y seco con sistema de drenes, con gasto hemático ''',

			"neurologico": ''' consciente, Glasgow 15/15 ptos ''',
			"extremidades": '''simétricas, eutróficas, sin edema ''',

		}, 

		"diagnosticoIngresoUCI": [
						"Post operatorio inmediato de laparotomía exploratoria",
						"Peritonitis apendicular.",
						"Síndrome adherencial.",
						"Sepsis punto de partida abdominal",
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: mmHg	FC: lpm	FR:rpm SPO2: %''',
			
			"piel": ''' Morena, normotérmica, llenado capilar < 3 segundos.	''',
			
			"cardiopulmonar": '''Tórax simétrico, expansible, ruidos respiratorios presentes, sin agregados respiratorios , ruidos cardíacos rítmicos, regulares, sin soplos ni galope''',
			
			"abdomen": '''distendido, Ruidos hidroaéreos presentes, timpánico, doloroso a la palpación difuso''',
			
			"neurologico": '''conservado ''',

		}, 
		
	}, # 42

	{
		"nombre": "Luis Eduardo Berbesic Torres", 		
		"edad": "22",
		"sexo": "M",	
		"fechaNacimiento": datetime(1991,7,23), 		
		"lugarNacimiento": "Rubio - Edo Táchira", 		
		"ci": "19.541.245", 				
		"fechaIngresoHUAPA": datetime(2016,12,23), 		
		"fechaIngresoUCI":datetime(2016,12,23), 
		"resumenIngreso": '''Se trata de paciente masculino 22 años de edad, natural del Estado Táchira y procedente de la cocollar, sin antecedentes de enfermedad de importancia, el cual inicia enfermedad actual el día 23 de diciembre de 2013 en horas de la tarde cuando posterior a accidente automovilístico tipo volcamiento con impacto de vehículo en marcha sobre objeto contuso fijo (casa) presenta politraumatismos, dolor en región de pelvis y limitación funcional para la marcha y es trasladado a este centro de salud en donde evalúan e ingresan por el servicio de Cirugía con el diagnóstico de Politraumatizado: Traumatismo Craneoencefálico Leve y Fractura iliaca izquierda. Se mantiene en el área de emergencia bajo observación, signos vitales TA: 90/60mmHg FC: 70lpm FR : 17rpm, se asocia al cuadro hipotensión a pesar de recibir fluidoterapia,  posteriormente descenso en los controles de hemoglobina y signos de irritación peritoneal, por lo que es llevado a mesa operatoria en donde realizan laparotomía explorado evidenciándose hemoperitoneo de aproximadamente 2000cc en cavidad, con lesión grado V esplénica que ameritó esplenectomía y evacuación del mismo. Solicitan evaluación por UCI y en vista de disponer de cupo se ingresa. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente en regulares condiciones generales, conectado a ventilación mecánica a través de tubo endotraqueal, conectado a monitor cardíaco externo continuo., En vista de que el paciente amerita antibioticoterapia con Linezolid debido a Infección Respiratoria Baja asociada a Ventilación Mecánica y actualmente la institución no cuenta con este medicamento se agradece su colaboración.''',
			
			"piel" : 	'''Morena, normotérmica al tacto, llenado capilar >3 segundos''',

			"cardiopulmonar":  '''Tórax simétrico, normo expansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos, rítmicos, regulares,  sin soplos ni galope''',
			
			"abdomen": '''blando, plano, depresible, se evidencian apósitos que cubren herida de laparotomía infraumbilical con dren de látex en hipogastrio, ruidos hidroaéreos ausentes, no megalias.,''',

			"neurologico": '''Consciente, Glasgow: 10/15 pts, Respuesta Motora: 6pts, Respuesta Verbal:1pt, Apertura Ocular: 3pts''',

		}, 

		"diagnosticoIngresoUCI": [

								"Politraumatizado: traumatismo Toracoabdominal cerrado complicado con: Ruptura esplénica, Hemoperitoneo. Traumatismo craneoencefálico leve",
								"Postopratorio inmediato de Laparotomía exploradora y Esplenectomía",
								"Shock hipovolémico",
								"Estado PostRCP",
								"Trastorno hematológico: Anemia severa",
								"Trastorno Acido Base: Acidosis metabólica descompensada + hiperoxemia",

								],  
		
	}, # 43

	{
		"IdHistoria": "19-52-78", 
		"nombre": "Haide Josefina Benitez", 		
		"edad": "44",
		"sexo": "F",	
		"fechaNacimiento":datetime(1968,8,5),  		
		"lugarNacimiento": "Cumaná", 		
		"ci": "10.468.864", 		
		"dirección": "Brasil Sector III vereda 25 N 2 cerca del comedor popular.", 		
		"fechaIngresoHUAPA": datetime(2013,11,6),	
		"fechaIngresoUCI":datetime(2013,11,6),		
		"resumenIngreso": '''APP: DM tipo I tratada con Insulina humulin R 10 uds en la mañana y 5 en la noche. HTA tratada con Enalapril 10 mg OD. IRA por Nefropatía Diabética. Intervenciones: Esterilización quirúrgica. Transfusiones: No refieren. Alergias: No refieren. Se trata de paciente femenina de 44 años de edad natural y procedente de la localidad, con antecedentes de diabetes Mellitus desde los 13 años quien recibe tratamiento con Humulin R 10 uds en la mañana y 5 uds en la noche; Hipertensión Arterial hace 15 días recibe tratamiento con Enalapril 10 mg OD; IRA por nefropatía diabética. Quien inicia enfermedad actual el día miércoles 6/11/13 cuando comienza con aumento de volumen en miembros inferiores, vómitos, dificultad respiratoria que no tolera el decúbito y dolor precordial, motivo por el cual es llevada a ambulatorio de la localidad donde evalúan, colocan tratamiento (familiar no conoce) y en vista de no mejorar la paciente es referida a este centro donde es ingresada por servicio de medicina.''', 


		"examenFisicoIngresoUCI": {
			
			"piel" : 	'''normohídrica, afebril al tacto. ''',
			"TCS": '''infiltrado en ambos miembros inferiores, edema grado II''',

			"cardiopulmonar":  ''' tórax simétrico, expandible; ruidos respiratorios presentes, MV abolido en ambas bases pulmonares, sin agregados. Ruidos cardiacos rítmicos, Normofonéticos, taquicárdicos, sin soplos ni galope.''',
			"abdomen": ''' globuloso, no doloroso a la palpación, no megalias.  ''',

			"neurologico": ''' consciente, orientada en tres planos. ''',
		}, 

		"diagnosticoIngresoUCI": [

				"Emergencia Hipertensiva expresada en SCA IM con elevación de ST de cara Anterior.",
				"Insuficiencia Cardiaca.",
				"Derrame pleural bilateral",
				"Diabetes Mellitus tipo I ",
				"IRC reagudizada no oligurica",
				"Trast Hematológico: anemia moderada",
				"Trast Hidro electrolítico: hiprekalemia; hiponatremia",
				"Trast Metabólico: Hiperglicemia.",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Signos vitales: Fc: 138 lpm Fr: 26 rpm TA: 170/100 mmHg ''',
			"piel": '''humeda y elástica, llene capilar < 3 seg ''',
			"cardiopulmonar": '''tórax simétrico, expandible, ruidos respiratorios disminuidos en ambas bases pulmonares, se auscultan crepitantes bibasales. Ruidos cardiacos rítmicos, taquicardicos, sin soplo ni galope.	''',
			"abdomen": '''globuloso a expensa de panículo adiposo, no doloroso a la palpación, no megalias''',
			"neurologico": '''Paciente consciente orientada en tres planos.''',

		},  

		"diagnosticoIngresoHUAPA": [
								
			"Derrame pleural bilateral.",
			"Hipertensión Arterial descompensada",
			"Anasarca.",
			"Diabetes Mellitus descompensada",
			"Pericarditis AD.",
			{"resumen": ''' La paciente es evaluada hoy en revista médica por Dr. Romero quien en vista del estado de la paciente, solicita cupo en UCI, se realiza EKG evidenciando infarto d cara anterior con elevación  del segmento ST. Por todo lo anterior se decide ingresar  la paciente en nuestro servicio. Se recibe paciente en camilla de traslado recibiend oxígeno por mascarilla facial, es trasladada a cama UCI, se conecta a monitor cardiac continuo que reporta Fr: 29 rpm Fc: 128 lpm TA: 180/95 (116) mmHg SATO2: 99%; oxígen húmedo por mascarilla facial a 10 lts por min, recibiendo nitroglicerina 1 amp diluida e 250 cc Sol 0.9% VEV a razón de 10 cc/hora '''},

		], 
		
	}, # 44

	{
		"nombre": "Ruben Miguel Benitez ", 		
		"edad": "39",
		"sexo": "M",	
		"fechaNacimiento": datetime(1973,11,24),		
		"lugarNacimiento": "Cumana", 		 		
		"dirección": "Brasil barrio el manguito ", 		
		"fechaIngresoHUAPA": datetime(2013,10,19),  		
		"fechaIngresoUCI":datetime(2013,10,19),  		 
		"resumenIngreso": '''Se trata de paciente masculino de  39  años de edad natural  procedente de la localidad con antecedentes de cosumo de sustancias ilícitas . El paciente incia enfermedad actual el dia 12 -10-13  motivo por el cual es traido a este centro asistencial con movimientos tónico clónicos generalizados perdida de la conciencia relajación de esfínter anal y vesical posterior a ingestión de sustancias ilícitas y alcohol etílico es llevado y evaluado en ambulatorio de la localidad y posterior a colocación de diazepam es enviado a este centro donde es evaluado y se hospitaliza por servicio de medicina   Examen Físico:FR: 20x´ FC: 90x´ TA: 180/110.Piel: normotérmica, normoelástica, llenado capilar menor a 3 segundos.Cardiopulmonar: Tórax simétrico, expansible, ruidos respiratorios presentes, se auscultan roncos universales, ruidos cardíacos rítmicos regulares taquicárdicos, no soplos no galope.Abdomen: Globoso, blando, depresible, Ruidos Hidroaéreos presentes, no megalias.Neurológico: inconsciente, glasgow 11/15 ptos ( RM 5, RO 4, RV 2), pupilas hiporreactivas a la luz.''', 

		"diagnosticoIngresoUCI": [
				"Encefalopatía por drogas de abuso complicada con edema cerebral difuso",
				"IRB neumonía por broncoaspiración ",
				"TTNO HE hipocaliemia ",
				"TT AB alcalosis metabolica e hiperoxemia ",
								],  

		"diagnosticoIngresoHUAPA": [

		"Primoconvulsion del adulto", 
		"Hipertensión arterial en crisis", 
		"Broncoaspiración ",
		"Evc a descartar", 
		{"resumen":''' El paciente es evaluado por equipo UCI el dia 14 el cual se encuentra intubado debido a deterioro neurológico con un glasgow de 3 puntos conectado a pieza en T recibiendo oxigeno ghumedos a 8 lt por minuto con signos vitales FC 140 FR 29 TA 115 -70  SAT 74 % por lo que se solicita conectar a ventilación mecánica MA1 con los siguientes parámetros VC 560 FR 12 FL 50 FIO2 60 y se sugiere realizar TAC de cráneo la cual se realiza el dia 16 reportando edema encefálico a predominio de lóbulo occipital y hemisferios cerebelosos  manteniéndose con evaluación diaria por servicio de UCI hasta que por disposición de cupo se decide su ingreso .Examen físico de ingreso a U.C.I.Paciente en As.Ms.Cs.Gs. conectado por tubo endotraqueal a bolsa autoinsuflable con fuente de oxigeno, febril 38,5°C , hemodinamicamente estable se pasa de cama de  traslado a cama de U.C.I. signos vitales por monitor saturación de oxigeno 100%, T.A. 132/90 (148) mmHg. F.C.98 lpm.Cardiopulmonar: tórax, simétrico, hipoexpansibles, Rs.Rs. audibles, simetricos sin adventicios. Corazón: Rs.Cs.Rs.R. sin soplos ni frotes.Abdomen plano, Blando no doloroso a la palpación profunda.Neurológico: reflejo osteotendinosos patelar y bicipital II/IV. Glasgow 4/15   RM:2ptos RO 1ptos. RV 1pto limitado por tubo.'''}
		], 
		
	}, # 45

	{
		"IdHistoria": "33-16-04", 
		"nombre": "Raiza Mercedes Sanchez de Blondel", 		
		"edad": "44",
		"sexo": "F",	
		"fechaNacimiento": datetime(1969,1,8), 		
		"lugarNacimiento": "", 		
		"ci": "11.831.210", 		
		"dirección": "Cumanacoa, Calle Anias, Casa 113, Edo sucre.", 		
		"fechaIngresoHUAPA": datetime(2013,10,7),			
		"fechaIngresoUCI": datetime(2013,10,7),		
		"resumenIngreso": '''Paciente femenina de 44 años de edad, natural y procedente de Cumanacoa, con antecedente de Histerectomía hace aproximadamente 2 años, cuyo familiar refiere inicio de enfermedad actual el día 21/09/13 cuando de forma electiva la paciente es llevada a mesa operatoria para realización de colecistectomía laparoscópica, la cual en el transoperatorio debe ser convertida a colecistectomía abierta por presencia de múltiples adherencias que imposibilitan laparoscopia, es trasladada al piso de hospitalización y egresada el día 22/09/13. El mismo día del egreso comienza a presentar vómitos postpandriales en repetidas oportunidades y evacuaciones líquidas; el día 27/09/13 se anexa al cuadro distención abdominal, por lo que el día 28/09/13 consulta especialista de su localidad quien refiere a este centro donde es valorada por el servicio de cirugía blanda quien decide ingresar con el diagnóstico e POT de colecistectomía abierta complicada con colección intraabdominal; es llevada a mesa operatoria realizándosele laparotomía exploratoria con hallazgo de importante síndrome adherencial, colección interna de aproximadamente 3000cc entero-purulenta, lesión puntiforme en asa delgada (yeyuno); se le realiza evacuación de secreción, lavado de cavidad, cierre de lesión puntiforme con seda 2-0, lavado de cavidad y se dejan 2 drenes dirigidos a lecho de la lesión y fondo de saco, cierre por planos. Permanece en el piso de hospitalización de cirugía blanda donde comienza a presentar abundante gasto serohemático a través de drenes y contenido purulento, fétido a través de herida quirúrgica. El día de hoy 07/10/13 por presentar abundante salida de contenido hemático y coágulos a través de herida quirúrgica e hipotensión arterial es llevada nuevamente de emergencia a mesa operatoria, realizándosele relaparotomía exploratoria con hallazgos de 500cc de contenido entérico, síndrome adherencial interesa, absceso interesa con 50cc de contenido purulento, con 2 orificios fistulosos puntiformes en asa delgada (yeyuno), se procedió a evacuación de secreción entérica, lavado de cavidad, exteriorización de ambos orificios fistulosos con sonda Foley #12 y cierre por puntos de tensión; la paciente se mantuvo durante todo el transoperatorio con cifras tensionales bajas y en vista de mal estado general solicitan valoración por UCI. Se comunica caso a Dra. Begglia Roa (Intensivista de Guardia) quien por estado general de la paciente y disponibilidad de cupo autoriza ingreso a UCI y dicta ordenes médicas.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, en condiciones clínicas de cuidado, hemodinámicamente estable, intubada y conectada a ventilador de traslado, se conecta a ventilación mecánica EVITA 4 modo IPPV, Vc: 480, FR: 12, FiO2: 100, Fl. 50, Ti: 0,90, PEEP:0 y a monitor cardíaco externo que reporta los siguientes signos vitales: TA: 84/33(48) mmHg FC: 93 lpm FR: 12 rpm SPO2:100 % Recibiendo 1 unidad de concentrado globular por VVC y se indican 500cc de solución fisiológica 0,9% con lo que mejoran cifras de tensión a 99/56(79).''',
			
			"piel" : 	'''	Morena, hipotérmica al tacto, llenado capilar < 3 segundos. ''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, crepitantes dispersos a predominio derecho, ruidos cardíacos rítmicos, regulares, normofonéticos,  sin soplos ni galope. 	''',
			"abdomen": ''' cubierto con apósitos secos, no fétido, se evidencian salida de 4 drenes conectados a bolsa recolectora con escaso contenido serohemático.''',

			"neurologico": ''' consciente, pupilas isocóricas, normorreactivas a la luz, con períodos de somnolencia, glasgow 10/15pts (RM: 6pts, RO: 3pts, RV: 1pto limitado por TET). ''',

		}, 

		"diagnosticoIngresoUCI": [
									"POI DE RELAPAROTOMIA EXPLORATORIA POR COLECCIÓN INTRAABDOMINAL POR FISTULA ENTERICA",
									"POT DE LAPAROTOMIA EXPLORATORIA POR COLECCIÓN INTRAABDOMINAL POR PERFORACION DE VISCERA HUECA",
									"POT DE COLECISTECTOMIA ABIERTA ", 
									"TRASTORNO HEMATOLOGICO",
									"ANEMIA MODERADA",
									"TROMBOCITOPENIA",
									"TRASTORNO HIDROELECTROLITICO",
									"HIPOKALEMIA",
									"TRASTORNO ACIDO-BASE",
									"ALCALOSIS RESPIRATORIA DESCOMPENSADA MÁS HIPEROXEMIA",
									{"resumen": '''Paciente  que se  recibe en regulares condiciones evoluciona satisfactoriamente es extubada sin complicaciones tolerando oxigeno húmedo por bigote nasal a arazon de 3 lt por minuto continua antibioticoterapia con imipenem y metronidazol  con globulos blancos dentro de limites adecuados ,gastos escasos por drenes serohemático herida quirúrgica sin signos de infección. '''},
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 124/83(68) mmHg FC: 93 lpm FR: 12 rpm SPO2:100''',
			"piel": ''' Morena, hipotérmica al tacto, llenado capilar < 3 segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, crepitantes dispersos a predominio derecho, ruidos cardíacos rítmicos, regulares, normofonéticos,  sin soplos ni galope.  ''',
			"abdomen": '''cubierto con apósitos secos, no fétido, se evidencian salida de 4 drenes conectados a bolsa recolectora con escaso contenido serohemático. ''',
			"neurologico": '''consciente, pupilas isocóricas, normorreactivas a la luz, glasgow 15/15pts  ''',

		},  


		"diagnosticoEgresoHUAPA": [
						"POI DE RELAPAROTOMIA EXPLORATORIA POR COLECCIÓN INTRAABDOMINAL POR FISTULA ENTERICA",
						"POT DE LAPAROTOMIA EXPLORATORIA POR COLECCIÓN INTRAABDOMINAL POR PERFORACION DE VISCERA HUECA",
						"POT DE COLECISTECTOMIA ABIERTA  ",
						"TRASTORNO HEMATOLOGICO",
						"ANEMIA MODERADAB ",
		], 
		
	}, # 46

	{
		"IdHistoria": "20-19-14", 
		"nombre": "Omilsa Rojas Parejo Gonzalez", 		
		"edad": "48",
		"sexo": "F",	
		"fechaNacimiento": datetime(1965,8,25),			
		"ci": "8.643.977", 		
		"dirección": "Urbanizacion cristobal colon n270 Cumaná, Edo sucre ", 		
		"fechaIngresoHUAPA": datetime(2013,10,26), 		
		"fechaIngresoUCI": datetime(2013,12,5),			
		"resumenIngreso": '''Paciente que se realiza intervención quirúrgica el dia 26-10-13 gastrectomia vertical con manga sin complicaciones, luego de 48 horas de post operatorio comienza a presentar dificultad respiratoria dolor torácico indicándose rx torax donde se aprecia opacidad en hemitorax derecho compatible con derrame pleural  por lo que se  realiza toracocentesis con 200 cc contenido seropurulento por lo que se traslada a quirófano para la cplocacion de tubo de drenaje torácico 36 f drenándose 1000 cc de contenido purulento fetido se toma muestra para cultivo gran cito químico  manteniéndose hospitalizada en área de recuperación quirúrgica con ATB ciprofloxacina meropenem y aelox  siendo evaluada diariamente por equipo de UCI ,dichos cultivos dieron como resultados estreptococo anginosus sensible a clindamicina  y enterococo especies sensible a linezolid  indicándose antibioticoterapia con cefoperazona sulbactam y tygacil anexándose al siguiente dia por evaluación con infectologia zyvox y piperacilina tazobactam,para el dia 18 -11 se omite zyvox y se coloca clindamicina por cultivo,manteniendo gasto por tubo de tórax sin burbujeo ,siendo trasladada a piso 7 manteniendose recibiendo oxigeno por mascarilla facial a razón de 10 lt por minuto  con antibioticoterapia manteniendo evolución favorable  y gasto sero purulento escaso ,aparentemente con mejoría del cuadro por lo que se egresa el día 21 de noviembre ,mantiene en su casa dolor torácico disnea a medianos esfuerzos por lo que es evaluada por cirugía de torax en vista de persistencia de imagen compatible con con empiema tabicado se planifica para intervención quirúrgica .Se realiza el dia de hoy (5-12-13) toracotomía posterolateral derecha donde se encontró como hallazgos 1000 c/c de contenido purulento  con múltiples cámaras a nivel pleural múltiples adherencias y pinzamiento del hemidiafragma derecho ,se evacua contenido purulento tomándose muestra para cultivos decoticacion pleural lavado de cavidad ,evacuación de cámaras pleurales ,y se decide traslado a terapia intensiva para su seguimiento  ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, en regulares condiciones generales, hemodinámicamente estable, intubada y conectada a ventilador de traslado, se conecta a monitor cardíaco externo que reporta los siguientes signos vitales:TA: 99/53(65) mmHg FC 70 lpm FR:14 rpm SPO2:100 %	                  ''',
			
			"piel" : 	'''	blanca, normotérmica al tacto, llenado capilar < 3 segundos ''',

			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos rítmicos, regulares, hipofonéticos, sin soplos ni galope. Presencia de tubo de drenaje torácico derecho anterior y posterior con burbujeo positivo ascilante y gasto sero hemático de 20 cc 		''',
			"abdomen": ''' globoso , blando, depresible, ruidos hidroaéreos presentes, no megálico.''',

			"neurologico": ''' Bajo efectos de anestesia general inhalatoria por lo que no es evaluable el estado de consciencia, pupilas isocoricas, miótica  hipo reactivas.''',
		
		}, 

		"diagnosticoIngresoUCI": [
									"POI TORACOTOMÍA POSTEROLATERAL DERECHA POR",
									"EMPIEMA PLEURAL TABICADO DERECHO ",
									"POT CIRUGÍA BARIATICA TIPO MANGA GÁSTRICA ",
									"OBESIDAD MÓRBIDA", 
									"DIABETES MELLITUS TIPO 2",
									"SX METABOLICO ",
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se trata de paciente femenino de 48 años de edad, natural y procedente de la localidad, con antecedentes de Obesidad Morbida y diabetes mellitus tipo 2,Sx Metabolico la cual inicia enfermedad actual el dia 20 de octubre cuando es hospitalizada por aumento de peso corporal para la realización de cirugía bariatica tipo  manga gástrica  Al momento del ingreso TA: 122/83  mmHg FC:99 lpm FR:14 rpm SPO2:100 %''',
			"piel": ''' Blanca , normotérmica al tacto, llenado capilar < 3 segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, normo expansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos rítmicos, regulares, hipofonéticos,  sin soplos ni galope. ''',
			"abdomen": '''globoso , blando, depresible, ruidos hidroaéreos presentes, no megálico. se encuentra consciente, pupilas isocoricas con  respuesta a la luz, glasgow 15/15 ''',
		},  
		
	}, #47

	{
		"IdHistoria": "51-27-85", 
		"nombre": "José Camino", 		
		"edad": "65",
		"sexo": "M",	
		"fechaNacimiento": datetime(1977,10,8),	
		"lugarNacimiento": "Cumaná estado Sucre", 		
		"ci": "2.928.751", 		
		"dirección": "Parcelamiento Miranda, sector C1, calle El palmar, Qta. Edural", 		
		"fechaIngresoHUAPA": datetime(2013,11,12),		
		"fechaIngresoUCI": datetime(2013,11,12),		
		
		"resumenIngreso": '''Paciente masculino de 65 años de edad, con antecedente de HTA diagnosticada desde hace 12 años aproximadamente, en tratamiento regular con losartan 50mg OD y bisoprolol/HCT 5/12,5mg OD, quien refiere inicio de enfermedad actual el dia de hoy 12/11/13 en horas de la mañana, cuando presenta de forma súbita mareo, diaforesis y desvanecimiento sin llegar a pérdida de consciencia, motivo por el cual es trasladado al área de emergencia de este centro asistencial donde es evaluado y se decide su ingreso a cargo de medicina interna. Se conecta a monitor cardíaco continuo donde se evidencia TA: 80/50(60) mmHg, FC: 48 lpm y FR: 18 rpm, se le administran 500cc de solución 0,45% y 500cc de solución 0,9% con mejoría de tensión arterial a 130/72(92) mmHg. Es valorado por Dra. Baptista (Cardiólogo) quien sugiere omitir β-bloqueante para posterior colocación de Holter cardíaca en 3 días, solicitar electrolitos sericos y perfil isquémico,  marcadores tumorales para descartar NEO oculto y TAC cerebral para descartar EVC transitorio. Es evaluado además por servicio de UCI y en vista de cuadro clínico y disponibilidad de cupo, por autorización de Dr. Guaimare, Dra.  Cortesía y Dra. Roa, se decide su ingreso en UCI.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, tolerando aire ambiente, estable hemodinamicamente, se pasa a cama de UCI y se conecta a monitor cardíaco continuo que reporta TA: 120/61(79) mmHg, FC: 56 lpm, FR: 24 rpm, SatO2: 98%.''',
			
			"piel" : 	'''	morena, normotérmica al tacto, llenado capilar < 3 segundos''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares sin agregados. Ruidos cardíacos rítmicos y regulares, bradicardicos, sin soplo ni galope.''',
			"abdomen": ''' globoso a expensas de panículo adiposo, ruidos hidroaereos presentes, blando, depresible, no doloroso a la palpación, no megalico.''',

			"neurologico": ''' consciente, orientado en los tres planos, lenguaje coherente, pupilas isocóricas normorreactivas a la luz, reflejos y fuerza muscular conservados.''',
		

		}, 

		"diagnosticoIngresoUCI": ["SINCOPE","HTA CRONICA CONTROLADA"], 
		
	}, # 48


	{
		"nombre": "Juan Isidro Soria", 		
		"edad": "68",
		"sexo": "M",	
		"fechaNacimiento": datetime(1945,4,4),		
		"lugarNacimiento": "Argentina.", 		
		"ci": "24.716.949", 		
		"dirección": "Banco Obrero s/n Guiria.", 		
		"fechaIngresoHUAPA": datetime(2013,4,4),
		"fechaIngresoUCI": datetime(2013,4,4),
		"antecedentes": ''' APP: PTI. Hipertensión Arterial controlada con Adalat Oros, Candesartan. Hab. Tóxicos: Ex fumador (hace 15 años). Intervenciones: No refieren. Transfusiones: No refieren. Alergias: No refieren''',
		
		"resumenIngreso": '''Se trata de paciente masculino de 68 años de edad con antecedentes de ser ex fumador, PTI,HTA controlado con adalat oros y candesartan,quien inicia enfermedad actual  14/10/2013 cuando presenta astenia, marcado tinte ictérico en piel y mucosas y edema en ambos miembrosinferiores, motivo por el cual acude a hospital de Carúpano donde evalúan e ingresan  donde permanece hospitalizado por 10 días y realizancolangioresonancia que reporta dilatación de vías biliares intra y extra hepáticas con terminación abrupta del colédoco sugestiva de LOE deampolla de Vater. Por tal motivo es referido a este centro, donde es hospitalizado por servicio de cirugía. ''', 


		"examenFisicoIngresoUCI": {
			
			"piel" : 	'''deshidratada, tinte ictérico de piel y mucosas.''',

			"cardiopulmonar":  ''' tórax simétrico expandible, ruidos cardiacos rítmicos normo fonéticos, sin soplos ni galope. Ruidos respiratorios presentes, murmullo vesicular conservado, no se auscultan estertores.''',
			
			"abdomen": ''' plano, presencia de apósito estéril limpio y sin secreción, presencia de drenes en flanco izquierdo dirigidos a área peripancreatica con succión, dren en hipogastrio dirigido a fondo de saco y yeyunostomia, doloroso, no megalias.   ''',

			"neurologico": ''' consciente orientado, pupilas isocóricas reactivas a la luz.''',

		}, 

		"diagnosticoIngresoUCI": [
				"Sépsis punto de partida abdominal",
				"POI de laparotomía exploradora",
				"POT de CEPRE",
				"Hipertensión arterial.",
				"Trastorno hidro electrolítico: hipokalemia.",

									
								],  

		"examenFisicoIngresoHUAPA": {
		
			"piel": ''' morena, con tinte ictérico de piel y mucosas.''',
			
			"cardiopulmonar": '''tórax simétrico, expandible, ruidos respiratorios presentes murmullo vesicular conservado, sin agregados. Ruidos respiratorios cardiacos rítmicos, normofonéticos, sin soplos ni galope.''',
			
			"abdomen": '''plano, doloroso a la palpación en hipocondrio derecho. ''',
		
			"neurologico": '''consciente orientado en tres planos, lenguaje claro coherente, pupilas isocóricas normo reactivas a la luz  ''',

		},  

		"diagnosticoIngresoHUAPA": [
								"LOE de ampolla de Vater.",
								"PTI sin signos de sangrado",
								"Colecistitis alitiasica",
								"Hipertensión arterial.",
								{"resumen": ''' El paciente permanece en servicio de cirugía con elevación de bilirrubinas, el día 31/10/13 es llevado a mesa operatoria para realizar CEPRE la cual tiene que interrumpirse por no localizar la papila duodenal. Posteriormente el día 6/11/13 es llevado nuevamente a quirófano donde se realiza CPRE, realizando esfinterotomia amplia y colocación de STENT con drenaje abundante de bilis. El paciente es llevado a hospitalización donde comienza a presentar leucocitosis, dolor abdominal, distensión y aumento de volumen en hemiabdomen izquierdo; se le realiza ecosonograma, el cual no reporta colección intraabdominal. El paciente continúa con distensión abdominal se le realiza TAC de abdomen que reporta estómago de retención, debido al cuadro del paciente se decide llevar el día de hoy a mesa operatoria,  se realiza laparotomía exploradora con hallazgo de 5500 cc de contenido hematobiliosoy purulento, multiples adherencias laxas, abundante fibrina, se palpa TU a nivel de cabeza de páncreas. Se drena contenido, lavado de cavidad con 8000 cc de solución 0.9%, se realiza yeyunostomia y se dejan drenes aspirativos. El paciente se recupera sin dificultad, es llevado a hospitalización. En horas de la tarde se solicita valoración por UCI y evaluo paciente en cama, que presenta hipotensón, taquicardia, con signos de deshidratación. Se comunica caso a Dra Roa quien autoriza ingreso del paciente a UCI y dicta órdenes médicas. Se recibe paciente en camilla de traslado, tolerando aire ambiente, se traslada a cama UCI y se conecta a monitor cardiaco que reporta FR: 30 rpm FC: 69 lpm TA 109/55 (70) mmHg SATO2: 100%, se coloca oxigeno por mascara facial a 10 lts.''' }


		], 
		
	}, # 49

	{
		"IdHistoria": "50-93-95", 
		"nombre": "Angel Eutinio Fuentes", 		
		"edad": "52",
		"sexo": "M",	
		"fechaNacimiento": datetime(1961,1,26),			
		"dirección": "Calle Rendón, casa S/N. Cumana Edo sucre ", 		
		"fechaIngresoHUAPA": datetime(2013,7,24), 		
		"fechaIngresoUCI": datetime(2013,7,24),		 
		"resumenIngreso": '''Se trata de paciente masculino de 52 años de edad, natural y procedente de la localidad, con antecedentes de HTA sistémica de larga data en tratamiento irregular con Atacand plus 16/12,5 mg, Tensomax LP 30mg, Coraspirina 81mg y Atorvastatina, cuyos familiares refieren inicio de enfermedad actual el día 21/07/2013 cuando en horas de la tarde comienza a presentar malestar general, intranquilidad y hemiparesia derecha, motivo por el cual es llevado a ambulatorio cercano donde evidencian cifras tensionales elevadas y se anexa al cuadro clínico disartria, se le administra captopril 25mg VSL y es referido a este centro asistencial donde es valorado por el servicio de medicina interna y se ingresa con el diagnóstico de Crisis Hipertensiva expresada en EVC en evolución. Permanece en el área de choque. El día 23/07/2013 se le realiza TAC cerebral que reporta hematoma intraparenquimatoso agudo en región parietal izquierda, con edema periférico asociado y borramiento de surcos adyacentes con compresión del sistema ventricular y desplazamiento a la derecha de la línea media de 5mm; cambios involutivos corticales y centrales no acordes a lo esperado para la edad del paciente.Es valorado por Dr. Acevedo (Neurocirujano de guardia) quien decide resolución quirúrgica. El día 24/07/2013 es llevado a mesa operatoria realizándosele craneotomía para evacuación de hematoma intraparenquimatoso de aproximadamente 55cc. Se solicita valoración y cupo en UCI para cuidados postoperatorios. En vista de contar con cupo, Dr. Alpino (Intensivista de Guardia) autoriza su ingreso a UCI y dicta órdenes médicas. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, en regulares condiciones generales, hemodinámicamente estable, intubado y conectado a ventilador de traslado, se conecta a monitor cardíaco externo que reporta los siguientes signos vitales TA: 122/76(86) mmHg FC: 82 lpm	FR:30rpm SPO2: 98%''',
			
			"piel" : 	'''	Morena, normotérmica al tacto, turgor conservado, llenado capilar < 3 segundos. ''',
			"cabeza": ''' herida quirúrgica en región parieto-occipital izquierda cubierta por apósitos con escasa secreción serohemática ''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares sin agregados, ruidos cardíacos rítmicos y regulares, normofonéticos,  sin soplos ni galope.  ''',
			"abdomen": ''' globoso a expensas de panículo adiposo, ruidos hidroaéreos presentes, blando,  depresible, no impresiona doloroso a la palpación, no megálico.''',

			"neurologico": '''incosciente, pupilas isocoricas, con tendencia a la miosis y reacción lenta a la luz, glasgow no evaluable por efectos de sedación farmacológica.''',

		}, 

		"diagnosticoIngresoUCI": [

					"POI DE CRANEOSTOMIA PARA DRENAJE DE HEMATOMA INTRAPARENQUIMATOSO PARIETOOCCIPITAL IZQUIERDO",  
					"EMERGENCIA HIPERTENSIVA EXPRESADA EN EVC HEMORRAGICO",
					"HTA SISTEMICA ",
					"ACIDOSIS METABOLICA COMPENSADA + HIPEROXEMIA",

									
								],  
	}, # 50

	{
		
		"nombre": "Monica de la Rosa", 		
		"edad": "53",
		"sexo": "F",	
		"fechaNacimiento": datetime(1960,11,20),				
		"ci": "5.703.463", 		
		"dirección": "A venida carupano Caiguire , Edo sucre. ", 		
		"fechaIngresoHUAPA":  datetime(2013,12,13),		
		"fechaIngresoUCI": datetime(2013,12,13), 		
		"resumenIngreso": '''Paciente femenina de 53 años de edad, natural y procedente de la localidad  , con antecedente de DM tipo 2 controlada con glibenclamida y glucofage y HTA no controlada   ,los familiares  refieren inicio de enfermedad actual el día  9/ 12 / 13  cuando comienza con cuadro respiratorio dado por rinorrea serosa tos seca  acompañado de otalgia bilateral acompañada de cefalea de fuerte intensidad  por lo cual acude a ambulatorio de la localidad donde comenzó a presentar deterioro neurológico caracterizado por disartria desviación de rasgos faciales y disminución de fuerza muscular izquierda y perdida del conocimiento por lo cual se refiere a centro clínico  y evaluada por internista quien en vista de deterioro neurológico llama intensivista de guardia quien decide su ingreso.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, en condiciones clínicas criticas , hemodinámicamente inestable, intubada y recibiendo oxigeno con bolsa autoinsuflable  no conectada a ventilador de traslado,ni a monitor cardiaco  se conecta a ventilación mecánica EVITA 4 modo IPPV, Vc: 600, FR: 12, FiO2: 100, Fl. 50, Ti: 0,90, PEEP:0 y a monitor cardíaco externo que reporta los siguientes signos vitales: TA: 45/33(48) mmHg FC: 21 lpm	FR: 12 rpm SPO2:% Se evidencia asistolia se procedea realizar RCP básica y avanzada logrando que la paciente salga a ritmo sinusal con 2 ampollas de atropina y adrenalina ,posteriormente se  observa fibrilación ventricular con inestabilidad hemodinámica por lo que se procede a desfibrilar con 200 j lográndose ritmo sinusal con fc 56 lpm  fr 12 rpn conectada a VM sat o2 99 % y TA DE 124 –78 MMHG CON VASOACTIVOS ''',
			
			"piel" : 	'''Morena, hipotérmica al tacto, llenado capilar < 3 segundos. ''',

			"cardiopulmonar":  '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, roncus dispersos , ruidos cardíacos arítmicos, irregulares, normofonéticos,  sin soplos ni galope.''',
			
			"abdomen": '''globoso blando depresible no impresiona dolorosos no magalias''',

			"neurologico": '''inconsciente, coma pupilas aniisocóricas,midriasis izquierda  no reactivas a la luz, , glasgow 3/15pts (RM: 1pts, RO: 1pts, RV: 1pto). Reflejo corneal ausente . ''',
		}, 

		"diagnosticoIngresoUCI": [

								"NEUROINFECCION MENINGOENCEFALITIS BACTERIANA", 
								"HEMORRAGIA SUBARACNOIDEA BILATERAL",
								"ESTADO POST RCP",
								"DIABETES MELLITUS TIPO 2 ",
								"HTA SISTEMICA", 
								"TTNO ACIDO BASICO ACIDOSIS METABOLICA DESCOMPENSADA CON ALCALOSIS RESPIRATORIA", 

									
								], 
		"diagnosticoIngresoPrivado": [

				"NEUROINFECCION : MENINGITIS AGUDA PARCIALMENTE TRATADA CON EVOLUCION TORPIDA ",
				"DIABETES MELLITUS TIPO 2", 
				"FARVLENTA", 
				"HTA SISTEMICA ",
				{"resumen":''' Paciente que  por no disponibilidad de recursos se decide trasladoa acentro hospitalario.'''}


		],

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' 	Por tal motivo se procede a realizar intubación endotraqueal con tubo endotraqueal  8 f sin complicaciones y es conectada a ventilación mecánica NEWPORT parámetros no descritos  se realiza TAC de cráneo el dia 10 /12/13  que reporta edema cerebral severo  , se indica ATB con cefotaxima y vancomicina  en el contexto de meningoencefalitis además de manitol ,se realiza PL el cual reporta aspecto ligeramente turbio ph alcalino hties 8 -10 por campo  leu 12 -15 por campo células 1300 con 80% seg glucosa 32 mgdl proteínas 585 grdl con observación de cocos gran positivos en pares ,posteriormente a las 24 horas comienza con inestabilidad hemodinámica y bradicardia y es tratada con Vasoactivos levophed y dopamina ,para el dia 12 de diciembre se mantiene anurica gasto urinario de 0,12 cckg min ,se realiza una segunda TAC de cráneo donde se informa edema cerebral severo y hemorragia subaracnoidea bilateral para este momento con Glasgow de 3/ 15 puntos pupilas anisocoricas midriasis izquierda con reflejo corneal ausente ''',
			
			"piel": ''' blanca , hipotérmica al tacto, llenado capilar < 3 segundos. Panículo adiposo aumentado.''',

			"cardiopulmonar": '''Tórax simétrico, hipo expansible, ruidos respiratorios presentes en ambos campos pulmonares, roncus bilaterales, ruidos cardíacos rítmicos, regulares, normofonéticos,  sin soplos ni galope.''',
			
			"abdomen": '''blando globoso depresible no doloroso palpación superficial ni profunda no megalias.''',
		
			"neurologico": '''inconsciente, pupilas aniisocóricas izquierda con midriasis , no reactivas a la luz, , glasgow 6/15pts (RM: 4pts, RO: 1pts, RV: 1pto). ''',

		},  

		
	}, # 51


	{
		"nombre": "Mata Acosta Carmen Teresa", 		
		"edad": "24",
		"sexo": "F",	
		"fechaNacimiento": datetime(1989, 3, 12), 		
		"lugarNacimiento": "Cariaco, Estado Sucre.", 		
		"ci": "19.330.459", 		
		"dirección": "Maracay, Estado Aragua", 		
		"fechaIngresoHUAPA":  datetime(2013, 11, 2), 		
		"fechaIngresoUCI": datetime(2013, 11, 2), 		
		"antecedentes": '''ALERGIA AL IODO. Asma Bronquial y Litiasis Renal.''', 
		"resumenIngreso": ''' Se trata de paciente femenina de 24 años de edad, con antecedentes de cefalea desde la infancia, en tratamiento irregular y no específico, cuya madre refiere inicio de enfermedad actual hace 15 dias aproximadamente cuando presenta rigidez de nuca motivos por los cuales es llevada a Especialista (Traumatólogo) quien indica tratamiento ambulatorio y egresa, el día jueves 31/10/2013 presenta cefalea de fuerte intensidad en región bitemporal, vómitos en múltiples oportunidades, posteriormente movimientos tónicos generalizados, desviación de la mirada y relajación de esfínter vesical, motivos por los cuales es llevada a ambulatorio de la localidad donde colocan tratamiento no especificado y trasladan a centro privado en esta ciudad, donde ingresa en el Área de Hospitalización a cargo del Servicio de Medicina Interna con el diagnóstico de: 1) Hemorragia Subaracnoidea a descartar, 2) Síndrome Convulsivo. El día 01/11/2013 se le realiza Tomografía de Cráneo que reporta: Hallazgos sugestivos de Hemorragia Subaracnoidea asociada a colección hemática en Valle Silviano derecho por probable ruptura de aneurisma en la Arteria Cerebral Media derecha. Borramiento asociado de surcos regionales adyacentes y compresión del sistema ventricular derecho. El día 02/11/2013 la paciente presenta movimientos tónico-clonico generalizados, durante media hora, se le coloca tratamiento, al examen físico se evidencia paciente inconsciente, pupilas midriáticas, Glasgow: 7/15pts, Respuesta Motora: 5pts, Respuesta Verbal: 1pt, Apertura Ocular:1pt. En vista de escasos recursos deciden trasladar a este centro hospitalario. Es trasladada el día 02/11/2013 donde se ingresa a cargo de Medicina Interna con el diagnóstico de: 1) Hemorragia Subaracnoidea, 2) Síndrome Convulsivo. En vista de condiciones clínicas de la paciente solicitan valoración por Servicio de UCI. Se acude a valorar paciente evidenciándose deterioro neurológico caracterizado por Escala de Glasgow: 5/15pts, Respuesta Motora: 3pts, Respuesta Verbal: 1pt, Apertura Ocular: 1pts, pupilas midriáticas sin respuesta a la luz por lo que se decide realizar intubación endotraqueal con tubo número 6,5 en un intento, sin complicaciones, se conecta a T de Ayres. Se plantea caso a Especialista de Guardia (Dra. Cortesía) y en vista de disponibilidad de cupo se decide su ingreso.''', 


		"examenFisicoIngresoHUAPA": {

			"resumen": ''' 1) Hemorragia Subaracnoidea2) Síndrome Convulsivo.Se traslada paciente a Servicio de UCI, recibiendo oxígeno húmedo por ambú, se conecta a ventilación mecánica, se le realiza cateterización de Vía Venosa Central con Catéter número 7,5 french, bilumen, se conecta a monitor cardíaco externo, que reporta:TA: 118/67mmHg FC: 89lpm FR: 20rpm SPO2: 100%''',
			
			"piel" : 	'''	Morena, normotérmica, turgor conservado, llenado capilar < 3 segundos, se evidencia pálidez leve cutáneo-mucosa.''',

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes, no se auscultan agregados, ruidos cardíacos rítmicos, regulares, no ausculto soplos.''',
			
			"abdomen": ''' plano, blando, depresible, no doloroso a palpación, ruidos hidroáreos presentes. ''',

			"neurologico": ''' Inconsciente, Glasgow: 5/15 pts, Respuesta Motora: 3pts, Respuesta Verbal: 1pt, Apertura Ocular: 1pt, Pupilas Midriáticas sin respuesta a la luz. ''',

		}, 

		"diagnosticoIngresoUCI": [

						"Enfermedad Cerebrovascular",
						"Trastorno Hematológico: Anemia Leve.",
						"Trastorno Hidroelectrolítico: Hiponatremia",
						"Trastorno Acido/Base: Acidosis Metabólica Compensada con Alcalosis Respiratorio",

									
								],  

		"examenFisicoIngresoUCI": {
			"resumen": ''' Paciente en malas condiciones generales, hemodinámicamente estable, ventilando espontáneamente, recibiendo oxígeno húmedo por bigote nasal a 3 litros por minuto, conectada a monitor cardíaco externo que reporta: TA: 115/82mmHg FC: 80lpm FR: 13rpm''',
			
			"piel": '''Morena, normotérmica, turgor conservado, llenado capilar < 3 segundos, se evidencia pálidez leve cutáneo-mucosa.''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes, no se auscultan agregados, ruidos cardíacos rítmicos, regulares, no ausculto soplos.	''',
			"abdomen": '''plano, blando, depresible, no doloroso a palpación, ruidos hidroáreos presentes.''',
			
			"neurologico": '''Inconsciente, Glasgow: 5/15 pts, Respuesta Motora: 3pts, Respuesta Verbal: 1pt, Apertura Ocular:1pt, Pupilas Midriáticas sin respuesta a la luz ''',

		},  
		
	}, # 52

	{
		"nombre": "Elena Valdez", 		
		"edad": "32",
		"sexo": "F",	
		"fechaNacimiento": datetime(1981,7, 17),	
		"lugarNacimiento": "Cariaco", 		
		"ci": "17.243.589", 		
		"dirección": "Quebrada de piedra de Cariaco, Santa Cruz Municipio Rivero.", 		
		"fechaIngresoHUAPA": "", 		
		"fechaIngresoUCI":"", 		
		"resumenIngreso": '''Se trata de paciente femenina de 32 años de edad natural de Cariaco y procedente de Carúpano, con antecedentes de IV gesta, II A y I C. Inicia enfermedad actual el día 17 de diciembre de 2013, cuando presenta cefalea y epigastralgia, siendo llevada a ambulatorio de la localidad, donde evalúan y evidencian cifras de tensión arterial elevadas que no precisan y refieren a el Hospital Domingo Luciani de Carúpano, durante su traslado la paciente presenta movimientos tónico clónicos generalizados en 3 oportunidades, con posterior pérdida del conocimiento e ingresa en malas condiciones, con el diagnóstico de Eclapmsia; le realizan Cesárea segmentárea obteniéndose RNPT/AEG masculino P: 2500gr T 45cm, durante acto quirúrgico la paciente presenta episodio convulsivo, indican  epamin y sulfato de magnesio . El día 18/12/13 en horas de la madrugada presenta depresión respiratoria ameritando intubación endotraqueal y ventilación mecánica;  en vista de no disponer de cupo en la UCI de dicho centro de salud, se decide trasladar a este centro e ingresa al área de cuidados intermedios de sala de partos en muy malas condiciones, TA 155/90mmHg FC: 100lpm Sat: 54%, FR 20rpm, inconsciente, palidez cutánea mucosa acentuada, cardiopulmonar: tórax simétrico, hipo expansible Rs Rs Ps abolidos en HT izquierdo, Rs Cs Rs  taquicárdicos  S/S S/G, Neurológico: Glasgow: 3/15 ptos.  Solicitan evaluación por el servicio de terapia intensiva y se ingresa por disponibilidad de cupo y por orden de Dr. Carlos Guaimares Especialista de Guardia.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe  paciente en camilla de traslado con intubación endotraqueal con apoyo de ambú y oxigeno a 10 lts por min, se traslada  a cama UCI y se conecta monitor cardiaco continuo que reporta signos vitales: FC:94  lpm   FR:10 rpm  TA158/105mmHg  (124)mmHg SATO2: 87%. ''',
			
			"piel" : 	'''morena, normotérmica, hidratada, llenado capilar <3segundos. ''',

			"cardiopulmonar":  '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes y abolidos en HT izquierdo. Ruidos cardíacos rítmicos, regulares, taquicárdicos, no se auscultan soplos. Impresiona tubo selectivo por lo que se retiran 2 cm, posteriormente se auscultan ruidos respiratorios simétricos, con roncus dispersos.''',
			"abdomen": ''' Globoso, blando, presencia de apósito estéril limpio y seco en hipogastrio que cubren herida de cesárea, depresible, no impresiona doloroso a la palpación, útero tónico infraumbilical, ruidos hidroaéreos ausentes. ''',

			"neurologico": ''' Inconsciente, pupilas isocóricas hiporeactivas a la luz, glasgow RO: 1pto, RV: 1pto, RM: 4 ptos 6/15 puntos, arreflexica.''',

		}, 

		"diagnosticoIngresoUCI": [
									"Postoperatorio mediato de cesárea segmentárea por Eclapmsia.",
									"Síndrome de Hellp.",

								],  

	},# 53

	{
		"nombre": "Darwin José Suarez Fuentes", 		
		"edad": "30",
		"sexo": "M",	
		"fechaNacimiento": 	datetime(1983,7,4),
		"lugarNacimiento": "Cumaná estado Sucre", 		
		"ci": "17.445.453", 		
		"dirección": "Vía Cumanacoa, sector Chirigua, casa S/N.", 		
		"fechaIngresoHUAPA": datetime(2013,11,13),		
		"fechaIngresoUCI":	datetime(2013,11,13),	
	
		"resumenIngreso": '''Paciente masculino de 30 años de edad, cuyo familiar refiere inicio de enfermedad actual el día 09/11/13 en horas de la madrugada, cuando posterior a arrollamienro por vehículo en marcha, presenta traumatismos múltiples, aumento de volumen, deformidad, dolor y limitación funcional en ambos miembros inferiores y escoriaciones dispersas, motivo por el cual es trasladado a este centro asistencial donde es evaluado e ingresado por el servicio de traumatología con el diagnóstico de polifracturado. Es evaluado además por el servicio de cirugía blanda, se le realiza lavado peritoneal el cual resulta positivo macroscópicamente por lo que es llevado a mesa operatoria de emergencia, se le realiza laparotomía exploratoria con hallazgo de 500cc de hemoperitoneo, lesión esplénica grado II y lesión hepática grado I, se toma por conducta evacuación de hemoperitoneo, se constata hemostasia, sin evidencias de sangrado activo, lavado de cavidad y cierreb por planos, además se le realiza reducción cruenta de de fracturas en ambos miembros inferiores. Se mantienen en el área de recuperación de quirófano, intubado y conectado a ventilación mecánica por 24 horas, siendo evaluado diariamente por servicio de UCI, posteriormente se extuba y se mantiene con oxigeno húmedo por mascarilla facial. Se evidencian en paraclínicos, retención de azoados y presenta además oligoanuria por lo que solicitan valoración por nefrología quien hace sugerencias. El día 12/11/2013, en horas de la tarde, el paciente de manera progresiva comienza a presentar disnea, trabajo respiratorio, tiraje intercostal y supraclavicular y aleteo nasal, motivo por el cual se acude nuevamente a valorar paciente, se evidencia cuadro anteriormente descrito y saturación de oxigeno por monitor de 70% y en descenso, se procede a intubación endotraqueal y se conecta a ventilación mecánica con MA1, mejorando cuadro clínico. En vista de mal estado general del paciente y por disponibilidad de cupo, Dr. Alpino y Dra. Cortesia, autorizan su ingreso en UCI y dictan órdenes médicas.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubado con tubo 8Fr y recibiendo oxígeno por ambú®, estable hemodinamicamente, se pasa a cama de UCI y se conecta a monitor cardíaco continuo que reporta TA: 142/88(120) mmHg, FC: 99 lpm, FR: 20 rpm, SatO2: 94%.''',
			
			"piel" : 	'''morena, normotérmica al tacto, llenado capilar < 3 segundos''',

			"cardiopulmonar":  ''' tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pdisminuidos en 2/3 y base pulmonar derecha, con roncus universales. Ruidos cardíacoy regulares, taquicardicos, sin soplo ni galope.''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico, con herida quirúrgica supra-para e infraumbilical cubierta por apósitos con escasa secreción serohemática, no fétida.''',

			"neurologico": ''' inconsciente, pupilas mióticas arreactivas a la luz, glasgow no evaluable por efectos de sedación farmacológica.''',
			"extremidades": '''fractura de fémur, tibia y peroné derechos fijada con tutores externos, fractura de fémur izquierda fijada con tutor externo, inmovilización con férula braquiopalmar en miembro superior izquierdo. ''',

		}, 

		"diagnosticoIngresoUCI": [
								"TCE SEVERO",
								"POM DE LAPAROTOMIA EXPLORATORIA POR TRAUMATISMO TORACOABDOMINAL CERRADO COMPLICADO CON",
								"LESION ESPLENICA GRADO II",
								"LESION HEPATICA GRADO I EN SEGMENTO 5 Y 6",
								"POLIFRACTURADO",
								"FX ⅓ ½ FEMUR DERECHO",
								"FX ⅓ ½ TIBIA DERECHA",
								"FX ⅓ ½ FEMUR IZQUIERDO",
								"FX SEGMENTARIA DE CUBITO IZQUIERDO",
								"FX ⅓ ½ RADIO IZQUIERDO",
								"INFECCION RESPIRATORIA BAJA: NEUMONIA BILATERAL NOSOCOMIAL",
								"INSUFICIENCIA RENAL AGUDA",
								"TRASTORNO HEMATOLOGICO",
								"ANEMIA MODERADA",
								"TROMBOCITOPENIA",
								"TRASTORNO ACIDO-BASE",
								"ACIDOSIS METABOLICA DESCOMPENSADA + HIPEROXEMIA",
								{"resumen": ''' Paciente con 9 dias de estadía en terapia intensiva conectado a ventilación mecánica modoAC VC 560 FL 50 FIO2 50 FR12 con necesidad de PEEP de 12 por SDRA que mejor en el plazo de 5 ias tolerando destete ventilatorio hasta que hace 72 horas se extuba sin complicaciones actualmenterecibiendo oxigeno húmedo por mascarilla facial a razón de 10 lt por minuto ,además infección respiratoriaasociada a ventilación mecánica con la presencia de acynetobacter por cultivo de secreción bronquial tratadacon Tygacil y Meropenem mejorando significativamente se han realizado por parte de traumatología limpiezasquirúrgicas de lesiones esperando materiales para resolución definitiva de fractura de fémur  en ambos miembrosy de tibia derecha , por su evolución favorable y sin necesidad de ventilación mecánica ni monitoreo continuose decide traslado a observación adultos para su posterior seguimiento .'''}
								],  

		"examenFisicoEgreso": {
			"resumen": ''' monitor cardíaco continuo que reporta TA: 135/88(110) mmHg, FC: 86 lpm, FR: 20 rpm, SatO2: 99%.''',
			"piel": ''' morena, normotérmica al tacto, llenado capilar < 3 segundos ''',
			"cardiopulmonar": ''' tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, disminuidos en 2/3 y base pulmonar  derechO. Ruidos cardíacos rítmicos y regulares, sin soplo ni galope.''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación,  no megálico, con herida quirúrgica supra-para e infraumbilical cubierta por apósitos con escasa  secreción serohemática, no fétida.''',
			"extremidades": '''fractura de fémur, tibia y peroné derechos fijada con tutores externos, fractura de fémur izquierda fijada con tutor externo, inmovilización con férula braquiopalmar en miembro superior izquierdo. ''',
			"neurologico": '''consciente, pupilas isocoricas reactivas a la luz, glasgow 15 puntos .''',

		},  

		"diagnosticoEgreso": [
						"TCE SEVERO",
						"POM DE LAPAROTOMIA EXPLORATORIA POR TRAUMATISMO TORACOABDOMINAL CERRADO COMPLICADO CON",
						"LESION ESPLENICA GRADO II",
						"LESION HEPATICA GRADO I EN SEGMENTO 5 Y 6",
						"POLIFRACTURADO",
						"FX ⅓ ½ FEMUR DERECHO",
						"FX ⅓ ½ TIBIA DERECHA",
						"FX ⅓ ½ FEMUR IZQUIERDO",
						"FX SEGMENTARIA DE CUBITO IZQUIERDO",
						"FX ⅓ ½ RADIO IZQUIERDO",
						"INFECCION RESPIRATORIA BAJA: NEUMONIA BILATERAL NOSOCOMIAL RESUELTA ",
						"INSUFICIENCIA RENAL AGUDA RESUELTA ",
						"TRASTORNO HEMATOLOGICO",
						"ANEMIA MODERADA",
						"TRASTORNO ACIDO-BASE:",
						"ACIDOSIS METABOLICA DESCOMPENSADA + HIPEROXEMIA",
	
		], 
		
	}, # 54


	{
		"nombre": "Dominga Antonia Lisboa", 		
		"edad": "86",
		"sexo": "F",	
		"fechaNacimiento": datetime(1927,12,20), 			
		"ci": "8.428.584", 		
		"dirección": "Cumaná, Edo sucre ", 		
		"fechaIngresoHUAPA":datetime(2013,7,27), 		
		"fechaIngresoUCI":datetime(2013,7,27), 
		"resumenIngreso": '''Se trata de paciente femenino de 86 años de edad, natural y procedente de la localidad, con antecedentes de HTA sistémica de larga data, insuficiencia cardíaca en fase dilatada y EVC isquémico hace 12 años aproximadamente, en tratamiento regular con Cozaar 50mg OD, Digoxina 0,125mg, Lasix 40mg BID, Aldactone 25mg, Hidroclorotiazida 12,5 mg y Clopidogrel 75mg, cuyos familiares refieren inicio de enfermedad actual el día 23/07/2013 cuando comienza a presentar malestar general, evacuaciones líquidas en repetidas oportunidades, motivo por el cual es llevada a ambulatorio cercano donde indican tratamiento médico y egresa. El día 24/07/2013 presenta disartria y debilidad generalizada, es llevada a centro privado donde indican valoración por medicina interna. El día 25/07/2013 es valorada por internista quien ajusta tratamiento y anexa Clonac 0,25mg hora sueño. El 26/07/2013 presenta caída desde la altura de la cama, además progresa disartria y deterioro progresivo del estado de consciencia, por lo que es llevada nuevamente a centro privado donde es valorada por médico de guardia, se le realiza TAC cerebral donde se evidencia hematoma subdural con colapso ventricular ipsilateral, desplazamiento de línea media y edema cerebral difuso, es valorada por neurólogo de guardia quien indica epaminización y refiere a este centro asistencial por petición de familiares. Es trasladada y previa valoración por servicio de medicina interna, se ingresa con los diagnósticos de: 1) Hematoma Subdural, 2) Hemorragia Difusa, 3) HTA de larga data, 4) Cardiopatía Mixta Difusa.  Al momento del ingreso se encuentra inconsciente, pupilas anisocoricas (derecha con tendencia a la midriasis, izquierda puntiforme, ambas sin respuesta a la luz), glasgow 6/15ptos (RM: 4ptos, RO: 1pto, RV: 1pto) por lo que realizan intubación endotraqueal y se conecta a T de Ayres. Es evaluada por Dr. Acevedo (Neurocirujano de Guardia) quien decide resolución quirúrgica. Es llevada a mesa operatoria, donde bajo Anestesia General Inhalatoria, se le realiza craneotomía frontotemporoparietal derecha para evacuación de hematoma subdural agudo de 90ml. Sangrado profuso de aproximadamente de 1000ml, se realiza cierre por planos, asepsia y antisepsia, finalmente se traslada a Servicio de UCI previa autorización de Dr. Alpino (Intensivista de Guardia) quien dicta ordenes médicas. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, en regulares malas condiciones generales, hemodinámicamente estable, intubada y conectada a ventilador de traslado, se conecta a monitor cardíaco externo que reporta los siguientes signos vitales: TA: 84/33(48) mmHg FC:99 lpm FR:14 rpm SPO2:100 %''',
			
			"piel" : 	'''Morena, normotérmica al tacto, llenado capilar < 3 segundos. ''',

			"cardiopulmonar":  '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos arrítmicos, irregulares, hipofonéticos,  sin soplos ni galope. ''',
			"abdomen": ''' plano, blando, depresible, ruidos hidroaéreos presentes, no megálico.''',

			"neurologico": '''Bajo efectos de anestesia general inhalatoria por lo que no es evaluable el estado de consciencia, pupilas anisocoricas, pupila derecha midriática sin respuesta a la luz, pupila izquierda miótica hiporreactiva.''',
			"cabeza": '''herida quirúrgica en región frontotemporoparietal derecha cubierta por apósitos y malla con escasa secreción serohemática. ''',

		}, 

		"diagnosticoIngresoUCI": [


				"POI DE CRANEOTOMIA FRONTOTEMPOROPARIETAL DERECHA PARA DRENAJE DE HEMATOMA SUBDURAL AGUDO",
				"TCE SEVERO",
				"HTA SISTEMICA",
				"INSUFICIENCIA CARDIACA EN FASE DILATADA",
				"TRASTORNO HEMATOLOGICO",		
				"ANEMIA MODERADA",
				"TROMBOCITOPENIA",
				"TRASTORNO ACIDO-BASE",
				"ACIDOSIS METABOLICA DESCOMPENSADA CON ALCALOSIS RESPIRATORIA + HIPEROXEMIA",

									
								],  
		
	}, # 55



	{
		"nombre": "Cedeño Emiliano", 		
		"edad": "71",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1942,2, 18), 		
		"lugarNacimiento": "Monagas", 				
		"dirección": "Boca de sabana, calle cardonal N° 103.", 		
		"fechaIngresoHUAPA":  datetime(2013,9, 25), 		
		"fechaIngresoUCI": datetime(2013,9, 25), 		
		"ocupacion": "albañil", 
		"antecedentes": '''asmático, HTA, fumador.''',
		"resumenIngreso": '''Se trata de paciente masculino de 71 años, natural de Monagas y procedente de la localidad, con antecedentes de Asma Bronquial desde la infancia, sin tratamiento, HTA sin tratamiento, fumador desde la infancia. Inicia enfermedad actual el día 25/09/13 cuando comenzó a presentar disnea a pequeños esfuerzos que evolucionan a la ortopnea, cianosis distal, tiraje universal , y posterior alteración del sensorio, se le realizan gases que reportan disminución de la saturación de O2,motivo por el cual se realiza su ingreso. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' TA:110/72mmHg FC95lpm FR:20rpm Sat: 91% Consciente, Glasgow: 11/15pts, Respuesta Motora: 6pts, Respuesta Verbal: 1pts (limitado por tubo endotraqueal), Apertura Ocular: 4pts, pupilas isocóricas normorreactivas. ''',
			
			"piel" : 	'''	morena, elasticidad conservada llenado capilar ‹ 3 sg.''',

			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible, ruidos respiratorios presentes, con sibilantes y crepitantes basales izquierdos. Ruidos cardíacos rítmicos, regulares, taquicárdicos, no se auscultan soplos.	''',
			
			"abdomen": ''' globoso, blando, depresible, ruidos hidroaéreos presentes. ''',

			

		}, 

		"diagnosticoIngresoUCI": [

						"Infección respiratoria baja",
						"Emergencia Hipertensiva",
						"Insuficiencia cardiaca complicada con edema agudo de pulmón",
						"Asma bronquial",
						"FA con respuesta ventricular adecuada",
						"EPOC descompensado",
						"IM sin elevación del segmento S",
						"Trastorno Hidroelectrolitico hipokalemia",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA:170/80 mmHg FC:120LPM  FR:33rpm Sat: 79%. Paciente en malas condiciones generals, afebrilo, taquipneico, conectado a pieza en T por tubo endotraqueal. ''',
			"piel": ''' se evidencia cianosis distal en miembros inferiores y superiores.''',
			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes con roncus, sibilantes y crepitantes universales, y abolidos en 1/3 medio y bases bilaterales. Ruidos cardíacos rítmicos, regulares, taquicárdicos, no se auscultan soplos.''',
			"abdomen": '''globoso , blando, depresible, sin visceromegalias, ruidos hidroaéreos presentes. ''',
			
			"neurologico": '''Somnolienta, Glasgow: 11/15pts, Respuesta Motora: 6pts, Respuesta Verbal: 1pts, Apertura Ocular: 4pts, limitado por tubo.''',

		},  

		"diagnosticoIngresoHUAPA": [
				"Insuficiencia respiratoria aguda",
				"Emergencia Hipertensiva expresada en edema agudo de pulmón",
				"EPOC descompensado",
				"Asma bronquial",
				"Hta",
				"FA con respuesta ventricular adecuada",
				{"resumen": ''' Es solicitada valoración por UCI en vista de no haber mejoría clínica es evaluado por residente de guardia quien realiza gases arteriales reportando pH:7,31   pCO2:32   pO2:66   HCO3:16.1   E.B:-10,2   SatO2:91. Con dificultad respiratoria, cianosis peribucal y distal se plante caso a la Dra Cortesía quien indica su ingreso a UCI.'''},
				

		], 
		
	}, # 56

	{
		"IdHistoria": "12-78-42", 
		"nombre": "María Elena Gómez", 		
		"edad": "48",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1964,12,7), 		 		
		"ci": "6.933.651", 		
		"dirección": "Caigüire, calle la marina, Cumaná, Edo sucre ", 		
		"fechaIngresoHUAPA":  datetime(2013,11,1), 		
		"fechaIngresoUCI": datetime(2013,11,1), 		
	
		"resumenIngreso": ''' Paciente femenina de 48 años de edad, natural de Cumanacoa, procedente de la localidad, con antecedente de fibromatosis uterina diagnosticada hace 18 años aproximadamente y en control por el servicio de ginecología e hipotiroidismo no controlado, cuyo familiar (hermana) refiere inicio de enfermedad actual hace 2 semanas aproximadamente cuando comienza a presentar anorexia, pirosis y reflujo gastroesofágico. Para el día 20/10/13 se anexa al cuadro vómitos de contenido bilioso eventual. Para el día 28/10/13 aproximadamente comienza a presentar distensión abdominal, disnea de grandes a pequeños esfuerzos, el día 30/10/13 por acentuación de sintomatología previa, acude a ambulatorio de su localidad de donde refieren a este centro asistencial donde es evaluada por el servicio de medicina interna encontrándose al examen físico palidez cutáneo-mucosa, tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares con crepitantes universales, ruidos cardíacos rítmicos y regulares sin soplo, TA 180/80mmHg, abdomen globoso, distendido, con presencia de arañas vasculares, ruidos hidroaereos disminuidos, matidez en hemiabdomen izquierdo y timpanismo en hemiabdomen derecho, orientada en los 3 planos. Previa valoración se ingresa con los diagnósticos de  Tumor Intraabdominal, síndrome ascítico, fibroma uterino, anemia moderada y deshidratación moderada. El día 31/10/13 solicitan valoración por los servicios de ginecología, cirugía blanda y UCI, es trasladada a servicio de sala de parto donde se le realiza eco abdominal evidenciándose abundante líquido libre en cavidad abdominal, por lo que cirugía realiza paracentesis obteniéndose aproximadamente 500cc de líquido de aspecto seroso, se toman muestras para citoquímico, citológico y cultivo, se hacen sugerencias por el servicio de UCI. Es trasladada nuevamente al área de observación adultos siendo tórpida su evolución. El día 01/11/13 es reevaluada por el servicio de cirugía blanda quien decide llevar a mesa operatoria de emergencia y bajo anestesia general se le realiza laparotomía exploratoria encontrándose: 1500cc de secreción purulenta libre en cavidad abdominal, útero de 30x15cm con múltiples miomas subserosos, ovarios de 2x2cm de diámetro, tumoración a 220cm de asa fija en epiplón complicada con perforación intestinal; se realiza evacuación de secreción purulenta, histerectomía abdominal total más anexectomía bilateral, ligadura de ligamento redondo, resección y anastomosis T-T a 220cm de asa fija y resección de Tu. de 12x7cm de diámetro, lavado de cavidad con 5000cc de solución 0,9%, comprobación de hemostasia, se deja dren rígido dirigido a fondo de saco, puntos de tensión y rafia de piel, asepsia final. En vista de malas condiciones generales de la paciente solicitan valoración por UCI y cupo para manejo post-quirúrgico. Se comunica caso a Dra. Roa y Dra. Cortesia (Intensivista de Guardia) quienes en vista de estado general de la paciente y contar con disponibilidad de cupo, autorizan su ingreso a la UCI y dictan órdenes medicas.     ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, en malas condiciones generales, intubada y conectada a ventilador de traslado, se conecta a monitor cardíaco externo que reporta los siguientes signos vitales:TA: 29/20(23) mmHg FC: 125 lpm	FR: 12 rpm SPO2:100 %Se indican 1000cc de solución 0,9% VEV STAT, se solicitan 2 unidades de concentrado globular, con lo que mejora presión arterial y se reporta:TA: 91/47(62) mmHg	FC: 88 lpm FR: 25 rpm SPO2:100 %''',
			
			"piel" : 	'''	con marcada palidez cutáneo-mucosa, hipotérmica al tacto, llenado capilar < 3 segundos. ''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos rítmicos, regulares, sin soplos ni galope. 	''',
			
			"abdomen": ''' globoso a expensas de panículo adiposo, ruidos hidroaereos presentes, herida quirúrgica supra-para e infraumbilical cubierta por gasas limpias y secas, se evidencia dren rígido conectado a bolsa recolectora con moderado contenido serohemático, blando, depresible, no megalico, con red venosa colateral.''',

			"neurologico": ''' Bajo efectos de anestesia general por lo que no es evaluable el estado de consciencia, pupilas anisocoricas, pupila izquierda midriática, pupila derecha con tendencia a la midriasis, ambas con respuesta lenta a la luz,. ''',
			"extremidades": '''simétricas, edema II/IV que deja fóvea. ''',

		}, 

		"diagnosticoIngresoUCI": [

						"POI DE LAPAROTOMIA EXPLORATORIA POR FIBROMATOSIS UTERINA GIGANTE COMPLICADA CON",
						"PERFORACION DE ASA DELGADA",
						"COLECCIÓN INTRAABDOMINAL",
						"SHOCK SEPTICO VS. SHOCK HIPOVOLEMICO",
						"INSUFICIENCIA RENAL AGUDA",
						"HIPOTIROIDISMO",
						"TRASTORNO HEMATOLOGICO",
						"ANEMIA SEVERA",
						"PROLONGACION DE TIEMPOS DE COAGULACION ",
						"TRASTORNO ACIDO-BASE",
						"ACIDOSIS METABOLICA DESCOMPENSADA CON ALCALOSIS RESPIRATORIA + HIPEROXEMIA",
								], 
		
	}, # 57


	{
		"IdHistoria": "51-47-11", 
		"nombre": "Luis José Ramírez Sánchez", 		
		"edad": "48",
		"sexo": "M",	
		"fechaNacimiento": datetime(1966, 6, 22),	 			
		"dirección": "Tampiarito, casa S/N, Vía Caripito. ", 		
		"fechaIngresoHUAPA": datetime(2013, 12, 5),			
		"fechaIngresoUCI": datetime(2013, 12, 5),		
		"antecedentes": '''Niega alergia a medicamentos, niega hábitos tabáquicos, ni antecedentes quirúrgicos. ''', 
		"resumenIngreso": ''' Se trata de paciente masculino de 48años de edad quien inicia enfermedad actual hace aproximadamente 6 meses  cuando presenta dolor torácico, posteriormente se anexa al cuadro edema facial y tos seca, motivos por los cuales acude a facultativo donde realizan paraclínicos para descarte de TBC, sin hallazgos positivos, posteriormente se anexa al cuadro aumento de volumen en región esternal, acudiendo nuevamente a facultativo quien indica TAC de Tórax, la cual se realiza el día 02/12/13 y reporta masa mediastínica voluminosa de localización anterior que contiene zona de baja atenuación, probablemente producida por necrosis, las estructuras vasculares mediastínicas se aprecian desplazadas en sentido posterior, lesión que mide 11,2x8,6x13,8cms, motivo por el cual es referido a este centro hospitalario donde previa valoración se decide su ingreso el día 05/12/2013.''', 


		"examenFisicoIngresoUCI": {
			
			"piel" : 	'''Morena, con acentuado tinte ictérico en piel y mucosas, llenado capilar < 3 segundos.''',

			"cardiopulmonar":  ''' tórax asimétrico, hipoexpansible, se evidencia aumento de volumen en región antero-superior del tórax y se evidencia herida quirúrgica cubierta por apósitos limpios, sin secreciones.	''',
			"abdomen": ''' Globoso, blando, depresible, ruidos hidroaéreos presentes, no impresiona doloroso a la palpación.''',

		}, 

		"diagnosticoIngresoUCI": [
									
									"Postoperatorio Inmediato de Toma de Biopsia de Tu de Mediastino",
									"Tu. De Mediastino",
									"Inestabilidad Hemodinámica",
									"Síndrome Ictérico en estudio",
									"Trastorno A/B: Acidosis Mixta.",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se evalúa paciente que luce en aparentes regulares condiciones generales, afebril, eupneico, hidratrada. Permanece ingresado durante 2 meses en el Servicio de Medicina Interna, siendo valorado por el Servicio de Cirugía de Tórax quien sugiere perfil pre-operatorio para planificar intervención quirúrgica, la cual tuvo que ser diferida en repetidas oportunidades por múltiples causas.  Es llevado a mesa operatoria el día de hoy 13/02/14 donde  bajo Anestesia General Combinada le realizan toma de biopsia con Trucut Nº16, comprobación de hemostasia, se deja dren de látex derecho y se realiza cierre por planos. Posteriormente es trasladado al Área de Recuperación donde en vista de evidenciar cifras de saturación en descenso, pálidez cutáneo-mucosa marcada, sudoración profusa solicitan valoración por el Servicio de Terapia Intensiva y en vista de condiciones del paciente y disponibilidad de cupo se decide su ingreso a esta unidad.Se traslada paciente en cama, intubado, recibiendo oxígeno por Ambú, hemodinámicamente inestable, sin monitorización, se ingresa a la unidad, se realiza cambio de tubo endotraqueal y se coloca tubo Nº8, se conecta a ventilación mecánica y a monitor cardíaco externo que reporta:TA: 79/53mmHg FC: 66lpm FR: 27rpm SPO2:90%''',
			"piel": ''' turgor y elasticidad conservado, llenado capilar < 3segundos.''',
			"cardiopulmonar": '''tórax asimétrico, hipoexpansible, se evidencia aumento de volumen que comprende desde manubrio esternal hasta tercio distal de esternón ''',
			"abdomen": '''Doloroso a la palpación, ruidos hidroaéreos presentes, no impresiona doloroso a la palpación.''',

			"neurologico": '''Orientado en tiempo, espacio y persona.''',

		},  

		"diagnosticoIngresoHUAPA": [
								
			"Tu. De Mediastino",
			"Enfermedad Linfoproliferativa A/D.",
			"HTA",

		], 
		
	}, # 58

	{
		"nombre": "Luis Esteban Mota", 		
		"edad": "64",
		"sexo": "M",	
		"fechaNacimiento": datetime(1948,11,28),				
		"ci": "", 		
		"dirección": "Urbanización Bermúdez, Bloque 15, Apto 02.", 		
		"fechaIngresoHUAPA": datetime(2013,7,21),
		"fechaIngresoUCI": datetime(2013,7,21),
		"resumenIngreso": ''' Se trata de paciente masculino de 64 años de edad, con antecedentes de IM de cara inferior hace 3 años, en tratamiento con: ASA, Clopidogrel, Atorvastatina, Atenolol y Enalapril, hace 2 años Angioplastia de Arteria Iliaca Derecha por Pseudoaneurisma, hace 2 años diagnóstico de Enfermedad Arterial Coronaria Obstructiva de Arteria Coronaria Derecha, quien refiere inicio de enfermedad actual el dia 21/07/2013 cuando presenta de manera súbita sudoración, desvanecimiento que llegó a la pérdida del conocimiento, desviación de la mirada, sin relajación de esfínteres, motivo por el cual es trasladado a centro de salud privado donde es valorado por Especialista (Dr. Alpino) quien decide su ingreso a Unidad de Cuidados Intensivos. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, en aparentes regulares condiciones generales, hemodinámicamente estable, ventilando espontáneamente, recibiendo oxígeno húmedo por mascarilla facial, se conecta a monitor cardíaco externo que reporta los siguientes signos vitales: TA: 127/48mmHg	FC: 45lpm FR: 14rpm SPO2: 100% ''',
			
			"piel" : 	'''Morena, normotérmica, turgor conservado, llenado capilar menor de 3 segundos.''',

			"cardiopulmonar":  '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes, no se auscultan agregados, ruidos cardíacos rítmicos, hipofonéticos, bradicardicos, no ausculto soplos ni galopes.''',
			
			"abdomen": ''' Plano, blando, depresible, no doloroso a la palpación, Ruidos Hidroaéreos presentes.''',

			"neurologico": '''Consciente, orientado en 3 planos, Glasgow: 15/15pts. ''',
		}, 

		"diagnosticoIngresoUCI": [

							"Síndrome Coronario Agudo: Angina Inestable.",
							"Cardiopatía Isquémica Crónica.",
							"Enfermedad Arterial Coronaria Obstructiva de Arteria Coronaria Derecha.", 
							"Angioplastia de Arteria Iliaca derecha por Pseudoaneurisma.",
							"Arteriopatía Obstructiva Periférica en miembro inferior derecho.",
							{"resumen": ''' El paciente permanece durante 72 horas  en el Servicio de UCI, hemodinámicamente estable, recibiendo oxígeno húmedo por canula nasal, el día 23/07/ 13 le realizan colocación de Holter, la cual debe ser retirado a las 24 horas por técnico de Cardiología, se le realizará informe del resultado del Holter el dia 25/7/2013, y el resto del manejo debe ser a cargo de la Cardiologa Dra Edith Rodríguez.'''}
								],  

		"examenFisicoIngresoHUAPA": {

			"resumen": ''' Paciente evaluado en cama, en condiciones clínicas de cuidado, recibiendo oxígeno húmedo a 5 litros por minuto, conectado a monitor cardíaco externo que reporta: TA: 122/58mmHg, FC: 40lpm, FR: 22rpm ''',
			
			"piel": ''' Morena, turgor conservado, sin lesiones. ''',
			
			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, ruidos cardíacos rítmicos, regulares, bradicardicos, sin soplos. ''',
			
			"abdomen": '''Blando, depresible, no doloroso a la palpación, Ruidos Hidroaéreos presentes.''',
			
			"extremidades": '''Simétricos, sin edemas.''',
			
			"neurologico": '''Conservado, Glasgow: 15/15pts.''',
		},  

		"diagnosticoEgreso": [

							"Síndrome Coronario Agudo: Angina Inestable de alto riesgo.",
							"Enfermedad del Nodo Sinusal.",
							"Cardiopatía Isquémica Crónica.",
							"Enfermedad Arterial Coronaria Obstructiva de Arteria Coronaria Derecha. ",
							"Angioplastia de Arteria Iliaca derecha por Pseudoaneurisma.",
							"Arteriopatía Obstructiva Periférica en miembro inferior derecho.",
		], 

		"diagnosticoIngresoHUAPA": [
			"Síndrome Coronario Agudo: Angina Inestable de Alto Riesgo.",
			"Enfermedad del Nodo Sinusal con Braadicardia Extrema, Presíncope.",
			"Hipertensión Arterial",
			{"resumen": ''' Estando en centro privado, es evaluado por Dra. Edith Rodríguez (Cardióloga) quien indica colocación de Marcapasos Definitivo para el día 22/7/2013, en vista de condiciones socio-económicas del paciente y en vista de contar con cupo en la Unidad de Cuidados Intensivos de este centro hospitalario se decide su traslado e ingreso.'''}

		],
		
	}, # 59

	{
		"nombre": "Jorge Pereira", 		
		"edad": "49",
		"sexo": "M",	
		"fechaNacimiento": datetime(1963, 10, 1),		
		"ci": "8.436.746", 		
		"dirección": "Ave. Jose Vicente Gutierrez casa # 74 Cumana.", 		
		"fechaIngresoHUAPA": datetime(2013, 9, 13), 		
		"fechaIngresoUCI":datetime(2013, 9, 13), 		
		"resumenIngreso": ''' Se trata de paciente masculino de 49 años de edad natural de barcelona y procedente de la localidad con antecedentes de HTA quien lleva tratamiento con cardiosol 1 tab OD; Bifril 1 tab OD; atrovastatina 40 mg OD,  ERC en diálisis peritoneal desde hace 2 años y ECV hace aproxiamdamente 7 meses. El paciente incia enfermedad actual el dia 6/9/13 cuando en el momento de realizar diálisis peritoneal en el baño de su casa refiere el familiar presenta ”convulsion”, vomitos de contenido alimenticio, perdida de conciencia y relajación de esfínter vesical y anal motivo por el cual es traido a este centro asistencial donde es evaluado y se hospitaliza por servicio de medicina.  Examen Físico:FR: 20x´ FC: 90x´ TA: 180/110.Piel: normotérmica, normoelástica, llenado capilar menor a 3 segundos.Cardiopulmonar: Tórax simétrico, expansible, ruidos respiratorios presentes, se auscultan roncos universales, ruidos cardíacos rítmicos regulares taquicárdicos, no soplos no galope.Abdomen: Globoso, blando, depresible, Ruidos Hidroaéreos presentes, no megalias.Neurológico: inconsciente, glasgow 5/15 ptos ( RM 2, RO 2, RV 1), pupilas hiporreactivas a la luz.''', 

		"diagnosticoIngresoUCI": [
									
									"Emergencia Hipertensiva expresada en ECV hemorrágico",
									"IRB: neumonía por broncoaspiracion.",
									"ERC en diálisis peritoneal.",
									"HTA sistemica",
									{"resumen": ''' Emergencia Hipertensiva expresada en E.V.C. hemorrágico. Neumonía por broncoaspiración. Enfermedad renal crónica en diálisis peritoneal. Hipertensión arterial sistémica.Paciente que se mantiene en sevicio de UCI en regulares condiciones con mejoría de estado neurológico con glasgow de 7 puntos dados por RM 5  RV 1 RO 1  , en ocasiones con apertura ocular espontanea pero sin conexión con el medio , en diálisis peritoneal  con 4 recambios diarios tipo DPAC  pero intrahospitalaria ,cuantificándose ultrafiltrados  diariamente  , desde el punto de vista respiratorio  se diagnostica una IRB neumonía asociada a ventilación mecánica para lo cual recibió tratamiento con tazopril a dosis ajustadas al clereance renal observándose mejoría significativa , estuvo por espacio de 10 dias – Paciente en regulares condiciones . conectado por TQT a T de AYRES con oxigeno húmedo a 8 lt por minuto , afebril , hemodinamicamente estable . signos vitales por monitor saturación de oxigeno 100%, T.A. 165/108 (148) mmHg. F.C.88 lpm.Cardiopulmonar: tórax, simétrico, hipoexpansibles, Rs.Rs. audibles, simetricos sin adventicios. Corazón: Rs.Cs.Rs.R. sin soplos ni frotes.Abdomen plano, se aprecia en flanco derecho catéter de tenkoff, con cura limpia y seca. Blando no doloroso a la palpación profunda.Miembros: con ligera atrofia, evidencia hiperextension plantar.Neurológico: reflejo osteotendinosos patelar y bicipital II/IV. Glasgow 8/15   RM:5ptosRO 2ptos. RV 1pto limitado por tubo.'''},

								],  


		"diagnosticoIngresoHUAPA": [
			{"resumen": ''' El paciente es evaluado por equipo UCI quien en vista de deterioro neurológico se realiza intubación endotraqueal y se conecta a T de Ayres, en vista de no tener disponibilidad de cupo se presenta caso a Dra Cortesia (intensivista de guardia) quien dicta ordenes medicas. El pcte permanece en área de choque con apoyo ventilatorio MA1 y dialítico (hemodiálisis) diaria con apoyo y soporte de equipo UCI.El día de hoy por disponibilidad de cupo se presenta caso a Dra Begglia (intensivista de guardia) quien decide ingreso a UCI .Examen físico de ingreso a U.C.I.Paciente en As.Ms.Cs.Gs. conectado por tubo endotraqueal a bolsa autoinsuflable con fuente de oxigeno, febril 38,5°C , hemodinamicamente estable recibiendo nitroprusiato sódico por microgotero, se pasa de cama de  traslado a cama de U.C.I. signos vitales por monitor saturación de oxigeno 100%, T.A. 172/110 (148) mmHg. F.C.88 lpm.Cardiopulmonar: tórax, simétrico, hipoexpansibles, Rs.Rs. audibles, simetricos sin adventicios. Corazón: Rs.Cs.Rs.R. sin soplos ni frotes.Abdomen plano, se aprecia en flanco derecho catéter de tenkoff, con cura limpia y seca. Blando no doloroso a la palpación profunda.Miembros: con ligera atrofia, evidencia hiperextension plantar.Neurológico: reflejo osteotendinosos patelar y bicipital II/IV. Glasgow 8/15   RM:5ptos RO 2ptos. RV 1pto limitado por tubo. '''}
		],

		"diagnosticoEgreso": [
						"Emergencia Hipertensiva expresada en E.V.C. hemorrágico.",
						"Neumonía asociada a ventilación mecánica resuelta ",
						"Enfermedad renal crónica en diálisis peritoneal.",
						"Hipertensión arterial sistémica.",
						"Anemia  moderada ",
		], 
		
	}, # 60

	{
		"IdHistoria": "338126", 
		"nombre": "Sorveidys Josefina Díaz Andrade ", 		
		"edad": "21",
		"sexo": "F",	
		"fechaNacimiento": datetime(1993,5,25), 		
		"lugarNacimiento": "Cumaná", 		
		"ci": "24.690.249", 		
		"dirección": "Barrio El pinar  Sector E casa numero 27", 		
		"fechaIngresoHUAPA": datetime(2015,1,26), 		
		"fechaIngresoUCI":datetime(2015,1,26),		

		"examenFisicoIngresoUCI": {

			"piel" : 	'''	palidez cutáneo mucosa marcada, afebril al tacto, deshidratada, sequedad de mucosa oral, se evidencia edema facial,  llenado capilar <3seg. ''',

			"cardiopulmonar":  ''' Tórax simétrico normoexpansible Ruidos respiratorios presentes en ambos hemitorax, no se auscultan agregados. Ruidos cardiacos rítmicos no soplos ''',
			
			"abdomen": ''' blando depresible, ruidos hidroaéreos presentes, doloroso a la palpación superficial y profunda en toda su extensión. ''',

			"neurologico": ''' consciente orientada en tiempo, espacio y persona, lenguaje coherente, Glasgow 15/15ptos. Fuerza muscular 5/5pts.  Sensibilidad conservada. ROT: II/IV. ''',

			"gases_arteriales": '''PH 7.32 PO2 130 mmHg PCO2 26 mmHg  HCO3 13.4mmol/L EB -12.7mmol/L  SATO297 % ''',
			
			"extremidades": ''' se evidencia edema en ambos miembros inferiores grado I.''',

		}, 

		"diagnosticoIngresoUCI": [

								"Diabetes Mellitus tipo I descompensada en hipoglicemia", 
								"Nefropatía diabética ",
								"Hipertensión arterial",
								"Trastorno Hematológico : Anemia severa ",
								"trastorno Acido – Base: acidosis metabólica",
								{"resumen": ''' Paciente permanece en el servicio desde el día 26/1/15 hasta el día 30/1/15 con evolución clínicasatisfactoria recibió tratamiento médico a base de insulina cristalina por bomba de infusión que fuecalculada a razón de 4uds por hora y se modifica según parámetros de glicemia séricas y capilares hastalograr su destete total el cual se realizo en un periodo de 48 horas, además cumplió tratamiento a base deFluconazol durante 4 días en vista de uro análisis el cual reporto levaduras moderadas. Reiniciándose dieta alas 48 horas de su ingreso, modificación del tratamiento de insulina cristalina a 3 unidades pre pandrial y 10unidades de Lantus 10 en horas de la noche manteniéndose cifras de glicemia sérica y capilar dentro de parámetrosaceptables además de corrección de trastorno acido básico y por evolución clínica satisfactoria se decide su egreso.'''}, 

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Fr: 19 rpm Fc: 109 lpm TA: 122/81 mmHg. Paciente es evaluada por el servicio de terapia intensiva en vista de persistir con la hipoglicemia y en vista de disponibilidad de cupo se decide su ingreso a la unidad. Se recibe paciente en silla de ruedas, procedente del servicio de emergencia. Se traslada a cama UCI y se conecta a monitor cardiaco continuo que reporta Fr: 18rpm Fc: 105 lpm TA: 111/66 mmHg  SATO2: 99%. ''',
			
			"piel": ''' marcada palidez cutánea mucosa, piel fría, sudorosa, llenado capolar <3seg. ''',
			
			"cardiopulmonar": '''Tórax simétrico normoexpansible Ruidos respiratorios presentes en ambos hemitorax, no se auscultan agregados. Ruidos cardiacos rítmicos regulares no ausculto soplo.''',
			
			"abdomen": '''plano, ruidos hidroaéreos presentes, blando, depresible doloroso a la palpación difusa.''',
			
			"extremidades": '''se evidencia edema grado II en miembro inferior derecho, duro que deja fóvea y edema grado I en miembro inferior izquierdo.''',
			
			"neurologico": '''Paciente consiente, orientada con lenguaje coherente. ''',

		},  

		"diagnosticoIngresoHUAPA": [

				"DIABETES MELLITUS TIPO 1 DESCOMPENSADA EN HIPOGLICEMIA.",
				"HIPERTENSIÒN ARTERIAL CONTROLADA.",
				"ENFERMEDAD RENAL AGUDA.",

		],

		"diagnosticoEgresoUCI": [
						"Diabetes Mellitus tipo I descompensada en Cetoacidosis Diabética(R) ",
						"Nefropatía diabética", 
						"Hipertensión arterial",
						"Trastorno Hematológico : Anemia leve",
						"trastorno Acido – Base: acidosis metabólica descompensada(R)", 
		

		], 

		"resumenEgreso": ''' Se trata de paciente femenina de 21 años de edad natural y procedente de la comunidad  con antecedentes patológicos personales de Diabetes Mellitus TIPO I  desde la infancia para lo cual lleva tratamiento habitual con Insulina Lantus®20 unidades 800 pm  e Insulina cristalina 13 unidades para 24 horas repartidas en 5 Uds. Desayuno ,5 Uds. Almuerzo  y 3 Uds. en la Cena ,además antecedentes de nefropatía diabética en seguimiento por consulta externa e hipertensión arterial sistémica en tratamiento con Ramipril 20mg diarios, quien inicia enfermedad actual el día 20/01/15  en horas de la mañana cuando posterior a controles de glicemias capilares evidencian descensos de las mismas (48mg/dl) por lo que acuden en varias oportunidades a ambulatorio de su localidad donde optimizan cifras y egresan, para el día de hoy 26/01/15 en horas de la madrugada (3:am) se le anexa al cuadro clínico movimientos tónico clónicos generalizado, cianosis peribucal y distal, y perdida del conocimiento por más de 15minutos por lo que acuden a emergencia donde es evaluado por el servicio de medicina interna e ingresan con los diagnósticos de: DIABETES MELLITUS TIPO 1 DESCOMPENSADA EN HIPOGLICEMIA. HIPERTENSIÒN ARTERIAL CONTROLADA. ENFERMEDAD RENAL AGUDA.''',

		"examenFisicoEgresoUCI": {
			"piel": ''' palidez cutáneo mucosa moderada, afebril al tacto, hidratada, se evidencia edema facial,  llenado capilar <3seg. ''',
			"cardiopulmonar": ''' Tórax simétrico normoexpansible Ruidos respiratorios presentes en ambos hemitorax, no se auscultan agregados. Ruidos cardiacos rítmicos no soplos ''',
			"abdomen": ''' blando depresible, ruidos hidroaéreos presentes, no doloroso a la palpación superficial y profunda en toda su extensión. ''',
			"extremidades": ''' simétricas sin edema.''',
			"neurologico": ''' consciente orientada en tiempo, espacio y persona, lenguaje coherente, Glasgow 15/15ptos. Fuerza muscular 5/5pts.  Sensibilidad conservada. ROT: II/IV. ''',

		},
	}, # 61

	{
		"IdHistoria": "46-08-90", 
		"nombre": "Robert Alfredo Mendoza Blanco", 		
		"edad": "15",
		"sexo": "M",	
		"fechaNacimiento": datetime(1998,8,3), 		
		"lugarNacimiento": "Cumaná-Estado Sucre", 		
		"ci": "26.721.912", 		
		"dirección": "Fe y alegría, el valle sector A. casa nro 13 ", 		
		"fechaIngresoHUAPA":  datetime(2014,1,17), 		
		"fechaIngresoUCI": datetime(2014,1,17),		
		
		"resumenIngreso": '''Se trata de paciente masculino 15 años de edad, natural y procedente de cumaná, sin antecedentes de enfermedad de importancia, quien inicia enfermedad actual el día 17 de enero de 2014, cuando posterior a recibir herida por arma de fuego en miembro superior izquierdo y epigastrio es llevado a este centro, donde es evaluado e ingresa por el servicio de Cirugía Blanda con el Diagnóstico de Traumatismo abdominal penetrante por arma de fuego complicado con lesión gástrica y Herida penetrante en miembro superior izquierdo, se lleva a mesa operatoria en donde realizan laparotomía exploradora supra- media- para- infraumbilical, encontrándose los siguientes hallazgos: 3000 cc de hemoperitoneo, lesión grado III de vena cava inferior, lesión grado II de cuerpo de estómago y lesión grado II de 3ra porción de duodeno. Tomándose como conducta evacuación del hemoperitoneo y rafia de las lesiones descritas, con colocación de parche y duodenostomía descompresiva más yeyunostomía de alimentación. El paciente durante acto quirúrgico permanece inestable hemodinámicamente y solicitan evaluación por el servicio de Uci, en vista de disponer de cupo se ingresa.  ''', 


		"examenFisicoIngresoUCI": {

			
			
			"piel" : 	'''	morena, fría al tacto, con piloerección.''',

			"cardiopulmonar":  ''' tórax simétrico hipoexpansible, ruidos respiratorios presentes, sin agregados; ruidos cardiacos taquicárdicos, hipofonéticos, sin soplos ni galope. ''',
			
			"abdomen": ''' plano, se observa herida de laparotomía quirúrgica cubierta de apósitos estériles, se observan 2 drenajes dirigidos a ambas correderas parietocólicas, y yeyunostomía con Foley. ''',

			"neurologico": ''' Glasgow: 3/15ptos (RM: 1pto, RO: 1pto, RV: 1 pto), pupilas midriáticas no reactivas a la luz. ''',
			
			"extremidades": '''herida penetrante en brazo izquierdo con orificio de entrada y de salida. ''',

		}, 

		"diagnosticoIngresoUCI": [

								"Postoperatorio inmediato de laparotomía supra-para e infra umbilical, duodenostomía descompresiva y yeyunostomía.",
								"Traumatismo penetrante por arma de fuego en miembro superior izquierdo. ",
								"Traumatismo abdominal penetrante  por arma de fuego complicada con:",
								"Lesión grado III de Vena Cava inferior.",
								"Lesión grado II de estómago (cuerpo).",
								"Lesión grado II de 3era porción duodenal.",
								"Inestabilidad hemodinámica: hipovolemia.",
								"Trastorno hematológico: Anemia Leve",
								"Trastorno ácido base: acidosis metabólica descompensada +Hiperoxemia",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se recibe paciente en camilla de traslado, intubado, se pasa a cama UCI y se conecta a monitor cardiaco que reporta Fr  rpm Fc 230 lpm TA  -/- TAM 34mmHg SATO2 85%  y se conecta a ventilación mecánica modo AC,  VC 560 (8cc/kg), Fr 12, FiO2 100, Fl 50, PEEP 0.''',
			
			"piel": ''' morena, afebril, múltiples escoriaciones en miembros escoriaciones.''',
			
			"cardiopulmonar": '''tórax simétrico expansible, ruidos respiratorios presentes, sin agregados; ruidos cardiacos rítmicos, normofonéticos, sin soplos ni galope.''',
			
			"abdomen": '''plano,  doloroso a la palpación con herida penetrante en epigastrio. ''',
			
			"extremidades": '''herida penetrante en brazo izquierdo con orificio de entrada y de salida. ''',

			"neurologico": '''Glasgow 3/15 ptos (RM: 1 RO: 1 RV: 1), pupilas midriáticas no reactivas a la luz. ''',

		},  

		
	}, #62

	{
		"IdHistoria": "35-83-40", 
		"nombre": " Luis Antonio Millán Cortesía", 		
		"edad": "33",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1980,5,2), 		
		"lugarNacimiento": "Cumaná-Estado Sucre", 		
		"ci": "14.125.624", 		
		"dirección": "LLANADA sector A vereda 68 nro.12", 		
		"fechaIngresoHUAPA":  datetime(2014,1,6), 		
		"fechaIngresoUCI": datetime(2014,1,17), 		 
		"resumenIngreso": '''Se trata de paciente masculino 33 años de edad, natural y procedente de la localidad, sin antecedentes patológicos de importancia, quien inicia enfermedad actual el día 06 de enero de 2014, cuando posterior a recibir múltiples traumatismos por arma de fuego en abdomen (flanco derecho), región genital y en miembro inferior izquierdo, es trasladado a este centro, donde es evaluado e ingresa por el servicio de Cirugía Blanda con el Diagnóstico de Traumatismo toraco-abdominal penetrante por arma de fuego,  traumatismo urogenital y traumatismo penetrante por arma de fuego en miembro inferior izquierdo. Se lleva a mesa operatoria en donde realizan laparotomía exploradora xifopúbica, encontrándose los siguientes hallazgos: 2500 cc de hemoperitoneo, lesión grado V de bazo, lesión grado I de curvatura mayor de estómago, lesión grado I de cola de páncreas,  lesión grado I en ángulo esplénico del colon y lesión grado III de uretra peneana. Tomándose como conducta evacuación del hemoperitoneo, esplenectomía,  rafia de las lesiones descritas, cistostomía con Foley Nro 18. El paciente posterior a acto quirúrgico permanece en el área de recuperación durante su postoperatorio inmediato y solicitan evaluación por UCI, en vista de no disponer de cupo se hacen sugerencias. Evolucionando de forma no satisfactoria en el Servicio de hospitalización de Cirugía blanda, permanece durante 11 días, recibiendo Metronidazol y Ciprofloxacina. El día 08/01/14 se evidencia en control radiológico de tórax imagen compatible con hemotórax izquierdo por lo que colocan tubo de drenaje torácico, obteniéndose 200 cc de gasto hemático, con posterior control radiológico que demuestra expansibilidad pulmonar y mejoría. Sin embargo el paciente persiste febril y se asocia  en región escrotal salida de secreción purulenta y  fétida con aumento de volumen. Se realiza Eco Doppler Escrotal (13/01/14) que reporta Orquiepididimitis Bilateral. En vista de presentar absceso testicular izquierdo es llevado a mesa operatoria  realizándose drenaje del mismo y se observa trayecto fistuloso a recto extraperitoneal, se realiza abordaje de relaparotomía supra-para-infraumbilical evidenciándose filamentos de fibrina interasas, colección hemato-purulenta en ángulo esplénico de colon y corredera parietocólica izquierda, se evidencia lesión hemidiafragmática izquierda grado III y lesión grado II de curvatura mayor de estómago.  Conducta: colostomía del sigmoide, rafia de lesión gástrica y diafragmática, toracotomía mas colocación de tubo de drenaje torácico izquierdo. Solicitan evaluación y cupo por el servicio de Terapia intensiva y se ingresa. Se recibe paciente en camilla de traslado, intubado, se pasa a cama UCI y se conecta a monitor cardiaco que reporta Fr  26 rpm Fc 160 lpm TA  94/81 TAM 86mmHg SATO2 95%  y se conecta a ventilación mecánica modo AC,  VC 560 (8cc/kg), Fr 12, FiO2 100, Fl 50, PEEP 0.''', 


		"examenFisicoIngresoUCI": {
			
			"piel" : 	'''	morena, fría al tacto, con palidez mucocutánea moderada.''',

			"cardiopulmonar":  '''tórax simétrico hipoexpansible, ruidos respiratorios presentes, sin agregados; ruidos cardiacos taquicárdicos, hipofonéticos, sin soplos ni galope. Tubo de drenaje torácico en HT izquierdo conectado a trampa de agua con gasto serohemático.''',
			
			"abdomen": '''plano, se observa herida de re-laparotomía quirúrgica cubierta de apósitos estériles, y colostomía cubierta por apósitos estériles. ''',

			"neurologico": ''' Glasgow: 3/15ptos (RM: 1pto, RO: 1pto, RV: 1 pto), pupilas isocóricas, hiporeactivas a la luz, bajo sedación. ''',
			"extremidades": '''se observa tutor externo en muslo izquierdo. Sin edema.''',

		}, 

		"diagnosticoIngresoUCI": [
									
									"Postoperatorio inmediato de Relaparotomía supra-para e infra umbilical, drenaje de absceso testicular izquierdo y Colostomía.",
									"Postoperatorio tardío de laparotomía supra-para e infra umbilical por traumatismo toracoabdominal penetrante por arma de fuego complicado con:",
									"Lesión grado V esplénica.",
									"Lesión grado III de Uretra peneana.",
									"Lesión grado I de estómago (curvatura mayor).",
									"Lesión grado I en cola de páncreas.",
									"Lesión grado I en ángulo esplénico de cólon.",
									"Traumatismo urogenital complicado con absceso escrotal izquierdo.",
									"Trastorno Hematológico: Anemia Severa.",
									"Trastorno ácido base: acidosis metabólica descompensada +Hiperoxemia.",

								],  

		"examenFisicoIngresoHUAPA": {
		
			"piel": ''' morena, palidez cutáneo mucosa moderada, afebril, normohidratada. ''',
			"cardiopulmonar": '''tórax simétrico hipoexpansible, ruidos respiratorios presentes, discretamente disminuidos en HT izquierdo, sin agregados; ruidos cardiacos rítmicos taquicárdicos, sin soplos ni galope.''',
			"abdomen": '''globoso,  doloroso a la palpación superficial y profunda, con herida penetrante en flanco izquierdo. ''',
			"extremidades": '''Herida penetrante en miembro inferior izquierdo con orificio de entrada y de salida. ''',
			"neurologico": '''Somnoliento FM: 2/4.''',
			"genitales": ''' se observan múltiples heridas por proyectil por arma de fuego en testículos y región perineal; uretrorragia.''',

		},  
		
	}, # 63

	{
		"IdHistoria": "52-02-99", 
		"nombre": "Ramón Gabriel Montaño Lárez", 		
		"edad": "44",
		"sexo": "M",	
		"fechaNacimiento": datetime(1969,8,31),		
		"lugarNacimiento": "Carúpano - Estado Sucre", 		
		"ci": "12.288.473", 		
		"dirección": "Calle Junin Nro 2 - Carúpano", 		
		"fechaIngresoHUAPA": datetime(2014,5,8),		
		"fechaIngresoUCI":datetime(2014,5,8),		
		"antecedentes": ''' Paciente con antecedentes de hipertensión arterial sin tratamiento. Accidente de tránsito tipo colisión en moto con TCE hace 8 meses. Hábitos Psicobiológicos:Fumador de larga data de cigarrillo y tabaco 1 caja diaria desde los 15 años aproximadamente.Hábitos alcohólicos acentuados, hasta llegar a la embriaguez, todos los días desde hace 5 meses.''',

		"resumenIngreso": '''Se trata de paciente masculino 44 años de edad, natural y procedente de Carúpano, con antecedentes de Hipertensión Arterial no tratada y de accidente de tránsito tipo colisión en moto hace 8 meses, cuyo familiar refiere inicio de enfermedad actual hace una semana, caracterizada por cefalea de aparición súbita, leve intensidad, atenuado con acetaminofén. Persiste sintomático, el día 05/05/2014 se anexa al cuadro clínico somnolencia; el día 07/05/2014  presenta perdida de la consciencia, del tono postural y relajación de esfínter vesical, es trasladado al Hospital de la localidad en donde evalúan e ingresan encontrándose con estado de agitación psicomotriz,  lenguaje disártrico y pupilas anisocóricas.  Se realiza TAC de Cráneo la cual reporta: Hematoma Subdural fronto-parietal derecho con desplazamiento de línea media, colapso de ventrículo derecho, por lo que es evaluado por el servicio de Neurocirugía el día 09/05/2014, indicando drenaje del mismo sin embargo por no contar con cupo en terapia intensiva, para el post-quirúrgico, lo refiere a este centro de salud, en donde ingresa por el Servicio de Neurocirugía y es evaluado por Dr. Montaño quien por hallazgos clínicos y paraclínicos decide llevar a mesa operatoria para exploración y drenaje, se solicita cupo a UCI para el postoperatorio inmediato.  ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente es trasladado en camilla de transporte, conectado a monitor cardíaco externo que reporta signos vitales: TA: 130/78mmHg TAX: 89mmHg FC: 90lpm FR: 14rpm SatO2: 99%, intubado conectado a ventilador de transporte, se pasa a cama de UCI, conectándose a monitor cardiaco externo que reporta signos vitales: TA: 150/114 mmHg TAX: 121mmHg FC: 118 lpm FR: 16 rpm SPO2: 99% ''',
			
			"piel" : 	'''Blanca, hipertérmica al tacto, llenado capilar <3 segundos.''',

			"cardiopulmonar":  ''' se conecta a ventilador EVITA 4 con parámetros: A/C Fr: 12 FIO2: 95 FL: 50 VC: 560 (8cc/kg) Peep: 0. A la auscultación tórax simétrico, normo expansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos normofonéticos, taquicárdicos,  sin soplos ni galope. 	''',
			
			"abdomen": ''' blando, plano, depresible, no impresiona doloroso a la palpación, ruidos hidroaéreos presentes, no megalias. ''',

			"neurologico": ''' bajo efectos de sedación y relajación, pupilas anisocóricas, hiporreactivas a respuesta a la luz, Glasgow: no evaluable por sedación.''',
			
			"cabeza": '''De aspecto y configuración normal, se evidencia signo de equimosis palpebral bilateral y múltiples escoriaciones faciales.''',

		}, 

		"diagnosticoIngresoUCI": [
									"Postoperatorio Inmediato de Drenaje de hematoma subdural frontoparietal derecho.",
									"Hipertensión Arterial.",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente en Rs Cs Gs, eupneico, tolerando aire ambiente, afebril.''',
			"piel": ''' Blanca, normotérmica al tacto, llenado capilar <3 segundos.''',
			"cardiopulmonar": '''Tórax simétrico, normo expansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos normofonéticos, taquicárdicos,  sin soplos ni galope.  ''',
			"abdomen": '''blando, plano, depresible, no impresiona doloroso a la palpación, ruidos hidroaéreos presentes, no megalias ''',
			"extremidades": '''simétricas sin edema. ''',
			"neurologico": '''Estuporoso, agitado, pupilas anisocóricas, pupila derecha puntiforme hiporreactiva, midriasis izquierda arreactiva a la luz, Glasgow: 12/15ptos dado por RO: 3 pto, RV: 3 ptos  RM: 6 ptos.  ''',
			"cabeza": ''' De aspecto y configuración normal, sin evidencia de estigmas ni equimosis.''',

		},  

		"diagnosticoIngresoHUAPA": [
						"Hematoma Subdural fronto-parietal derecho.",	

		], 
		
	}, #64

	{
		"nombre": "Berhioska Valentina Pérez Velázquez", 		
		"edad": "27",
		"sexo": "F",	
		"fechaNacimiento": datetime(1987,10, 13),		
		"lugarNacimiento": "Carúpano - Estado Sucre", 		
		"ci": "18.416.870", 		
		"dirección": "Urbanización Los Araguaney. ", 		
		"fechaIngresoHUAPA": datetime(2015,4, 10), 		
		"fechaIngresoUCI":datetime(2015,4, 10), 		
		"resumenIngreso": '''Se trata de paciente femenina de 27 años de edad, natural de Carúpano procedente de la localidad con antecedentes quirúrgico de mamoplastia del año (2015), amigdalectomia (2009). Quien refiere inicio de enfermedad actual el día sábado cuando presenta malestar general y rinorrea hialina anterior. El día martes 07/04/2015 se anexa al cuadro aumento de la temperatura corporal cuantificado en 39 ºC acompañado de escalofríos y cefalea Holocraneana de moderada intensidad irradiado a región cervical, por lo que auto medica con atamel forte (acetaminofén 650mg) cada 4 horas, persistiendo sintomática motivo por el cual acude a centro privado donde indican novalcina (1 gramo) e hidratación parenteral, con mejoría del cuadro febril durante 4 horas aproximadamente. En vista de persistir sintomática acude el día  08/04/2015 a Especialista Dra. Maribel Morillo (infectólogo) quien le impresiona diagnóstico de Mononucleosis Infecciosa por lo cual indica tratamiento con atamel  y migren. Persistiendo sintomática y anexándose al cuadro clínico fotofobia y exacerbación de la cefalea por lo que acude el día 09/04/2015 a centro privado donde es evaluada por intensivista Dra. Norka Patiño quien decide ingreso en UCI con los diagnósticos. Encefalitis viral  Síndrome viral Cefalea en estudio. Permanece durante 24 horas en servicio de terapia intensiva, es evaluada por neurólogo Dr.  Aponte quien realiza punción lumbar que reporta solo hallazgo positivo (proteinorraquia), recibiendo tratamiento médico con Manitol al 18 % (24 horas), Aciclovir 500mg cada 8 horas (24 horas) y por condiciones socioeconómicas se decide su traslado a este centro asistencial donde se evalúa e ingresa.''', 

		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente  en camilla de transporte respirando aire ambiente sin monitoreo cardiaco se traslada a cama de uci y se conecta a monitor cardiaco que reporta:  TA: 112/75 (96) mmHg FC: 75 lpm	FR: 16 rpm	SPO2:98%''',
			
			"piel" : 	'''	morena, Hidratada, Normotérmica al tacto, llenado capilar <3 segundos.	''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible ruidos respiratorios presentes en ambos hemitorax sin agregados. Ruidos cardiacos rítmicos no soplos. ''',
			"abdomen": ''' Blando depresible no doloroso a la palpación superficial ni profunda no megalias''',

			"neurologico": '''Paciente consciente, orientada en 3 planos lenguaje coherente, pupilas isocóricas normorreactivas a la luz Glasgow 15/15 pts, Respuesta Motora: 6pts, Respuesta Verbal: 5pts, Apertura Ocular: 4pt.  FM V/V. sin signos meníngeos. ''',
			"ojos": '''movimientos oculares conservados, fotofobia.''',

		}, 

		"diagnosticoIngresoUCI": [

									"Síndrome viral",
									"Encefalitis viral a descartar",
									"Trastorno hematológico:",
									"Anemia leve.",
									"Ttrombocitopenia.",
									"Leucopenia.",
									"Prolongación del PTT",
									"Trastorno hidroelectrolítico: hipokalemia",

									
								],  
		
	},# 65

	{
		"nombre": "Carmen Virginia Martínez De Guzmán ", 		
		"edad": "56",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1958, 2, 1), 		
		"lugarNacimiento": "Carúpano-Estado Sucre, ", 		
		"ci": "5.861.435", 		
		"dirección": "Cumaná, Residencias Santa Elena. Frente al IUT- Vía Cantarrana", 		
		"fechaIngresoHUAPA":  datetime(2014, 3, 2), 		
		"fechaIngresoUCI": datetime(2014, 3, 2), 		
		
		"resumenIngreso": '''Se trata de paciente femenina de 56 años de edad, natural de Carúpano y procedente de la localidad, con antecedentes de LES en tratamiento con Medrol 4mg OD, Mielitis Transversa desde hace 5 años encamada con escara sacra, Hipertensa controlada con Cardiopril y Norvasc 5mg OD. Antecedente de hospitalización reciente en centro privado por cuadro diarreico agudo tipo Amebiasis Intestinal recibiendo Metronidazol y Ciprofloxacina durante 3 días y egresa sin tratamiento. Inicia enfermedad actual el 27 de Enero del presente año cuando presenta movimiento tónico clónico focalizado en hemicara y miembro superior izquierdo, acompañado de agitación psicomotriz y llegando a status convulsivo, es evaluada el día 28/01/14 por intensivista Dra. Begglia Roa quien indica ingresar a UCI de centro privado en donde por deterioro neurológico y ventilatorio, se realiza intubación endotraqueal y se conecta a ventilación mecánica, con los diagnósticos: Estatus convulsivo, Neumonía por Broncoaspiración, Sepsis de p/p partes blandas, LES e HTA. Permanece en condiciones de cuidado recibiendo Tazopril en el contexto de la IRB, sin embargo por presentar trastorno hidroelectrolítico tipo Hipokalemia se decide suspender y rotar a Meropenem, se asocia Zyvox y fluconazol. Es  evaluada por Neurólogo Dr. Ortíz  quien indica Tegretol 400mg cada 8 horas.  Se toman muestras para pancultivar y pruebas inmunológicas. Por tratarse de una paciente de larga estancia y con autorización de los familiares se decide su traslado a UCI HUAPA.''', 

		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente es trasladada en camilla de transporte, intubada con apoyo de oxígeno por Ambú, se pasa a cama de UCI, conectándose a monitor cardiaco externo que reporta: TA: 98/72mmHg    TAX: 72mmH  FC: 90 lpm	FR:12 rpm   SPO2: 100 %. Recibiendo Levophed a una concentración de 64 mcg /cc, Dosis de 10,66 mcg/min. Se conecta a ventilación mecánica EVITA 4 con parámetros: MODO SIMV/ FR 12/ FIO2 90/VC 560/ FL50/ PS 15/ PEEP 0/ tinsp 0,95. ''',
			
			"piel" : 	'''	Blanca, normotérmica al tacto, con ligero tinte ictérico, llenado capilar >3 segundos con múltiples equimosis y escara en región glútea y escapular derecha y  región sacra izquierda con exposición de tejidos blandos.''',

			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos rítmicos, hipofonéticos,  sin soplos ni galope. 	''',
			"abdomen": ''' Blando, globoso a expensas de panículo adiposo en anasarca, depresible, deja fóvea, ruidos hidroaéreos ausentes, no megalias. ''',

			"neurologico": ''' Somnolienta, pupilas isocóricas, hiporreactivas la luz, Glasgow: 9/15ptos dado por RO: 2 ptos RV: 1pto limitado por tubo RM: 6 ptos. Arreflexica.''',
			"extremidades": '''Masas musculares hipotróficas, con múltiples equimosis en piel.''',
			"genitales": ''' vulva y periné edematizados con múltiples flictenas. ''',

		}, 

		"diagnosticoIngresoUCI": [
									

									"Shock séptico.",
									"Infección Respiratoria Baja: Neumonía por Broncoaspiración Vs Nosocomial.",
									"Escaras en región glútea- sacra- escapular.",
									"Síndrome convulsivo.",
									"Lupus Eritematoso Sistémico.",
									"Mielitis Transversa.",
									"HTA Sistémica.",
									"Trastorno Metabólico: Hipoalbuminemia e Hipoglicemia. ",
									"Trastorno Acido-Base: Acidosis metabólica compensada.",
									"Trastorno Hematológico: Anemia Moderada, Ptt y Pt prolongados y Trombocitopenia.",

								],  
		
	},# 66

	{
		"nombre": "Euliser Del Rosario Ceijas", 		
		"edad": "50",
		"sexo": "M",	
		"fechaNacimiento": datetime(1963, 10, 7), 		
		"lugarNacimiento": "Urb. Cristobal Colón, Las villas, calle 7 nro 436. Estado Sucre.", 		
		"ci": "8.649.784", 		
		"dirección": "Cumaná – Estado Sucre.", 		
		"fechaIngresoHUAPA":  datetime(2014, 2, 7), 		
		"fechaIngresoUCI": datetime(2014, 2, 7), 		
	
		"resumenIngreso": ''' Se trata de paciente masculino de 50 años de edad, natural y procedente de la localidad, con antecedentes patológicos de Hipertensión Arterial Sistémica e Insuficiencia Cardíaca de larga data tratada con Betalok y Exforge, Alergia a la Novalcina. Cuyo familiar refiere inicio de enfermedad actual el día 07/02/2014 cuando posterior a perdida de la consciencia, presenta accidente de tránsito tipo colisión con objeto fijo, es trasladado a la Emergencia del HUAPA en donde evidencian desviación de la comisura labial derecha y pérdida de la fuerza muscular de hemicuerpo derecho, por petición de los familiares es llevado a centro clínico privado e ingresa a la unidad de cuidados intensivos con signos vitales TA: 200/100mmHg, FC 110lpm, FR: 22rpm, piel: palidez moderada, Cardíaco: ápex palpable en 7mo-8vo espacio intercostal, línea axilar anterior, Ruidos cardiacos taquicárdicos R3-R4 presentes soplo holosistólico mitral. Pulmonar: roncus difusos bilaterales. Abdomen: distendido, RsHsPs, Neurológico: somnoliento, desviación de rasgos faciales, hemiplegía derecha, afasia mixta, babinsky derecho presente. Impresión diagnóstica Crisis hipertensiva tipo Emergencia expresada en EVC Isquémico, Taquicardia supraventricular, Cardiopatía hipertensiva e Isquémica, Insuficiencia Cardíaca, Valvulopatía Mitral, Trastorno de la conducción BRIHH, Gastritis Crónica y Pancreatitis crónica.  En vista de condiciones socio-económicas y disponibilidad de cupo se decide su traslado  a este centro de salud. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de transporte con monitor cardíaco externo que reporta TA: 166/11mmHg FC: 102lpm FR 16rpm. Recibiendo apoyo de Oxígeno por bigote nasal a 5 litros por minuto. Se coloca en cama de UCI y se conecta a monitor cardíaco que reporta Signos Vitales: TA: 168/111 mmHg TAX: 128mmHg FC: 118lpm FR: 14rpm SatO2: 98% ''',
			
			"piel" : 	'''	afebril al tacto, deshidratado, mucosa oral escasa saliva.''',

			"cardiopulmonar":  '''ruidos cardíacos taquicárdicos con ritmo de galope, ruidos respiratorios disminuidos en ambas bases, Roncus dispersos.''',
			"abdomen": '''plano blando depresible, no megalias; no impresiona doloroso.''',

			"neurologico": ''' Somnoliento, afásico, pupilas isocóricas normoreactivas a la luz, Glasgow: RO: 4ptos, RV: 2 ptos; RM: 6 ptos  12/15ptos. Reflejos osteotendinosos presentes hiperreflexico. Hemiparesia derecha. ''',
			"extremidades": '''simétricas sin edema, hemiparesia derecha. ''',

		}, 

		"diagnosticoIngresoUCI": [

								"Emergencia Hipertensiva Expresada en EVC isquémico HCI extenso.",
								"Hipertensión Arterial Sistémica.",
								"Cardiopatía Isquémica e Hipertensiva.",
								"Insuficiencia Cardíaca.",
								"Valvulopatía  Mitral.",
								"Gastritis crónica.",
								"Trastorno Hematológico: PTT prolongado.",
								"Trastorno Acido-Base: Acidosis Metabólica compensada en Alcalosis Respiratoria con normoxemia.",

									
								],  
	}, #67

	{
		"nombre": "Ángel Gregorio Cabello Rojas", 		
		"edad": "73",
		"sexo": "M",	
		"fechaNacimiento": datetime(1941,1,30), 		
		"lugarNacimiento": "Cumaná. Edo. Sucre.", 		
		"ci": "538.857", 		
		"dirección": "Parcelamiento Miranda, sector “F”, 2da transversal, calle Caicara, qta. Adela #41.", 		
		"fechaIngresoHUAPA":  datetime(2014,5,25), 		
		"fechaIngresoUCI": datetime(2014,5,25), 		

		"resumenIngreso": '''Paciente masculino de 73 años de edad, natural y procedente de la localidad, con antecedente de HTA sistémica de larga data controlada con losartan y enalapril (no precisan dosis), cuyo familiar refiere inicio de enfermedad actual el día de hoy 25/05/14 a las 6pm aproximadamente, cuando presenta dolor típico coronario, acompañado de disnea en reposo, motivo por el cual es traído a este centro asistencial donde evalúan e ingresan por el servicio de Medicina Interna con los diagnósticos de SCA: IM con elevación del segmento ST, indican isordil 5mg VSL en 2 oportunidades sin mejoría de cuadro clínico. En vista de estado general del paciente, solicitan valoración por UCI, se acude a valorar paciente al área de choque y previa autorización de Dra. Roa, por cuadro clínico antes descrito, se decide su ingreso.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, recibiendo O2 por bigote nasal, se pasa a cama UCI, se conecta a monitor cardíaco continuo que reporta: TA: 117/57(79) mmHg; FC: 115 lpm; FR: 25 rpm; SatO2: 99%. Se realiza ECG de 12 derivaciones evidenciándose elevación del segmento ST desde V1 a V6, por lo que en vista de encontrarse dentro de ventana terapéutica, se procede a trombolizar con Estreptoquinasa 1500000Uds, obteniendo mejoría del dolor precordial y ligera disminución de elevación del segmento ST. ''',
			
			"piel" : 	'''	morena, normotérmica al tacto, llenado capilar < 3seg.''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, taquicárdicos, sin soplo ni galope.	''',
			"abdomen": ''' globoso a expensas de panículo adiposo, ruidos hidroaéreos presentes, blando, depresible, no doloroso a la palpación, no megálico''',

			"neurologico": ''' consciente, agitado, pupilas isocóricas, normorreactivas a la luz, Glasgow 15/15pts ''',

		}, 

		"diagnosticoIngresoUCI": [
									"SINDROME CORONARIO AGUDO: IM CON ELEVACION DEL SEGMENTO ST ANTERIOR EXTENSO TROMBOLIZADO",
									"HTA SISTEMICA",
								],  
		
	},# 68

	{
		"IdHistoria": "52-05-82 ", 
		"nombre": "Cesar Augusto Leonice ", 		
		"edad": "40",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1965,9,28), 		
		"lugarNacimiento": "cumana ", 		
		"ci": "11.373.893", 		
		"dirección": "Mundo Nuevo con santa Inés ", 		
		"fechaIngresoHUAPA":  datetime(2014,5,17), 		
		"fechaIngresoUCI": datetime(2014,6,5), 		
	
		"resumenIngreso": ''' Paciente masculino de 40  años de edad , natural y procedente de la localidad sin antecedentes patológicos conocidos quien inicia enfermedad actual hace aproximadamente  20 dias cuando posterior a herida por proyectil de  arma de fuego en hemitorax izquierdo es traido a este centro donde se evalua y se ingresa ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubado recibiendo O2 por ventilador mecanico , se pasa a cama de UCI y se conecta a monitor cardíaco continuo que reporta: TA: 115/68(67) mmHg; FC: 106 lpm; FR: 25 rpm; SatO2: 100% ''',
			
			"piel" : 	'''	morena, normotérmica al tacto, llenado capilar < 3seg. Temperatura: 36,4 ''',

			"cardiopulmonar":  '''tórax simétricos, normoexpansible , ruidos respiratorios presentes disminuidos en base derecha, sin agregados. Ruidos cardíacos rítmicos, taquicardicos, sin soplo ni galope.''',
			"abdomen": ''' plano, blando, ruidos hidroaéreos presentes no impresiona doloroso a la palpación, no megálico.''',

			"neurologico": ''' Bajo efectos de sedantes y relajantes musculares. ''',
			
			"extremidades": '''Miembro superior izquierdo con herida en región pectoral cubierta por aposito esteril sin evidencia de sangrado ''',

		}, 

		"diagnosticoIngresoUCI": [

								"POI BYPASS DE ARTERIA AXILAR IZQUIERDA  DE TERCIO PROXIMAL A TERCIO DISTAL CON AUTOINGERTO DE VENA SAFENA  INTERNA DERECHA INVERTIDA  LATEROTERMINAL.",
								"TTNO METABOLICO : HIPERGLICEMIA ",
								"TTNO ACIDO BASICO ACIDOSIS METABOLICA DESCOMPENSADA ",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 107/68(67) mmHg; FC: 86 lpm; FR: 15 rpm; SatO2: 100%. Paciente que permanece en sala de cirugía siendo evaluado por cirugía vascular indicándose ANGIOTAC de MS Izquierdo donde se evidencia signos de compromiso tatal de flujo vascular en arteria axilar izquierda  con circulación compensadora colateral con recanalizacion hacia el aspecto proximal de la arteria braquial o humeral izquierda  Paciente que es plnificado para intervención quirúrgica abordaje transpectoral con extensión axilar izquierda donde se evidencia lesión de 5 cm diámetro con obliteración de la luz se toma como conducta realización de : BYPASS DE ARTERIA AXILAR IZQUIERDA  DE TERCIO PROXIMAL A TERCIO DISTAL CON AUTOINGERTO DE VENA SAFENA  INTERNA DERECHA INVERTIDA  LATEROTERMINAL. Paciente que es trasladado a area de terapia intensiva para su adecuado seguimiento ''',
			"piel": ''' morena, normotérmica al tacto, llenado capilar < 3seg. Temperatura: 36,5 ''',
			"cardiopulmonar": '''tórax simétricos, hipoexpansible, ruidos respiratorios presentes disminuidos en base derecha, sin agregados. Ruidos cardíacos arrítmicos, taquicardicos, sin soplo ni galope.Se evidencia orificio de 1 cm en hemitorax  izquierdo  primer espacio intercostal con línea axilar anterior con salida de gasto hematico abundante asi como aumento de volumen de tercio superior de hemitorax.''',
			"abdomen": '''plano, blando, ruidos hidroaéreos presentes aumentados, no impresiona doloroso a la palpación, no megálico. ''',
			"extremidades": '''Extremidad superior izquierda aumento de volumen de brazo izquierdo que no deja fóvea doloroso limitación funcional pulso presente y disminuido''',
			"neurologico": '''Consciente orientado en tiempo espacio y persona.''',

		},  

	},#69


	{
		"IdHistoria": "44–60–86", 
		"nombre": "Ángel Gabriel Medina Zerpa", 		
		"edad": "22",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1992,11,10), 		
		"lugarNacimiento": "Cumaná, Edo. Sucre", 		
		"ci": "20.992.622", 		
		"dirección": "La Chica, calle principal, casa S/N, Mariguitar, Edo. Sucre.", 		
		"fechaIngresoHUAPA":  datetime(2014,3,14), 		
		"fechaIngresoUCI": datetime(2014,3,15), 		
	
		"resumenIngreso": '''Paciente masculino de 22 años de edad, natural de Cumaná y procedente de Mariguitar, sin antecedentes patológicos, cuyo familiar refiere inicio de enfermedad actual el 14/03/2014 cuando posterior a riña recibe herida por proyectil de arma de fuego transfixiante en cráneo, con orificio de entrada en región parietal izquierda y salida en región maxilar derecha, motivo por el cual es traído a este centro asistencial donde es ingresado por el servicio de neurocirugía; al momento del ingreso se encuentra consciente, desorientado, con pupilas anisocóricas (midriasis izquierda, arreactiva a la luz, izquierda normorreactiva a la luz), Glasgow 11/15pts (RM: 6pts, RO: 3pts, RV: 2pts). Solicitan valoración por UCI, siendo evaluado en área de quirofanito de emergencia, en vista de condiciones generales del paciente y por autorización de Dr. Guaimare (Intensivista de Guardia) se decide su ingreso a UCI y dicta órdenes médicas.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, recibiendo O2 por mascarilla facial con sonda corrugada a 10LtrsX’, se pasa a cama UCI y se conecta a monitor cardíaco continuo que reporta: TA: 142/89(115) mmHg; FC: 100 lpm; FR: 24 rpm; SatO2: 100% ''',
			
			"piel" : 	'''	morena, normotérmica al tacto, llenado capilar < 3seg. ''',

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, taquicardicos, sin soplo ni galope.''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, blando, depresible, no doloroso a la palpación, no megálico.''',

			"neurologico": '''consciente, con agitación psicomotriz, desorientado en tiempo y espacio, orientado en persona, pupilas anisocóricas, izquierda midriática arreactiva a la luz, derecha normorreactiva a la luz, de aproximadamente 4mm, ROT II/IV, impresiona monoparesia braquial derecha, Glasgow 14/15pts (RM: 6pts, RO: 3pts, RV: 5pts). ''',
			"extremidades": '''	herida por arma de fuego en ambos miembros superiores, sin deformidades ni limitación funcional.''',
			"cabeza": ''' con apósitos con secreción hemática moderada sobre orificios de entrada en región parietal izquierda y orificio de salida en región maxilar derecha.''',

		}, 

		"diagnosticoIngresoUCI": [

								"TRAUMATISMO CRANEOENCEFALICO LEVE POR HERIDA POR PROYECTIL DE ARMA DE FUEGO",
								"TRASTORNO ACIDO-BASE:",
								"ACIDOSIS METABOLICA COMPENSADA CON ALCALOSIS RESPIRATORIA + HIPEROXEMIA",
								],  

		
	}, # 70

	{
		"nombre": "Angela Custodia Acosta de Salazar ", 		
		"edad": "88",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1926,10,2), 		
		"lugarNacimiento": "San Antonio del Golfo ", 		
		"ci": "2.647.604", 		
		"dirección": "San Antonio del Golfo ", 		
		"fechaIngresoHUAPA":  datetime(2014,9,6), 		
		"fechaIngresoUCI": datetime(2014,9,6), 		
		"antecedentes": ''' DIABETES MELLITUS TIPO 2, QX : Fractura fémur derecho CARDIOPATIA HIPERTENSIVA ''', 
		"resumenIngreso": '''Paciente femenina de 88 años de edad natural y procedente de la localidad con antecedentes patológicos conocidos de diabetes Mellitus tipo 2 para lo cual lleva tratamiento que no precisa e hipertensión arterial sistémica con tratamiento habitual Norvasc 10 mg OD ,inicia enfermedad actual hace aproximadamente 24 días ( 12-08-14) cuando presenta  lesión eritematosa en región del hallux pie derecho con posterior salida de secreción purulenta por lo cual fue llevada a ambulatorio de la localidad indicándose tratamiento con ciprofloxacina sin mejoría de cuadro clínico  es llevada nuevamente a ambulatorio y referida a este centro donde ingresa el día 22-08 14  ,evidenciándose necrosis completa del hallux y ulcera en dorso del pie derecho y lesiones húmedas vesiculares en tobillo y cara anterior de la pierna ,se indica tratamiento que no se precisa manteniendo evolución tórpida ,siendo trasladada a clínica de la localidad a petición de los familiares el día 1-09-14 donde ingresa con los diagnósticos: 1. Necrosis compleja de hallux y pie derecho, 2. Arteropatía obstructiva periférica,  3. Hipertensión arterial sistémica,  4. Diabetes Mellitus tipo 2,  Paciente que es ingresada en sala de cuidados intensivos iniciándose tratamiento antibióticoterapia  con tazopril y tygacil , al tercer día de hospitalización comienza con disnea intensa , utilización de músculos accesorios , presencia de estertores crepitantes en bases pulmonares, desaturaciòn por lo que se inicia tratamiento con diuréticos y se realiza intubación endotraqueal sin complicaciones ,conectándose a ventilación mecánica con los parámetros MODO AC  VC 590 FR 14 FIO2 60 FL 70 .Es evaluada por traumatólogo de guardia quien decide el día 5-09-14 realizar Amputación infrapatelar de miembro inferior derecho debido a necrosis múltiples en pie derecho por arteropatia obstructiva ,debido a situación socioeconómica desfavorable se refiere a HUAPA. Se recibe paciente en camilla de traslado, intubado y recibiendo O2 por Ambú®, se pasa a cama UCI, se conecta a ventilación mecánica modo A/C, Vc: 400, FR: 12, FiO2: 50, Fl: 50, PEEP: 0 y se conecta a monitor cardíaco continuo que reporta: TA: 122/48  mmHg;     FC: 85 lpm;      FR: 25 rpm;      SatO2: 100% Paciente inestable hemodinámicamente recibiendo Levophed a razon de 21.3 mcg min Electrocardiograma : RS/83/0,16/0,16/0/0,36 TAS: LESION SUBEPICARDICA ANTERIOR EXTENSO, BIRIHH, FARVA  ''', 


		"examenFisicoIngresoUCI": {

			
			"piel" : 	'''	blanca, hipotérmica al tacto, llenado capilar < 3seg.''',

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, sin soplo ni galope.''',
			"abdomen": ''' globoso, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico, con herida quirúrgica cubierta por apósitos con escasa secreción serohemática.''',

			"neurologico": ''' somnolienta Glasgow 9/15 puntos dados por RM 5 RO 3  RV 1 Pupilas isocóricas reactivas ''',
		}, 

		"diagnosticoIngresoUCI": [

									"SHOCK CARDIOGENICO ",
									"SINDROME CORONARIO AGUDO : IM CON ELEVACION DEL ST ANTERIOR EXTENSO", 
									"SEPSIS PUNTO DE PARTIDA PARTES BLANDAS", 
									"POM AMPUTACION INFRAPATELAR MIEMBRO INFERIOR DERECHO",
									"ARTEROPATIA OBSTRUCTIVA MIEMBRO INFERIOR DERECHO",
									"DIABETES MELLITUS TIPO 2 EN HIPERGLICEMIA", 
									"HIPERTENSION ARTERIAL SISTEMICA ",
									"TTNO HEMATOLOGICO : ANEMIA MODERADA ",
									"TTNO METABOLICO: HIPERGLICEMIA", 
									"TTNO HE : HIPOKALEMIA SEVERA", 

									
								],  

	

		"diagnosticoIngresoHUAPA": [
								"POI DE AMPUTACION INFRAPATELAR DERECHA", 
								"SEPSIS PUNTO PARTIDA PIE DERECHO ",
								"INSUFICIENCIA RESPIRATORIA EDEMA AGUDO DEL PULMON", 
								"INFECCION RESPIRATORIA BAJA ",
								"DIABETES MELLITUS DESCOMPENSADA ",
								"CARDIOPATIA HIPERTENSIVA ",
								"SHOCK SEPTICO", 

		], 
		
	}, #71

	{
		
		"nombre": "Meaño Campos Carlos Eduardo", 		
		"edad": "51",
		"sexo": "M",	
		"fechaNacimiento": datetime(1962,10,29), 		 		
		"ci": "5.700.705", 		
		"dirección": "Urb. Cristóbal Colon Calle 6 Nro. 384", 		
		"fechaIngresoHUAPA": datetime(2014,4,18), 		
		"fechaIngresoUCI":datetime(2014,4,18), 		
		"resumenIngreso": '''Paciente masculino de 51 años de edad, natural y procedente de la localidad,  antecedentes patológicos: HTA y Diábetes Mellitus tipo  mal controlada con nefropatía diabética complicada con Fallo Renal en Estadío V (hemodiálisis 3 veces por semana) con fistula arterio-venosa desde hace 1 mes, cuyo familiar refiere inicio de enfermedad actual cuando presenta lesiones tipo vesículas en dorso de mano izquierda (sitio de la fistula) las cuales evolucionan a pústulas, con extensión progresiva y aleatoria, posteriormente se anexa crepitación en toda la extremidad afectada, por lo cual es evaluado por infectólogo  quien indica su ingreso a centro clínico privado  el 15/04/2014, en vista de las malas condiciones se decide pasar a Unidad de Cuidados Intensivos, al examen físico de ingreso de  UCI se observa intolerancia al decúbito dorsal, con leve tinte ictérico de piel y mucosas, hipotenso, se inicia oxigenoterapia y monitoreo cardíaco continuo obteniéndose signos vitales: TA 85/45mmHg, TAX 62 mmHg FC: 80lpm, FR: 15 rpm; Sat O2 100%. Tórax simétrico expansible, Rs Rs Ps  disminuidos en ambas bases, sin agregados  pulmonares. Abdomen blando globoso, Rs Hs Ps, depresible no doloroso. Extremidades: simétricas edema º II/VI de extremidades inferiores, miembro superior izquierdo se observa edematizado, con lesiones tipo ampollas que confluyen en  flictenas de diversos tamaños con contenido seropurulento de distribución aleatoria. Neurológico: somnoliento, pupilas isocóricas normorreactivas, lenguaje coherente. El paciente permanece durante 72 horas sin embargo con evolución tórpida recibiendo tratamiento con Meropenem, Zyvox, Penicilina Cristalina y Clindamicina, inicia apoyo de Vasoactivos el día 17/04/2014 y en vista de ameritar apoyo de hemodiálisis por elevación de azoados se solicita cupo en UCI – HUAPA y se traslada a este centro donde se ingresa por orden del Dr. Alpino y Dra. Cortesia Intensivista de guardia.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, recibiendo O2 por bigote nasal a 5LtrsX’, se pasa a cama UCI y se conecta a monitor cardíaco continuo que reporta: TA: 129/68 (89) mmHg; FC: 53 lpm; FR: 15 rpm;SatO2: 94% T: 35 ºC''',
			
			"piel" : 	'''palidez cutáneo mucosa, tinte ictérico de piel y escleras, fría al tacto, llenado capilar <3seg, deshidratado, mucosa oral escasa saliva''',

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes disminuidos en ambas bases, sin agregados. Ruidos cardíacos rítmicos y regulares, bradicárdicos, sin soplo ni galope.	''',
			"abdomen": '''Plano, ruidos hidroaéreos presentes, blando globoso a expensas de panículo adiposo, depresible, no impresiona doloroso a la palpación, no megálico.''',

			"neurologico": '''Somnoliento, orientado en tiempo y persona, pupilas isocóricas, normorreactivas a la luz, ROT II/IV, Glasgow 14/15pts (RM: 6pts, RO: 3pts, RV: 5pts).''',
			"extremidades": '''Miembro superior izquierdo cubierto con apósitos estériles con escasa secreción purulenta en lesiones tipo flictenas. Miembros inferiores edema º II/VI.''',

		}, 

		"diagnosticoIngresoUCI": [

									"SHOCK SÉPTICO. ",
									"SEPSIS DE P/P BLANDAS: ",
									"CELULITIS GANGRENOSA DE MIEMBRO SUPERIOR IZQUIERDO (FISTULA A-V)",
									"FALLA DE MÚLTIPLES ÓRGANOS: HEPÁTICO, CARDIOVASCULAR Y NEUROLÓGICO.",
									"ENFEMEDAD RENAL CRÓNICA ST V(HEMODIÁLISIS)",
									"HIPERTENSIÓN ARTERIAL SISTÉMICA.",
									"DIÁBETES MELLITUS TIPO 2.",
									"TRASTORNO HEMATOLOGICO:",
									"ANEMIA MODERADA.",
									"PTT PROLONGADO.",
									"TRASTORNO ACIDO-BASE:",
									"ACIDOSIS METABÓLICA COMPENSADA.",
									"TRASTORNO HIDROELECTROLÍTICO:",
									"DESHIDRATACIÓN MODERADA.",
									"HIPERKALEMIA.",

									
								],  

	},# 72

	{
		"nombre": "Carmen Hortencia Arrioja de Castillo", 		
		"edad": "71",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1943,1,25), 		
		"lugarNacimiento": "Cumaná, Edo. Sucre", 		
		"ci": "5.689.760 ", 		
		"dirección": "San Luis II, Vereda 19, casa # 10.", 		
		"fechaIngresoHUAPA":  datetime(2014,4,28), 		
		"fechaIngresoUCI": datetime(2014,4,28), 		
		"resumenIngreso": '''Paciente femenina de 71 años de edad, natural y procedente de la comunidad, con antecedente de Hipotiroidismo diagnosticado hace 8 años aproximadamente, en tratamiento con Eutyrox® 100mg OD, cuyo familiar refiere inicio de enfermedad actual el día 23/04/14 cuando presenta disnea en reposo, posteriormente somnolencia, debilidad generalizada y lenguaje disártrico, es llevada a centro privado y evaluada por especialista (Neurólogo) quien diagnostica Síndrome de Pickwick y solicita valoración por Internista quien evalúa y decide su ingreso en sala de hospitalización. Permanece hasta el día 26/04/14  cuando por evolución tórpida de cuadro clínico caracterizado por aumento de temperatura corporal, deterioro del sensorio y acrocianosis, se decide su ingreso a UCI; ingresa en malas condiciones generales, hipotensa, taquicárdica, con cianosis peribucal y distal, se realizan paraclínicos evidenciándose acidosis respiratoria acentuada, por lo que se realiza intubación endotraqueal y se conecta a ventilación mecánica con parámetros de Vc: 700, FR: 14, FiO2: 50, Fl: 50, PEEP: 0. El día 27/04/14 se anexa inestabilidad hemodinámica ameritando apoyo con Vasoactivos tipo Norepinefrina. El día de hoy por disponibilidad de cupo y previa autorización de Dra. Teresa Cortesía se indica su traslado e ingreso a la UCI del HUAPA.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubada y conectada a ventilador mecánico de transporte, recibiendo Levophed® VEV por cuentagotas a razón de 32µgr/min, se pasa a cama UCI, se conecta a ventilación mecánica modo A/C, Vc: 600, FR: 12, FiO2: 60, Fl: 50, PEEP: 0 y se conecta a monitor cardíaco continuo que reporta: TA: 109/57(74) mmHg; FC: 105 lpm; FR: 26 rpm; SatO2: 91% ''',
			
			"piel" : 	'''	normotérmica al tacto, con acantosis nigrans en cuello y región interna de muslos, llenado capilar < 3seg.s''',

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, con escasos crepitantes finos bibasales. Ruidos cardíacos rítmicos y regulares, taquicárdicos, sin soplo ni galope.	''',
			"abdomen": ''' globoso a expensas de panículo adiposo, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico. ''',

			"neurologico": ''' no evaluable por efectos de sedación y relajación farmacológica.''',
			

		}, 

		"diagnosticoIngresoUCI": [

								"SHOCK SEPTICO",
								"SEPSIS PUNTO DE PARTIDA RESPIRATORIO: NEUMONIA ADQUIRIDA DE LA COMUNIDAD",
								"INFECCION DEL TRACTO URINARIO MIXTA",
								"SINDROME DE PICKWICK",
								"HIPOTIROIDISMO",
								"TRASTORNO ACIDO-BASE: ACIDOSIS RESPIRATORIA COMPENSADA CON ALCALOSIS METABOLICA + NORMOXEMIA",

									
								],  
		
	},# 73

	{
		"IdHistoria": "02-85-46", 
		"nombre": "Carmen Elvira Hermnadez", 		
		"edad": "58",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1950,11,1), 		
		"lugarNacimiento": "Cumaná-Estado Sucre", 		
		"ci": "8.434.145", 		
		"dirección": "los tejados numero 175", 		
		"fechaIngresoHUAPA":  datetime(2015,4,20), 		
		"fechaIngresoUCI": datetime(2015,4,30), 		
		
		"resumenIngreso": '''Se trata de paciente femenina de 58 años de edad natural y procedente de la localidad con antecedentes de fumadora crónica desde los 14 años de edad, hipertensión arterial de larga data en tratamiento regular con corentel (bisoprolol 5mg, hidroclorotiazida 6.5 mg) inicia enfermedad actual en el mes de octubre cuando presenta hemoptisis por lo que acude a facultativo centro privado permaneciendo hospitalizada durante 48 horas y es egresada con referencia a la consulta de cirugía de tórax, acudiendo a consulta con especialista DR sotillet quien indica estudio imagenologicos evidenciando LOE a nivel de lóbulo superior de pulmón, motivo por el cual se planifica para videofibrobroncoscopia la cual se realiza el día  21/10/2014 reportando células epiteliales atípicas compatibles con carcinoma sugiriendo toma de biopsia para decidir conducta definitiva; permanece en control por consulta de cirugía de tórax donde es planificada para toma de biopsia mediante toracotomía, siendo ingresada el día 28/04/2015''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubado, conectado a ventilar de traslado, se traslada a cama UCI, se conecta a monitor cardiaco continuo que reporta: Fc 65 lpm Fr: 22 rpm TA: 129/68 (125) mmHg SATO2: 100%.''',
			
			"piel" : 	'''	normo hidratada, afebril al tacto, llenado capilar < 3 Seg.''',

			"cardiopulmonar":  '''Tórax simétrico, normoexpansible; se evidencia tubo de tórax conectado a trampa de agua con presencia de secreción hemática escasa  oxilante , ruidos respiratorios presentes en ambos hemitorax y disminuidos en hemitorax derecho  se auscultan roncos ipsilateral, ruidos cardiacos rítmicos regulares, sin soplo ni galope.''',
			"abdomen": '''plano ruidos, ruidos hidroaéreos presentes,  depresible, no doloroso a la palpación, no se palpan visceromegalia.''',

			"neurologico": ''' inconsciente, paciente bajo efecto de sedación farmacológica Glasgow no evaluable, pupilas isocóricas hiporreactivas a la luz.''',
			"extremidades": '''simétricas sin edemas.''',

		}, 

		"diagnosticoIngresoUCI": [
									

									"Post operatorio inmediato de toracotomía postero lateral derecha para toma de biopsia. ",
									"Lesión ocupante de espacio pulmonar derecho complicado con hemoptisis.", 
									"Hipertensión arterial sistémica ",
									"Trastorno", 

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Fc:  lpm Fr:  rpm TA: / mmHg SATO2:? %. Es llevada a mesa operatoria el dia 30/04/2015, bajo anestesia general toracotomía pastero lateral derecha se evidencia TU de 5 cm x 5 cm de diámetro en lóbulo superior derecho que se extiende hasta híleo    pulmonar ipsilateral , además de múltiples adenopatías perihiliares, realizando resección en cuña de TU pulmonar, rafia de defecto pulmonar, comprobación de hemostasia y se deja tubo de drenaje torácico # 32 extraído por contra abertura a nivel del 6to espacio intercostal se realiza rafiado por capas se traslada a unidad de cuidados intensivos para cuidados post operatorio. ''',
			"piel": ''' morena, llenado capilar <3 Seg. ''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes, disminuidos en ápice  pulmonar derecho, ruidos cardiacos rítmicos regulares.''',
			"abdomen": '''plano ruidos hidroaéreos presentes, no doloroso a la palpación, no se palpan megalias''',
			"neurologico": '''orientado en 3 planos lenguaje coherente.''',

		},  

		"diagnosticoIngresoHUAPA": ["Lesión ocupante de espacio pulmonar derecho complicado con hemoptisis"], 
		
	},#74

	{
		"nombre": "Carmen del valle Ledesma Ramos", 		
		"edad": "49",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1965,8,29), 			
		"ci": "8.639.241", 		
		"dirección": "AV bolívar nº 72", 		
		"fechaIngresoHUAPA":  datetime(2015,7,10), 		
		"fechaIngresoUCI": datetime(2015,7,10), 		
		"resumenIngreso": '''Paciente femenina de 68 años de edad, natural y procedente de la localidad, con  antecedentes patológicos de diabetes mellitus de reciente diagnóstico, sin tratamiento médico, antecedentes de ingreso en el mes de enero por meningitis para lo cual permaneció ingresada durante 21 días en el hospital Razetti, inicia enfermedad actual hace 2 semanas aproximadamente con rinorrea, malestar general y aumento de la temperatura corporal no cuantificada, para el día 4/07/2015 se anexa al cuadro otalgia persistiendo sintomática del cuadro febril, el día 8/07/2015 se anexa al cuadro vómitos en múltiples oportunidades además dolor en región posterior del cuello (nuca) por lo que acude a centro privado donde es tratada con profenid (ketoprofeno), irtopam (metrocloropramida), siendo egresada, persistiendo sintomática, el día   09/07/2015 se anexa al cuadro alteración del estado de conciencia (somnolencia) alternado con periodos de agitación psicomotriz, imposibilidad para la marcha por lo que es trasladado a centro privado donde es evaluada constatando rigidez de nuca con signos meníngeos positivos (kerning y brudzinski), proptosis de ojo izquierdo con edema y Glasgow de 13/15 pts. Por lo que es ingresado. Realizando punción lumbar reportando citoquímico patológico realizando confirmación de diagnóstico: Meningoencefalitis bacteriana, Trombosis del seno cavernoso? Diabetes mellitus tipo 2. Paciente permanece ingresado durante 24 horas en centro privado recibiendo antibioticoterapia a base de cefotaxima y vancomicina, y en vista de condiciones socioeconómicas se decide tu traslado a nuestro centro asistencial donde en vista de disponibilidad de cupo y  condiciones clínicas de cuidado de paciente se decide su ingreso. Realizando punción lumbar reportando citoquímico patológico confirmando el diagnóstico de: INFECCION DEL SNC: Meningoencefalitis bacteriana.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente recibiendo oxigeno por mascarilla facial se traslada a camilla de uci y se conecta a monitor cardiaco que reporta FR: 22 rpm, FC: 95 lpm, TA: 132/84 (112) mmHg, SatO2: 96% ''',
			
			"piel" : 	'''	piel blanca, se evidencia moderada palidez cutáneo mucosa, normotermica al tacto normohidratada. Llenado capilar < de 3 Seg  se evidencia edema palpebral izquierdo con hiperemia calor. ''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, con agregados roncos en 1/3 medio de hemitorax derecho. Ruidos cardiacos rítmicos y regulares, sin soplos ni galope.''',
			"abdomen": ''' globoso, a expensa de panículo adiposo,  ruidos hidroaéreos presentes, depresible, no doloroso a la palpación superficial y profunda, no se palpan megalias. ''',

			"neurologico": ''' somnolienta, pupilas isocóricas normorreactivas a la luz, con desviación de  la mirada hacia la derecha ROT II/V, Glasgow 11/15 pts. Dado por RM 5 pts. RO 4 sin conexión con  el medio externo, limitación de la apertura ocular izquierda pts. RV 2 pt ''',
			
			"extremidades": '''simétricas, sin alteraciones. ''',

		}, 

		"diagnosticoIngresoUCI": [

									"Infección del sistema nervioso central:",
									"Meningoencefalitis bacteriana",
									"Absceso cerebral AD",
									"Trombosis del seno cavernoso AD",
									"Diabetes mellitus tipo 2", 
									"Trastorno hidroelectrolítico: hipokalemia",
									{"resumen":''' Paciente permanece durante 26 días en la unidad de cuidados intensivos, recibiendo antibioticoterapia con Ceftriaxona, Vancomicina y Metronidazol, la cual cumple por 21 días, el día 12/07/15 presentó mayor deterioro neurológico ameritando intubación endotraqueal y permaneciendo conectada a ventilación mecánica; el día 23/07/15, por intubación prolongada y no tolerar destete ventilatorio, se realiza traqueotomía sin complicaciones, se mantiene conectada a ventilación mecánica hasta el día 04/08/15 y actualmente con 24 horas en T de Ayres tolerándolo satisfactoriamente. Por lo que es egresada de la unidad de cuidados intensivos. Se solicita cupo en servicio de larga estancia en vista de  requerir de cuidados especiales además de iniciar terapia de rehabilitación física.'''},

								],  

		"diagnosticoEgreso": [
						"INFECCION DEL SISTEMA NERVIOSO CENTRAL: MENINGOENCEFALITIS BACTERIANA",
						"DIABETES MELLITUS TIPO 2 COMPENSADA",
						"INFECCION RESPIRATORIA BAJA: NEUMONIA ASOCIADA A VENTILACION MECANICA",
						"INFECCION DEL TRACTO URINARIO MICOTICA",
						"POST-OPERATORIO TARDIO DE TRAQUEOSTOMIA",
						"TRASTORNO HEMATOLOGICO: ANEMIA MODERADA",
						"TRASTORNO ACIDO – BASE: ALCALOSIS METABOLICA DESCOMPENSADA MAS HIPEROXEMIA",

		], 
		
	},#75

	{
		"nombre": "Adolfo Antonio Jiménez", 		
		"edad": "78",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1956,2,20), 		
		"lugarNacimiento": "Cumaná - Estado Sucre", 		
		"ci": "349.337", 		
		"dirección": "Urbanización Araya calle 07 casa # 17", 		
		"fechaIngresoHUAPA":  datetime(2015,2,18), 		
		"fechaIngresoUCI": datetime(2015,2,18), 		
		"resumenIngreso": ''' Se trata de paciente masculino de 78 años de edad  natural y procedente de Araya, con antecedentes de Hipertensión Arterial en tratamiento con Enalapril 10mgOD, Alzheimer, tratada con Somazina 1gramo diario y Eutobrol, quien inicia enfermedad actual el día 16/02/201 en horas de la madrugada,  cuando posterior a caída de sus propios pies presenta deterioro del estado neurológico, por lo que es llevado a centro privado, donde evalúan e  ingresan, realizan Resonancia Magnética Nuclear, donde se reporta Hematoma Subdural, por lo que es valorado por Especialista (Neurocirujano) quien decide llevar a mesa operatoria, donde drenan 120cc de contenido hemático procedentes de Hematoma Epidural y Subdural, posteriormente es trasladado a la UCI de dicho centro privado donde permanece durante 48 horas recibiendo antibióticoterapia y medidas anti edema cerebral.  En vistas de condiciones socio económicas es referido a esta  institución, donde previa valoración se ingresa.''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''  TA: 168/74(105) mmHg FC: 67 lpmFR: 19 rpm SPO2: 99% ''',
			
			"piel" : 	'''	Blanca, pálida normotérmica al tacto, llenado capilar <3 segundos, con pálidez cutáneo mucosa.''',

			"cardiopulmonar":  ''' tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, no agregados, ruidos cardíacos arrítmicos hipofonéticos, sin soplos ni galope. 	''',
			"abdomen": ''' blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes.''',

			"neurologico": ''' Paciente somnoliento, Glasgow: RM: 5pts, RO: 3pts., RV: 1pto 9/15ptos. Pupilas isocóricas no reactivas a la luz hemiparesia derecha ''',
			"cabeza": '''se evidencia herida quirúrgica cubierta con apósitos en región fronto-temporo- parietal izquierda limpia y seca.''',
			"extremidades": ''' eutróficas, simétrica sin edema ''',

		}, 

		"diagnosticoIngresoUCI": [

									"Post-operatorio Mediato de Craneotomía fronto parietal izquierda para drenaje de  hematoma subdural agudo Fronto-Temporo- Parietal Izquierdo",  
									"Post-operatorio Mediato de Craneotomía fronto parietal izquierda para drenaje de  hematoma subdural reformado ipsilateral",
									"Post-operatorio mediato de Traqueostomía",
									"Síndrome de Hipertensión Endocreneana (R)",
									"Hipertensión arterial",
									"Enfermedad de Alzheimer",
									"Trastorno Hematológico: Anemia moderada.",
									"Trastorno Hidroelectrolítico: Hiponatremia.", 
									"Trastorno Acido Base: Alcalosis respiratoria descompensada más hiper oxemia",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": '''  TA: 217/106 mmHg   FC: 75   lpm	FR: 24 rpm  SPO2: 99 %. Paciente es trasladado en camilla de transporte, intubado recibiendo oxigeno por ventilador mecánico de transporta; se traslada a cama UCI, conectándose a ventilación mecánica y a monitor cardiaco externo que reporta signos vitales: 
					   ''',
			"piel": ''' Blanca, pálida normotérmica al tacto, llenado capilar <3 segundos, con pálidez cutáneo mucosa.''',
			"cardiopulmonar": '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, no agregados, ruidos cardíacos arrítmicos hipofonéticos, sin soplos ni galope.''',
			"abdomen": '''blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes.''',
			"extremidades": '''eutróficas, simétrica sin edema ''',
			"neurologico": '''Paciente inconsciente, Glasgow: RM: 2pts, RV:1pto, RV:1pto 4/15ptos. Pupilas isocóricas no reactivas a la luz.''',
			"cabeza": ''' se evidencia herida quirúrgica cubierta con apósitos en región fronto-temporo- parietal izquierda.''',

		},  

		"diagnosticoIngresoHUAPA": [
						"Post-operatorio Mediato de Craneotomía fronto parietal izquierda para drenaje de hematoma subdural agudo Fronto-Temporo- Parietal Izquierdo.",
						"Síndrome de Hipertensión Endocreneana.",
						"Hipertensión arterial",
						"Alzheimer",
						"Trastorno Hematológico: Anemia severa",
						"Trastorno Acido Base: Alcalosis respiratoria descompensada más hiper oxemia.",
						{"resumen":'''Paciente que permanece durante 11 días en el Servicio de Uci. Recibiendo tratamiento médico a base de ceftazidima, vancomicina, epamin  (12  días)manitol (8 días), a su ingreso el día  18/02/2015 con 48 horas de post operatorio de craneotomía de fronto temporo parietal izquierdo de drenaje de hematoma subdural. Manteniendo cifras de tensión elevadas, bradicardia que amerita colocación de atropina (fenómeno Cushing) evolución clínica tórpida desde el punto de vista neurológico  Glasgow de 4/15 pts. Dado por RM 2 pts., RO 1pt RV 1 pt limitado por tubo endotraqueal por lo que se decide realizar control tomográfico el cual se cumple el día 19/02/2015 evidenciando reformación  de hematoma subdural ipsilateral comunicando caso a Servicio de Neurocirugía el cual  decide llevar a mesa operatoria realizando Craneotomía fronto temporo parietal izquierda para drenaje de hematoma subdural reformado ipsilateral. siendo trasladado nuevamente a Servicio de Uci para cuidados post operatorio. Permanece hipertenso durante las 24 horas posteriores a acto quirúrgico requiriendo tratamiento a base de Amlodipino 10 mg, Ramipril 10 mg, Hidroclorotiazida 12.5mg, Aldactone 25 mg. El día 25/02/2015 se realiza Traqueostomía sin complicaciones  en vista de intubación prolongada iniciando plan de destete ventilatorio permaneciendo durante 48 horas en T de Ayres tolerando satisfactoriamente. El día 27/02/2015 se realiza control tomográfico donde se evidencia mejoría de Edema cerebral sin desplazamiento de línea media sin signos de nuevo sangrado. Evidenciando evolución clínica satisfactoria, además regulación de cifras de tensión arterial y frecuencias cardiacas, en revista médica con DRA Roa se decide su Egreso.'''}

		], 
		
	},#76

	{
		"IdHistoria": "51-26-15", 
		"nombre": "Arturo Rafael Velázquez García ", 		
		"edad": "66",
		"sexo": "M",	
		"fechaNacimiento": datetime(1948,9,17), 		
		"lugarNacimiento": "Cumaná - Estado Sucre", 		
		"ci": "4.048.551", 		
		"dirección": "sector brisas del Mar Calle Araguaney", 		
		"fechaIngresoHUAPA":  datetime(2015,2,17), 		
		"fechaIngresoUCI": datetime(2015,2,21), 		
	
		"resumenIngreso": '''Se trata de paciente masculino de 66 años de edad  natural y procedente de la localidad, con antecedentes de Hipertensión Arterial en tratamiento con Captopril 25 mg OD, Diabetes Mellitus en tratamiento con Glucofage 1 gr BID, enfermedad renal crónica desde hace 5 años. Inicia enfermedad actual el día sábado 14/02/2015 en horas de la madrugada cuando presenta cefalea intensa, auto-medicándose con Migren sin mejoría, motivo por el cual acuden a nuestro centro asistencial siendo evaluado por servicio de medicina interna constatando cifras te tensión arterial elevadas 240/120 mmhg  medicando antipertensivo (no precisado) y egresan. Persistiendo sintomático. Para el día lunes 16 /02/2015 se anexa al cuadro disartria. Hemiparesia izquierda y dolor precordial no irradiado. Acudiendo el día martes 17/02/2015 a nuestro centro asistencial es reevaluado por el servicio de medicina y deciden su ingreso.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente es trasladado en camilla de transporte,  intubado recibiendo oxigeno por ambú; se traslada a cama UCI, conectándose a ventilación mecánica y a monitor cardiaco externo que reporta signos vitales: TA: 73/44(50) mmHg FC: 77 lpm FR:18 rpm SPO2: 98% ''',
			
			"piel" : 	'''Blanca, hipotérmica al tacto, llenado capilar <3 segundos, con marcada palidez cutáneo mucosa.''',

			"cardiopulmonar":  ''' tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, no agregados, ruidos cardíacos rítmicos regulares, sin soplos ni galope.''',
			"abdomen": '''blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes.''',

			"neurologico": ''' Paciente inconsciente, Glasgow no evaluable en vista de paciente encontrarse baje sedación farmacológica. Pupilas isocóricas no reactivas a la luz. ''',
			"extremidades": '''eutróficas, simétrica sin edema ''',
			"cabeza":''' se evidencia apósitos estériles en herida quirúrgica  en región parietal bilateral con moderada secreción hemática, se evidencian drenes en dichas heridas quirúrgicas con salida de secreción hemática moderada en dren izquierdo.''',

		}, 

		"diagnosticoIngresoUCI": [
									"Síndrome coronario agudo infarto al miocardio  sin elevación  del segmento ST ",
									"Crisis hipertensiva",
									"Anemia moderada(9 gr/dl)",
									"Enfermedad renal crónica",
									"Hipertensión arterial sistémica",
									"Diabetes Mellitus tipo II compensada",
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA:220/120 MmHg FC: 98 lpm FR:18 rpm SPO2:%.Permanece ingresado en área de emergencia recibiendo tratamiento médico a base de antiagregantes plaquetarios. Para el día  18/02/2015 es evaluado por Servicio de Cardiología (Dr. kan) quien decide omitir diagnostico de síndrome coronario agudo en vista de no evidenciar signos electro cardiográficos subjetivos de dicha patología y realiza sugerencias entre ellas omitir anti-agregación plaquetaria realizar perfil isquémico y solicitar valoración por nefrología y realizar TAC de cráneo el cual se realiza el día 19/02/2015. Para el día 20/02/2015 se lleva a cabo evaluación por Servicio de nefrología Dr. Arandia  quien indica depuración de creatinina y proteínas en 24 horas evidenciando evolución tórpida con deterioro progresivo del estado neurológico no precisado. El día 21/02/2015 se reciben resultados de TAC cerebral solicitan valoración por servicio de neurocirugía en vista de evidenciar hematoma subdural subagudo acudiendo al llamado evaluando pacientes en condiciones clínicas de cuidado con deterioro del estado neurológico dado por Glasgow 8/15 pts RM 4pts RV 2pts RO 2pts comunicando caso a especialista del Servicio de  guardia DR Montaño quien en vista de dichos hallazgos decide llevar a mesa operatoria donde bajo anestesia general, previa asepsia y antisepsia, disección de planos hasta ose se realiza craneotomía mínima a través de 3 agujeros, durotomía con drenaje de hematoma subdural subagudo a tensión mas lavado, se realiza colocación de drenes y cierre por planos, solicitando valoración por servicio de terapia intensiva quien en vista de disponibilidad de cupo se decide su ingreso para manejo post operatorio. ''',
			"cabeza": ''' normo configurada, no se palpan tumoraciones. ''',
			"piel": ''' morena, normotérmica al tacto, llenado capilar <3 segundos.''',
			"cardiopulmonar": '''tórax simétrico, normo expansible, ruidos respiratorios presentes en ambos campos pulmonares, no agregados, ruidos cardíacos rítmicos regulares, sin soplos ni galope.''',
			"abdomen": '''globoso  blando, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes ''',
			"extremidades": '''eutróficas, simétrica sin edema ''',
			"neurologico": '''Paciente consciente, orientado en tiempo espacio y persona. Lenguaje coherente. Fuerza muscular conservada.''',

		},  

		"diagnosticoIngresoHUAPA": [

								"Post-operatorio inmediato de Craneotomía descompresiva para drenaje de hematoma subdural subagudo.",
								"enfermedad renal crónica reagudizada.",
								"Hipertensión arterial",
								"diabetes Mellitus tipo II", 
								"Trastorno Hematológico: Anemia severa",
								"Trastorno Hidroelectrolítico: hiperkalemia ",
								"Trastorno Acido Base: Acidosis metabólica descompensada con  Alcalosis respiratoria  más normoxemia.",
				
		], 
		"examenFisicoEgreso": {
			"resumen": ''' TA: 171/87(114) mmHg FC: 99 lpm FR:18 rpm SPO2: 99% ''',
			"piel": ''' Blanca, normotérmica al tacto, llenado capilar <3 segundos, con moderada palidez cutáneo mucosa.''',
			"cabeza": ''' se evidencia apósitos estériles en herida quirúrgica  en región parietal bilateral limpia y seca''',
			"extremidades": ''' eutróficas, simétrica sin edema''',
			"abdomen": ''' blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes.''',
			"neurologico": '''Paciente consciente, Pupilas isocóricas normorreactivas a la luz fuerza muscular V/V ROT II/IV Glasgow 15/15 pts. ''',
			"cardiopulmonar": ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, no agregados, ruidos cardíacos rítmicos regulares,  sin soplos ni galope. ''',
		},

		"diagnosticoEgreso": [
				"Post-operatorio mediato de Craneotomía descompresiva para drenaje de hematoma subdural subagudo.",
				"2- enfermedad renal crónica reagudizada.",
				"Hipertensión arterial",
				"diabetes Mellitus tipo II", 
				"Trastorno Hematológico: Anemia moderada",
				"Trastorno Hidroelectrolítico: hiperkalemia ",
				"Trastorno Acido Base: Acidosis metabólica descompensada con  Alcalosis respiratoria  más normoxemia",
				{"resumen":'''Al ingreso se le plantea caso a la Dra. Cortesía quien indica realizar Vía central para manejo de líquidos y control de PVC, en vista de cifras tensionales bajas, ameritando de reposiciones con solución Ringer 800cc, obteniéndose mejoría de la misma. Se le realiza Vía central Yugular izquierda sin complicaciones, PVC en 11 cm3 H2O. Paciente permanece durante 72 horas en UCI, recibiendo tratamiento médico a base de cefotaxima y vancomicina durante (3 días) con evolución clínica satisfactoria de post operatorio, permaneciendo con retención de azoados e hiperkalemia por lo cual se solicito valoración por el servicio de nefrología la cual se cumple el día 23/02/2015   en vista de no contar con disponibilidad de catéter de diálisis y turno en dicha unidad se decide diferir el procedimiento. Además se cumple retiro de drenes de herida quirúrgicas por parte del servicio de Neurocirugía sin complicaciones. En vista de evolución clínica satisfactoria en revista médica se decide su egreso.  '''}, 


		],
		
	},#77
	{
		"IdHistoria": "52-86-66", 
		"nombre": "Adolfo Sanchez Mata", 		
		"edad": "50",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1964,11,10), 		
		"lugarNacimiento": "Cumaná - Estado Sucre", 		
		"ci": "8.636.066", 		
		"dirección": "Fe y Alegría", 		
		"fechaIngresoHUAPA":  datetime(2015,2,10), 		
		"fechaIngresoUCI": datetime(2015,2,10), 		
	
		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente recibido  en camilla de transporte, intubado, conectado a ventilador de transporte y a monitor cardiaco externo, se traslada a cama UCI y es conectado a monitor cardíaco  que reporta  TA: 101/69 (79) mmHg FC:123 lpm FR: 14 rpm SatO2: 100%, y a ventilación mecánica AC Vc: 640 (8cc/Kg) FiO2: 50 Fr: 12 Fl: 50 PEEP: 0. ''',
			
			"piel" : 	'''	Normotérmica al tacto, llenado capilar <3 segundos''',

			"cardiopulmonar":  '''Tórax  simétrico, expandible, apósito estéril con escasa secreción hemática, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos normofonéticos, taquicárdicos,  sin soplos ni galope.''',
			"abdomen": ''' blando, depresible, no impresiona doloroso a la palpación, ruidos hidroaéreos presentes, no megalias. ''',

			"neurologico": ''' paciente bajo efectos de sedación y relajación farmacológica, pupilas isocóricas hiporreactivas a la luz. ''',
			"extremidades": '''En miembro inferior derecho se observa apósito estéril limpio sin secreciones''',

		}, 

		"diagnosticoIngresoUCI": [

								"Post operatorio inmediato de pseudoaneurisma de arteria subclavia derecha",
								"Trastorno hematológico: Anemia Moderada",
								"Trastorno Metabólico: Hiperglicemia",
								"Trastorno acido – base: Acidosis Metabólica descompensada más hiperoxemia.",
								{"resumen": ''' El paciente se le mide PVC que reporta 2 cmH2O, tensión arterial sistólica de de 85 mmHg por lo que se realizan retos de líquidos hasta optimizar PVC de 10 cmmH2O y tensión sistólica de 110 mmHg, se reciben paraclínicos que reportan PTT 17.7 por lo que se trasfunden 4 uds de plasma fresco congelado. '''},

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se trata de paciente blanco masculino de 50 años de edad, natural y procedente de la localidad, con antecedentes de hipertensión arterial controlada con losartan , quien inicia enfermedad actual el día 08/01/15 cuando posterior a herida por proyectil de arma de fuego con orificio de entrada en región  supraclavicular derecha con orificio de salida en 2do espacio intercostal anterior derecho línea media clavicular. Motivo por el cual se evalúa e ingresa por servicio de cirugía blanda ''',
			"piel": '''Morena fría  al tacto, palidez cutáneo mucosa, llenado capilar <3 segundos.''',
			"cardiopulmonar": '''Tórax simétrico, ruidos respiratorios presentes, disminuidos en hemitorax derecho; se evidencia herida por proyectil de arma de fuego con orificio de entrada en región supra clavicular derecha y salida en 2do espacio intercostal anterior derecho con línea medio clavicular, evidenciando en dicha región hematoma pulsátil no expansible. Ruidos cardiacos rítmicos, sin soplos ''',
			"abdomen": '''Globoso a expensa de panículo adiposo, no doloroso a la palpación, ruidos hidroaéreos presentes, no megalias''',
			"extremidades": '''Parestesia en miembro superior derecho, pulsos cubital y radial disminuidos ''',
			"neurologico": '''Paciente consciente orientado en tres planos ''',

		},  

		"diagnosticoIngresoHUAPA": [

				"Traumatismo torácico no penetrante por herida por proyectil de arma de fuego",
				"Hernia inguinal derecha",
				"Hipertensión Arterial.",
				{"resumen": ''' El paciente permanece hospitalizado por servicio de cirugía siendo evaluado por Dr.Soto Cirujano cardiovascular quien indica paraclínicos. El día 07/01/15 se realiza angiotac la cual reporta pseudoaneurisma de arteria subclavia derecha. El paciente fue llevado en varias ocasiones a mesa operatoria para resolución quirúrgica de dicho pseudoaneurisma siendo suspendido por problemas técnicos en área de quirófano y falta de material quirúrgico; el día 10/02/15 el paciente presenta gasto hemático por orificio de proyectil de arma de fuego  a nivel de región clavicular derecha por lo que es evaluado por Dr Soto y solicita turno quirúrgico de emergencia. El paciente es llevado a mesa operatoria donde se realiza apertura de capsula pseudoaneurismática, control vascular proximal y distal, disección de vasos subclavios y plexo braquial, confección de autoingerto de vena safena interna invertida termino terminal. Durante acto quirúrgico el paciente hace hipotensión severa, siendo resuelta sin complicaciones. '''},

		], 
		
	},#78


	{
		"IdHistoria": "54-11-08 ", 
		"nombre": "AIMARA JOSEFINA INDRIAGO JIMENEZ", 		
		"edad": "39",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1976,7,23), 		
		"lugarNacimiento": "CARACAS, DTTO. CAPITAL", 		
		"ci": "13.348.617", 		
		"dirección": "RIO GRANDE ARRIBA, CASA S/N, IRAPA, EDO. SUCRE ", 		
		"fechaIngresoHUAPA":  datetime(2015,12,24), 		
		"fechaIngresoUCI": datetime(2015,12,24), 		
		"resumenIngreso": '''Paciente femenina de 39 años de edad, natural de Caracas y procedente de Irapa, sin antecedentes patológicos conocidos, quien cursa con II gesta, embarazo de 30 semanas más 6 días por FUR, y refiere inicio de enfermedad actual el día 06/12/2015 cuando presenta rash cutáneo generalizado y urticaria, además edema en miembros inferiores, es llevada el día 07/12/15 a centro asistencial de su localidad, donde evalúan, indican tratamiento a base de Sultamicilina y Diclofenac y egresan. El día 08/12/15 se anexa al cuadro disminución de la fuerza muscular en miembros inferiores, progresiva, motivo por el cual acude nuevamente a centro asistencial de su localidad de donde refieren a Maternidad de Carúpano el día 12/12/15, permanece con sintomatología muscular hasta la pérdida completa de la fuerza muscular en miembros inferiores, el día 23/12/15 se anexa amaurosis izquierda, en vista del cuadro clínico plantean polineurorradiculopatía aguda y el día 24/12/15 refieren a este centro asistencial donde previa evaluación por el servicio de Ginecología y Obstetricia. ''', 


		"examenFisicoIngresoUCI": {

			"piel" : 	'''Morena, normotérmica al tacto, llenado capilar <3 Seg. ''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax, sin agregados. Ruidos cardiacos rítmicos, regulares, taquicardicos, sin soplos ni galope.''',
			"abdomen": '''ruidos hidroaéreos presentes, globoso a expensas de útero grávido, feto único longitudinal, cefálico, movimientos fetales presentes, no doloroso a la palpación, no megálico.''',

			"neurologico": ''' consciente, lenguaje coherente, orientada en los 3 planos, pupilas isocóricas, reactivas a la luz, FM II/V en miembros inferiores y V/V en miembros superiores, ROT II/IV en miembros inferiores y superiores, Glasgow 15/15pts. ''',
			"extremidades": '''eutróficas, edema II/IV en miembros inferiores.''',

		}, 

		"diagnosticoIngresoUCI": [

									"Embarazo de 30 semanas + 2 días por FUR",
									"ARO:",
									"Síndrome Guillain – Barre ",
									"Cesárea anterior (hace 15 años)",
									"Bicitopenia E/E (Hb: 9,6 gr/dL, Plaq: 112)",
									"Domicilio lejano",
									"Alergia a la dipirona",
									"Edad materna",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' SIGNOS VITALES: TA: 130/80 mmHg. Solicitan valoración por el servicio de Terapia Intensiva en vista de cuadro clínico, se evalúa en el área de cuidados intermedios de sala de parto, por no contar con cupo se realizan sugerencias y posteriormente el mismo día 24/12/15, por disponibilidad de cupo, previa autorización de Dra. Cortesía (Intensivista de Guardia) se decide su ingreso a la UCI. Se recibe paciente en camilla de traslado, respirando aire ambiente, se conecta a monitor cardíaco continuo que reporta  TA: 131/85 (102) mmHg, FC: 120 lpm,  FR: 20 rpm, SatO2: 90%. ''',
			"tacto": ''' vagina normotérmica, normoelástica, cuello central largo, permeable en OCE''',
			"piel": ''' normotérmica al tacto, llenado capilar < 3 segundos. ''',
			"cardiopulmonar": '''tórax simétrico, expandible, ruidos respiratorios presentes en ambos hemitórax, sin agregados. ''',
			"abdomen": '''globoso a expensas de útero grávido, feto único, longitudinal, cefálico, movimientos fetales presentes, dinámica uterina negativa, FCF: 150 lpm.  ''',
			"extremidades": '''simétricas, sin edema, fuerza muscular I/V en miembros inferiores, normorreflexica. ''',
			"neurologico": '''consciente, orientada en los 3 planos.''',

		},  

		"diagnosticoIngresoHUAPA": [

			"POLINEURORRADICULOPATIA AGUDA: SINDROME DE GUILLIAM – BARRE A DESCARTAR.",
			"II GESTA",
			"EMBARAZO DE 30 SEMANAS + 2 DÍAS POR FUR",
			"TRASTORNO HEMATOLOGICO: ANEMIA MODERADA TROMBOCITOPENIA"				
		], 
		
	},#79

	{
		"IdHistoria": "24-90-86 ", 
		"nombre": "Antonio José Cumana", 		
		"edad": "57",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1956,12,19), 		
		"lugarNacimiento": "Cumana", 		
		"ci": "8.429.238", 		
		"dirección": "San José de Macarapana San Juan", 		
		"fechaIngresoHUAPA":  datetime(2014,5,8), 		
		"fechaIngresoUCI": datetime(2014,5,8), 		
		"resumenIngreso": '''Paciente masculino de 57 años de edad sin antecedentes patológicos personales ,que inicia enfermedad actual hace aproximadamente 5 meses cuando presenta dolor pleurítico derecho acompañado de disnea motivo por el cual acude a diferentes centros de salud en los cuales solo medicaban  con fármacos anti inflamatorios ,hace 2 meses se indica Rayos X de tórax donde se observa derrame pleural derecho por lo que acude a consulta de Cirugía de Tórax indicándose TAC Tórax en la cual se describe : Signos tomográficos sugestivos de empiemas encapsulados extensos localizados en hemitorax derecho asociado con atelectasias pasivas ipsilaterales por lo que se toma la conducta de toracocentesis evidenciándose liquido seroso ,  paciente que continua con disnea intensa por lo que se realiza  nuevo control tomográfico donde se evidencia derrame pleural derecho tabicado,  obteniéndose muestras para cultivo (negativo ) y cito químico cuyo resultado con características de exudado , empeorando progresivamente el cuadro por lo que se hospitaliza para resolución quirúrgica.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, recibiendo O2 mediante ventilador de transporte, se traslada  a cama de UCI y se conecta a monitor cardíaco continuo que reporta: TA: 118/68(67) mmHg; FC: 88 lpm; FR: 25 rpm; SatO2: 100%  ''',
			
			"piel" : 	'''normo térmica al tacto, húmedas y normo coloreadas ''',
			

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible ruidos respiratorios presentes, sin agregados. Ruidos cardíacos rítmicos, taquicárdicos, sin soplo ni galope. Tubo de tórax 34 F derecho conectado a pleurevac con salida de escasa secreción serohematica burbujeo positivo ''',
			"abdomen": ''' plano, blando, depresible no dolorosos a la palpación superficial y profunda no megalias RHA presentes.''',

			"neurologico": ''' Paciente bajo efectos de sedantes y relajante muscular.''',
			

		}, 

		"diagnosticoIngresoUCI": [
								"POI TORACOTOMIA POSTEROLATERAL DERECHA DEBIDO A DERRAME PLEURAL DERECHO TABICAD", 
								"ANEMIA LEVE",  
								"TTNO AB ACIDOSIS METABOLICA DESCOMPENSADA CON HIPEROXEMIA", 


									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se recibe paciente en regulares condiciones, tolerando aire ambiente. TA: 121/58(67) mmHg; FC: 78 lpm; FR: 25 rpm; SatO2: 100% ''',
			"piel": '''Normotermica hidratada llenado capilar menor de 3 seg ''',
			"cardiopulmonar": '''tórax simétricos, normo expansible ruidos respiratorios presentes, disminuido en hemitorax derecho. Ruidos cardíacos rítmicos, taquicárdicos, sin soplo ni galope.''',
			"abdomen": '''plano, blando, depresible no dolorosos a la palpación superficial y profunda no megalias RHA presentes ''',
			
			"neurologico": '''Consciente orientado en TEP sin signos meníngeos ni de focalización motora ''',

		},  

		"diagnosticoIngresoHUAPA": [
			{"resumen": ''' DERRAME PLEURAL DERECHO TABICADO. Paciente que es intervenido quirúrgicamente en el día de hoy realizándose toracotomía Posterolateral derecha evidenciándose cámara con liquido de color vinoso y lesiones granulomatosas a nivel pleural tomándose muestras para estudio cito químico y cultivo, se mantiene estable hemodinámicamente en acto quirúrgico donde recibió 2000 cc de solución 0.9 %´y 2 unidades de concentrado globular, por disponibilidad de cupo se decide traslada UCI para mejor seguimiento.'''},
								

		], 
		
	},#80

	{
		"IdHistoria": "53-77-41", 
		"nombre": "Ender Jesús Maita Andrade", 		
		"edad": "14",
		"sexo": "M",	
		"fechaNacimiento":  datetime(2001,3,2), 		
		"lugarNacimiento": "Cumana estado sucre", 		
		"ci": "30.143.326 ", 		
		"dirección": "Turimiquire Sector Vega Grande S/N ", 		
		"fechaIngresoHUAPA":  datetime(2015,2,5), 		
		"fechaIngresoUCI": datetime(2015,2,7), 		
		
		"resumenIngreso": '''Paciente masculino de 14 años de edad natural y procedente de la localidad con antecedente de traumatismo craneoencefálico desde hace 6 meses por lo que lleva tratamiento con Valcote tableta de 500 mg VO cada 12 horas. Cuyo familiar refiere inicio de enfermedad actual el jueves en hora de la tarde cuando presenta aumento de temperatura corporal cuantificada en 40,5 ºC no atenuado con atamel de 650 mg. Motivo por el cual es llevado a ambulatorio de su localidad donde se evalúa y se constatan aumento de temperatura corporal, anexándose al cuadro clínico vómitos no precedidos de nauseas en varias oportunidades concomitantemente palpitaciones, en vista de persistencia de sintomatología es referido a este centro, en previa valoración presenta movimientos tónico-clónico por lo que se administra diazepam, en vista de deterioro neurológico se evalúa e ingresa en el área de choque. ''', 


		"examenFisicoIngresoUCI": {

			
			"piel" : 	'''	Blanca, normotérmica al tacto, deshidratada  ligera palidez cutánea-mucosa, llenado capilar < 3 segundos.''',

			"cardiopulmonar":  '''Tórax simétrico normoexpansible ruidos respiratorios presentes en ambos campos pulmonares sin agregados, rudos cardiacos rítmicos y regulares sin soplo ni galope.''',
			"abdomen": '''plano, ruidos hidroaéreos presentes, blando, depresible, no doloroso a la palpación superficial ni profunda, no megálico. ''',

			"neurologico": ''' somnoliento, pupilas isocóricas normorreactivas a la luz Glasgow 15/15 pts. Al momento del ingreso Se realiza, previa asepsia y antisepsia, cateterización de vía venosa femoral derecha, con catéter, mono lumen, sifonaje positivo en, se fija a piel con, asepsia final, se cubre con apósitos limpios, sin complicaciones.''',
		
		}, 

		

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' En vista de condiciones clínicas de la paciente, solicitan valoración por UCI y por disponibilidad de cupo se decide su ingreso. Se recibe paciente en camilla de traslado, recibiendo O2 húmedo por bigote nasal a 3 ltrsX’, se pasa a cama UCI, se conecta a monitor cardíaco continuo que reporta: TA: 94/45 mmHg, FC: 65 lpm, FR: 19 rpm, SatO2: 100%. TA: 100/80mmHg FC: 81 lpm FR: 18 rpm T: 37ºC''',
			"piel": ''' Blanca, deshidratada, normotérmica, normoelástica llenado capilar <3seg se evidencia palidez cutáneo mucosa.''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible ruidos respiratorios presentes en ambos hemitorax no se auscultan agregados, ruidos cardiacos rítmicos y regulares sin soplo ni galope. ''',
			"abdomen": '''ruidos hidroaéreos presentes, plano, blando, depresible, no doloroso a la palpación superficial ni profunda. ''',
			"extremidades": '''simétricas, sin edema.''',
			"neurologico": '''Consciente, orientado en tiempo espacio y persona con lenguaje claro''',
	
		},  

		"diagnosticoIngresoHUAPA": [

			"SINDROME EMETICO",
			"DESHIDRATACION MODERADA",
			"SINDROME FEBRIL AGUDO",
		], 
		
	},#81

	{

		"IdHistoria":"54-03-72",
		"nombre": "Cipriano Lobaton ", 		
		"edad": "84",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1930,9,16), 		
		"lugarNacimiento": "cumana ", 		
		"ci": "516.797", 		
		"dirección": "Vía Cumana -Cumanacoa, Comunidad Agua Santa.", 		
		"fechaIngresoHUAPA":  datetime(2015,11,29), 		
		"fechaIngresoUCI": datetime(2015,12,4), 		
		
		"resumenIngreso": '''Se trata de paciente masculino de 84 años de edad con antecedentes patológicos conocidos, de Hipertensión Arterial en tratamiento con Hidroclorotiazida 12.5mg BID,  quien inicia enfermedad actual el día jueves 26/11/2015 cuando presenta cefalea intensa que se atenúa con la administración de analgésicos orales,  el día sábado 28/11/2015 presenta nuevo cuadro de cefalea intensa con relajación de esfínter vesical por lo que acude a ambulatorio de la localidad donde constatan cifras de tensión arterial elevadas 180/100 mmHg indicando captopril vía sublingual por mejoría de cifras tensionales es egresado sin tratamiento médico  persistiendo sintomático, el día 29/12/2015 se intensifica cuadro de cefalea, con palidez cutáneo mucosa y sudoración profusa con cifras de tensión arterial 90/60 mmHg y  posteriormente  perdida súbito del estado de consciencia, por tal motivo es traslado a nuestro centro asistencial donde es evaluado por el Servicio de Medicina Interna e ingresado.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubado, recibiendo oxigeno por ambu, se conecta  a monitor cardiaco que reporta: SIGNOS VITALES: TA153/96(117) mmHg  FC 85 lpm FR 12 SAT O2: 99% ''',
			
			"piel" : 	'''Morena, normotérmica, hidratada, llenado capilar <3segundos.''',
			"cabeza": '''Normocéfalo, se evidencia cura quirúrgica cubierta por vendaje, con drenaje externo con salida de secreción hemático en escasa cantidad. ''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax con estertores roncus bilaterales.Ruidos cardíacos rítmicos, regulares, no se auscultan soplos. ''',
			"abdomen": ''' Blando, ruidos hidroaéreos presentes, no doloroso a la palpación superficial y  profunda, no visceromegalias''',

			"neurologico": '''No evaluable por sedación farmacológica, pupilas mióticas, no reactivas a la luz. ''',
			

		}, 

		"diagnosticoIngresoUCI": [

									"Postoperatorio Inmediato de Craneostomía Mínima para drenaje de Hematoma Subdural Subagudo Fronto-Temporal Izquierdo",
									"Crisis Hipertensiva tipo Emergencia expresado en Evento Cerebrovascular Hemorrágico: Hematoma Subdural Fronto-Temporal Izquierdo.",
									"Infección Respiratoria Baja: Neumonía Nosocomial.",
									"Insuficiencia Renal Aguda Prerrenal",
									"Hipertensión Arterial Sistémica",
									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' SIGNOS VITALES: FC 90 LPM  TA130 /90() MMHG FR 18 rpm. Se evalúa paciente en regulares condiciones generales, respirando espontáneamente afebril eupneica. ''',
			"piel": ''' morena,  Normotérmica, llenado capilar <3segundos.''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax sin agregados.  Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos. ''',
			"abdomen": '''globoso a expensa de panículo adiposo,  ruidos hidroaéreos presentes, no  doloroso a la palpación''',
			
			"neurologico": '''consciente, orientado en 3 planos, se evidencia monoparesia crural derecha Glasgow 14/15.''',
			

		},  

		"diagnosticoIngresoHUAPA": [
								
			"EVC de  etiología a precisar",
			"Trastorno hematológico anemia leve.",
			{"resumen": ''' El  paciente permanece en el área de observación, es trasladado el día 30/11/2015 para estudio tomográfico que reporta imagen de concavidad medial, localizada en la región fronto temporal izquierda, en el espacio subdural, isodensa en relación parénquima adyacente, que condiciona efecto de masa y desplazamiento del sistema ventricular hacia la derecha, subjetivo de Hematoma Subdural Subagudo, siendo evaluado por (Intensivista del servicio Dr. Quijada) quien indica iniciar medidas anti edema cerebral con Manitol al 18% y Lasix 20 mg BID,  el día 03/12/2015 presenta deterioro del estado de consciencia  es reevaluado por Intensivista del área (Dra. Patiño) quien indica oxigenoterapia y valoración por el Servicio de Neurocirugía, quien acude al llamado evaluando paciente en condiciones clínicas de cuidado con Glasgow de 6/15 pts. RM 4 RO 1 pt RV 1 pt.  Comunican caso a especialista de guardia Dr. Montaño quien indica omitir manitol, completar preoperatorios para resolución quirúrgica y solicitar valoración por el servicio de terapia intensiva, es evaluada y por estado neurológico se realiza maniobra de intubación endotraqueal conectándose a ventilación mecánica con parámetros pre establecidos, en vista de no contar con cupo en UCI se realizan sugerencias, el día 04/12/2015 es llevado a mesa operatoria donde bajo anestesia general se realiza craniotomia mínima frontal y parietal izquierda, durotomia, evidenciándose salida a presión de gran cantidad de secreción hemática en fase crónica, se realiza drenaje de hematoma se comprueba hemostasia y cierre por planos  y se traslada a unidad de cuidados intensivos para cuidados post operatorio.'''},

		], 
		
	},#82

	{
		"IdHistoria": "53-35-35", 
		"nombre": "José Miguel Rodríguez Segura", 		
		"edad": "15",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1999,12,31), 		
		"lugarNacimiento": "Cumana ", 		
		"ci": "27.208.255", 		
		"dirección": "Tumiriquire El bajo ", 		
		"fechaIngresoHUAPA":  datetime(2015,5,10), 		
		"fechaIngresoUCI": datetime(2015,5,13), 		
		
		"resumenIngreso": '''Se trata de paciente masculino, de 15 años de edad, natural del Estado Miranda y procedente de los Valles del Tuy , sin antecedentes patológicos conocidos, quien inicia enfermedad actual el día 10/05/2015 cuando posterior a accidente tipo colision vehiculo moto  presenta multiples traumatismos en cráneo ,pelvis y pierna izquierda además deterioro del estado de consciencia por lo que es traido a nuestro centro asistencial, es evaluado por el servicio de  traumatología siendo ingresado. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente es trasladado en camilla de transporte, sin recibir oxigeno no  conectado a ventilador de traslado,; se traslada a cama UCI, conectándose a monitor cardiaco externo que reporta signos vitales: TA: 131/72 mmHg (97)   FC: 65   lpm	FR: 12 rpm    	SPO2: 100%. Se realiza intubación endotraqueal con TET 8 F sin complicaciones y se conecta a ventilación mecánica modo AC VC 560 FL 50 FIO2 50 FR 12 PEEP ,se realiza además colocación de VVC yugular posterior izquierda sin complicaciones con xifonaje positivo''',
			
			"piel" : 	'''	morena, Normotérmica al tacto, llenado capilar <3 segundos, con ligera pálidez cutáneo mucosa.''',
			"cabeza": ''' Escoriaciones a nivel facial ''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos rítmico regulares, sin soplos ni galope.''',
			"abdomen": ''' blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes. ''',

			"neurologico": ''' Paciente bajo efectos de sedación farmacológica, Glasgow 7/15 RM 5 RO 1 RV 1. Pupilas isocóricas reactivas reflejo corneal presente  ''',
			"extremidades": '''Fractura abierta de tibia y peroné izquierda fijada con tutores externos ''',

		}, 

		"diagnosticoIngresoUCI": [

								"POLITRAUMATIZADO", 
								"TRAUMATISMO CRANEOENCEFALICO SEVERO COMPLICADO CON", 
								"EDEMA CEREBRAL DIFUSO ",
								"HEMORRAGIA SUBARACNOIDEA POSTRAUMATICA ",
								"TRAUMATISMO TORACO ABDOMINAL CERRADO",
								"FRACTURA ABIERTA DE TIBIA Y PERONE IZQUIERDO ",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 120/80 mmHg FC: 95 lpm FR: 15 rpm SPO2: % Paciente evaluado por servicio de neurocirugía evidenciando deterioro neurológico dado por Glasgow de 12/15 puntos RM 5  RO 4 RV 3 ,pupilas isocóricas reactivas a la luz reflejo corneal presente ,se indica TAC de cráneo en la cual se evidencia HEMORRAGIA SUBARACNOIDEA POSTRAUMATICA Y EDEMA CEREBRAL DIFUSO ,solicitándose valoración por UCI la cual se cumple anexando sugerencias. Para el día de hoy 13/05/2015 el paciente es llevado a mesa operatoria donde se realiza Fijación externa con tutor en miembro inferior izquierdo  presentando  deterioro neurológico evidenciándose Glasgow 7/15 puntos dado por RM 5 RO 1  RV 1 por lo que se decide traslado área de terapia intensiva ''',
			"piel": ''' Normotérmica al tacto, llenado capilar <3 segundos. ''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, no agregados. ''',
		
			"extremidades": '''eutróficas, simétrica sin edema''',
			"neurologico": '''Consciente.''',


		},  

		"diagnosticoIngresoHUAPA": [
								"FRACTURA DE TERCIO MEDIO DE TIBIA Y PERONE IZQUIERDA",

		], 
		
	},#83

	{
		"IdHistoria": "29-14-26", 
		"nombre": "Zaida Meneses", 		
		"edad": "49",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1964,5,8), 		
		"lugarNacimiento": "Cumana Edo Sucre", 				
		"dirección": "Miramar.", 		
		"fechaIngresoHUAPA":  datetime(2014,4,1), 		
		"fechaIngresoUCI": datetime(2014,4,1), 		
		
		"resumenIngreso": '''Se trata de paciente femenina de 49 años de edad natural de CUMANA  con antecedentes de ex fumadora, sin antecedentes patológicos importantes; quien inicia enfermedad actual el dia 25/03/14 cuando comienza con tos seca y fiebre, acude a ambulatorio donde indican tratamiento y egresan; la paciente continua con dificultad respiratoria, acude nuevamente a centro asistencial donde indican Rx de Torax. El dia 1/4/14 es traída a este centro por presentar dificultad respiratoria acentuada, es evaluada y hospitalizada ''', 


		"examenFisicoIngresoUCI": {

	
			"piel" : 	'''morena, normotérmica, deshidratada, llenado capilar <3segundos. ''',
		
			"cardiopulmonar":  '''Tórax simétrico, hipo expansible, ruidos respiratorios, MV disminuido en hemitorax derecho, se auscultan crepitantes en ACP. Ruidos  cardíacos rítmicos,taquicardicos regulares,  no se auscultan soplos.''',
			"abdomen": ''' globuloso , blando, no doloroso a la palpación, no megalias ''',

			"neurologico": ''' consciente, orientada,lenguaje claro y coherente.pupilas isocóricas reactivas a la luz ''',
		}, 

		"diagnosticoIngresoUCI": [

								"Infección respiratoria baja: neumonía bilateral",
								"SDRA",
								"Trastorno hidro electrolítico:hipokalemia",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' FC:79  lpm   FR 19 rpm  TA120/80 mmHg mmHg''',
			"piel": ''' morena, normotérmica,  llenado capilar <3segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, ruidos respiratorios presentes en campo pulmonar derecho se auscultan roncos y sibilantes.''',
			"abdomen": '''globuloso , blando, depresible, no doloroso a la plapación. Ruidos hidro aéreos presentes ''',
			
			"neurologico": '''consciente, orientada en 3 planos, lenguaje coherente.''',
			

		},  

		"diagnosticoIngresoHUAPA": [
				"Derrame pleural izquierdo",
				"MT pulmonar a descartar",
				"TBC a descartar",
				{"resumen":'''La paciente permanece en piso 9 se replantean diagnosticos de infección respiratoria baja, TBC a descartar, Neumonia bilateral complicada con derrame pleural. El dia 3/04/14 se realiza TAC de torax que informa Bronconeumonia bilateral en probable relación a enfermedad granulomatosa. TBC. La paciente se mantiene recibiendo tratamiento anti TBC VO, evolucionando de forma tórpida, hasta el día de hoy que se solicita valoración por UCI y vemos paciente en cama de hospitalización, recibiendo oxigeno húmedo por mascarilla facial a 5 lts por minutos, no conectada a monitor cardiaco, con cianosis distal, dificultad respiratoria, tos húmeda productiva con secreción amarillenta, taquicárdica y taquipneica; consciente, orientada en 3 planos. Se toman gases arteriales, se presenta caso a Dra Roa quien decide ingresar a la UCI. Se recibe paciente en camilla de traslado, recibiendo oxigeno húmedo por mascailla facial a 5 lts por min; se pasa a cama UCI, se conecta a monitor cardiaco que reporta Fr. 31 Fc 135 TA 105/56 (70) SATO2 61%, se toman gases arteriales que reportan Ph 7.41 PCO2 53  PO2 49 HCO3 33.6 EB 7.5 SATO2 77%; por lo que se decide intubación endotraqueal y conexión a ventilación mecánica. '''},
		], 
		
	},#84

	{
		"IdHistoria": "52-88-47", 
		"nombre": "Jose Reinaldo Salazar Martínez", 		
		"edad": "13",
		"sexo": "M",	
		"fechaNacimiento":  datetime(2001,12,4), 		
		"lugarNacimiento": "Barcelona estado Anzoátegui. ", 		
		"ci": "29.855.253", 		
		"dirección": "plan de lamesa vía cumana puerto la cruz  ", 		
		"fechaIngresoHUAPA":  datetime(2015,1,8), 		
		"fechaIngresoUCI": datetime(2015,1,15), 		
		"antecedentes": '''Asma bronquial''', 
		"resumenIngreso": '''Se trata de paciente masculino de 13 años de edad natural de Anzoátegui procedente de la localidad, con antecedentes de asma bronquial no controlada, quien inicia enfermedad actual el día 6/1/2015 cuando presenta fiebre cuantificada en 39ªC atenuada con acetaminofen, además tos sin expectoración y disnea, motivo por el cual  acude a ambulatorio de la localidad donde indican nebulizaciones. El día 8/1/2015 se anexa al cuadro dolor, aumento de volumen y limitación funcional en hombro izquierdo además persistencia del cuadro respiratorio. Motivo por el cual acude a nuestro centro asistencial, es evaluado por el servicio de medicina interna e ingresado.diagnósticos de: Asma bronquial en crisis severa. Infección del tracto urinario. El día 10/1/2015 es evaluado por servicio de cirugía en vista de presentar dolor abdominal difuso, realizan ecosonografia abdominal donde se aprecia hepatomegalia, barro vesicular, sugiriendo aumentar hidratación parenteral realizar ecosonograma abdominal por ecografista de manera formal, colocación de sonda de Foley por presencia de globo vesical valoración urgente por hematólogo, internista y UCI. El día 11/1/2015 es evaluado por residente de UCI por paciente en malas condiciones generales, febril, taquipneico y sin monitoreo  continuo, por lo que sugiere trasladar al área de choque por no contar con cupo en UCI y plante diagnostico de: Sepsis punto de partida respiratorio. El dia 12/1/2015 es evaluado por el servicio de traumatología por persistencia del cuadro de aumento de volumen y limitación funsional en hombro y codo izquierdo sugiriendo ecosonografia de partes blandas de hombro afectado, planteando diagnostico de:artritis séptica de hombro izquierdo. Es valorado el dia 13/1/15 por intensivista DRA (Norka patiño) quien replantea diagnostico: sthapylococcemia, artritis séptica de hombro izquierdo, trastorno Hidroelectrolítico: hipokalemia(R), Bicitopenia. Ajustando tratamiento antibiótico con vancomicina, meropenem, para el día 15/1/2015 por disponibilidad de cupo se ingresa a unidad de cuidados intensivos. ''', 

		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, con apoyo de Oxígeno húmedo por mascarilla nasal, no conectado a monitor cardiaco. Se traslada a cama UCI, se conecta a monitor cardiaco que reporta: TA: 86/94 (57) mmHg FC: 103 lpm	FR: 28 rpm	SPO2: 100%. Se realiza Control de T: 37ºC PVC: 23cm3H2O .''',
			
			"piel" : 	'''afebril al tacto, moderada palidez cutánea mucosa, hidratado, llenado capilar menor de 3 segundos.''',
			
			"cardiopulmonar":  '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes, con  crepitantes bibasales a predominios derecho ruidos, cardíacos rítmicos, regulares, sin soplos.''',
			"abdomen": ''' Plano, depresible, no doloroso a la palpación, no visceromegalia. Ruidos Hidroaéreos presentes.''',

			"neurologico": '''Consciente, orientado en 3 planos, sin signos de focalización neurológica. Normoreflexico. ''',
			"genitales": '''Aspecto y configuración normal, se evidencia sonda de Foley con orinas claras.''',

		}, 

		"diagnosticoIngresoUCI": [

									"Sepsis punto de partida respiratorio.",
									"Infección respiratoria baja: neumonía por sthapylococo aureos",
									"Artritis séptica de hombro izquierdo",
									"Trastorno hematológico: Anemia severa.",
									"trastorno acido básico: alcalosis metabólica descompensada.",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Tº: 37ºC    TA: 130/80 mmHg Fr: 20 rpm Fc:68 lpm.''',
			"piel": ''' palidez cutáneo mucosa , hidratado''',
			"cardiopulmonar": '''tórax simétrico hipoexpansible, ruidos respiratorios presentes , se evidencia tiraje intercostal, supra e infra clavicular se auscultan sibilantes bilaterales, ruidos cardiacos rítmicos regulares sin soplo ni galope.''',
			"abdomen": '''abdomen plano ,blando , depresible no doloroso a la palpación ruidos hidroaéreos presentes. ''',
			"extremidades": '''se evidencia aumento de volumen en miembro superior izquierdo con calor al tacto.''',
			"neurologico": '''consiente orientado en tiempo espacio y persona ,lenguaje coherente. ''',
	

		},  

		"diagnosticoIngresoHUAPA": [
								"Asma bronquial en crisis severa ",
								"Infección del tracto urinario",

		], 
		
	},#85

	{
		"IdHistoria": "40-30-13", 
		"nombre": "Saray Alexandra Correa marchan", 		
		"edad": "27",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1987,9,21), 		
			
		"ci": "19.761.616", 		
		"dirección": "urbanización fe y alegría sector 1 detrás del nexa  ", 		
		"fechaIngresoHUAPA":  datetime(2015,6,22), 		
		"fechaIngresoUCI": datetime(2015,6,22), 		

		"resumenIngreso": '''Se trata de paciente femenina de 27 años de edad natural y procedente de la localidad, con antecedentes  conocidos de mamo plastia de 2012 , quien refiere inicio de enfermedad actual hace 1 mes aproximadamente cuando posterior a viaje a Estado bolívar presenta aumento de temperatura corporal cuantificado en 39 ºC acompañado de escalofríos, posteriormente  se anexa al cuadro epistaxis, por lo que acude  a ambulatorio de la   localidad donde egresan con tratamiento médico sintomático, persistiendo sintomática, para el día 11/06/2015 se anexa al cuadro hematuria macroscópica y nauseas por lo que acude el día 12 a nuestro centro asistencial donde previa evaluación  es ingresada por el servicio de Medicina Interna con los diagnósticos de:Trombocitopenia severa. Dengue AD Paludismo AD. Anemia moderada (8.5 gr/dl) ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Fr: 18 rpm  Fc: 82 lpm TA: 120/70 mmHg. Se recibe paciente en camilla de traslado, procedente del servicio de choque recibiendo O2 por ambu. Se traslada a cama UCI y se conecta a monitor cardiaco continuo que reporta Fr: 27rpm Fc: 103 lpm TA: 139/87(107) mmHg SATO2: 99%.''',
			
			"piel" : 	'''	palidez cutáneo mucosa moderada, afebril al tacto, deshidratada, llenado capilar <3seg. ''',
			

			"cardiopulmonar":  ''' Tórax simétrico normoexpansible Ruidos respiratorios presentes en ambos hemitorax con agregados roncus bibasales. Ruidos cardiacos rítmicos taquicardicos no soplos ''',
			"abdomen": ''' blando depresible, ruidos hidroaéreos presentes, no impresiona  dolor a la palpación superficial y profunda.  ''',

			"neurologico": ''' estuporosa, pupilas isocóricas normorreactivas a la luz  Glasgow 8/15ptos RM: 3pts RV: 1 pt limitado por TEV RO: 4 pts. sin conexión con el medio externo. Sensibilidad conservada. ROT: II/IV. ''',
			"extremidades": '''simétricas sin edema.''',

		}, 

		"diagnosticoIngresoUCI": [

									"Estado post RCP",
									"Encefalopatía post hipoxia",
									"Paludismo por Plasmodium falciparum.",
									"Infección respiratoria baja: Neumonía bilateral",
									"Trastorno hematológico:  Anemia moderada",
									"Trastorno acido base Acidosis metabólica compensada  con Alcalosis respiratoria más normoxemia",
									{"resumen": ''' Permanece en área de terapia intensiva recibiendo tratamiento antipalúdico (solo una dosis) se realiza toma de muestra en dos ocasiones que reporta negativa para plasmodium omitiendo tratamiento antipalúdico, conectada a ventilación mecánica con parámetros EVITA 4 MODO: AC, FR: 12, FIO2: 50, FL: 50, PEEP: 0 manteniendo  deterioro neurológico por lo que se realiza TAC de cráneo evidenciándose Edema cerebral difuso por lo que se inicia tratamiento médico con Manitol al 18 % por 7 días, se imposibilita destete ventilatorio debido a INFECCION RESPIRATORIA BAJA NEUMONIA ASOCIADA A VENTILACION MECANICA por lo que recibe tratamiento médico con  LINEZOLID, MEROPENEM, AZTREONAM, CIPROFLOXACINA, PIPERACILINA -TAZOBACTAN y CEFEPIME. Por imposibilidad de destete ventilatorio se realiza traqueotomía por intubación prolongada, se recibe cultivo de secreción bronquial con presencia de Acinetobacter sp ,Pseudomona auriginosa sensible únicamente a Colistin, recibió 6 días de dicho tratamiento mejorando desde el punto de vista ventilatorio lográndose destete hasta permanecer por 72 horas en T  de AYRES con oxígeno húmedo a 10 lt por minuto con descenso de contaje blanco, afebril, sin embargo la paciente sigue ameritando de ventilación mecánica en varias oportunidades y fisioterapia respiratoria cada 2 horas y SOS. Actualmente recibe CEFOTAOXIMA (9 días) por no haber disponibilidad de otros recursos en el Hospital y por solicitud de familiares se expide informe para solicitar cupo en CDI para continuar con los cuidados respiratorios, rehabilitación y fisiatría de la misma. Agradeciendo su colaboración en dicho caso ya que se ha tratado con una paciente de larga estancia hospitalaria.'''},

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente refiere el día 8/06/2015 haberse realizado serología para dengue el cual reporta negativo, por lo que a su ingreso se indican gota gruesa  y repetir serología para dengue, reportando positivo para (plasmodium vivax), por lo que se replantea diagnósticos a paludismo por plasmodium vivax, iniciando tratamiento a base de (cloroquina-primaquina). El día 14/06/2015 es traslada a piso, persistiendo sintomática, anexándose el día 16/06/2015 dificultad para respirar, disminución de las cifras de tensión arterial 90/50 mmhg, deshidratación y alteración del estado de conciencia, motivo por el cual es traslada a área de choque (emergencia adulto), donde se anexa al diagnóstico shock hipovolémico, es evaluada por especialista del servicio DR Manuel  Ríos quien es vista de a la auscultación constata crepitantes, indica iniciar tratamiento antibiótico a base de (cefotaxima). El día 17/06/2015 es  valuada por el servicio de epidemiologia, quien indica toma de nueva muestra de gota gruesa. Determinando presencia de (plasmodium falciparum) por lo que ordena iniciar tratamiento con (artemether lumefantrina) 20/120 mg orden día por 3 días, paciente permanece sintomático por lo que el día 18/06/2015 se indica toma de muestra de hemocultivo y uro cultivo,  el día 19/06/2015 se anexa al tratamiento (Amikacina) en vista de evolución clínica tórpida solicitando valoración por el servicio de terapia intensiva, acudiendo al llamado realizando sugerencia en vista de no contar con cupo en dicha unidad, el día 20/06/2015 solicitan revaloración por el servicio de terapia intensiva para colocación de vía venosa central en vista de difícil acceso para cateterización de vías periféricas, realizándose dicho proceder sin complicaciones. El día 22/06/2015 en horas de la madrugada se anexa al cuadro deterioro del estado neurológico, acrocianosis y evoluciona a parada cardio respiratoria, por lo que realizan RCP básico y avanzado, además, intubación endotraqueal, permaneciendo en anoxia durante 3 minutos aproximadamente. Con evolución satisfactoria a RCP. Paciente es evaluada por el servicio de terapia intensiva en vista de condiciones clínicas de cuidados y de disponibilidad de cupo se decide su ingreso a la unidad.''',
			"piel": ''' Normotérmica, normo hidratada. Llenado capilar < de 3 segundos, se evidencia palidez cutáneo mucosa. ''',
			"cardiopulmonar": '''tórax simétrico,  normoexpansible, ruidos respiratorios presentes en ambos hemitorax, no se auscultan agregados, ruidos cardiacos rítmicos regulares sin soplo.''',
			"abdomen": '''plano, ruidos hidroaéreos presentes, blando depresible, no doloroso a la palpación, no megalias''',
			"extremidades": '''simétricas sin edema.''',
			"neurologico": '''Paciente consiente, orientada en tiempo espacio y persona fuerza muscular V/V''',
			

		},  

		"diagnosticoActual": [
					"Infección Respiratoria baja: Neumonía Asociada a Ventilación Mecánica.",
					"Estado post RCP(Resuelta)",
					"Encefalopatía Hipoxia (Resuelta) ", 
					"Paludismo por Plasmodium falciparum. (Resuelta)",
					"Trastorno hematológico: Anemia moderada.",
					"Trastorno hidroelectrolítico: hipokalemia leve.",
			

		], 
		
	},#86

	{
		"IdHistoria": "52-92-23", 
		"nombre": "Ohannel jose otero oyague ", 		
		"edad": "36",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1979,1,2), 		
		"ci": "13.630.581", 		
		"dirección": "", 		
		"fechaIngresoHUAPA":  datetime(2015,1,15), 		
		"fechaIngresoUCI": datetime(2015,1,16), 		
		


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en cama de traslado, en aparentes regulares condiciones generales, hemodinámicamente estable, ventilando con mascarilla autoinsuflable con oxigeno húmedo a 5 lts por minutos , se traslada a cama de uci y se conecta a monitor cardíaco externo que reporta:TA: 122/79mmHg FC: 119lpm FR: 17rpm SPO2: 93%''',
			
			"piel" : 	'''	Morena, normotérmica, turgor conservado, llenado capilar < 3 segundos. Escoriaciones múltiples, quemadura por friccion en región de hombro derecho asi como en región dorso lumbar derecha hasta flanco ipsilateral, lesión en cuello tipo abrasión. ''',
	
			"cardiopulmonar":  '''Tórax simétrico, hipomoexpansible, ruidos respiratorios presentes se auscultan roncos dispersos en hemitorax izquierdo, se evidencia tubo torácico izquierdo funcionante, ruidos cardíacos rítmicos, regulares, sin soplos''',
			"abdomen": ''' se evidencia apósitos quirúrgicos limpios y secos,. doloroso en toda su extensión ruidos hidroaéreos disminuidos.''',

			"neurologico": ''' consciente,  Glasgow 14 /15 puntos dados por RM 6 RV 4 RO 4 pupilas isocóricas y normo reactivas. Anestesia de miembros inferiores hasta nivel de las rodillas. hipoestesia de rodilla hasta región umbilical. Sin fuerza muscular.''',
	
		}, 

		"diagnosticoIngresoUCI": [
							"POSTOPERATORIO INMEDIATO DE LAPAROTOMIA EXPLORATORIA.",
							"POLITRAUMATIZADO: SINDROME RAQUIMEDULAR",
							"TRAUMATISMO TORACOABDOMINAL CERRADO COMPLICADO CON NEUMO TORAX IZQUIERDO Y FRACTURA DE TERCER ARCO COSTAL POSTERO IZQUIERDO.",
							"ESCOREACIONES MULTIPLES",
							"TRAUMATISMO CERVICAL IZQUIERDO EN ZONA I Y II NO COMPLICADO.",
							"TRASTORNO HEMATOLOGICO: ANEMIA MODERADA ",
							{"resumen": ''' Paciente que permanece en servicio de terapia intensiva por 72 horas manteniendo estabilidad hemodinámica ,recibió  tratamiento con esteroides Metilprednisolona en infusión continua dosis de 5.4 mg /kg/h así como antibióticoterapia con Ciprofloxacina , recibió una unidad de concentrado globular ,debido a evolución favorable se decide traslado a sala de Cirugía para su posterior seguimiento '''},


									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente es evaluado el día 16/01/15 2:05am por el servicio de cirugía blanda. y en vista de hipo expansibilidad y ausencia de ruidos respiratorios y rayo x, evidencian signos de neumotórax izquierdo, proceden a realizar toracotomía con colocación de tubo torácico. donde se obtienen 20cc de contenido sero hemático, burbujeo(¬¬+++), tope oscilante >3cm. Paciente es revalorado por cirugía alas 4:20am en vista de  descenso en las cifras de hemoglobina  y dolor abdominal, realiza lavado peritoneal el cual reporta positivo, por lo que es llevado a mesa operatoria. Realizando laparotomía exploratoria con los  siguientes hallazgos: Hematoma sin sangrado en mesocolon. Lesión grado I de asa delgada, (hematoma) a 220 CM de asa fija, grado I ciego (laceración) grado I-de Angulo hepático del colon (hematoma). Hematoma no expansivo ni pulsátil en zona III derecho y III de retroperioneo. Toman como conducta: 1).Rafia de lesión del ciego. 2).Se explora hematoma en zona II de retro peritoneo sin hallazgos patológico. Solicitan valoración por el servicio de traumatología. Quien indica  RX centrado en pubis, donde no hay evidencia de trazos de fractura indican mantener conducta expectante. Es valorado por el servicio de neurocirugía solicitando estudios imageneologicos. tratatamiento con: solumedrol y epamin.Es valorado por UCI  y por disponibilidad de cupo se decide su ingreso. ''',
			"piel": ''' Morena, normotérmica, normoelastica turgor conservado, se evidencia lesión zona 2 del cuello llenado capilar < 3 segundos.''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes, sin agregados, ruidos cardíacos rítmicos, regulares, sin soplos. ''',
			"abdomen": '''Globoso, blando, depresible, doloroso a la palpación, ruidos hidroaéreos presentes.  ''',
			"extremidades": '''sin edema, sin sensibilidad miembro superior derecho, en ambos miembros inferiores y conservados en miembro superior izquierdo.''',
			"neurologico": '''paciente que al momento del ingreso tenia Glasgow de 10/15 ptos con descenso neurológico con 8 ptos en la escala de Glasgow. (No discriminan) TA: 100/90mmHg FC: 70lpm FR: 16rpm	''',
			
		},  

		"examenFisicoEgreso":{
			"neurologico": ''' consciente,  Glasgow 14 /15 puntos dados por RM 6 RV 4 RO 4 pupilas isocóricas y normo reactivas. Anestesia de miembros inferiores hasta nivel de las rodillas. Hipoestesia de rodilla hasta región umbilical. Sin fuerza muscular''',
			"abdomen": ''' se evidencia apósitos quirúrgicos limpios y secos,. Doloroso en toda su extensión ruidos hidroaéreos presentes ''',
			"cardiopulmonar": ''' Tórax simétrico, hipoexpansible, ruidos respiratorios presentes se auscultan roncos dispersos en hemitorax izquierdo, se evidencia tubo torácico izquierdo funcionante, ruidos cardíacos rítmicos, regulares, sin soplos.''',
			"piel": ''' Morena, normotérmica, turgor conservado, llenado capilar < 3 segundos. Escoriaciones múltiples, quemadura por fricción en región de hombro derecho así como en región dorso lumbar derecha hasta flanco ipsilateral, lesión en cuello tipo abrasión.  ''',
			"resumen": ''' TA: 134/89mmHg FC: 88 lpm FR: 15rpm SPO2: 98%''',
		},
		"resumenEgreso": ''' Se trata de paciente masculino de 36 años de edad natural y procedente de la localidad sin antecedentes patológicos conocidos, inicia enfermedad actual el día 15/01/15cundo posterior a accidente de tránsito tipo coholicion, presenta traumatismos múltiples, por lo que es traído a esta institución, donde ingresan con los diagnósticos: 1)	POLITRAUMATIZADO: 1.1) SINDROME RAQUIMEDULAR 1-2 TRAUMATISMO TORACOABDOMINAL CERRADO COMPLICADO CON NEUMO TORAX IZQUIERDO Y FRACTURA DE TERCER ARCO COSTAL POSTERIOR IZQUIERDO. 1.3) ESCOREACIONES MULTIPLES 1.4) TRAUMATISMO CERVICAL IZQUIERDO EN ZONA I Y II NO COMPLICADO ''',
		
	}, #87

	{
		"IdHistoria": "52-97-18", 
		"nombre": "karliu Anyeline Gomez Mota", 		
		"edad": "14",
		"sexo": "F",	
		"fechaNacimiento":  datetime(2000,2,27), 		
		"lugarNacimiento": "Maturín", 		
		"ci": "", 		
		"dirección": "san Antonio de Maturín barrio el rincón", 		
		"fechaIngresoHUAPA":  datetime(2015,1,28), 		
		"fechaIngresoUCI": datetime(2015,1,31), 		
		 
		"resumenIngreso": '''Paciente femenina de 14 años de edad, natural y procedente de san Antonio de Maturín, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual el día 18/01/15 cuando comienza a presentara aumento de la temperatura corporal no cuantificada atenuada  con acetaminofen así como mialgia y altralgia tratadas con piroxican, ademas como ligero  rash cutáneo, el día martes 20/01/15 se asocia al cuadro clínico vómitos en dos oportunidades de contenido liquido, diarrea en tres oportunidades. Para el día domingo 25/01/15 se anexa al cuadro clínico tinte ictérico de piel y mucosas, acude al ambulatorio de la localidad el día lunes 26/01/15 donde ingresan por 24 horas bajo observación en vista de no mejoría es evaluada por especialista el cual decide referir a Maturín, por condiciones sociales de familiar decide traerla a esta istitucion el día 28/12/79,es evaluada por el servicio de medicina interna e ingresa con las diagnosticos. ''', 


		"examenFisicoIngresoUCI": {
			
			"piel" : 	'''	se evidencia tinte ictérico de piel y mucosa llenado capilas rapido''',
		

			"cardiopulmonar":  '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados; ruidos cardíacos rítmicos, regulares, taquicárdicos, sin soplos ni galope.''',
			"abdomen": ''' globoso, ruidos hidroaéreos presentes, doloroso ala palpación profunda en toda su extencion se palpa por debajo del reborde costal izquierdo espleno megalia ''',

			"neurologico": ''' estuporosa, con agitación psicomotriz, pupilas isocóricas, normorreactivas a la luz, Glasgow 15/15pts.''',
			
		}, 

		"diagnosticoIngresoUCI": [

									"LEPTOSPIROSIS ",
									"SINDROME ICTERICO",
									"TRASTORNO HEMATOLOGICO:ANEMIA MODERADA",
									"TRASTORNO ACIDO – BASE:ASIDOSIS METABOLICA DESCOMPENSADA",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Signos Vitales: TA: 110/80mmHg	 FC: 115 lpm	FR: 18 rpm. En vista de presentar dolor abdominal es valorada por el servicio de cirugía blanda, planteando colongitis aguda versus leptospirosis hacen sugerencias, solicitan valoración por terapia intensiva y nefrología por retención de azoados. El día 29 es valorada por el servicio de uci y por no contar con cupo hace sugerencias-el día 30 es valorada por el servicio de nefrología quienes hacen sugerencia. el día 30 presenta movimientos tónico clónicos generalizados en dos oportunidades yuguladas con dizepan en horas de la madrugada por condiciones clínicas de la paciente, solicitan revaloración por UCI y por disponibilidad de cupo se decide su ingreso. Se recibe paciente en camilla de traslado, respirando aire ambiente, se pasa a cama UCI, se conecta a monitor cardíaco continuo que reporta: TA: 129/84(94) mmHg, FC: 137 lpm, FR: 38 rpm, SatO2: 97%''',
			"piel": '''Blanca, normotérmica, normoelastica, buen llenado capilar, se evidencia ligera palidez cutánea-mucosa.''',
			
			"abdomen": '''ruidos hidroaéreos presentes, globoso, doloroso a la palpación en epigastrio, hipocondrio y flanco izquierdo, se palpan  reborde esplénico a 2 centímetros del reborde costal(espleno megalia).''',
			"extremidades": '''simétricas, sin edema.''',
			"neurologico": '''Consciente, orientada en los 3 planos.''',

		},  

		"diagnosticoIngresoHUAPA": [
							"Leptospirosis a descartar",
							"Síndrome ictérico febril",
							"Enfermedad renal en estudio",
		], 
		
	}, #88

	{
		"IdHistoria": "52-57- 82", 
		"nombre": "Asdrubal Jose Payares Ramirez", 		
		"edad": "41",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1973,3,2), 		
		"lugarNacimiento": "Carúpano - Estado Sucre", 		
		"ci": "11.436.165", 		
		"dirección": "Macarapana recta la rinconada.", 		
		"fechaIngresoHUAPA":  datetime(2014,10,5), 		
		"fechaIngresoUCI": datetime(2014,10,6), 		
		
		"resumenIngreso": '''Se trata de paciente masculino de 41 años de edad natural y procedente de Carúpano sin antecedentes patológicos importantes quien inicia enfermedad actual el día 04/10/14 cuando posterior a accidente de tránsito tipo colisión moto-vehículo presenta pérdida de estado de consciencia por lo que es trasladado al hospital de Carúpano donde evalúan, realizan paraclínicos que reportan Hb 12 g/dl Hto: 38.8 PLT: 330 Leuc: 11.9. Rx de cráneo que evidencia fractura frontal, parietal y cigomático y TAC cráneo. Por no constar con cupo en UCI se decide traslado a este centro asistencial. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente es trasladado en camilla de transporte, conectado a monitor cardíaco externo que reporta signos vitales: TA: 130/78 (89)mmHg FC: 90lpm FR: 14rpm SatO2: 99%, intubado recibiendo oxigeno por ambu, se pasa a cama UCI, conectándose a ventilador mecánico Vc 560 Fr 12 FiO2 50 Fl 50 TI 1:4 PEEP 0 y a monitor cardiaco externo que reporta signos vitales: TA: 100/54 (71) mmHg FC: 87  lpm FR: 13 rpm  SPO2: 100 % ''',
			
			"piel" : 	'''	Blanca, afebril al tacto, llenado capilar <3 segundos.''',
			"cabeza": ''' Se evidencia signo de equimosis palpebral bilateral y herida quirúrgica en región fronto-parietal derecha cubierta por apósito estéril y drene conectado a bolsa recolectora. ''',

			"cardiopulmonar":  '''tórax simétrico, normo expansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos normofonéticos, taquicárdicos, sin soplos ni galope.''',
			"abdomen": ''' blando, plano, depresible,, ruidos hidroaéreos presentes, no megalias.''',

			"neurologico": '''bajo efectos de sedación, pupilas anisocóricas, midriasis derecha hiporreactivas a respuesta a la luz, Glasgow: no evaluable por sedación.''',
			

		}, 

		"diagnosticoIngresoUCI": [

									"Postoperatorio Inmediato de Drenaje de hematoma intraparenquimatoso frontoparietal derecho.",
									"Traumatismo cráneo encefálico severo.",
									"Fractura de hueso frontal, parietal y cigomático.",
									"Trastorno Hematológico Anemia moderada",

									
								],  

		"examenFisicoIngresoHUAPA": {
			
			"piel": ''' Blanca, normotérmica al tacto, llenado capilar <3 segundos.''',
			"cardiopulmonar": '''Tórax simétrico, normo expansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos normofonéticos, taquicárdicos,  sin soplos ni galope. ''',
			"abdomen": '''blando, plano, depresible,  ruidos hidroaéreos presentes, no megalias. ''',
		
			"neurologico": '''Inconsciente, Glasgow 6/15 puntos (RM 4 RO1 RV1), pupilas isocóricas e hiporreactivas a la luz. ''',
			"cabeza": ''' De aspecto y configuración normal, sin evidencia equimosis y edema bipalpebral bilateral.''',

		},  

		"diagnosticoIngresoHUAPA": [
							"Politraumatizado",
							"Traumatismo Craneo Encefálico Severo",
							"Fractura Fronto Parietal",
							{"resumen": ''' Se solicita valoración por UCI donde se evalúa paciente en emergencia intubado conectado a T de Ayres, no conectado a monitor cardiaco, inconsciente con galsgow 6/15 puntos (RM4 RV1 RO1), pupilas isocóricas hiporreactivas a luz, por lo que se traslada a sala de choque, se conecta a ventilador mecánico AC Vc 560 Fr 12 Fl 50 FiO2 50 PEEP 0; por no contar con cupo disponible en UCI se hacen sugerencias. El paciente es llevado a mesa operatoria el día 05/10/14 donde se realiza craniectomía fronto-parietal derecha drenando hematoma de gran magnitud. El paciente permanece en área de recuperación conectado a ventilación mecánica. El día de hoy por disponibilidad de cupo se decide traslado a UCI.'''},
								
		], 
		
	},#89

	{
		 
		"nombre": "Rosa Elena López Narvaez", 		
		"edad": "50",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1963,10,16), 		
		"lugarNacimiento": "Península de Araya ", 		
		"ci": "535.046", 		
		"dirección": "Guayacán Península de Araya ", 		
		"fechaIngresoHUAPA":  datetime(2014,10,21), 		
		"fechaIngresoUCI": datetime(2014,10,21), 		
		"resumenIngreso": '''Se trata de paciente femenina de 50 años de edad con antecedentes de Hipertensión Arterial desde hace 6 años en tratamiento con Enalapril 10mg BID, Norvasc 5mg O y Amaurosis Bilateral quien inicia enfermedad actual hace 2 meses cuando presenta cefalea, acompañada de náuseas y vómitos, en ocasiones con pérdida del nivel de consciencia, motivos por los cuales acude a este centro privado donde indican TAC de Cráneo evidenciándose TU de Hipófisis por lo que es referida a este centro hospitalario el día 03/09/2014 donde se evalúa y se ingresa.   Es valorada por el Servicio de Neurocirugía quien indica realizar Resonancia Magnética Cerebral con contraste evidenciándose: LOE de apariencia tumoral en la región selar, apariencia sólida, produciendo ruptura de la silla turca, compresión del quiasma óptico y sobre el III ventrículo, posterior a la administración de contraste (Gadolinio) se evidencian algunas áreas hipointensas probablemente por necrosis tumoral, lesión de aproximadamente 7x5cms de diámetro. Ejerce compresión sobre el tallo cerebral. Efecto compresivo de la lesión tumoral sobre la arteria comunicante anterior y la arteria cerebral anterior. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe  paciente en camilla de traslado conectada a ventilación mecánica, se traslada  a cama UCI y se conecta monitor cardiaco continuo''',
			
			"piel" : 	'''	blanca, fría al tacto, llenado capilar <3segundos.''',
			

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes sin agregados. Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos. ''',
			"abdomen": ''' globoso, blando, ruidos hidroaéreos presentes.''',

			"neurologico": ''' no evaluable por efectos anestésicos. Pupilas isocóricas con tendencia a la midriasis, hiporreactivas a la luz.''',
		}, 

		"diagnosticoIngresoUCI": [

									"Postoperatorio Inmediato de Craneotomía Pterional Derecha para Exceresis de Tu de Hipófisis (no resecado)",
									"Macroadenoma de Hipófisis",
									"Hipertensión Arterial Sistémica.",

									
								],  

		"examenFisicoIngresoHUAPA": {
		
			"piel": ''' Normotérmica, deshidratada, llenado capilar <3segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, con estertores roncus. Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos.''',
			"abdomen": '''globoso, blando, no doloroso a la palpación superficial ni profunda, no visceromegalias. ''',
			
			"neurologico": '''Conservado''',
			

		},  

		"diagnosticoIngresoHUAPA": [
							"Tu. Cerebral",
							"Hipertensión Arterial",
							"Deshidratación Leve",
							{"resumen":''' La paciente permanece en Área de Hospitalización hasta el día de hoy cuando es llevada a mesa operatoria y bajo anestesia general inhalatoria se realiza craneotomía, retiro de flap óseo, disección subfrontal y temporal con evidencia de accidente de vasos sanguíneos, control de sangrado, síntesis por planos, asepsia final. Se mantiene durante acto operatorio hemodinámicamente estable con un sangrado estimado de 800 cc y se traslada a UCI. '''}

		], 
		
	},# 90

	{ 
		"nombre": "Eduard Tomas Ramos Padrón", 		
		"edad": "37",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1976,1,25), 		
		"lugarNacimiento": "Cumaná", 		
		"ci": "15.288.431", 		
		"dirección": "San Agustin, Vía Cumanacoa.", 		
		"fechaIngresoHUAPA":  datetime(2014,8,17), 		
		"fechaIngresoUCI": datetime(2014,8,17), 		
		"resumenIngreso": '''Se trata de paciente masculino de 37 años de edad, con antecedentes de Fumar Cigarrillo una caja diaria, quien refiere inicio de enfermedad actual el día 16/08/2014 presenta traumatismos múltiples con objeto desconocido (posiblemente arma blanca), permanece sin recibir atención hasta el día de hoy cuando es encontrado y trasladado a este centro hospitalario donde es evaluado y se decide su ingreso.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Signos Vitales: TA: 130/70mmHg FC: 80lpm FR: 16rpm''',
			
			"piel" : 	'''	Hidratada, normotérmica, normoelastica, llenado capilar < 3 segundos.''',
			"cabeza": ''' Normocefalo, múltiples traumatismos con laceración, bordes bien definidos.''',

			"cardiopulmonar":  '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes, disminuidos en hemitórax izquierdo, ruidos cardíacos sin soplos. ''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, doloroso a la palpación superficial y profunda.''',

			"neurologico": ''' consciente, orientado en tiempo, espacio y persona. Glasgow: 12/15pts (no discriminado). ''',
			"extremidades": '''simétricas, dolorosas a la movilización.''',

		}, 

		"diagnosticoIngresoUCI": [

				"Politraumatizado",
				"Traumatismo Craneoencefálico Severo",
				"Traumatismo Torácico Cerrado complicado con Neumotórax Completo",
				"Traumatismo Abdominal Cerrado",
				"Trauma Renal a descartar",
				"Shock Hipovolémico",
				"Trastorno Hematológico: Anemia Leve",
				"Trastorno Acido/Base: Acidosis Metabólica Descompensada con Alcalosis Respiratoria.",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se recibe paciente en malas condiciones generales, hemodinámicamente inestable, se procede a intubar y conectar a ventilación mecánica, en vista de cifras tensionales se inicia Norepinefrina por Bomba de Infusión Contínua a razón de 53, 3 mic/min, se cateteriza Vía Venosa Central en Vena Yugular Izquierda, se conecta a monitor cardíaco externo que reporta: TA: 66/54mmHg	FC: 74lpm FR: 19rpm SPO2:100%''',
			"piel": ''' blanca, normotérmica, se evidencian múltiples escoriaciones, de bordes irregulares, sin secreciones. Se evidencia aumento de volumen y equimosis en región palpebral y cigomática izquierda.''',
			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes, disminuidos en base pulmonar izquierda, se evidencia tubo de drenaje torácico conectado a trampa de agua, oscilante, con escasa salida de contenido hemático, Ruidos cardíacos rítmicos, regulares, sin soplos.	''',
			"abdomen": '''plano, blando, se le realiza lavado peritoneal el cual resulta macroscópicamente negativo. ''',
		
			"neurologico": '''Inconsciente, Glasgow: 3/15 pts. Respuesta Motora: 1pt, Respuesta Verbal: 1pt. Apertura Ocular: 1pt. Pupilas levemente anisocóricas, midriasis izquierda, hiporreactivas a la luz.''',
			"cabeza": ''' Normocefalo, con múltiples laceraciones en cuero cabelludo, de bordes bien definidos, rafiadas, sin secreciones.''',

		},  

		"diagnosticoIngresoHUAPA": [
								
			"Traumatismo Craneoencefálico Moderado",
			{"resumen":''' El paciente en el Área de Emergencia es valorado por Servicio de Cirugía quien realiza radiografía de tórax evidenciándose Neumotórax Completo y se toma como conducta colocación de tubo de drenaje torácico de 36 french con toracotomía mínima, se conecta a Trampa de Agua y se evidencia burbujeo, se toman laboratorios para control hematológico, se coloca Sonda de Foley Transuretral obteniéndose gasto urinario hemático por tal motivo realizan ECO FAST el cual no muestra presencia de líquido libre en cavidad abdominal por lo que sugieren realización de UROTAC. Durante su estancia presenta de forma súbita deterioro neurológico 3pts de Glasgow además de trabajo respiratorio motivos por los cuales solicitan valoración por el Servicio de UCI quien en vista de disponibilidad de cupo se decide su ingreso.'''}
		], 
		
	},# 91


	{
		"IdHistoria": "52-44-87 ", 
		"nombre": "Emiliana Del Carmen Caraballo Medina ", 		
		"edad": "65",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1949,6,6), 		
		"lugarNacimiento": "Carúpano", 		
		"ci": "3.834.324", 		
		"dirección": "Carúpano", 		
		"fechaIngresoHUAPA":  datetime(2014,10,7), 		
		"fechaIngresoUCI": datetime(2014,10,9), 		
		"antecedentes": '''Alergia a ZALDIAR Y CEFALEXINA. Diabetes Mellitus tipo 2 tratada con Amaryl. Hábitos tabáquicos tipo cigarrillo (½ caja) desde los 14 años hasta hace 10 años.''', 
		"resumenIngreso": '''Se trata de paciente femenina de 65 años de edad natural y procedente de Carúpano quien hace 5 meses aproximadamente cuando acude a valoración por Neumonólogo y realiza el hallazgo casual de Lesión radiológica compatible con Tu. Pulmonar derecho motivo por el cual refiere a Servicio de Cirugía de Tórax, es valorada por Especialista quien decide referir a este centro para ingreso y resolución quirúrgica. El día 14/08/2014 se realiza TAC de Tórax con Contraste que reporta: Imagen de LOE SOLIDO en segmento Laterobasal derecho, densidad para tejido sólido, tamaño 3,5x 2,6cms.''', 


		"examenFisicoIngresoUCI": {
			"piel" : 	'''	Morena, normotérmica, turgor disminuido, leve palidez cutáneo-mucosa, llenado capilar < 3 segundos.''',
			

			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible, ruidos respiratorios presentes, no se auscultan agregados, se evidencia tubo de drenaje torácico conectado a Pleuroevac con salida de escaso contenido hemático, oscilante, ruidos cardíacos rítmico , sin soplos.	''',
			"abdomen": ''' globoso, blando, depresible, no doloroso a la palpación, no se palpan visceromegalias.''',

			"neurologico": ''' Consciente orientada Glasgow 15/15 puntos . Pupilas isocóricas, reactivas a la luz.''',
		
		}, 

		"diagnosticoIngresoUCI": [

				"Postoperatorio Inmediato de Toracotomía Posterolateral Derecha.",
				"LOE en segmento posterobasal de pulmón derecho.",
				{"resumen": ''' Paciente que evoluciona de forma satisfactoria tolerando extubación a las 48 horas del post quirúrgico sin complicaciones permanece 36 horas recibiendo oxigeno húmedo a razón de 10 lt por minuto con mascarilla facial ,recibiendo antibióticoterapia con ciprofloxacino con paraclínicos dentro de limites normales ,debido a evolución satisfactoria se decide su egreso para seguimiento por servicio tratante .En estos momentos conectada  a monitor cardiaco que reporta FC 88 LPM    FR 23 RPM    TA 130/67 MMHG   SATO2 99 % '''},

									
								],  

		"examenFisicoIngresoHUAPA": {
			
			"piel": ''' Morena, normotérmica, turgor disminuido, leve palidez cutáneo-mucosa, llenado capilar < 3 segundos.''',
			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes, no se auscultan agregados,  se evidencia tubo de drenaje torácico conectado a Pleuroevac con salida de escaso contenido hemático, oscilante, ruidos cardíacos rítmicos, taquicárdicos, sin soplos.''',
			"abdomen": '''globoso, blando, depresible, no doloroso a la palpación, no se palpan visceromegalias.''',
			
			"neurologico": '''no evaluable por sedación farmacológica. Pupilas isocóricas, no reactivas a la luz.''',
			

		},  

		"diagnosticoIngresoHUAPA": [
			"LOE en segmento posterobasal de pulmón derecho. ",
			{"resumen":''' Paciente permanece en el Área de Hospitalización y es llevada a mesa operatoria el día 09/10/2014 donde bajo anestesia general balanceada se le realiza Toracotomía Posterolateral Derecha encontrándose lo siguiente: Tu pulmonar de 2x2cms en región basal derecha, se toma como conducta segmentomía basal derecha, rafia con seda 2,0 y aerostasia con crómico 3,0, comprobación de hemostasia, colocación de tubo de drenaje torácico 32french anterior y posterior derecho a nivel de 7mo EIC derecho, se conecta a Pleurovac, rafia por planos y asepsia final, se traslada a cama de UCI, intubada, conectada a ventilación mecánica, se conecta a monitor cardíaco externo que reporta: TA: 179/96mmHg FC: 127lpm FR: 19rpm SPO2: 99% '''},
								

		], 
		"diagnosticoEgreso": [
			"Postoperatorio mediato de Toracotomía Posterolateral Derecha.",
			"LOE en segmento posterobasal de pulmón derecho.",

		],
		
	},# 92

	{
	
		"nombre": "ARELIS CASTRO ", 		
		"edad": "57",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1957,1,2), 		
		"fechaIngresoHUAPA":  datetime(2014,4,9), 		
		"fechaIngresoUCI": datetime(2014,4,9), 		
		"antecedentes": '''DM TIPO 2   HIPERTENSION ARTERIAL ''', 
		"resumenIngreso": ''' Se trata de paciente femenina de 57 años de edad con antecedentes de hipertensión arterial y diabetes Mellitus tipo 2 no controladas .Inicia enfermedad actual el dia 2 del presente mes con cuadro caracterizado por cefalea intensa vomitos a repetición y disminución de la fuerza muscular del hemicuerpo derecho ingresa a centro privado donde se evidencian cifras de TA elevadas cuantificadas en 190 /100 mmhg motivo por el cual es evaluada por cardiología quien decide su ingreso en sala de hospitalización con dignostico de Crisis hipertensiva  y Diabetes Mellitus tipo 2 descompensada siendo evaluado además por internista de guardia quienes indican la realización de TAC cráneo que reporta : hallazgos sugestivos de HSA con mayor representación entre lobulos frontales y cisura interhemisferica frontal donde hay colección hemática y con discreto componente asociado a IV ventrículo y asta occipital izquierda ,Edema cerebral difuso  ,se mantiene hospitalizada en habitación recibiendo nimotop ,antihipertensivos insulina lantus e hidratación parenteral ,para el dia de ayer se evidencia deterioro neurológico acentuado con Glasgow de 11 puntos disartria hemiplejia derecha se pactica estudio tomográfico que revela hallazgos sugestivos de isquemia secundaria a vasoespasmo localización frontoparietal izquierda  ,reabsorción parcial del componente hemorrágico subaracnoideo motivo por el cual se decide ingreso a terapia intensiva de centro privado. En vista de inestabilidad hemodinámica se decide colocar levophed y solicitar cupo en UCI HUAPA debido a situación socioeconómica ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente evaluada que luce en malas condiciones generales, afebril, eupneica. TA: 120/87mmHg FC: 67lpm FR: 14rpm''',
			
			"piel" : 	'''palidez cutáneo mucosa, llenado capilar < 3segundos.''',
			

			"cardiopulmonar":  ''' tórax simétrico expansible, ruidos respiratorios presentes en ambos hemitórax, no ausculto agregados, ruidos cardíacos rítmicos, regulares, no ausculto soplos.''',
			"abdomen": ''' blando, depresible, ruidos hidroaéreos presentes.''',

			"neurologico": ''' paciente bajo efectos de sedantes pupilas mióticas hiporreactivas  ''',

		}, 

		"diagnosticoIngresoUCI": [

									"HSA Fisher IV HH 2 complicada con isquemia secundaria debida a vasoespasmo", 
									"Deshidratación moderada",
									"Ttno he hipokalemia severa", 
									"HTA sistémica", 
									"DM TIPO 2 descompensada",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente evaluada que luce en malas condiciones generales, afebril, eupneica. TA: 120/87mmHg	FC: 67lpm FR: 14rpm Paciente que es recibida en camilla de traslado  conectada a mascarilla con reservorio recibiendo oxigeno húmedo a razón de 10 lt por minuto se conecta a monitor cardiaco que reporta TA 132/78 MMHG  FR 13 FC 67 LPM SAT O2 100 %  se conecta a ventilación mecánica con parámetros establecidos .
					   ''',
			"piel": ''' palidez cutáneo mucosa, llenado capilar < 3segundos.''',
			"cardiopulmonar": '''tórax simétrico expansible, ruidos respiratorios presentes en ambos hemitórax, no ausculto agregados, ruidos cardíacos rítmicos, regulares, no ausculto soplos. ''',
			"abdomen": '''blando, depresible, ruidos hidroaéreos presentes.''',
			
			"neurologico": '''paciente bajo efectos de sedantes pupilas mióticas hiporreactivas ''',
			

		},  

		"diagnosticoIngresoHUAPA": [
					"HSA Fisher IV HH 2 complicada con isquemia secundaria debida a vasoespasmo ",
					"Deshidratación moderada",
					"Ttno he hipokalemia severa ",
					"HTA sistémica ",
					"DM TIPO 2 descompensada ",
			

		], 
		
	},# 93

	{
	
		"nombre": "Egdina Solangel Campos de Boada", 		
		"edad": "62",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1952,2,17), 		
			
		"ci": "3.872.734", 		
		"dirección": "URB F e y Alegria ", 		
		"fechaIngresoHUAPA":  datetime(2014,3,19), 		
		"fechaIngresoUCI": datetime(2014,3,19), 		
		"antecedentes": ''' Alergias: NO REFIERE. Transfusiones: SI. Intervenciones quirúrgicas: TU COLON 2012. APP:  TU COLON SIGMOIDES ''', 
		"resumenIngreso": '''Se trata de paciente femenino de 62  años de edad con antecedentes de Hemicolectomia Radical Izquierda con confección de Colostomía de Harman en el mes de marzo del año de 2013 por Cáncer de Colon  izquierdo obstruido ,la cual recibió posteriormente quimioterapia coadyuvante 5Fu por 6 dosis ,comienza enfermedad actual hace aproximadamente 3 meses dado por la presencia de sangrado rectal abundante ameritando transfusiones sanguíneas en múltiples ocasiones ,se realiza seguimiento especializado por cirugía oncológica realizándose multiples studios dentro de los que se incluyen : Biopsia la cual informa ADC DE COLON ST IIIB ,Endoscopia digestiva baja ,Ecosonografia abdominal cuyos informes se anexan ,decidiéndose realizar Laparotomia exploradora por lo que se hospitaliza a cargo de cirugía blanda . ''', 


		"examenFisicoIngresoHUAPA": {

			"resumen": ''' TA: 128 /80  mmHg FC: 67 lpm FR: 12 rpm SPO2: 99 %''',
			
			"piel" : 	'''	Blanca, normotermica al tacto, llenado capilar < 3 segundos. ''',
			

			"cardiopulmonar":  '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos rítmicos, regulares, bradicárdicos  hipofonéticos,  sin soplos ni galope.''',
			"abdomen": ''' globoso, blando, depresible, ruidos hidroáreos presentes, no megálico.''',

			"neurologico": ''' consciente Glasgow 15/ 15 puntos dados por RM 6 RV 5 RO 4 Pupilas isocóricas reactivas reflejos osteotendinosos presentes ''',
			
		}, 

		"diagnosticoIngresoUCI": ["POI",],  

		"examenFisicoIngresoUCI": {
			"resumen": '''TA: 125 /76 mmHg FC: 75 lpm FR: 12 rpm SPO2: 100 %''',
			"piel": ''' Blanca, normotérmica al tacto, llenado capilar < 3 segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible , ruidos respiratorios presentes en ambos campos pulmonares, sin agregados estertores, ruidos cardíacos rítmicos, regulares,  hipofonéticos,  sin soplos ni galope. ''',
			"abdomen": '''blando, depresible, doloroso a la palpación superficial y profunda ,herida quirúrgica cubierta por apósito estéril drenes colocados en región de fondo de saco ,otro ubicado en espacio parieto cólico izquierdo  y citostomia  ruidos hidroáreos presentes, no megálico.''',
			"neurologico": '''bajo efectos de sedación''',
			

		},  

		"diagnosticoIngresoHUAPA": [
			{"resumen":''' Paciente que es intervenida el día de hoy. Recibimos paciente en  camilla de traslado recibiendo oxigeno mediante mascarilla autoinsuflable conectada  a reservorio, no conectado a monitor cardiaco. Se conecta a monitor cardiaco.'''},
			"TU COLON SIGMOIDES ",
								

		], 
		
	},# 94

	{
		"nombre": "Carmen Julieta alfonzo", 		
		"edad": "75",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1939,7,9), 		
		"lugarNacimiento": "Cumana ", 			
		"dirección": "calle Vargas, #98, Cumaná, Edo. Sucre", 		
		"fechaIngresoHUAPA":  datetime(2015,5,31), 		
		"fechaIngresoUCI": datetime(2015,5,31), 		
 
		"resumenIngreso": '''Paciente femenina de 75 años de edad, natural y procedente de la localidad, con antecedentes de diabetes mellitus tipo 2, en tratamiento con Januvia® (100 mg) y Biofit® 500mg OD, hipertensión arterial en tratamiento con Exforge®, cuyo familiar refiere inicio de enfermedad actual hace 20 días aproximadamente cuando presenta de manera súbita cuadro de dificultad respiratoria a pequeños esfuerzos, por lo cual es traslada a hospital Julio Rodríguez donde permanece ingresada durante 9 días con diagnósticos de edema agudo de pulmón, egresando posteriormente en vista de mejoría clínica, acude posteriormente a consulta de cardiología donde omiten tratamiento antipertensivo en vista de constatar cifras de tensión con tendencia a la hipotensión arterial, permanece asintomática durante 15 días.  El día 29/05/2015 en horas de la noche presenta nuevo episodio de disnea a pequeños esfuerzos, cianosis peribucal y diaforesis, acude a centro privado donde  es evaluada e ingresada en área de terapia intensiva. ''', 

		"diagnosticoIngresoUCI": [

								"INSUFICIENCIA RESPIRATORIA AGUDA ",
								"NEUMONIA NOSOCOMIAL BILATERAL",
								"EDEMA AGUDO DEL PULMON NO CARDIOGENICO",
								"TRASTORNO DE LA CONDUCCION :BCRIHH",
								"DIABETES MELLITUS TIPO ii",
								"PIE DIABETICO DERECHO",
								"HIPERTENSION ARTERIAL SISTEMICA",
								{"resumen":''' Permanece en área de UCI durante 24 horas y por presentar trabajo respiratorio, desaturación por monitor y corroborado por gases arteriales, se procede a intubación endotraqueal y se conecta a ventilación mecánica, en vista de condiciones socioeconómicas se decide su traslado a la UCI HUAPA  Se recibe paciente en camilla de traslado conectada a ventilación mecánica de trasporte,  se traslada a cama de uci y se conecta a monitor cardiaco externo que reporta. Signos Vitales: TA: 93/59(71) mmHg	        FC: 88 lpm            	FR: 18 rpm               SO2: 85%'''},

									
								],  

		"examenFisicoIngresoHUAPA": {

			"piel": ''' Blanca, hipotérmica al tacto, llenado capilar < 3 segundos, se evidencia ligera palidez cutánea-mucosa.''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, con agregados crepitantes bibasales; ruidos cardíacos rítmicos, regulares, sin soplos ni galope.''',
			"abdomen": '''ruidos hidroaéreos presentes, globoso a expensa de panículo adiposo, no doloroso a la palpación profunda, no se palpan visceromegalias.''',
			"extremidades": '''simétricas, sin edema se evidencia apósito estéril que cubre lesión de pie diabético limpio y seco no fétido.''',
			"neurologico": '''no evaluable por efectos de sedación y relajación farmacológica.''',
			

		},  

		"diagnosticoIngresoHUAPA": [
						"SINDROME DE DISTRES RESPIRATORIO AGUDO",
						"EDEMA AGUDO DE PULMON NO CARDIOGENICO",
						"NEUMONIA NOSOCOMIAL BILATERAL",
						"TRASTORNO DE CONDUCCION: BCRIHH",
						"HIPERTENSION ARTERIAL SISTEMICA",
						"DIABETES MELLITUS TIPO 2",
						"PIE DIABETICO DERECHO",
						"TRASTORNO HEMATOLOGICO: ANEMIA MODERADA",
						"TRASTORNO ACIDO – BASE:ASIDOSIS METABOLICA DESCOMPENSADA CON ALCALOSIS RESPIRATORIA MAS HIPEROXEMIA",
		

		], 
		
	},# 95

	{
		"IdHistoria": "523596", 
		"nombre": "MIREYA DEL VALLE GUZMAN SIMANCAS ", 		
		"edad": "51",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1962,12,6), 		
		"lugarNacimiento": "ANZOATEGUI", 		
		"ci": "6.120.514", 		
		"dirección": "Campeche calle 10 casa numero 12", 		
		"fechaIngresoHUAPA":  datetime(2014,8,27), 		
		"fechaIngresoUCI": datetime(2014,8,27), 		
		
		"resumenIngreso": '''Se trata de paciente femenina de 51 años de edad natural de Anzoátegui y procedente de la localidad quien inicia enfermedad actual en el pasado mes de diciembre dado por sangrado genital abundante concomitante  dolor en hipogastrio de moderada intensidad ,debilidad muscular y mareos acude a facultativo de la localidad indicando tratamiento sin mejoría clínica ,el día 9 de agosto acude a este centro asistencial previa realización de TAC de ABDOMEN Y PELVIS en la que se evidencia TU CUERPO UTERINO es referida por especialista para resolución quirúrgica motivo por el cual se decide su ingreso''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' inconsciente, pupilas isocóricas reactivas reflejo corneal presente Glasgow 3/15	''',
			
			"piel" : 	'''	Blanca, normotérmica, hidratada, llenado capilar < 3 segundos.se observa via venosa central subclavia derecha ''',

			"cardiopulmonar":  ''' tórax simétrico normo expansible, sin agregados, ruidos cardíacos taquicárdicos , regulares, sin soplos.''',
			"abdomen": ''' blando,globoso depresible, no doloroso a la palpación, no megalias.Se observa herida suprapara e infraumbilical cubierta por aposito esteril impregnados en secreción hemática RHA ausentes  ''',
		}, 

		"diagnosticoIngresoUCI": [

									"Shock hipovolemico debido a :  ",
									"POI laparotomía para resección de TU CUERPO UTERINO  complicado con lesión iatrogénica de vejiga ",
									"Ttno hematológico Anemia severa", 
									"Ttno AB Acidosis metabólica descompensada ",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": '''Paciente en aparentes regulares condiciones generales, afebril, eupneica. Sin Signos Vitales al ingreso. ''',
			"piel": ''' Blanca, normotérmica, hidratada, llenado capilar < 3 segundos.''',
			"cardiopulmonar": '''tórax simétrico normo expansible, sin agregados , ruidos cardíacos rítmicos, regulares, sin soplos. ''',
			"abdomen": '''blando, depresible, no doloroso a la palpación, no megalias.RHA presentes ''',
			
			"neurologico": '''consciente, somnolienta, orientada en TEP pupilas isocóricas reactivas refelejo corneal presente ''',
		},  

		"diagnosticoIngresoHUAPA": [
							{"resumen": ''' TU CUERPO UTERINO. Paciente que para el día de hoy es llevada a mesa operatoria donde se realiza laparotomía media suprapara umbilical  donde se observa TU en cuerpo uterino tomándose como conducta HISTERECTOMIA ABDOMINAL TOTAL MAS RESECCION DE TU ,LESION IATROGENICA DE VEJIGA LA CUAL SE REPARA EN DOS PLANOS ,CON PERDIDA APROXIMADA DE 3000 CC DE SANGRE. En  acto operatorio se constata hipotensión arterial, desaturacion por lo que es llamado residente de UCI quien en vista de disponibilidad de cupo se decide su ingreso.'''},	

		], 
		
	},# 96

	{
		 
		"nombre": "Jose Gregorio Hernandez", 		
		"edad": "63",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1952,10,16), 		
		"lugarNacimiento": "Cumana", 		
		"ci": "6.425.595", 		
		"dirección": "calle cocollar numero 58 ", 		
		"fechaIngresoHUAPA": datetime(2015,12,30), 		
		"fechaIngresoUCI": datetime(2015,12,30), 		
 
		"resumenIngreso": '''Se trata de paciente  masculino 63 años de edad natural y procedente de la localidad sin antecedentes patológicos conocidos de Güira  quien inicia enfermedad actual el 26/12/15  caracterizada por fiebre no cuantificada y malestar general , el 28/12/2015 presenta dificultad respiratoria a medianos y pequeños esfuerzos de corrobora tensión arterial en 80/50 mm hg, frecuencia cardiaca en 110 por minuto , frecuencia respiratoria de 38 por minuto motivo por el cual se evalua y se decide su ingreso. ''', 

		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente evaluado en conjunto con la doctora roa intensivista de guardia  quien indica ingreso a la unidad de  cuidados intensivos. Se conecta a ventilación mecánica y se realiza vía venosa femoral derecha''',
			
			"piel" : 	'''	 TA:85 /57 mmHg FC90: lpm  FR:  16rpm SPO2:97 % morena, se evidencia palidez cutánea y sudoración profusa , llenado capilar menor de tres segundos.''',
			

			"cardiopulmonar":  ''' torax simétrico normoexpansible se auscultan crepitantes en ambos hemitorax ,ruidos cardiacos rítmicos sin soplo  ni galope.''',
			"abdomen": ''' RsHsAs positivos, globoso, blando, depresible, no impresiona doloroso.''',

			"neurologico": ''' Inconsciente, pupilas mióticas reactivas a la luz, Glasgow no evaluable por sedación farmacológica. ''',
			"extremidades": '''simetricas, sin edemas.''',

		}, 

		"diagnosticoIngresoUCI": [

									"Post operatorio mediato de craneotomia fronto temporal derecha para drenaje de hematoma epidural frontotemporal derech.", 
									"Politraumatizado :",
									"TCE  severo.",
									"Traumatismo toracoabdominal cerrado. ",
									"Fractura de tercio medio de humero izquierdo con tutor externo.",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 80/ 50 mmHg  FC:11o  lpm FR: 38  rpm SPO2: 90  %. Se evalua paciente en cama quien luce en aparentes regulares condiciones generales , febril , disneico , conectado a ventilación mecánica . ''',
			"piel": ''' morena , febril al tacto , llenado capila menor de tres segundos , se evidencia cianosis distal. torax simétrico normoexpansible , ruidos respiratorios presentes con agregados tipo crepitantes en ambos campos pulmonares , ruidos cardiacos rítmicos sin soplo ni galope.''',
			
			"extremidades": '''simetricas , sin edemas.''',
			"neurologico": '''insconciente, Glasgow no evaluable paciente bajo sedación farmacologica ''',
			


		},  

		"diagnosticoIngresoHUAPA": [
								"Síndrome viral agudo a precisar.",
								"Insuficiencia cardiaca descompensada.",
								"Miocardiopatía viral.",
								"Síndrome coronario agudo sin elevación del ST ",
								"Sindrome metabolico.",
								"Infección respiratoria baja. ",


		], 
		
	},# 97

	{
		"IdHistoria": "53-80-10", 
		"nombre": "Luis Rafael Jiménez", 		
		"edad": "61",
		"sexo": "M",	
		"fechaNacimiento":  datetime(1954,9,15), 		
		"lugarNacimiento": "Cumaná - Estado Sucre.", 		
		"ci": "4.494.061", 		
		"dirección": "Sector Tres picos", 		
		"fechaIngresoHUAPA":  datetime(2015,9,25), 		
		"fechaIngresoUCI": datetime(2015,11,17), 		

		"resumenIngreso": '''Se trata de paciente masculino de 61 años de edad con antecedentes de Hipertensión Arterial Sistémica en tratamiento con Adalat Oros 30mg OD, Furosemida 20mg OD,  Enfermedad Renal Crónica en Hemodiálisis y Enfermedad Poliquística Renal. Quien inicia enfermedad actual el día 02/09/2015 cuando presenta dolor de fuerte intensidad en región precordial, por tal motivo acude a ambulatorio de la localidad realizan paraclínicos constatando cifras elevadas de azoados  y egresan sin tratamiento. El día 14/09 presenta nuevamente episodio de dolor precordial acudiendo nuevamente a ambulatorio de la localidad donde constatan cifras de tensión elevadas y arritmia no precisada, por tales motivos refieren a este centro hospitalario e ingresado por el Servicio de Medicina Interna, permaneciendo durante 9 días en Área de Hospitalización, egresando posteriormente con seguimiento por Servicio de Cardiología. El día 19/10/15 se realiza Ecocardiograma donde se evidencia Ventrículo Izquierdo Dilatado,  con función sistólica conservada FE=41%, Aurícula Izquierda Dilatada, Derrame Pericárdico Anterior y Posterior Derecho con Colapso Diastólico de Aurícula y Ventrículo Derecho, Válvula Aórtica con regurgitación leve, Válvula Tricúspidea con regurgitación moderada, por lo que referido a  este centro asistencial e ingresado nuevamente por el Servicio de Medicina Interna ''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente intubado, recibiendo oxígeno por Ambú, se traslada a cama de UCI, se conecta a ventilación mecánica, se conecta a monitor cardíaco externo que reporta: Signos Vitales: TA: 131/72mmHg	FC: 147lpm  FR: 12rpm SPO2: 98% ''',
			
			"piel" : 	'''	Blanca, normotérmica, normoelástica, turgor conservado, llenado capilar < 3 segundos.''',
			

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitórax, se auscultan crepitantes  sin agregados, se evidencia tubos de drenaje en región anterolateral izquierda con salida de moderada cantidad de secreción serohemática,  ruidos cardíacos rítmicos, regulares, con soplo en foco mitral.''',
			
			"abdomen": '''globoso, blando, depresible, no impresiona dolor a la palpación, se evidencia aumento de volumen en región de hipocondrio izquierdo. ''',

			"neurologico": '''No evaluable por sedación farmacológica.  Pupilas isocóricas reactivas la luz.  ''',
			"extremidades": '''simétricas, eutróficas, sin edema ni deformidades. ''',

		}, 

		"diagnosticoIngresoUCI": [
							"Postoperatorio Inmediato de Pericardiectomía para drenaje de Derrame Pericárdico.",
							"Derrame Pericárdico Anterior y Posterior moderado con colapso diastólico de aurícula y ventrículo derecho.",
							"Enfermedad Poliquística Renal",
							"Enfermedad Renal Crónica en Hemodiálisis",
							"Hipertensión Arterial Sistémica",
							"Trastorno Hematológico: Anemia Moderada, PTT prolongado",
							"Trastorno Acido/Base: Acidosis Metabólica Descompensada.",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' El paciente permanece durante 53 días en el Área de Hospitalización a cargo del Servicio de Cirugía Vascular y Medicina Interna en espera de resolución quirúrgica, es valorado por el Servicio de Nefrología quien decide colocación de Catéter de Hemodiálisis y brindar apoyo dialítico hasta la actualidad. El día de hoy (17/11/2015) es llevado a mesa operatoria donde bajo anestesia general realizan toracotomía anterior izquierda,  pericardiectomía de aproximadamente 10cms2, se toma muestra para biopsia, citológico, citoquímico, cultivo y antibiograma, comprobación de hemostasia, cierre por planos, se dejan 2 drenes conectados a Pleurevac y Trampa de Agua. Posteriormente se traslada a Servicio de UCI. ''',
			"piel": ''' Blanca, normotérmica, normoelástica, se evidencia pálidez cutánea.''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitórax, sin agregados,ruidos cardíacos rítmicos, regulares, sin soplos.''',
			"abdomen": '''globoso, blando, depresible, no impresiona dolor a la palpación, no megalias. ''',
			"extremidades": '''simétricas, eutróficas, sin edema ni deformidades. ''',
			"neurologico": '''paciente consciente, orientado en los 3 planos.''',
		

		},  

		"diagnosticoIngresoHUAPA": [
								
			"Cardiopatía Isquémica Aguda ",
			"Miocardiopatía en fase dilatada en ICC CFIII",
			"Fibrilación Auricular con RVR",
			"Trastorno de Conducción: BSARIHH",
			"Derrame Pericárdico Anterior y Posterior Moderado con colapso diastólico de Aurícula Derecha",
			"Tu. en Hipocondrio Derecho.",

		], 
		
	},# 98

	{
		
		"nombre": "MARIO ANTONIO RIVAS GONZALEZ", 		
		"edad": "50",
		"sexo": "M",	
		"fechaNacimiento":  datetime(9954,9,26), 		
		"lugarNacimiento": "VALENCIA", 		
			
		"dirección": "Cumanacoa, Estado SUCRE", 		
		"fechaIngresoHUAPA":  datetime(2015,1,13), 		
		"fechaIngresoUCI": datetime(2015,1,25), 		
		
		"resumenIngreso": '''Se trata de paciente masculino de 60 años de edad natural de valencia  y procedente de Mariguitar, con antecedentes de leucemia mielomonocitica crónica diagnosticada en Julio de 2014 en quimioterapia, quien inicia enfermedad actual el 13/1/15  posterior a consulta de hematología realiza hematología especial que reporta descenso de hemoglobina (Hb 5.7g/dl) y leucocitosis en 144.000  a predominio de blastos 100%, por lo que refiere al servicio de medicina interna e ingresan con los diagnósticos de: LEUCEMIA MIELOMONOCITICA CRONICA. TRASTORNO HEMATOLOGICO: ANEMIA SEVERA. Para el 24/01/15 comienza a presentar fiebre 38,7ºc, cefalea ipsilateral y nauseas precedida de vómitos en 2 oportunidades. El día de hoy 25/01/15  el servicio de medicina interna pide valoración  por el servicio de cirugía blanda por paciente presentar  abdomen distendido, dolor a la palpación superficial y profunda en toda su extensión y por evidencia de masa en hipocondrio izquierdo,  es evaluado por cirugía blanda e indica preparar para quirófano, donde realizan  bajo anestesia general,  laparotomía media xifopubica, encontrando como hallazgo: 500cc de liquido purulento no fétido, hepato-esplenomegalia, bazo con múltiples orificios de abscesos, donde realizan evacuación de secreción purulenta y lavado de cavidad abdominal con 5000cc de solución 0,9% y procedieron a cierre de dicha cavidad. Por paciente encontrarse en malas condiciones generales, piden valoración por servicio de terapia intensiva que por disponibilidad de cupo se ingresa.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, en condiciones clínicas de cuidado, conectado a ventilación mecánica a través de tubo endotraqueal modo IPPV, FiO2: 90%, Vt: 560, Fl:50, Tins: 0.9, Fr: 12; se conecta a monitor cardíaco que reporta: TA: 121/80mmHg TAM: 96mmhg FC: 113 lpm FR: 10 rpm  SPO2: 100%''',
			
			"piel" : 	'''	blanca, con marcada palidez cutaneomucosa, llenado capilar < 3 segundos.''',
			

			"cardiopulmonar":  '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, no ausculto agregados, ruidos cardíacos taquicárdicos y regulares, no ausculto  soplos.''',

			"abdomen": ''' plano, se evidencia herida quirúrgica en línea media xifopubica cubierta con apósitos húmedos y se evidencian dos dren funcionantes con gasto serohemático   dolorosa la palpación en toda su extensión, ruidos hidroaéreos presentes.''',

			"neurologico": ''' bajo efecto  de anestesia general por lo que no se puede evaluar, pupilas isocóricas, reactivas a la luz. ''',
			
			"extremidades": '''simétricas, sin edema''',

		}, 

		"diagnosticoIngresoHUAPA": [
									"POSTOPERATORIO INMEDIATO DE LAPAROTOMIA EXPLORADORA POR PERITONITIS PUNTO DE PARTIDA ABSCESO ESPLENICO.",
									"LEUCEMIA MIELOMONOCITICA CRONICA.",
									"TRASTORNO HEMATOLOGICO: ANEMIA SEVERA.",
									"TRASTORNOS ACIDO-BASICO: ACIDOSIS METABOLICA DESCOMPENSADA.",
									{"resumen":''' Paciente que no responde de manera satisfactoria, cursa con inestabilidad hemodinámica, que no mejora con el tratamiento, realizando parada cardiaca a las 11:00pm, se le realiza maniobras de RCP básicos, siendo no satisfactoria y de procede a realizar EKG evidenciando líneas isoeléctricas declarandose su fallecimiento a las 11:05pm de 25/01/15.'''},
		], 
		
	},#99

	{
		"IdHistoria": "29-14-26", 
		"nombre": "Zaida Meneses", 		
		"edad": "49",
		"sexo": "F",	
		"fechaNacimiento":  datetime(1964,5,8), 		
		"lugarNacimiento": "Cumana", 		
		"antecedentes": "hábito tabáquico de 2 cajas diarias",
		"dirección": "Miramar. Cumana Edo Sucre", 		
		"fechaIngresoHUAPA":  datetime(2014,4,1), 		
		"fechaIngresoUCI": datetime(2014,4,1), 		
		
		"resumenIngreso": '''Se trata de paciente femenina de 49 años de edad natural de CUMANA con antecedentes de hábito tabáquico de 2 cajas diarias hasta hace aproximadamente 1 mes , sin antecedentes patológicos importantes; quien inicia enfermedad actual el dia 25/03/14 cuando comienza con tos seca y fiebre, acude a ambulatorio donde indican tratamiento y egresan; la paciente continua con dificultad respiratoria, acude nuevamente a centro asistencial donde indican Rx de Torax. El dia 1/4/14 es traída a este centro por presentar dificultad respiratoria acentuada, es evaluada y hospitalizada   ''', 


		"examenFisicoIngresoUCI": {

			
			"piel" : 	'''	morena, normotérmica, deshidratada, llenado capilar <3segundos.''',
			

			"cardiopulmonar":  ''' Tórax simétrico, hipo expansible, ruidos respiratorios, MV disminuido en hemitorax derecho, se auscultan crepitantes en ACP. Ruidos  cardíacos rítmicos, taquicardicos regulares,  no se auscultan soplos. ''',
			"abdomen": ''' globuloso a expensa de panículo adiposo , blando, no doloroso a la palpación, no megalias ''',

			"neurologico": '''consciente, orientada, lenguaje claro y coherente. pupilas isocóricas reactivas a la luz ''',
		

		}, 

		"diagnosticoIngresoUCI": [

									"Shock séptico",
									"Sepsis punto de partida respiratorio",
									"Bronconeumonía bilateral",
									"SDRA",
									"Trastorno hidro electrolítico: hipokalemia",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' FC:79  lpm   FR 19 rpm  TA120/80 mmHg )mmHg  ''',
			"piel": ''' morena, normotérmica,  llenado capilar <3segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, ruidos respiratorios presentes en campo pulmonar derecho se auscultan roncos y sibilantes. ''',
			"abdomen": '''globuloso , blando, depresible, no doloroso a la plapación. Ruidos hidro aéreos presentes ''',
			
			"neurologico": '''consciente, orientada en 3 planos, lenguaje coherente. ''',
			

		},  

		"diagnosticoIngresoHUAPA": [
			"Derrame pleural izquierdo",
			"MT pulmonar a descartar",
			"TBC a descartar",
			{"resumen":''' La paciente permanece en piso 9 se replantean diagnosticos de infección respiratoria baja, TBC a descartar, Neumonia bilateral complicada con derrame pleural. El dia 3/04/14 se realiza TAC de torax que informa Bronconeumonia bilateral en probable relación a enfermedad granulomatosa. TBC. La paciente se mantiene recibiendo tratamiento anti TBC VO, evolucionando de forma tórpida, hasta el día de hoy que se solicita valoración por UCI y vemos paciente en cama de hospitalización, recibiendo oxigeno húmedo por mascarilla facial a 5 lts por minutos, no conectada a monitor cardiaco, con cianosis distal, dificultad respiratoria, tos húmeda productiva con secreción amarillenta, taquicárdica y taquipneica; consciente, orientada en 3 planos. Se toman gases arteriales, se presenta caso a Dra Roa quien decide ingresar a la UCI. Se recibe paciente en camilla de traslado, recibiendo oxigeno húmedo por mascailla facial a 5 lts por min; se pasa a cama UCI, se conecta a monitor cardiaco que reporta Fr. 31 Fc 135 TA 105/56 (70) SATO2 61%, se toman gases arteriales que reportan Ph 7.41 PCO2 53  PO2 49 HCO3 33.6 EB 7.5 SATO2 77%; por lo que se decide intubación endotraqueal y conexión a ventilación mecánica.'''},

							
		], 
		
	},# 100

	{
		
		
		"nombre": "Yurisma Isabel Ruiz Roque", 		
		
		"edad": "41",
		
		"dirección": "Calle Sarmiento, Avenida Perimetral",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1973,12,12),

		"lugarNacimiento": "Cumaná- Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,7,18),

		"fechaIngresoUCI": datetime(2015,7,22),

		"resumenIngreso": '''Paciente que luce en aparentes regulares condiciones generales, afebril, disneica. La paciente permanece en el Área de Emergencia con evolución tórpida, el día 16/07/2015 presenta disnea, cifras de saturación por monitor en descenso por lo que es Valorada por Intensivistas del Área quien decide realizar intubación endotraqueal y conexión a ventilación mecánica. Es Valorada por Servicio de Infectología quien en vista de hallazgos Tomográficos en Tórax plantean diagnósticos de Neumonía por Estafilococos y SDRA, se plantea también Infección por el Virus H1N1 e iniciar tratamiento con Tamiflu  y se plantea el diagnóstico de Hipoxia Cerebral en vista de hallazgos en Tomografía de Cráneo. Se replantean los diagnósticos a: Inestabilidad Hemodinámica, Sepsis punto de partida respiratorio, Infección Respiratoria Baja: Neumonía Bilateral Estafilococcica, SDRA, ECV Isquémico Extenso Fronto-Temporo-Parietal Derecho complicado con Edema Cerebral e Hipoxia Cerebral, Síndrome Convulsivo, Trastorno del Ritmo: FARVR, Postoperatorio Tardío de Cesárea Segmentaria  Trastorno HE: (Deshidratación Severa, Hipokalemia). La paciente permanece en el Área de Choque con evolución no satisfactoria, presentando Insuficiencia Renal Aguda requiriendo apoyo dialítico, siendo valorada en múltiples oportunidades por el Servicio de UCI, realizando sugerencias en vista de no contar con cupo. El día de hoy por disponibilidad del mismo se decide su ingreso. Se recibe paciente posterior a la Diálisis en malas condiciones generales, hemodinamicamente inestable recibiendo apoyo de Norepinefrina a razón de 10,6 mic/min, intubada, recibiendo oxígeno por Ambú.  Se traslada a cama de UCI y se conecta a monitor cardíaco externo que reporta: TA: 60/43mmHg FC: 151 FR: 12 SPO2: 99%.''', 


		"examenFisicoIngresoUCI": {

			"piel" : 	'''	morena, Normotérmica, normoelástica, con pálidez cutáneo-mucosa, llenado capilar > 3 segundos, con cianosis distal.''',
			

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible, ruidos respiratorios ausentes en ambas bases pulmonares, no se auscultan agregados, ruidos cardíacos rítmicos, taquicardicos, sin soplos ni galopes.''',
			"abdomen": '''globoso a expensas de panículo adiposo, ruidos hidroaéreos ausentes, se evidencia cicatriz infraumbilical limpia sin secreciones, sin megalias.''',

			"neurologico": ''' inconsciente, Glasgow: 3/15pts, Respuesta Motora: 1pt, Apertura Ocular: 1pt, Respuesta Verbal: 1pt, Reflejo Tusígeno ausente, Reflejo Córneal ausente, Pupilas midriáticas sin respuesta a la luz. ''',
			"extremidades": '''simétricas, eutróficas, sin edema.''',

		}, 

		"diagnosticoIngresoUCI": [
									"Shock Séptico ",
									"Sepsis punto de partida respiratorio",
									"Insuficiencia Renal Aguda en Hemodiálisis",
									"Evento Cerebrovascular Isquémico Extenso Fronto-Temporo-Parietal Derecho complicado con Edema Cerebral.",
									"Postoperatorio Tardío de Cesárea Segmentaria ",
									"Trastorno Hematológico: Anemia Moderada",
									"Trastorno Acido/Base: Acidosis Metabólica Compensada con Alcalosis Respiratoria más Hiperoxemia.",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": '''  Se trata de paciente femenina de 41 años de edad, natural y procedente de la localidad, con antecedente de Cesárea Segmentaria y Esterilización Quirúrgica, hace aproximadamente 49 días, sin antecedentes patológicos conocidos previos a la gestación y posterior a ella, cuyo familiar refiere inicio de enfermedad actual  el día 15/07/2015 cuando presenta desviación de la comisura labial, hemiplejía izquierda,  motivos por los cuales es trasladada a Ambulatorio de la localidad donde evidencian cifras tensionales elevadas (150/100mmHg), además de lo anteriormente mencionado, por lo que deciden referir a este centro hospitalario donde es evaluada por el Servicio de Medicina Interna quien decide su ingreso con los diagnósticos de: Hipertensión Arterial tipo Emergencia Expresada en EVC de etiología a precisar complicada con Edema agudo de pulmón. Primoconvulsión del Adulto.''',
			"piel": ''' Morena, Normotérmica, normoelástica, llenado capilar < 3 segundos.''',
			"cardiopulmonar": '''tórax simétrico, hipoexpansible, se auscultan crepitantes y bulosos abundantes, ápex visible y palpable, ruidos cardíacos rítmicos, regulares sin soplos. ''',
			"abdomen": '''globoso a expensas de panículo adiposo, ruidos hidroaéreos presentes, no doloroso a la palpaciín, sin megalias. ''',
			"extremidades": '''simétricas, sin edema.''',
			"neurologico": '''consciente, orientada en espacio y persona, desorientada en tiempo, hemiparesia e hiporreflexia, lenguaje disartrico. FM: 2/5.''',
		
		},  

		
	}, # 101

	{
		"IdHistoria": "51-56-42", 
		
		"nombre": "Yostin Nikenber Henriquez Monzalves", 		
		
		"edad": "13",
		
		"ci": "28.077.830", 
		
		"dirección": "Cumanacoa, 05 de julio las parcelas, Casa S/N cerca del hospital.",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(2000,3,25),

		"lugarNacimiento": "San Cristobal- Estado Táchira", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,1,10),

		"fechaIngresoUCI": datetime(2014,1,15),

		"resumenIngreso": '''Se trata de paciente masculino de 13 años de edad, natural de San Cristobal, Estado Táchira y procedente de Cumanacoa, sin antecedentes patológicos, quien refiere inicio de enfermedad actual el día 01-01-14, posterior a evento deportivo cuando presenta traumatismo y aumento de volumen en maléolo externo derecho, anexándose signos de flogosis la misma y posterior aumento de la temperatura corporal cuantificada en 39 ºC, motivo por el cual acude a centro ambulatorio de la localidad donde evalúan y egresan con tratamiento médico vía oral (Cefadroxilo) el cual cumple sin mejoría asociándose al cuadro aumento de volumen en 1/3 medio de pierna derecha y mano izquierda, motivo por el cual acude a este centro de salud  donde se ingresa el día 10-01-14 . ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente en camilla de transporte, tolerando aire ambiente, se conecta a monitor cardiaco y  pasa a cama de UCI, se reportan signos vitales: TA: 93/53 mmHg TAX: 69 mmH  FC: 65Lpm  FR: 44 Rpm  Sat O2: 97%, T: 37º C hemodinámicamente estable afebril.''',
			
			"piel" : 	'''blanca, normotérmica al tacto, llenado capilar < 3 segundos. ''',
			"cabeza": '''Forma y configuración normal no tumoraciones. ''',

			"cardiopulmonar":  '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos rítmicos, regulares,  sin soplos ni galope.  ''',
			"abdomen": ''' plano, blando, depresible, no doloroso palpación superficial y profunda  ruidos hidroaéreos presentes, no megálico. ''',

			"neurologico": ''' Consciente, orientado,  Glasgow 15/15 puntos, pupilas isocóricas normo reactivas. ''',
			"extremidades": '''se evidencia aumento de volumen y signos de flogosis en rodilla derecha, lesión ulcerada en tercio medio de pierna ipsilateral y brazo izquierdo. ''',

		}, 

		"diagnosticoIngresoUCI": [
							"Sepsis de Punto de partida de partes Blandas.",
							"Infección Micótica del tracto Urinario.",
							"Trastorno Hematológico: ",
							"Anemia Leve",
							"Trombocitosis. ",
							"Trastorno Hidroelectrolítico:", 
							"Hiperkalemia.",
							{"resumen": ''' El paciente permanece durante 5 días en la Unidad de Cuidado Intensivos, recibiendo antibióticoterapia con piperacilina-tazobactan, vancomicina y fluconazol. El día 17-01-14, se evidencia en tobillo derecho (maléolo externo) área de absceso fluctuante con color, rubor y dolor, por lo que en revista médica con Dr.Guaimares   se decide drenar previa colocación de campos estériles y asepsia, con salida de secreción hemopurulenta  abundante, no se logra tomar muestra para cultivo por no contar con medio para el mismo. Actualmente el paciente se encuentra en condiciones estables,  afebril con evolución satisfactoria clínica y paraclínica por lo que se decide egresar.'''},

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 120/80mmHg FC: 76lpm FR: 16rpm. Paciente eupneico, afebril. Impresión Diagnóstica: Sarcoma en miembro inferior derecho a descartar. Permaneciendo en el área de la emergencia durante 4 días, recibiendo tratamiento médico con evolución tórpida solicitan evaluación por UCI el día 13-01-14 y por no haber disponibilidad de cupo se mantiene en el área de choque. Se le realiza Eco abdominal el día de hoy que reporta hepatomegalia, esplenomegalia y quiste Renal Izquierdo.  El día 15-01-14 por  disponer de cupo en UCI se ingresa ''',
			"piel": ''' blanca, normotérmica al tacto, llenado capilar < 3 segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos rítmicos, regulares,  sin soplos ni galope. ''',
			"abdomen": '''plano, blando, depresible, no doloroso palpación superficial y profunda  ruidos hidroaéreos presentes, no megálico.''',
			"extremidades": '''se evidencia aumento de volumen y signos de flogosis en tobillo derecho y costra en rodilla izquierda sin signos de flogosis. ''',
			"neurologico": '''Consciente, orientado,  Glasgow 15/15 puntos, pupilas isocóricas normo reactivas.''',
			"cabeza": ''' Forma y configuración normal no tumoraciones.''',

		},  

		"diagnosticoEgreso": [
						"Sepsis de Punto de partida de partes Blandas.",
						"Infección Micótica del tracto Urinario.",
						"Trastorno Hematológico:",
						"Anemia Leve.",
						"Trombocitosis.",
		

		], 
		
	},#102

	{
		"IdHistoria": "", 
		
		"nombre": "Xiomaris Jose Rausseo Alfonzo", 		
		
		"edad": "16",
		
		"ci": "27.351.103 ", 
		
		"dirección": "La Manguita Cumanacoa.",
		
		"sexo": "",	
		
		"fechaNacimiento":  datetime(1998,2,22),

		"lugarNacimiento": "Cumanacoa", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,10,3),

		"fechaIngresoUCI": datetime(2014,10,4),

		"resumenIngreso": '''Se trata de paciente femenina de 16 años de edad sin antecedentes patológicos importantes quien inicia enfermedad actual el día 27/09/14 cuando comienza a presentar cefalea y fiebre de 38 y 39 ºC , y sangrado vaginal; al día siguiente se asocia al cuadro artralgia generalizadas y dolor abdominal por lo que acude a centro de salud más cercano e indican tratamiento con Diclofenac 1 tab cada 8 horas. El día 02/10/14 continúa con la sintomatología por lo que es llevada nuevamente a centro de salud  donde realizan paraclínicos evidenciando Trombocitopenia  (13 000) motivo por el cual es referida a este centro el día 03/10/14 donde es evaluada por servicio de medicina e ingresada. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, tolerando aire ambiente, no conectada a monitor cardiaco. Se traslada a cama UCI, se conecta a monitor cardiaco que reporta: TA: 114/84 (93)mmHg	 FC: 82 lpm FR: 12 rpm SPO2: 97%''',
			
			"piel" : 	'''	Palidez cutáneo mucosa ligera, normohídrica nomotérmica.''',
			

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes, sin agregados, ruidos cardíacos rítmicos, regulares, sin soplos.''',
			"abdomen": ''' Plano, depresible, doloroso a la palpación en Epigastrio e Hipocondrio Derecho, no visceromegalia. Ruidos Hidroaereos presentes ''',

			"neurologico": ''' Cosciente, orientada no signos de focalización neurológica.''',
			

		}, 

		"diagnosticoIngresoUCI": [
								"DENGUE HEMORRAGICO.",
								"EMBARAZO DE 5 SEM + 6 DIAS POR ECO",
								"TRASTORNO HEMATOLOGICO: ANEMIA MODERADA, TROMBOCITOPENIA",
								"TRASTORNO ACIDO BASE: ALCALOSIS RESPIRATORIA DESCOMPENSADA MAS ACIDOSIS METABÓLICA",
								{"resumen":''' Paciente que permanece en servicio de terapia intensiva por 48 horas  se realiza eco obstétrico donde se evidencia línea endometrial de 7 mm sin saco gestacional. Continúa con sangrado abundante en forma de coágulos, se recibe resultados de Serología para Dengue  IGG POSITIVA    IGM NEGATIVA por lo que se re discute diagnósticos planteándose: Síndrome febril agudo  etiología viral,  Aborto incompleto, Trastorno hematológico Anemia moderada. Desde su ingreso en UCI recibe tratamiento con Clindamicina, derivados sanguíneos: plasma fresco congelado, concentrado plaquetario y una unidad de concentrado globular recuperando satisfactoriamente, se interconsulta con hematología la cual reporta para el día de hoy en frotis de sangre GB 6300  SEG 50 %  LINF 47 % PLAQ  190 000 PT 1 SEG   PTT 5 SEG, además es valorada por servicio de epidemiologia quien  sugiere repetir Serología para dengue .Debido a evolución satisfactoria se decide egreso seguimiento y exploración por servicio de ginecología ya que se encuentra imagen hiperecoica con centro anecoico  en región de cuello uterino, por lo que en revista médica se sugiere considerar legrado uterino y en vista de derrame pleural se decide realizar rayos x tórax de pie y HCG cuantificada '''}

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 100/60 mmHg Fr: 16 rpm Fc: 71 lpm.''',
			"piel": ''' normohídrica, nomotérmica, biuen llene capilar''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes, sin agregados, ruidos cardíacos rítmicos, regulares, sin soplos. ''',
			"abdomen": '''Plano, blando, depresible, doloroso a la palpación en hipocondrio derecho, hepatomegalia de 2 cm por debajo del reborde costal.''',
			
			"neurologico": '''Consciente, orinetada, no signos de focalización neurológica.''',
		

		},  

		"diagnosticoEgreso": [
					"SINDROME FEBRIL AGUDO (RESUELTO)",
					"ABORTO INCOMPLETO EN EVOLUCION ",
					"TRASTORNO HEMATOLOGICO ANEMIA LEVE ,TROMBOCITOPENIA (RESUELTO)",
					"ASCITIS ,DERRAME PLEURAL DERECHO ",
					"TRASTORNO HIDROELECTROLITICO (HIPOKALEMIA )(RESUELTO) ",  
		

		], 
		"diagnosticoIngresoHUAPA": [
			"DENGUE CON SIGNOS DE ALARMA.",
			{"resumen":''' Se le realiza ecosonograma abdominal que reporta ascitis y derrame pleural derecho y sugiere realizar prueba de embarazo; la cual se realiza siendo positiva. En vista de este hallazgo es llevada a sala de parto donde realizan eco transvaginal que reporta embarazo de 5 sem + 6 días, huevo anembrionario. La paciente es evaluada por UCI quien hace sugerencias y en la mañana de hoy 04/10/14 se decide su ingreso por disponibilidad de cupo. '''}
		]
		
	},#103

	{
		
		"nombre": "William José Serrano", 		
		
		"edad": "47",
		
	
		"dirección": "Campeche, sector 3, calle 10, casa #6, Cumaná, Edo. Sucre",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1967,1,2),

		"lugarNacimiento": "Cumaná, Edo. Sucre.", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,8,31),

		"fechaIngresoUCI": datetime(2014,8,31),

		"examenFisicoIngresoUCI": {

			"resumen": ''' TA: 58/39(42) mmHg; FC: 116 lpm; FR: 21 rpm; SatO2: 100%. Paciente masculino de 47 años de edad, natural y procedente de la localidad, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual el día de hoy 31/08/14 en horas de la tarde, cuando posterior a accidente de tránsito tipo colisión (carro – moto) presenta traumatismos múltiples y pérdida del estado de consciencia sin recuperación espontánea de la misma, motivo por el cual es traído a éste centro asistencial donde se valora y es ingresado por el servicio de Cirugía Blanda. Al momento del ingreso presenta múltiples escoriaciones, tórax hipoexpansible, ruidos respiratorios disminuidos, ruidos cardíacos sin soplo, pulsos periféricos disminuidos, deterioro neurológico caracterizado por inconsciencia, pupilas anisocóricas ,Glasgow no descrito, se realiza intubación endotraqueal y lavado peritoneal el cual resulta positivo macroscópicamente, por lo que es llevado a mesa operatoria de emergencia, se le realiza laparotomía exploratoria con hallazgo de 2000cc de hemoperitoneo, lesión grado V de segmento hepático V al VIII y hematoma no expansivo ni pulsátil en zona II retroperitoneal derecha, tomando como conducta evacuación del hemoperitoneo, rafia de lesión hepática, lavado de cavidad y comprobación de hemostasia, se colocan 2 drenes dirigidos a lecho hepático y fondo de saco respectivamente, se realiza packing hepático con nueve (9) compresas y cierre de pared con Bolsa de Bogotá. En vista de estado general del paciente, solicitan valoración por UCI y por disponibilidad de cupo se  decide su ingreso. Se recibe paciente en camilla de traslado, intubado y recibiendo O2 por Ambú®, se pasa a cama UCI, se conecta a ventilación mecánica modo A/C, Vc: 480, FR: 12, FiO2: 90, Fl: 50, PEEP: 0 y se conecta a monitor cardíaco continuo que reporta: ''',
			
			"piel" : 	'''	morena, hipotérmica al tacto, con escoriaciones y laceraciones múltiples a nivel de cara, miembros superiores, miembros inferiores y tórax, con equimosis y edema bipalpebral derecho, llenado capilar < 3seg.''',
	

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, taquicárdicos, sin soplo ni galope.''',
			"abdomen": ''' globoso, con apósitos con moderada secreción serohemática sobre bolsa de Bogotá, ruidos hidroaéreos disminuidos, con 2 drenes con moderada secreción serohemática, blando, depresible.''',

			"neurologico": '''inconsciente, pupilas anisocóricas, derecha con tendencia a la midriasis, izquierda mióticas, hiporreactivas a la luz, reflejo tusígeno y corneal ausentes, Glasgow no evaluable por efectos de sedación farmacológica. Se transfunden 2 unidades de concentrado globular y 2000cc de solución 0,9%, persistiendo inestable hemodinámicamente, por lo que se indica Vasoactivos tipo Norepinefrina.''',
			"extremidades": '''deformidad y equimosis a nivel de hombro derecho, férula palmar derecha funcionante. ''',

		}, 

		"diagnosticoIngresoUCI": [


					"TRAUMATISMO CRANEOENCEFALICO SEVERO ",
					"TRAUMATISMO TORACOABDOMINAL CERRADO COMPLICADO CON:",
					"LESION GRADO V DE SEGMENTO V AL VIII HEPATICO",
					"HEMATOMA NO EXPANSIVO NI PULSATIL EN ZONA II RETROPERITONEAL DERECHO",
					"POST-OPERATORIO INMEDIATO DE LAPAROTOMIA EXPLORATORIA POR COLECCIÓN INTRAABDOMINAL (HEMOPERITONEO)",
					"SHOCK HIPOVOLEMICO ",
					"LESION DE IV Y V TENDON DE MANO DERECHA",
					"INSUFICIENCIA RENAL AGUDA PRE-RENAL",
					"TRASTORNO HIDROELECTROLITICO",
					"HIPOKALEMIA",
					"TRASTORNO HEMATOLOGICO:",
					"ANEMIA SEVERA",
					"TRASTORNO ACIDO-BASE:",
					"ACIDOSIS MIXTA DESCOMPENSADA MAS HIPEROXEMIA",

									
								],  

	},# 104

	{
		"IdHistoria": "52–86–66", 
		
		"nombre": "Adolfo Sanchez Mata ", 		
		
		"edad": "50",
		
		"ci": "8.636.066", 
		
		"dirección": "Fe y Alegría",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1964,11,10),

		"lugarNacimiento": "Cumaná - Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,12,30),

		"fechaIngresoUCI": datetime(2015,2,10),


		"resumenIngreso": '''Se trata de paciente blanco masculino de 50 años de edad, natural y procedente de la localidad, con antecedentes de hipertensión arterial controlada con losartan , quien inicia enfermedad actual el día 08/01/15 cuando posterior a herida por proyectil de arma de fuego con orificio de entrada en región  supraclavicular derecha con orificio de salida en 2do espacio intercostal anterior derecho línea media clavicular. Motivo por el cual se evalúa e ingresa por servicio de cirugía blanda ''', 


		"examenFisicoIngresoHUAPA": {

			"piel" : 	'''	Morena fría  al tacto, palidez cutáneo mucosa, llenado capilar <3 segundos.''',
			

			"cardiopulmonar":  '''Tórax simétrico, ruidos respiratorios presentes, disminuidos en hemitorax derecho; se evidencia herida por proyectil de arma de fuego con orificio de entrada en región supra clavicular derecha y salida en 2do espacio intercostal anterior derecho con línea medio clavicular, evidenciando en dicha región hematoma pulsátil no expansible. Ruidos cardiacos rítmicos, sin soplos''',
			"abdomen": ''' Globoso a expensa de panículo adiposo, no doloroso a la palpación, ruidos hidroaéreos presentes, no megalias''',

			"neurologico": '''Paciente consciente orientado en tres planos''',
			"extremidades": '''Parestesia en miembro superior derecho, pulsos cubital y radial disminuidos''',

		}, 

		"diagnosticoIngresoUCI": [
										"Post operatorio inmediato de pseudoaneurisma de arteria subclavia derecha",
										"Trastorno hematológico: Anemia Moderada",
										"Trastorno Metabólico: Hiperglicemia",
										"Trastorno acido – base: Acidosis Metabólica descompensada más hiperoxemia.",
										{"resumen":''' El paciente se le mide PVC que reporta 2 cmH2O, tensión arterial sistólica de de 85 mmHg por lo que se realizan retos de líquidos hasta optimizar PVC de 10 cmmH2O y tensión sistólica de 110 mmHg, se reciben paraclínicos que reportan PTT 17.7 por lo que se trasfunden 4 uds de plasma fresco congelado. '''}

									
								],  

		"examenFisicoIngresoUCI": {
			"resumen": ''' Paciente recibido  en camilla de transporte, intubado, conectado a ventilador de transporte y a monitor cardiaco externo, se traslada a cama UCI y es conectado a monitor cardíaco  que reporta  TA: 101/69 (79) mmHg FC:123 lpm FR: 14 rpm SatO2: 100%, y a ventilación mecánica AC Vc: 640 (8cc/Kg) FiO2: 50 Fr: 12 Fl: 50 PEEP: 0.''',
			"piel": ''' Normotérmica al tacto, llenado capilar <3 segundos.''',
			"cardiopulmonar": '''Tórax  simétrico, expandible, apósito estéril con escasa secreción hemática, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos normofonéticos, taquicárdicos,  sin soplos ni galope. ''',
			"abdomen": '''blando, depresible, no impresiona doloroso a la palpación, ruidos hidroaéreos presentes, no megalias. ''',
			"extremidades": '''En miembro inferior derecho se observa apósito estéril limpio sin secreciones.''',
			"neurologico": '''paciente bajo efectos de sedación y relajación farmacológica, pupilas isocóricas hiporreactivas a la luz. ''',
			

		},  

		"diagnosticoIngresoHUAPA": [
								
			"Traumatismo torácico no penetrante por herida por proyectil de arma de fuego",
			"Hernia inguinal derecha",
			"Hipertensión Arterial.",
			{"resumen": ''' El paciente permanece hospitalizado por servicio de cirugía siendo evaluado por Dr.Soto Cirujano cardiovascular quien indica paraclínicos. El día 07/01/15 se realiza angiotac la cual reporta pseudoaneurisma de arteria subclavia derecha. El paciente fue llevado en varias ocasiones a mesa operatoria para resolución quirúrgica de dicho pseudoaneurisma siendo suspendido por problemas técnicos en área de quirófano y falta de material quirúrgico; el día 10/02/15 el paciente presenta gasto hemático por orificio de proyectil de arma de fuego  a nivel de región clavicular derecha por lo que es evaluado por Dr Soto y solicita turno quirúrgico de emergencia. El paciente es llevado a mesa operatoria donde se realiza apertura de capsula pseudoaneurismática, control vascular proximal y distal, disección de vasos subclavios y plexo braquial, confección de autoingerto de vena safena interna invertida termino terminal. Durante acto quirúrgico el paciente hace hipotensión severa, siendo resuelta sin complicaciones. '''}

		], 
		
	},# 105

	{
		"IdHistoria": "07-83-82", 
		
		"nombre": "Víctor José Maza  Lunar ", 		
		
		"edad": "38",
		
		"ci": "12.662.446", 
		
		"dirección": "Barrio San Martin Caigüiré casa # 75 ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1972,2,26),

		"lugarNacimiento": "Cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,5,2),

		"fechaIngresoUCI": datetime(2014,5,5),

		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, recibiendo O2 por bolsa autoinsuflable conectada a bomona de oxigen, se traslada  a cama de UCI y se conecta a monitor cardíaco continuo que reporta: TA: 124/58(77) mmHg; FC: 98  lpm; FR: 35 rpm; SatO2: 100% ''',
			
			"piel" : 	'''	normo térmica al tacto se evidencian lesiones tipo quemadura de segundo grado de espesor parcial superficial en brazo y antebrazo izquierdo, región frontal y facial izquierda  y quemadura de tercer grado con exposición ósea y tendinosa en mano izquierda cubiertas por apósito estéril. ''',
			"cabeza": ''' se evidencia caída de cuero cabelludo ''',

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible ruidos respiratorios presentes, sin agregados. Ruidos cardíacos rítmicos, taquicardicos, sin soplo ni galope.''',
			"abdomen": ''' plano, blando, depresible no dolorosos a la palpación superficial y profunda no megalias RHA presentes. ''',

			"neurologico": ''' Paciente bajo efectos de sedantes y relajante muscular.''',
			"mucosas": '''Húmedas e hipo coloreadas.''',

		}, 

		"diagnosticoIngresoUCI": [
				"Quemadura eléctrica", 
				"Traumatismo craneoencefálico moderado ",
				"Trastorno hematológico : Trombocitopenia",
				{"resumen":''' Paciente el cual se mantiene en UCI por 48 horas intubado conectado a ventilación mecánica por 24 horas procediéndose a realizar destete ventilatorioprogresivo tolerando mascarilla facial con oxigeno húmedo a razón de 8 lt por minuto ,evolución clínica favorable desde el punto de vista hemodinamico y ventilatorio por lo que se decide traslado a sala de observación adulto para adecuado seguimiento por cirugía y traumatología ,se encuentra recibiendo ATB con ciprofloxacina ,profilaxis tromboembolica , e hidratación parenteral con liquidos totales a razón de 55 cc kg 24 horas .Fue evaluado por servicio de Neurocirugia poer el cual fue dado de alta al no encontrarse alteraciones clínicas ni imagenologicas  TA: 132/87(97) mmHg;     FC: 68  lpm;      FR: 21 rpm;      SatO2: 100% '''}

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se recibe paciente en malas condiciones con agitación psicomotora vía aérea permeable tolerando aire ambiente TA: 95/38(57) mmHg;FC: 108 lpm; FR: 24 rpm; SatO2: 100% Paciente que es evaluado por servicio de cirugía quien decide trasladar a quirófano donde se realiza bajo anestesia general cura quirúrgica, cateterizacion de vía venosa central ,inmovilización de mano izquierda con férula antebraquio palmar , es extubado y llevado a área de recuperación  el cual debido a agitación psicomotora  y necesidad de sedación y relajación muscular se decide re intubación endotraqueal y se conecta por servicio de terapia intensiva  a ventilación mecánica con ventilador MA1 con los siguientes parámetros VC 560 FIO2 60 FL 50 TI 1:4 PEEP 0 FR 12 debido a no contar con cupo en servicio de UCI de decide indicar sugerencias entre la que se destacan ATB ciprofloxacina ,hidratación parenteral ,sulfato de magnesio ,toxoide tetánico ,sedación y relajación continua , es valorado por servicio de Neurocirugía quienes sugieren la realización de TAC de cráneo urgente , el día de hoy por disponibilidad de cupo se decide traslado a UCI.''',
			"piel": ''' lesiones tipo quemadura de segundo grado de espesor parcial superficial en brazos y antebrazos cuello y cara y de tercer grado con exposición ósea y tendinosa en mano izquierda ''',
			"cardiopulmonar": '''tórax simétricos, hipoexpansibles ruidos respiratorios presentes, sin agregados. Ruidos cardíacos arrítmicos, taquicardicos, sin soplo ni galope. ''',
			"abdomen": '''plano, blando, depresible no dolorosos a la palpación superficial y profunda no megalias RHA presentes.''',
		
			"neurologico": '''Paciente agitado lenguaje incoherente ( no descrito ECG).''',
			"cabeza": ''' se evidencia caída de cuero cabelludo ''',

		},  

		"diagnosticoEgreso": [
							"Quemadura eléctrica ",
							"Traumatismo craneoencefálico moderado", 
							"Rabdomiolisis resuelta ",
							{"resumen": ''' Paciente masculino de 38 años de edad con  antecedentes patológicos conocidos de consumo de sustancias ilícitas que inicia enfermedad actual hace 48 horas cuando  es traído a servicio de emergencia  posteriormente a choque eléctrico  por encontrarse  manipulando cables de alta tensión  lo cual  produjo quemaduras de tercer grado en miembro superior izquierdo con exposición tendinosa y ósea en mano del mismo lado además de quemaduras de segundo grado en región frontal y pierna izquierda , concomitante a este cuadro se añade traumatismo craneoencefálico moderado debido a  caída de altura aproximadamente 6 metros por lo que es examinado y  hospitalizado con los diagnósticos :Quemadura eléctrica. Traumatismo craneoencefálico moderado '''}
									

		], 
		
	},# 106

	{
		"IdHistoria": "", 
		
		"nombre": "Tomas Aquiles Rondón Ávila", 		
		
		"edad": "77",
		
		"ci": "549803", 
		
		"dirección": "Calle bolívar numero 81 Mariguitar",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1938,12,21),

		"lugarNacimiento": "Cumana ", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,3,14),

		"fechaIngresoUCI": datetime(2015,3,14),

		"resumenIngreso": '''Paciente masculino de 77 años de edad procedente y natural de Mariguitar con antecedentes patológicos conocidos de Hipertensión arterial en tratamiento con Dropten 40 mg OD ,Carvedilol 6.25 mg OD , Diabetes Mellitus de reciente diagnostico sin tratamiento regular ,Insuficiencia renal crónica  en hemodiálisis y colocación de Marcapaso definitivo desde el año 2007 .Inicia enfermedad actual el día 10 de Marzo cuando presenta deterioro neurológico progresivo ,concomitantemente fiebre ,disnea a pequeños esfuerzos que se hizo más intensa hasta llegar  a la ortopnea  por lo que es  traído a este centro ingresando con diagnostico : EVC a descartar Paciente que se mantiene con deterioro progresivo sin aparente mejoría clínica  a  petición de la familia es trasladado el día 13/3/2015 a centro privado de la localidad donde se ingresa por servicio de Terapia intensiva con los diagnósticos: Meningoencefalitis bacteriana parcialmente tratada. EVC isquémico masivo AD. Sepsis punto de vista respiratoria y catéter de hemodiálisis. Insuficiencia renal crónica en hemodiálisis ''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente   recibiendo oxigeno por mascarila facial se traslada a cama de uci y se conecta a monitor cardiaco que reporta FR: 17 rpm, FC: 85 lpm, TA: 128/76 mmHg, SatO2: 99%''',
			
			"piel" : 	'''piel morena, se evidencia moderada palidez cutáneo mucosa, escara en región sacra normotermica al tacto hidratada. Llenado capilar < de 3 Seg''',
			

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, con crepitantes en ambos campos pulmonares  Ruidos cardiacos rítmicos y regulares, sin soplos ni galope.''',
			"abdomen": ''' Blando, depresible, no doloroso a la palpación superficial y profunda, no se palpan megalias.''',

			"neurologico": ''' Consciente, responde a estímulos dolorosos pupilas isocóricas con respuesta a la luz, Glasgow 9/15 pts. Dado por RM 5 pts. RO 3 pts. RV 1, no déficits sensitivo  ''',
			
			"extremidades": '''simétricas, sin alteraciones.''',

		}, 

		"diagnosticoIngresoUCI": [
						"INFECCION DEL SISTEMA NERVIOSO CENTRAL : MENINGOENCEFALITIS BACTERIANA PARCIALMENTE TRATADA ",
						"ABSCESO CEREBRAL AD",
						"INFECCION RESPIRATORIA BAJA ",
						"INSUFICIENCIA RENAL CRONICA  EN HEMODIALISIS",
						"HIPERTENSION ARTERIAL SISTEMICA ",
						"DIABETES MELLITUS TIPO 2 ",
						"TRASTORNO HEMATOLOGICO:ANEMIA SEVERA ",
						"TRASTORNO ACIDO BASE :ACIDOSIS METABOLICA +ALCALOSIS RESPIRATORIA DESCOMPENSADA ",

									
								],  

		"examenFisicoIngresoPrivado": {
			"resumen": ''' FR: 12 rpm, FC: 67 lpm, TA: 118/66 mmHg,  SatO2: 99%. Permanece en Unidad de cuidados intensivos 24 horas recibiendo oxigeno terapia y tratamiento antibiótico con Claforan, Unasyn ,Zyvox ,Metronidazol ,se realiza puncion lumbar demostrándose Infección del sistema nervioso central  siendo valorado por neurólogo Dr Ortiz ,se replantean diagnosticos : Meningoencefalitis bacteriana parcialmente tratada. Absceso cerebral AD. Sepsis punto partida respiratoria. Insuficiencia renal crónica en hemodiálisis. Debido a situación socioeconómica desfavorable se decide traslado a UCI HUAPA para la continuidad del tratamiento medico.''',
			"piel": ''' piel morena, se evidencia moderada palidez cutáneo mucosa, escara en región sacra normotermica al tacto deshidratada. Llenado capilar < de 3 Seg. ''',
			"cardiopulmonar": '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, con crepitantes en ambos campos pulmonares  Ruidos cardiacos rítmicos y regulares, sin soplos ni galope. ''',
			"abdomen": '''Blando, depresible, no doloroso a la palpación superficial y profunda, no se palpan megalias. ''',
			"extremidades": '''simétricas, sin alteraciones. ''',
			"neurologico": '''Consciente, responde a estímulos dolorosos pupilas isocóricas con respuesta a la luz  , Glasgow 9/15 pts. Dado por RM 5 pts. RO 3 pts. RV 1, no déficits sensitivo. ''',
			

		},  

		
	},# 107

	{
		"IdHistoria": "54-06-07 ", 
		
		"nombre": "Sulpicio Eriberto Torres", 		
		
		"edad": "64",
		
		"ci": "5.902.832", 
		
		"dirección": "Yaguaraparo vía Irapa",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1952,7,3),

		"lugarNacimiento": "", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,12,5),

		"fechaIngresoUCI": datetime(2015,12,8),

		"resumenIngreso": '''Se trata de paciente masculino de 64 años de edad natural y procedente de la localidad de Yaguaraparo, con antecedentes patológicos conocido de hipertensión arterial sistémica no controlado, inicia enfermedad actual el día 29/11/2015 Cuando presenta dolor en región lumbar derecha y glúteo derecho, que posteriormente se irradia a extremidad inferior derecha, motivo por el cual es trasladado a ambulatorio de la localidad donde administran analgésico vía IM, y se mantiene en observación, persistiendo sintomático, anexándose posteriormente aumento de volumen de dicha extremidad con calor, dolor y rubor, motivo por el cual deciden referir a hospital de Carúpano, donde es ingresado, con diagnóstico de sepsis punto de partida partes blandas, el día 04/12/2015 realizan punción de rodilla y muslo derecho para extracción de secreción para cultivo, el cual reporta, staphylococcus Aureus, permanece ingresado durante 4 días con evolución clínica tórpida,  evidenciando en paraclínicos retención de azoados , por lo que deciden referir a nuestro centro asistencial el día 05/12/2015, siendo evaluado por el servicio de Medicina Interna e ingresado con diagnóstico:''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Paciente es trasladado en camilla de transporte tolerando aire ambiente, se traslada a cama UCI, conectándose a monitor cardiaco externo que reporta signos vitales  TA: 107/70 (83) mmHg   FC: 154 lpm  FR: 25 rpm; SPO2: 92% ''',
			
			"piel" : 	'''	morena, Normotérmica  deshidratada, llenado capilar menor a 3 Seg, se evidencia leve palidez cutáneo mucosa.''',

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares con agregados roncus bilaterales, Ruidos cardiacos rítmicos taquicardicos no soplos.''',
			"abdomen": ''' plano, blando   depresible no dolorosos a la palpación sin visceromegalias''',

			"neurologico": '''consciente, orientado en tiempo espacio y persona, Glasgow 15/15 FM miembro inferior derecha 3/5 miembro inferior izquierdo 5/5 ROT II/IV.''',
			"extremidades": '''simétricas, se evidencia aumento de volumen en muslo derecho con signos de flogosis, se evidencia flictena en cara lateral de muslo ipsilateral. Limitación para la movilización. ''',

		}, 

		"diagnosticoIngresoUCI": [
									"Sepsis punto de partida piel y partes blandas ",
									"Stafilococcemia",
									"Insuficiencia renal aguda pre- renal no oligurica",
									"Hipertensión arterial sistémica no controlada",
									"Trastorno hematológico: trombocitopenia",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' FC: 170  lpm	FR: 26   rpm   TA: 90/60 mmhg T: 37 ºC. Paciente permanece en el área de emergencia durante 24 horas, posteriormente es trasladado a observación, donde se mantiene recibiendo antibioticoterapia a base de imipenem, vancomicina y trangorex,  posteriormente  se constata elevación de cifras de azoados (creatinina 5 mg/dl, urea 93 mg/dl) deciden solicitar valoración por el servicio de nefrología el cual se cumple el día 07/12/2015. El cual sugiere depuración de creatinina  proteína en 24 horas, en vista de persistir sintomático y7 anexarse al cuadro dificultad respiratoria a moderados esfuerzos, persistir leucocitosis con neutrofilia, deciden solicitar valoración por el servicio de terapia intensiva el día 8/12/2015, quien acude al llamado evaluando paciente en condiciones clínicas de cuidado, y en vista de disponibilidad de cupo se decide su ingreso a UCI.  ''',
			"piel": '''morena, Normotérmica normo hidratada, llenado capilar menor a 3 Seg ''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares con agregados crepitantes difusos, Ruidos cardiacos taquicardicos no soplos.''',
			"abdomen": '''blando plano  depresible no dolorosos a la palpación sin visceromegalias''',
			
			"neurologico": '''consciente, orientado en 3 planos.''',
		},  

		"diagnosticoIngresoHUAPA": [
								
			"Trastorno del ritmo fibrilación auricular con respuesta ventricular rápida.",
			"Piodermitis en muslo derecho.",
			"Hipertensión arterial sistémica.  ",

		], 
		
	},# 108

	{
		"IdHistoria": "51-53-53", 
		
		"nombre": "Carmen Beatriz de García", 		
		
		"edad": "52",
		
		"ci": "5.704.314", 
		
		"dirección": "Punta de Araya Sector el mercado casa numero 18 ",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1961,4,12),

		"lugarNacimiento": "Cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,2,18),

		"fechaIngresoUCI": datetime(2014,2,18),
		"ocupacion": "docente",
		"app":"no refiere",

		"antecedentes": ''' Alergias: Rinitis alérgica, Transfusiones: SI, Intervenciones quirúrgicas: Rinoplastia Cesarea ''', 

		"resumenIngreso": '''Se trata de paciente femenino de 52 años de edad, natural y procedente de la localidad, con antecedentes de HTA sistémica  sin tratamiento quien inicia enfermedad actual el dia 27/12/13 cuando presenta pérdida de consciencia por 8 minutos aproximadamente, anexándose al cuadro cefalea generalizada de fuerte intensidad por lo que es llevada a centro  médico donde es evaluada y referida a este centro, donde es examinada e ingresada con diagnostico de ECV en evolución. Se realiza TAC de cráneo que reporta ECV hemorrágico con hemorragia subaracniodea, ventriculomegalia y edema cerebral. Paciente que se mantiene hospitalizada se realiza estudio angiografico donde se identifica aneurisma  gigante de la arteria carótida interna y se solicita cupo para tratamiento quirúrgico ( clipaje del aneurisma),   el día de 14/01/14 es llevada a quirófano donde se realiza creaneotomia fronto parietal derecha llegando a espina  esfenoidal donde se observa sangrado profuso arterial de aproximadamente 1400 cc de contenido hemático asociada a  hipotensión arterial que responde a la administración de solución fisiológica  y sangre total ,se procede a dejar  packing de gelfoam y cierre por planos y traslado inmediato a sala de cuidados intensivos. Paciente que evoluciona  de forma estable, se procede a realizar protocolo de extubacion lográndose destetar de ventilación mecánica, se  realiza extubación y se mantiene por espacio de 24 horas recibiendo oxigeno húmedo por mascarilla facial a razón  de 5 lt por minuto ,recibiendo ATB con ceftazidima y Vancomicina así como nimodipino en el contexto de vasoespasmo  cerebral se mantiene en regulares condiciones por lo que se decide su egreso de UCI y traslado a Neurocirugia,  donde se mantiene hospitalizada hasta el día de hoy que es nuevamente llevada a quirófano para craneotomía parietal  dercha para clipaje de aneurisma de arteria carótida interna y colocación de válvula ventrículo peritoneal. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, en regulares condiciones generales, hemodinámicamente estable, intubada  conectada a ventilador de traslado, se conecta a monitor cardíaco externo que reporta los siguientes signos vitales: TA: 133 76  (87 ) mmHg FC: 104 lpm FR:12 rpm SPO2: 99% ''',
			
			"piel" : 	'''	Blanca, normotérmica al tacto, llenado capilar < 3 segundos. ''',
			"cabeza": ''' herida quirúrgica en región frontotemporoparietal derecha cubierta por apósito esteril''',

			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos arrítmicos, regulares, hipofonéticos,  sin soplos ni galope. ''',
			"abdomen": ''' plano, blando, depresible, ruidos hidroaéreos presentes, no megálico.''',

			"neurologico": ''' Bajo efectos de anestesia general inhalatoria por lo que no es evaluable el estado de consciencia, pupilas isocoricas mioticas normoreactivas a la luz ''',
		}, 

		"diagnosticoIngresoUCI": [
									"POM DE CRANEOTOMIA PARIETAL DERECHA PARA CLIPAJE DE ANEURISMA DE CAROTIDA INTERNA DERECHA Y COLOCACION DE VALVULA VENTRICULO PERITONEAL ",
									"ENFERMEDAD CEREBROVASCULAR HEMORRAGICA :HEMORRAGIA SUBARACNOIDEA CON VENTRICULOMEGALIA ",
									"HTA SISTEMICA",
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 124 72 mmHgFC: 78 lpmFR: 12 rpm SPO2: 99 %''',
			"piel": ''' Blanca, normotérmica al tacto, llenado capilar < 3 segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos rítmicos, regulares, hipofonéticos,  sin soplos ni galope.  ''',
			"abdomen": '''plano, blando, depresible, ruidos hidroaéreos presentes, no megálico.''',
		
			"neurologico": '''consciente orientada en tres planos Glasgow 15 /15 ''',
			"cabeza": ''' herida quirúrgica en región frontotemporoparietal derecha cubierta por apósito esteril''',

		},  

		"diagnosticoIngresoHUAPA": [
								"POI DE CRANEOTOMIA PARIETAL DERECHA PARA CLIPAJE DE ANEURISMA DE CAROTIDA INTERNA DERECHA Y COLOCACION DE VALVULA VENTRICULO PERITONEAL ",
									"ENFERMEDAD CEREBROVASCULAR HEMORRAGICA :HEMORRAGIA SUBARACNOIDEA CON VENTRICULOMEGALIA ",
									"HTA SISTEMICA",
									"HIPOKALEMIA",
									"ACIDOSIS METABOLICA DESCOMPENSADA MAS ALCALOSIS RESPIRATORIA CON HIPEROXEMIA ", 

		], 
		
	},# 109

	{
		
		"nombre": "Carmen de Lourdes Millán Jiménez ", 		
		
		"edad": "72",
		
		"ci": "4.683.101", 
		
		"dirección": "Urbanización La Trinidad calle H-5 casa numero 48",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1942,2,11),

		"lugarNacimiento": "Cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,10,7),

		"fechaIngresoUCI": datetime(2014,10,7),

		"antecedentes": '''Diabetes Mellitus. HTA sistémica .Trastorno del rimo Fibrilación auricular. EVC isquémico ''', 

		"resumenIngreso": '''Paciente femenina de 72  años de edad, natural y procedente de la localidad con antecedentes de Hipertensión arterial sistémica con tratamiento  Benicar, Trastorno del ritmo  Fibrilación auricular con tratamiento Amiodarona 200 MG OD, Diabetes Mellitus tipo 2 con tratamiento Metformina 500 mg,EVC isquémico hace 6 años dejando como secuela parecía de miembros inferiores y afasia en tratamiento con aspirina 81mg y clopidogrel 75 mg  ,  trombosis en miembro inferior derecho hace 2 años que amerito amputación infracondilea. Inicia enfermedad actual hace 2 días cuando posterior a ingesta de alimentos presenta deterioro súbito de estado de consciencia, vómitos,  movimiento tónico generalizado y relajación de esfínteres por lo que es trasladada a clínica de la localidad donde  se evidencian cifras de tensión arterial elevadas (no reportan signos vitales) , desde el punto de vista neurológico Glasgow 3/15 puntos . Se evalúa por medicina crítica  quien decide intubación endotraqueal y se conecta a ventilación mecánica con parámetros no descritos al ingreso. ''', 


		"diagnosticoIngresoUCI": [
			"Emergencia hipertensiva expresada en EVC hemorrágico",
			"Hematoma intraparenquimatoso temporo parieto occipital derecho", 
			"Hemorragia Subaracnoidea FISHER IV", 
			"Trastorno del ritmo Fibrilación auricular con respuesta ventricular rápida ", 
			"Diabetes Mellitus tipo 2 descompensada en hiperglucemia", 
			"HTA arterial sistémica", 
			"Trastorno acido básico : acidosis metabólica compensada", 
			"Trastorno Hidroelectrolítico: hipokalemia",
			{"resumen":''' La paciente ha permanecido hospitalizada en UCI, en post operatorio mediato de craniotomía para drenaje de hematoma intraparenquimatoso y colocación de sistema derivativo ventricular tipo Becker, el cual se le retiró a los 10 días; la paciente actualmente se encuentra estable, inconsciente con Glasgow 6/15 puntos, alimentación por sonda nasogástrica, con  Traqueostomía realizada el día 16/10/14 sin complicaciones,  recibiendo tratamiento médico. En revista médica se decide traslado a sala de hospitalización.   Informe que se expide a solicitud de la parte interesada el día 20/10/14 en Cumaná. Estado Sucre.'''}

									
								],  


		"diagnosticoIngresoPrivado": [
								"Crisis hipertensiva tipo Emergencia hipertensiva expresada en EVC hemorrágico",
								"Hematoma intraparenquimatoso temporo parieto occipital derecho ",
								"Hemorragia Subaracnoidea FISHER IV", 
								"Trastorno del ritmo Fibrilación auricular con respuesta ventricular adecuada ",
								"Diabetes Mellitus tipo 2 descompensada en hiperglucemia ",
								{"resumen":'''Diagnósticos de ingreso a centro privado: Paciente que es evaluada por Neurocirugía quien decide previa coordinación traslado a servicio público Hospital Universitario para resolución quirúrgica. Se recibe paciente en camilla de traslado recibiendo oxigeno húmedo mediante mascarilla  y bolsa autoinsuflable a razón 3 lt por minuto, no conectada a monitor cardiaco, se traslada a cama de UCI se conecta a ventilación mecánica con parámetros Modo AC VC 480 FR 12 FIO2 50 FL 50 PEEP 0 y a monitor cardiaco  que reporta FC 121 LPM  FR 16 RPM   TA 145/98 MMHG SATO2 100 % TAC CRANEO (06-10-14) Área hiperdensa en regiones temporo parieto occipital derecha con desplazamiento de línea media y drenaje a ventrículos. '''}


		], 
		
	},# 110

	{
		"IdHistoria": "51–27–71", 
		
		"nombre": "César José Brito Villarroel", 		
		
		"edad": "60",
		
		"ci": "5.897.155", 
		
		"dirección": "Cerezal, vía Cariaco, calle principal, casa S/N",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1953,2,25),

		"lugarNacimiento": "Güiria, Edo. Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2013,10,16),

		"fechaIngresoUCI": datetime(2014,2,11),


		"resumenIngreso": '''Paciente masculino de 60 años de edad, natural y procedente de la Güiria, con antecedente de Hipertensión arterial sistémica mal controlada y EVC secuelar de larga data, quien inicia enfermedad actual el mes de Octubre del año 2013 aproximadamente cuando presenta movimientos tónico-clónicos en miembro superior e inferior derechos, motivo por el cual es llevado a Hospital de Carúpano donde permanece hospitalizado por aproximadamente 15 días y posteriormente referido a este centro asistencial con el diagnóstico de LOE en fosa posterior para valoración por el servicio de Neurocirugía. Es ingresado el día 16/10/13 por el servicio de Medicina Interna con los diagnósticos de LOE en fosa posterior parasagital bilateral con características de meningioma, Estatus convulsivo, Epilepsia, HTA no controlada y EVC secuelar. Al momento del ingreso se encontraba orientado en tiempo, espacio y persona, con disminución de la sensibilidad en hemicuerpo derecho. Permanece desde entonces ingresado en el piso de hospitalización de medicina interna, donde es valorado por el servicio de Neurocirugía quien plantea resolución quirúrgica. El día 11/02/14 es llevado a mesa operatoria, bajo anestesia general inhalatoria, se le realiza incisión bicoronal y craniotomía bifrontal, durotomía, ligadura y sección del seno longitudinal superior en 1/3 anterior con medio y exceresis total de meningioma bilobulado que ameritó sección parcial del Falx en el 1/3 anterior, sección y ligadura de pedículo de duramadre en piso de fosa craneal anterior, control de hemostasia, resección de pericráneo para injerto autólogo de defecto dural, cierre a prueba de fuga, colocación de flap óseo, sutura de piel por planos, antisepsia y cura final. Sangrado estimado de 1000cc. Por disponibilidad de cupo y autorización de adjuntos del servicio se traslada a UCI.''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''TA: 155/91(113) mmHg; FC: 89 lpm;  FR: 32 rpm; SatO2: 99%	''',
			
			"piel" : 	'''	hipotérmica al tacto, llenado capilar < 3seg.''',
		

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, taquipneico, sin agregados. Ruidos cardíacos rítmicos y regulares, sin soplo ni galope.''',
			
			"abdomen": '''plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico''',

			"neurologico": '''inconsciente, pupilas isocóricas, mióticas, hiporreactivas a la luz, Glasgow no evaluable por efectos de sedación farmacológica''',
			"extremidades": ''' miembro inferior derecho en posición de flexión, con rigidez en articulación de la rodilla.''',

		}, 

		"diagnosticoIngresoUCI": [
									"POST-OPERATORIO INMEDIATO DE CRANIOTOMIA BIFRONTAL CON ABORDAJE INTERHEMISFERICO PARA EXCERESIS DE MENINGIOMA DEL FALX 1/3 ANTERIOR",
									"HTA SISTEMICA",
									"EVC SECUELAR",
									"TRASTORNO ACIDO – BASE: ",
									"ACIDOSIS METABOLICA DESCOMPENSADA CON ALCALOSIS RESPIRATORIA MAS HIPEROXEMIA",

								],  

		
	},# 111

	{
	
		"nombre": "Cai Fang Chen", 		
		
		"edad": "43",
		
		"ci": "82.134.728", 
		
		"dirección": "Av. Humboldt, Residencias Loli, Cumana, Edo. Sucre",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1971,4,17),

		"lugarNacimiento": "China.", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,5,10),

		"fechaIngresoUCI": datetime(2014,5,10),



		"resumenIngreso": ''' Paciente femenina de 43 años de edad, natural de China y procedente de la localidad, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual el día de hoy 10/05/14 en horas de la mañana, cuando posterior ingesta alimentaria y disgusto familiar presenta vómitos, diaforesis, palidez cutánea y pérdida del estado de consciencia con relajación de esfínter vesical, por lo que es trasladada a centro privado donde es evaluada por internista e intensivista y deciden su ingreso en UCI. Al momento del ingreso presenta TA: 183/96(122) mmHg, FC: 133X’, FR: 13X’, SatO2: 95%, con deterioro neurológico caracterizado por inconsciencia y Glasgow de 3/15pts por lo que se realiza intubación endotraqueal y se conecta a ventilación mecánica. En vista de estado general de la paciente, solicitan cupo en la UCI de este centro asistencial y previa autorización de Dr. Carlos Guaimare  se autoriza dicho ingreso.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubada y recibiendo O2 por Ambú®, se pasa a cama UCI, se conecta a ventilación mecánica modo A/C, Vc: 480, FR: 12, FiO2: 60, Fl: 50, PEEP: 0 y se conecta a monitor cardíaco continuo que reporta: TA: 194/123(150) mmHg; FC: 117 lpm;  FR: 13 rpm; SatO2: 100% ''',
			
			"piel" : 	'''	blanca, normotérmica al tacto, llenado capilar < 3seg.''',
		

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, con roncus escasos bilaterales. Ruidos cardíacos rítmicos y regulares, taquicárdicos, sin soplo ni galope.''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico''',

			"neurologico": ''' inconsciente, pupilas isocóricas, con franca tendencia a la midriasis, arreactivas a la luz, reflejo tusígeno y corneal presentes, Glasgow 4/15pts (RM: 2pts, RO: 1pto, RV: 1pto limitado por TET).Se realiza TAC cerebral simple donde se evidencia Hemorragia Intracraneal Cerebelosa, con extensión intraventricular (Hemorragia Subaracnoidea Fisher IV). En vista de cifras elevadas de TA se indica Nitropusiato de Sodio VEV por BIC a razón de 0,27µgr/Kg/min.''',
			

		}, 

		"diagnosticoIngresoUCI": [
									"CRISIS HIPERTENSIVA TIPO EMERGENCIA EXPRESADA EN EVC DE ETIOLOGIA HEMORRAGICA:", 
									"HEMORRAGIA INTRACRANEAL CEREBELOSA CON EXTENSION INTRAVENTRICULAR",
									"HEMORRAGIA SUBARACNOIDEA FISHER IV",
									"TRASTORNO ACIDO-BASE:",
									"ACIDOSIS METABOLICA COMPENSADA CON NORMOXEMIA",

								],  
		
	},#112

	{
		"IdHistoria": "52-94-13", 
		
		"nombre": "Emelsa  Margarita Restrepo Ramos", 		
		
		"edad": "68",
		
		"ci": " 3.045.001", 
		
		"dirección": "AV GRAN MARISCAL RECIDENCIAS ICABARO FRENTE A INTERCABLE ",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1946,10,7),

		"lugarNacimiento": "", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,3,1),

		"fechaIngresoUCI": datetime(2015,3,1),

		"resumenIngreso": '''Paciente femenina de 68 años de edad, natural y procedente de la localidad, con  antecedentes patológicos de hipertensión arterial en tratamiento con coaprobel 40 mg y concor 2.5 mg, operada de hernia discal  en año 2006 para lo cual recibe tratamiento infiltrativo por anestesiólogo en consulta de clínica del dolor, dislipidemia tratada con atorvastatina, quien inicia enfermedad actual el día martes 25/02/2015 cuando posterior a sesión infiltrativa para vertebral con lidocaína al 1%, Dexametasona , presenta bradipsiquia, bradilalia, somnolencia que evoluciona al estupor vómitos en 3 oportunidades  motivo por el cual es trasladada a centro privado siendo evaluada por medico tratante Anestesiólogo (DR salgado ) quien decide su ingreso y solicita valoración por servicio de medicina interna, el cual acude al llamado DR Vladimir Mago evaluando paciente disneica, acrocianosis  por lo cual solicita para clínicos(Dímero D) reportando positivo solicitando por dicho hallazgo valoración por servicio de Terapia intensiva acudiendo al llamado Dra. Roa quien en vista de condiciones clínicas del paciente decide su ingreso a UCI con diagnósticos: Encefalitis, Edema cerebral, Tromboembolismo pulmonar Infección respiratoria baja atípica, Deshidratación severa Insuficiencia renal aguda pre-Rena, Inmunosupresión. Para el día 27/02/2015 paciente cursa con trabajo respiratorio y deterioro del estado neurológico (no precisado) por  lo cual se decide  intubación endotraqueal y conexión a ventilación mecánica. Permanece durante 72 horas en UCI recibiendo tratamiento a base de Avelox y ceftazidima, en vista de condiciones socioeconómicas se decide su traslado a UCI Huapa. ''', 


		"examenFisicoIngresoHUAPA": {

			"resumen": ''' FR: 25 rpm, FC: 94 lpm, TA: 156/87 (129) mmHg,SatO2: 99% ''',
			
			"piel" : 	'''	piel blanca, normotermica al tacto normohidratada. ''',
			

			"cardiopulmonar":  ''' tórax simétrico, expansible, ruidos respiratorios presentes en ambos campos pulmonares, con agregados roncos bilaterales a predominio izquierdo . Ruidos cardiacos rítmicos y regulares, sin soplos ni galope. ''',
			"abdomen": ''' globoso, a expensa de panículo adiposo,  ruidos hidroaéreos presentes, depresible, no doloroso a la palpación superficial y profunda, no se palpan megalias. ''',

			"neurologico": ''' consciente, orientada, pupilas isocóricas normorreactivas a la luz, Glasgow 15/15 pts, no signos meníngeos.''',
			"extremidades": '''simétricas, sin alteraciones.''',

		}, 

		"diagnosticoIngresoUCI": [
									"Infección del sistema nervioso central AD",
									"Insuficiencia ventilatoria aguda",
									"Tromboembolismo pulmonar ",
									"Infección respiratoria baja ",  
									"Edema cerebral",
									"Deshidratación severa (R)",
									"Insuficiencia renal aguda pre-renal",
									"Inmunosupresión",
									"Trastorno Hidroelectrolítico:",
									"Hipernatremia",
									"Hipocalcemia",
									"Hipomagnesemia",
									"Hipertensión arterial sistémica",
									"Dislipidemia",
									"obesidad",
									{"resumen":''' Durante su estancia en el servicio la paciente presentó descompensación ventilatoria ameritando PEEP de 8 el cual en vista de mejoría de la paciente se fue disminuyendo hasta llegar a 0; se realiza punción lumbar la cual reporta antes de centrifugar aspecto turbio, leuc: 0-1 xC hematíes:20-15 xC contaje cel: 2 cel x mm; después de centrifugar aspecto trasparente gluc: 80 mg/dl pandy: + proteínas: 105 mg/dl. Por lo que se decide colocar antibióticoterapia con Ceftazidima; Vancomicina; Unasyn; Metronidazol. La paciente evoluciona de forma satsfactoria, con descenso de la cuanta blanca,  afebril. El día de ayer se realiza extubación de forma satisfactoria siendo bien tolerada, con gases control que reportan Ph: 7.44 PCO2: 43 PO2: 107 HCO3: 29.2 EB: 4.6 SATO2: 98%. Por lo que en la mañana de hoy se decide su egreso y a petición de familiar se traslada a centro privado.   '''}

								],  
		"diagnosticoEgreso":[


			"Insuficiencia ventilatoria aguda",
			"Tromboembolismo pulmonar", 
			"IRB Aguda ",
			"Encefalitis ",
			"Edema cerebral",
			"Deshidratación severa (R)",
			"Insuficiencia renal aguda pre-renal",
			"Inmunosupresión",
			"Trastorno Hidroelectrolítico:",
			"Hipernatremia",
			"Hipocalcemia",
			"Hipomagnesemia",
			"Hipertensión arterial sistémica",
			"Dislipidemia",
			"obesidad",

		],

		"examenFisicoIngresoUCI": {
			"resumen": '''Se recibe paciente  intubada  recibiendo oxigeno por ambú se traslada a cama de uci y se conecta a ventilación mecánica con parámetros SIMV Vc: 640 Fr: 12 FiO2: 60 Fl: 50 TI: 1:4 PEEP:0 y a monitor cardiaco que reporta FR: 27 rpm,  FC: 89 lpm,  TA: 158/104 (115) mmHg, SatO2: 85% ''',
			"piel": ''' piel blanca, se evidencia moderada palidez cutáneo mucosa, normotermica al tacto normohidratada. Llenado capilar < de 3 Seg. ''',
			"cardiopulmonar": '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, con agregados roncos bilaterales a predominio basal. Ruidos cardiacos rítmicos y regulares, sin soplos ni galope. ''',
			"abdomen": '''globoso, a expensa de panículo adiposo,  ruidos hidroaéreos presentes, depresible, no doloroso a la palpación superficial y profunda, no se palpan megalias. ''',
			"extremidades": '''simétricas, sin alteraciones. ''',
			"neurologico": '''somnolienta, pupilas isocóricas normorreactivas a la luz, ROT II/V, Glasgow 9/15 pts. Dado por RM 5 pts. RO 3 pts. RV 1 pt limitado por tubo endotraqueal sin signos meníngeos. ''',
			
		},  
		
	},# 113

	{
		"IdHistoria": "54-17-17", 
		
		"nombre": "Luis Nicolás Córdova Guzmán ", 		
		
		"edad": "74",
		
		"ci": "2.858.406", 
		
		"dirección": "Cumaná",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1940,3,29),

		"lugarNacimiento": "CUMANA", 		
			 		
		"fechaIngresoHUAPA":  datetime(2016,1,12),

		"fechaIngresoUCI": datetime(2016,1,12),


		"resumenIngreso": '''Se trata de paciente masculino de 74 años de edad con antecedentes de tratamiento con Foradil y Berodual sin especificar causa, antecedente de cumplimiento incompleto de tratamiento anti TBC,  exposición laboral a químicos para limpieza quien inicia enfermedad actual el día 10/01/2016 cuando presenta disnea a moderados esfuerzos que progresa a pequeños esfuerzos, edema en miembros inferiores, motivos por los cuales acude a ambulatorio de la localidad donde evalúan y deciden referir a este centro hospitalario para valoración y conducta. Es valorado por el Servicio de Medicina Interna quien decide su ingreso con el diagnóstico de: Neumonitis Tóxica complicada con derrame pleural bilateral.  ''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de transporte, ventilando espontáneamente, se traslada a cama UCI, conectándose a monitor cardiaco externo que reporta signos vitales: TA: 123/81mmHgFC: 76lpm FR: 18 rpm SPO2: 90% ''',
			
			"piel" : 	'''	Morena, turgor disminuido, con áreas hipopigmentadas, con cianosis distal, llenado capilar < 3 segundos.''',
			

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, abolidos en ambas bases pulmonares, se auscultan abundantes sibilantes y roncus en tercio superior y medio de ambos hemitórax.  Ruidos cardiacos hipofonéticos.''',
			"abdomen": '''blando, depresible,  no doloroso a la palpación, sin visceromegalias ''',

			"neurologico": ''' Consciente, Glasgow 15/15 puntos dados por RM: 6pts, RV: 5pts, AO: 4pts.Pupilas isocóricas reactivas, sin déficit neurológico. ''',
			"extremidades": '''simétricas, con edema grado 1 en ambos miembros inferiores, que no deja fóvea.''',

		}, 

		"diagnosticoIngresoUCI": [

								"Derrame Pericárdico Severo.",
								"Derrame Pleural Bilateral",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": '''    TA: 110/70mmHg FC: 84 lpm FR: 26 rpm Paciente luce en aparentes regulares condiciones generales, afebril, disneico.   El paciente permanece en el Área de Observación Adultos donde se anexan los diagnósticos: ICC Descompensada complicada con Derrame Pleural Bilateral y EBPOC sobreinfectado y se inicia tratamiento con Piperacilina-Tazobactan, se anexa furosemida al tratamiento y se solicita valoración por el Servicio de Cardiología. El día 12/01/2016 se realiza TAC de Tórax donde se reporta: Derrame Pleural Bilateral probablemente cardiogenico Vs de otra etiología. Derrame Pericárdico. Cardiomegalia. Arterioesclerosis. Espondilosis. El día 21/01/2016 se realiza Ecocardiograma donde se reporta Derrame Pericárdico Severo con abundantes miofibrillas además de colapso de la aurícula derecha. Se sugiere valoración por Cirugía Cardiovascular para ventana pericárdica. En vista de lo anteriormente mencionado solicitan valoración por Servicio de Cirugía Vascular quienes deciden preparar preoperatorios para realizar ventana pericárdica, solicitan valoración por el Servicio de Terapia Intensiva para manejo postoperatorio y en vista de contar con el cupo se decide su ingreso ''',
			"piel": ''' Blanca Normotérmica normo hidratada turgor acorde a la edad, llenado capilar menor a 3 segundos.''',
			"cardiopulmonar": '''tórax simétrico, hipoexpansible, ruidos respiratorios abolidos en ambos bases pulmonares, se auscultan crepitantes finos bilaterales. RsCsRsRs sin soplos.''',
			"abdomen": '''ligeramente globoso, depresible, RsHs presentes ''',
			"extremidades": '''se evidencia edema grado III, duro, no deja fóvea.''',
			"neurologico": '''consciente, orientado en tiempo.  ''',

		},  
		
	},# 114

	{
		"IdHistoria": "", 
		
		"nombre": "Jennifer De Jesús Gómez Bello ", 		
		
		"edad": "36",
		
		"ci": "14.661.139", 
		
		"dirección": "Turpialito Carretera Cumaná-Mariguitar.",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1979,7,31),

		"lugarNacimiento": "Cumaná", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,10,4),

		"fechaIngresoUCI": datetime(2015,10,4),


		"resumenIngreso": ''' Se trata de paciente femenina de 36 años de edad conocida con el Diagnóstico de Anemia Hemolítica y Esplenectomía desde hace 20 años aproximadamente, en tratamiento irregular por Servicio de Hematología. Además de antecedente de Rectocolitis Ulcerativa. Familiar refiere inicio de enfermedad actual desde el día 02/10/2015 cuando presenta evacuaciones líquidas en abundante cantidad, en múltiples oportunidades, concomitantemente debilidad generalizada, motivos por los cuales acude a centro privado donde se evidencia deshidratación severa e hipotensión arterial por lo que solicitan valoración por Especialista quien en vista de condiciones clínicas decide ingresar en la Unidad de Cuidados Intensivos, con los diagnósticos de Rectocolitis Ulcerativa y Amibiasis. Permanece durante 48 horas recibiendo tratamiento con Metronidazol y en vista de evolución satisfactoria se decide trasladar a Área de Hospitalización. El día de hoy 04/10/2015 la paciente presenta vómitos en múltiples oportunidades, disnea que progresa a la ortopnea, cianosis peribucal, distal, tos con expectoración muco-purulenta, es valorada por Especialista quien decide referir a este centro y por disponibilidad de cupo se decide su ingreso. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en malas condiciones generales, ventilando espontáneamente, recibiendo oxígeno por mascarilla facial, se traslada a cama de UCI, se conecta a monitor cardíaco externo que reporta: TA: 108/83  mmHg   FC: 153 lpm	FR: 30 rpm    	SPO2: 73 %. En vista de condiciones clínicas de la paciente, se evidencia saturación por monitor de 62%, se procede a realizar intubación endotraqueal, colocándose tubo número 7 french y se conecta a ventilación mecánica. Se procede posteriormente previa asepsia y antisepsia, en región lateral derecha de cuello, colocación de Vía Central número 6 french, monolumen en Vena Yugular Interna Derecha, se realiza prueba de xifonaje la cual resulta positiva y se verifica correcta colocación de la misma en Radiografía de Tórax.''',
			
			"piel" : 	'''	Morena, normotérmica, deshidratada, llenado capilar menor a 3 Seg, con marcada palidez cutáneo-mucosa, con cianosis peribucal y distal acentuada. ''',
			

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares con agregados tipo crepitantes bilaterales a predominio de hemitorax derecho, Ruidos cardiacos rítmicos taquicardicos sin soplos ni galopes.''',
			"abdomen": ''' globoso, blando depresible no doloroso a la palpación sin visceromegalias, se evidencia cicatrices de heridas quirúrgicas limpias sin secreciones.''',

			"neurologico": '''Somnolienta, Glasgow: 10/15pts, Respuesta Motora: 6pts, Respuesta Verbal: 1pt, Apertura Ocular: 3pts. Fuerza Muscular 5/5, ROT II/IV. Pupilas isocóricas reactivas a la luz. ''',
			"extremidades": '''simétricas, eutróficas, sin edema ni deformidades.''',

		}, 

		"diagnosticoIngresoUCI": [
										"Síndrome de Distress Respiratorio del Adulto",
										"Amibiasis Intestinal",
										"Rectocolitis Ulcerativa",
										"Anemia Hemolítica",
										"Trastorno Acido-Base: Hipoxemia.",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se evalúa paciente en malas condiciones generales, afebril, disneica. ''',
			"piel": ''' morena, Normotérmica, normo hidratada, llenado capilar menor a 3 Seg''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares y abolidos en base pulmonar derecha con crepitantes bibasales, Ruidos cardiacos rítmicos taquicardicos sin soplos.''',
			"abdomen": '''globoso, ruidos hidroaéreos presentes, no doloroso a la palpación superficial y profunda. ''',
			"extremidades": '''eutróficas, sin edema.''',
			"neurologico": '''consciente, desorientada, en tiempo espacio y persona. ''',
			

		},  

		"diagnosticoIngresoHUAPA": [
						"Infección Respiratoria Baja: Neumonía Bilateral",
						"Rectocolitis Ulcerativa",
						"Amibiasis ", 
								

		], 
		
	},# 115

	{
		
		"nombre": "Yackson Josué Rodríguez Lanza", 		
		
		"edad": "27",
		
		"ci": "19.082.326", 
		
		"dirección": "El Paraíso, Zona Industrial, Sector San Luis.",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1988,12,11),

		"lugarNacimiento": "Cumaná", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,12,28),

		"fechaIngresoUCI": datetime(2015,12,28),

		"resumenIngreso": '''Se trata de paciente masculino conocido con antecedentes de Diabetes Mellitus tipo 1 en tratamiento con Insulina NPH y Lantus no especificado, quien inicia enfermedad actual el día de hoy cuando presenta vómitos en múltiples oportunidades, evacuaciones líquidas, tos productiva, aumento de la temperatura corporal no cuantificada, motivos por los cuales es trasladado a este centro donde es valorado e ingresado con los diagnósticos de:1) Cetoacidosis Diabética.2) Diabetes Mellitus Tipo 1 Descompensada.3) Acidosis Metabólica Clínica. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' TA: 140/70mmHg FC: 126lpm FR:32rpm. En vista de condiciones clínicas del paciente es valorado por Especialista (Dra. Patiño) quien realiza Vía Central en región latero-cervical derecha. Solicita cupo en Servicio de Terapia Intensiva y en vista de disponibilidad del mismo se decide su ingreso.''',
			
			"piel" : 	'''	morena, normotérmica, deshidratada. ''',
			"abdomen": ''' Simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardiacos rítmicos sin soplo ni galope.''',

			"neurologico": ''' Estuporoso ''',
		}, 

		"diagnosticoIngresoUCI": [	"Diabetes Mellitus Tipo 1 Descompensada en Cetoacidosis Diabética",
									"Infección Respiratoria Baja: Neumonía Bilateral Adquirida en la Comunidad.",
									"Insuficiencia Renal Aguda Prerrenal",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se recibe paciente en camilla de traslado en malas condiciones generales, ventilando espontáneamente, sin aporte de oxígeno, se traslada a cama de UCI, se conecta a monitor cardíaco externo que reporta: TA: 117/79mmHg	FC: 115lpm	FR: 38rpm	SPO2:100% En vista de Vía Central no funcional se decide retirar y realizar Vía Venosa Central Yugular Derecha, se coloca Catéter Monolumen número 6 french, sin complicaciones.''',
			"piel": ''' Blanca, normotérmica, turgor disminuido, se evidencian mucosas oral seca.''',
			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes, se auscultan crepitantes bibasales, ruidos cardíacos rítmicos, regulares, taquicardicos, sin soplos ni galopes.''',
			"abdomen": '''Plano, blando, depresible, no doloroso a la palpación, ruidos hidroaéreos ausentes. ''',
			"extremidades": '''Simétricas, eutróficas, sin edema.''',
			"neurologico": '''Somnoliento, Glasgow: 14/15pts, Respuesta Motora: 6pts, Respuesta Verbal: 5pts, Apertura Ocular: 3pts. Pupilas isocóricas, reactivas a la luz.''',

		},  
	},# 116


	{
		"IdHistoria": "13-54-72", 
		
		"nombre": "Carmen del valle Rivas Ortiz", 		
		
		"edad": "53",
		
		"ci": "5.702.593", 
		
		"dirección": "URB la voluntad de Dios",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1962,6,12),

		"lugarNacimiento": "", 		
			 		
		"fechaIngresoHUAPA":  datetime(2005,5,12),

		"fechaIngresoUCI": datetime(2005,5,12),

		"resumenIngreso": '''Paciente femenina de 53 años de edad, natural y procedente de la localidad, con  antecedentes patológicos de hipertensión arterial en tratamiento con losartan (), diabetes mellitus tipo II en tratamiento con glibenclamida (5 mg) OD, quien refiere inicio de enfermedad actual en noviembre de 2014 cuando presenta tinte ictérico en piel y mucosa, el día 24/12/2015 presenta cuadro de vómitos post pandriales motivo por el cual  es traslada a nuestro centro asistencial y es ingresada por el servicio de cirugía donde permanece 15 días  por IDX de colecistitis aguda, es egresada por mejoría clínica y se planifica la realización de (CEPRE) de manera electiva. Permanece con tinte ictérico durante 2 meses y se realiza CEPRE en el mes de febrero del presente año, reportando como resultado TU de papila. Indicando estudios por imágenes y para clínicos para resolución quirúrgica definitiva.es ingresada el día 12/05/2015 con los diagnósticos de TU de papila.''', 


		"examenFisicoIngresoUCI": {

			
			"piel" : ''' piel blanca, se evidencia moderada  palidez cutáneo mucosa, normotermica al tacto deshidratada. Llenado capilar < de 3 Seg ''',
	

			"cardiopulmonar":  ''' tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares y disminuidos en ambas bases pulmonares, con agregados roncos en 1/3 medio de hemitorax izquierdo. Ruidos cardiacos rítmicos y regulares taquicardicos, sin soplos ni galope. ''',
			"abdomen": ''' globoso, a expensa de panículo adiposo,  ruidos hidroaéreos presentes, poco  depresible,  doloroso a la palpación  profunda, no se palpan megalias se evidencia 2 drenes conectada a hemovac con presencia de abundante secreción biliar. Y dren conectado a bolsa recolectora. Con escasa secreción  ''',

			"neurologico": ''' consciente, pupilas isocóricas normorreactivas a la luz, ROT II/V, Glasgow 14/15 pts. Dado por RM 6 pts. RO 4 pts. RV 4 pt  sin signos meníngeos. ''',
			"extremidades": '''simétricas sin con edema grado II.''',

		}, 

		"diagnosticoIngresoUCI": [

								"Post operatorio tardío  de relaparotomia por colección intraabdominal por fuga de anastomosis gastroenterica.",
								"Post operatorio tardío de whipple por adenocarcinoma de papila de váter.",
								"Adenocarcinoma de ampolla de váter",
								"Diabetes mellitus tipo II descompensada en hiperglicemia",
								"Hipertensión arterial sistémica",
								"Trastorno hematológico: ",
								"anemia severa",
								"trombocitopenia", 
								"Trastorno hidroelectrolítico: ",
								"hipokalemia ",
								"hipernatremia",
								"Trastorno acido base: ",
								"acidosis metabólica compensada ",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' FR:  FC: TA: / () mmHg, SatO2: % Paciente es llevada a mesa operatoria donde bajo anestesia general, laparotomía supra umbilical con hallazgos de dilatación de colédoco 2 cm aproximadamente, no evidenciando ni se palpa tumoración ni adenopatías, y se procede a extracción de prótesis en colédoco, duaodenopancreatoectomia  y confección de pancreatoyeyunoanastomosis A 20 cm de asa fija yeyunoanastomosis a 10 cm de la pancreatoyeyunoanastomosis y gastroenteroanastomosis. Se deja 2 drenes dirigidos a coledocoyeyunoanastomosis y pancreatoyeyunoanastomosis, se realiza comprobación de hemostasia cierre de pared por planos y asepsia final. Paciente con evolución clínica tórpida, presentado gasto por sonda nasogástrica de secreción biliar abundante por lo que el día 23/06/2015 es llevada a mesa operatoria donde bajo anestesia inhalatoria se realiza, relaparotomia xifopubica con hallazgos de colección biliar intraabdominal   de aproximadamente 500 cc, deshicencia de 30% aproximadamente en cara anterior de gastroenteroanastomosis, adherencia inter asas, se realiza evacuación de colección biliar, colocación de sonda de levin a nivel de anastomosis gastroenterica, dirigiéndose a 60 cm aproximadamente distal a la misma con posterior rafia con seda 2-0, rafia de gastroenteroanastomosis , extracción de dicha sonda en contraabertura, lavado de cavidad con 8 litros de sol 0,9% comprobación de hemostasis, se dejan drenes rigidos conectados a hemovac extraido por contraabertura dirigido a región subhepatica, se realiza cierre de cavidad y se traslada al área de recuperación de quirófano donde permanece durante 10 días, y en vista de disponibilidad de cupo en el servicio de Terapia Intensiva se decide su ingreso en la Unidad. ''',
			"piel": ''' piel blanca, Normotérmica, normo hidratada ''',
			"cardiopulmonar": '''estable ''',
			"abdomen": '''globoso, a expensa de panículo adiposo,  ruidos hidroaéreos presentes, depresible, no doloroso a la palpación superficial y profunda, se evidencia cicatriz post Qx en hipogastrio.''',
			
			"neurologico": '''conservado''',
		

		},  
		
	},# 117

	{
		"IdHistoria": "51–87–29 ", 
		
		"nombre": "Daniel José Vásquez Fajardo", 		
		
		"edad": "36",
		
		"ci": "13.052.049 ", 
		
		"dirección": "Bolivariano, casa #24, Cumana, Edo. Sucre",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1977,11,30),

		"lugarNacimiento": "Cumaná, Edo. Sucre.", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,5,20),

		"fechaIngresoUCI": datetime(2014,5,22),


		"resumenIngreso": ''' Paciente masculino de 36 años de edad, natural y procedente de la localidad, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual hace 2 meses aproximadamente, cuando presenta dolor de moderada intensidad en región retroesternal, acompañado de disnea de moderados a pequeños esfuerzos, tos seca y fiebre cuantificada en 39°C, motivo por el cual acude a centro de salud de su localidad donde realizan Rx AP de tórax y evidencian imágenes multinodulares parahiliar derecha, por lo que refieren a este centro asistencial a la consulta de cirugía de tórax donde evalúan y planifican para resolución quirúrgica. El día de hoy 22/05/14 es llevado a mesa operatoria, bajo anestesia general, realizándosele toracotomía Posterolateral derecha, con hallazgo de Tu. de 4x3cm de diámetro aproximadamente en hilio pulmonar derecho con múltiples adenopatías, además de múltiples lesiones de 0,5x0,5cm de diámetro blanquecinas en parénquima pulmonar, tomando como conducta toma de muestra para biopsia en cuña de ganglio hiliar derecho y de lesiones blanquecinas, comprobación de hemostasia, lavado de cavidad pleural, dejando tubo de tórax funcionante conectado a trampa de agua, síntesis por planos y asepsia final. En vista de estado general del paciente, solicitan cupo en la UCI para manejo postquirúrgico y previa autorización de Dra. Cortesía  se autoriza dicho ingreso. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubado y conectado a ventilador mecánico de traslado, se pasa a cama UCI, se conecta a ventilación mecánica modo A/C, Vc: 560, FR: 12, FiO2: 60, Fl: 50, PEEP: 0 y se conecta a monitor cardíaco continuo que reporta: TA: 194/123(150) mmHg;     FC: 117 lpm;      FR: 13 rpm;      SatO2: 100%''',
			
			"piel" : 	'''	normotérmica al tacto, llenado capilar < 3seg.''',
			

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, con tubo de tórax funcionante, conectado a trampa de agua, con escaso gasto serohemático. Ruidos cardíacos rítmicos y regulares, sin soplo ni galope.''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico.''',

			"neurologico": '''no evaluable por efectos de sedación y relajación farmacológica.''',
			
		}, 

		"diagnosticoIngresoUCI": [
									"POSTOPERATORIO INMEDIATO DE TORACOTOMIA POSTEROLATERAL DERECHA PARA TOMA DE BIOPSIA DE GANGLIO HILIAR PULMONAR", 
									"TRASTORNO HIDROELECTROLITICO",
									"HIPOKALEMIA",
									"TRASTORNO ACIDO-BASE:",
									"ACIDOSIS METABOLICA DESCOMPENSADA + HIPEROXEMIA",

									
								],  
	},# 118

	{
		
		"nombre": "Aladi Josefina Rivero Rodríguez ", 		
		
		"edad": "66",
		
		"ci": "3.874.062", 
		
		"dirección": "ARAYA - AVENIDA LOS CASCABEL ",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1949,2,27),

		"lugarNacimiento": "Cumaná ", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,6,17),

		"fechaIngresoUCI": datetime(2015,6,17),

		"resumenIngreso": '''Paciente femenina de 66 años de edad, con antecedentes patológicos de Hepatitis C con Hipertensión Portal diagnosticada hace 14 años en tratamiento con Moderan, Befol, Hemorragia Digestiva en 2 oportunidades (2001-2012), antecedentes de Hipertensión Arterial en tratamiento con Inderal (30 mg OD) quien inicia enfermedad actual el día 16/06/2015 cuando presenta hematemesis en 3 oportunidades abundantes además evacuaciones melenicas abundantes en 2 oportunidades motivo por el cual acude a centro privado donde es evaluada e ingresada en servicio de Terapia Intensiva con diagnósticos de. ''', 

		
		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se recibe paciente en camilla de traslado, respirando aire ambiente, se pasa a cama UCI, se conecta a monitor cardíaco continuo que reporta: TA: 148/91(103) mmHg, FC: 103 lpm, FR: 25rpm, SatO2: 98% ''',
			"piel": ''' Morena, Normotérmica, turgor conservado, con leve palidez cutáneo-mucosa, llenado capilar < 3 segundos, se evidencia con ligero tinte ictérico.''',
			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, se auscultan crepitantes en base pulmonar derecha. Ruidos cardíacos rítmicos, regulares, taquicárdicos, sin soplos ni galope.''',
			"abdomen": '''globoso, ruidos hidroaéreos presentes, blando, no doloroso a la palpación, se evidencia cicatriz de herida quirúrgica limpia sin secreciones.''',

			"neurologico": '''Consciente, orientada en 3 planos, lenguaje coherente, memoria conservada, FM 5/5, ROT II/IV.''',
		

		},  

		"diagnosticoIngresoPrivado": [

			"Hemorragia digestiva superior", 
			"Varices esofágicas sangrantes", 
			"Cirrosis hepática con hipertensión portal",
			"Hepatitis viral c",
			"Anemia moderada",
			"Hipertensión arterial sistémica",
			{"resumen": ''' Paciente presenta posterior a su ingreso nuevos episodios de hematemesis abundantes (2), y evacuaciones melenicas en 3 oportunidades, permaneciendo estable hemodinamicamente, recibe 2 unidades de concentrado globular además de 2 unidades de plasma fresco congelado, en vista de condiciones socioeconómicas se decide su traslado a nuestro centro asistencial donde en vista de contar con cupo en la Unidad de Cuidados Intensivos se decide su ingreso. '''},

		],

		"diagnosticoIngresoHUAPA": [
							"Hemorragia digestiva superior ",
							"Varices esofágicas sangrantes ",
							"Cirrosis hepática con Hipertensión Portal",
							"Hepatitis Viral C",
							"Hipertensión Arterial Sistémica",
							"Trastorno Hematológico: Anemia Moderada, Trombocitopenia, PTT prolongado",
							"Trastorno Acido/Base: Acidosis Metabólica Descompensada con Alcalosis Respiratoria.",
		

		], 
		
	}, #119

	{
		"IdHistoria": "49-79-36", 
		
		"nombre": "Angel Ignacio Jugador Castillo ", 		
		
		"edad": "45",
		
		"ci": "10.946.411", 
		
		"dirección": "cumana",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1969,8,2),

		"lugarNacimiento": "cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,9,6),

		"fechaIngresoUCI": datetime(2014,9,6),

		"resumenIngreso": '''Se trata de paciente masculino de 45 años de edad natural y procedente de la localidad con antecedentes patológicos conocidos de Herida por arma de fuego hace aproximadamente 17 meses para lo cual amerito laparotomía exploradora, inicia enfermedad actual el día de hoy 06-09-14 cuando es traído a este centro  luego de ser encontrado en la via publica con deterioro del nivel de consciencia y traumatismos múltiples posterior a accidente de tránsito tipo volcamiento en moto c por lo que es hospitalizado con los diagnósticos : ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en cama de traslado, en aparentes regulares condiciones generales, hemodinámicamente estable, ventilando con mascarilla autoinsuflable con oxigeno húmedo a 5 lt por minuto , se traslada a cama de uci y se conecta a monitor cardíaco externo que reporta: TA: 127/79mmHg		FC: 93lpm		FR: 17rpm		SPO2: 95% Al examen físico se constata que el TET se encuentra en vías digestivas por lo que se realiza intubación endotraqueal sin complicaciones con Tubo 7.5 FR ,se conecta a ventilación mecánica modo AC VC 560 FL 50 FIO2 50 FR 12 PEEP 0 ''',
			
			"piel" : 	'''Morena, normotérmica, turgor conservado, llenado capilar < 3 segundos. Escoriaciones múltiples región facial y hombro derecho edema palpebral derecho ''',

			"cardiopulmonar":  '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes, sin agregados, ruidos cardíacos rítmicos, regulares, sin soplos.''',
			"abdomen": ''' Globoso, blando, depresible, no doloroso a la palpación, ruidos hidroaéreos presentes, no megalias.Cicatriz quirúrgica antigua supra para e infraumbilical ''',

			"neurologico": ''' Inconsciente,  Glasgow 4 /15 puntos dados por RM 2 RV 1 RO 1 PUPILAS ANISOCORICAS REACTIVAS MIDRIASIS DERECHA Reflejo corneal presente ''',
	
		}, 

		"diagnosticoIngresoUCI": [
									"POLITRAUMATIZADO",
									"TRAUMATISMO CRANEOENCEFALICO SEVERO CERRADO ",
									"TRAUMATISMO TORACOABDOMINAL CERRADO ",
									"TRAUMATISMO FACIAL DERECHO",
									"TTNO METABOLICO HIPERGLICEMIA  ",
									{"resumen":''' Se realizan ordenes medicas en conjunto con Dra Cortesia especialista de guardia '''}

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 110/70mmHg FC: 112lpm FR: 14rpm Se solicita valoración por UCI por parte de residente de neurocirugía y por disponibilidad de cupo se decide su ingreso ''',
			"piel": ''' Morena, normotérmica, turgor conservado, llenado capilar < 3 segundos''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes, sin agregados, ruidos cardíacos rítmicos, regulares, sin soplos.''',
			"abdomen": '''Globoso, blando, depresible, no doloroso a la palpación, ruidos hidroaéreos presentes, no megalias.. Cicatriz quirúrgica supra para e infraumbilical antigua''',
		
			"neurologico": '''Inconsciente,  Glasgow 4 /15 puntos dados por RM 2 RV 1 RO 1pupilas anisocóricas midriasis derecha reactivas a la luz ''',
		

		},  

		"diagnosticoIngresoHUAPA": [
			"POLITRAUMATIZADO ",
			"TCE SEVERO CERRADO ",
			"TRAUMATISMO TORACOABDOMINAL CERRADO ",
			"TRAUMATISMO FACIAL DERECHO ",
		], 
		
	},# 120

	{
		"IdHistoria": "54-00-06", 
		
		"nombre": "Rubén Rafael yeguez Goitia", 		
		
		"edad": "72",
		
		"ci": "2.659.728", 
		
		"dirección": "el peñón 3 era calle casa sin número. ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1943,3,20),

		"lugarNacimiento": "", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,11,16),

		"fechaIngresoUCI": datetime(2015,11,22),

		"resumenIngreso": '''Se trata de paciente masculino de 72 años de edad, natural y procedente de la localidad, con antecedentes de hipertensión arterial no controlada, diabetes mellitus tipo II en tratamiento con glucofage 500 mg OD, quien inicia enfermedad actual el día 15/11/2015 cuando presenta dolor precordial que se irradia a cuello y miembros superiores izquierdo que se intensifica el día 16/11/2015 por lo que acude a ambulatorio de la localidad donde realizan electrocardiograma evidenciando cambios en el mismo, motivo por el cual es referido a nuestro centro asistencial donde es evaluado por el servicio de medicina interna quien decide su ingreso. ''', 

		"diagnosticoIngresoUCI": [
									"Síndrome coronario agudo infarto  al miocardio con elevación del segmento ST en cara anteroseptal",
									"Ángor post IM ",
									"taquicardia supra ventricular.",
									"Hipertensión arterial no controlada",
									"Diabetes mellitus tipo II descompensada en hipoglicia",
									{"resumen":''' Se realiza ecocardiograma por Dra. María Ledesma evidenciándose fracción  de eyección del 45'%' e hipocinesia de tabique interventricular se sugiere realizar CATETERISMO CARDIACO   por  tal razón se emite dicho informe a los 26 días del mes de  noviembre 2015 '''}
									
								],  

		"diagnosticoIngresoHUAPA": [
								
			"Síndrome coronario agudo infarto al miocardio sin elevación del segmento ST",
			"Isquemia sub endocardica en cara antero lateral ",
			"Hipertensión arterial sistémica no controlada.",
			"Diabetes mellitus tipo II",
			{"resumen":''' Paciente es evaluado por el servicio de cardiología Dra. María Ledesma el día 17/11/2015 quien replantea diagnostico a infarto agudo al miocardio con elevación del  segmento st no trombolizado, sugiriendo tratamiento a base de nitroglicerina en vista de paciente presentar dolor precordial, indica tratamiento a base de concor 2.5 mg OD, ecocardiograma y hollter cardiaco. Se anexa en horas de la noche dificultad respiratoria a pequeños esfuerzos con cifras de tensión arterial 200/100 mmHg por lo que administran dosis de lasix 40 mg stat. Con leve mejoría clínica, se plantea diagnóstico de edema agudo de pulmón  El día 18/11/2015 es reevaluado por el servicio de cardiología Dr. Khan quien realiza reajuste de tratamiento, permaneciendo en el área de choque durante 6 días con evolución clínica tórpida, el día 22/11/2015 se anexa al cuadro hipotensión arterial severa requiriendo soporte con vasoactivos levophed, se solicita valoración por el servicio de terapia intensiva evaluando paciente en condiciones clínicas de cuidado, por disponibilidad de cupo se decide su ingreso en la unidad de cuidados intensivos.'''}

		], 
		
	}, # 121

	{
		"IdHistoria": "51-56-80", 
		
		"nombre": "Eleazar José Rodriguez", 		
		
		"edad": "24",
		
		"ci": "19.538.707", 
		
		"dirección": "La Angoleta. Araya, frente a la capilla",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1989,5,9),

		"lugarNacimiento": "Cumaná-Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,1,11),

		"fechaIngresoUCI": datetime(2014,1,11),

		"antecedentes": '''APP: nada a señalar. Operaciones: nada a señalar. Transfusiones: no. Alergias: no. Hábitos tóxicos: fumador de tabaco ''', 

		"resumenIngreso": '''Se trata de paciente masculino 24 años de edad, natural de cumana y procedente de La angoleta, sin antecedentes de enfermedad de importancia, el cual inicia enfermedad actual el día 10 de enero de 2014, cuando posterior a caída de altura presenta traumatismo craneoencefálico severo, traumatismo cervical y traumatismo toraco-abdominal cerrado, con pérdida de la consciencia y convulsiones tónico clónicas generalizadas, motivo por el cual es llevado a centro privado donde es evaluado,se realiza TAC de cráneo que reporta fractura hundimiento parietal derecha, fractura lineal temporal derecha, edema cerebral, hematoma subdural agudo; por tener recursos es llevado al hospital de la localidad donde evalúan y por constar con neurocirugía se refieren a este centro. El paciente es evaluado por servicio de neurocirugía quien decide resolución quirúrgica.''', 


		"examenFisicoIngresoHUAPA": {

			
			"piel" : 	'''	blanca afebril, multiples escoriaciones.''',

			"cardiopulmonar":  '''tórax simétrico expandible, ruidos respiratorios presentes, sin agregados; ruidos cardiacos rítmicos, normofoneticos, sin soplos ni galope.''',
			"abdomen": ''' plano, impresiona doloroso a la palpación''',

			"neurologico": ''' Glasgow 8/15 ptos (RM 6 RO 1 RV 1), pupilas isocóricas hiporeactivas a la luz. ''',
		

		}, 

		"diagnosticoIngresoUCI": [
						"POI de craneotomía por drenaje de hematoma epidural temporal derecho",
						"TCE severo",
						"Infección respiratoria baja: neumonía derecha por bronco aspiración ",

									
								],  

		"examenFisicoIngresoUCI": {
			"resumen": ''' Se recibe paciente en camilla de traslado, intubado, se pasa a cama UCI y se conecta a monitor cardiaco que reporta Fr 17 rpm Fc 96 lpm TA 119/83 SATO2 99%; y se conecta a ventilación mecánica AC Vc 560 Fr 12 FiO2 60 Fl 50 PEEP 0; paciente bajo efectos de sedación, ''',
			"piel": ''' afebril al tacto, normohidrica; ''',
			"cardiopulmonar": '''ruidos cardiacos rítmicos normofoneticos, sin soplos ni galope, ruidos respiratorios presentes, MV disminuido en hemitorax derecho, sin agregados; ''',
			"abdomen": '''plano depresible, no megalias; ''',
			"neurologico": '''inconsciente, bajo efectos de sedación, Glasgow no evaluable, pupilas mioticas. ''',
			

		},  

		"diagnosticoIngresoHUAPA": [
								
			"TCE severo",
			"Traumatismo toraco abdominal cerrado.",
			{"resumen":''' El paciente es evaluado por UCI, se presenta caso a Dr Alpino quien autoriza  ingreso posterior a acto quirúrgico. Es llevado a mesa operatoria donde se realiza craneotomía evidenciando hematoma epidural, se drena hematoma, lavado con sol 0.9%, cierre por planos.'''}

		], 
		
	}, #122

	{
		"IdHistoria": "53-09-32", 
		
		"nombre": "Edgar Rafael Arismendi Rodríguez", 		
		
		"edad": "66",
		
		"ci": "4.689.958 ", 
		
		"dirección": "calle principal boca de sabana casa sin número",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1949,2,1),

		"lugarNacimiento": "Cumaná-Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,3,1),

		"fechaIngresoUCI": datetime(2015,3,2),

		"resumenIngreso": '''Se trata de paciente masculino de 66 años de edad natural y procedente de la localidad, con antecedentes de hipertensión arterial sistémica en tratamiento con enalapril 10 mg cada 12 horas, Diabetes Mellitus tipo II en tratamiento con euglucon (glibenclamida) 5 mg. Inicia enfermedad actual el día 01/03/2015 cuando es hallado por familiares inconsciente con desviación de la comisura labial hacia la izquierda, motivo por el cual es traslado a nuestro centro asistencial donde es evaluado por servicio de medicina interna y es ingresado. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, intubado, recibiendo oxigeno húmedo por ambú, se traslada a cama UCI, se conecta a monitor cardiaco continuo que reporta:  Fc 93 lpm  Fr: 18 rpm TA: 163/108 (125) mmHg SATO2: 95%. ''',
			
			"piel" : 	'''	normo hídrica, afebril al tacto, llenado capilar < 3 Seg.''',
			

			"cardiopulmonar":  '''Tórax simétrico, normoexpansible; ruidos respiratorios presentes en ambos hemitorax, se auscultan roncos bilaterales a predominio de base derecha, ruidos cardiacos rítmicos regulares, sin soplo ni galope. ''',
			"abdomen": ''' globoso, a expensa de panículo adiposo, ruidos hidroaéreos presentes,  depresible, no doloroso a la palpación, no visceromegalia.''',

			"neurologico": '''inconsciente, paciente bajo efecto de sedación farmacológica Glasgow no evaluable, pupilas isocóricas hiporreactivas a la luz.''',
			"extremidades": '''simétricas sin edemas. ''',

		}, 

		"diagnosticoIngresoUCI": [

								"Crisis hipertensiva tipo emergencia expresada en EVC de posible etiología hemorrágica a descartar.",
								"Infección respiratoria baja: neumonía por broncoaspiración.",
								"Hipertensión arterial sistémica. ",
								"Diabetes Mellitus tipo II",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": '''Fc: 95 lpm Fr: 15 rpm  TA: 190/100 mmHg SATO2:? %. En vista de condiciones clínicas de paciente comunican caso a Internista de guardia (Dr. Camino) quien indica solicitar valoración por UCI. Se acude al llamado evaluando paciente en área de choque en condiciones clínicas de cuidados constatando deterioro del estado neurológico, trabajo respiratorio además de desaturación por monitor constatado posteriormente por gases arteriales se decide  intubación endotraqueal con tubo 8.0 Fr. sin complicaciones evidenciando salida de secreción con contenido alimentario a través de tubo endotraqueal se conecta a ventilación mecánica y en vista de no contar cupo en el servicio se realizan sugerencias. Paciente permanece durante 24 horas en área de choque siendo evaluado el día 02/03/2015 por Intensivista Dra. Maritza Vásquez, quien decide rotar antibióticoterapia y administra dosis de manitol al 18%  de 500 cc stat, indica tratamiento antipertensivo y solicita valoración por el servicio de Neurocirugía. En vista de contar con cupo en UCI se decide su ingreso.	''',
			"piel": ''' morena, normo térmica, normohidratada llenado capilar <3 Seg.''',
			"cardiopulmonar": '''tórax simétrico, normo expansible, ruidos respiratorios presentes, no se  auscultan ruidos cardiacos rítmicos taquicárdicos  normofonéticos, no soplos. ''',
			"abdomen": '''globuloso, a expensa de panículo adiposo, ruidos hidroaéreos presentes.''',
			"extremidades": '''simétricas  sin edema.''',
			"neurologico": '''inconsciente desorientado, irritable  Glasgow 6/15 ptos.''',
		},  

		"diagnosticoIngresoHUAPA": [
								
			"Emergencia hipertensiva tipo ACV hemorrágico.",
			"Hipertensión arterial sistémica ",
			"Diabetes Mellitus ", 

		], 
		
	},# 123


	{
		"IdHistoria": "52–05–58", 
		
		"nombre": "Edinson Herrera", 		
		
		"edad": "31",
		
		"ci": "15.935.956", 
		
		"dirección": "Campeche sector 3",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1982,12,6),

		"lugarNacimiento": "Cumaná", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,5,17),

		"fechaIngresoUCI": datetime(2014,5,17),


		"resumenIngreso": '''Se trata de paciente masculino de 31 años de edad natural y procedente de la localidad sin antecedentes patológicos importantes quien inicia enfermedad actual el día 16/05/14 cuando presenta herida por proyectil de arma de fuego en región lumbar derecha y en cuarto espacio intercostal derecho línea medio clavicular por lo que acude a este centro donde se ingresa por servicio de cirugía blanda con diagnostico de Trauma abdominal penetrante por proyectil de arma de fuego. ''', 


		"examenFisicoIngresoUCI": {


			
			"piel" : 	'''	deshidratado, afebril al tacto.''',
		
			"cardiopulmonar":  ''' Tórax simétrico, hipoexpandible; presencia de tubo de tórax conectadoa trampa de agua, apósitos limpios sin secreción, enfisema subcutáneo. Ruidos cardiacos rítmicos, normo fonéticos, sin solplos ni galope . Ruidos respiratorios presentes MV conservado, sin agregados.''',
			"abdomen": ''' distendido, presencia de apósito esteril cubriendo herida quirúrgica limpio sin secreción, presencia de drenes funcionante conectado a bolsa recolectora con gasto hemático.RHA ausentes.''',

			"neurologico": ''' No evaluable por efectos de sedación.''',
		}, 

		"diagnosticoIngresoUCI": [
									

									"POM de Laparotomia exploradora por herida por proyectil de arma de fuego complicada con:",
									"Lesión grado IV de lóbulo hepático derecho",
									"Lesión grado III de hemidiafragma derecho",
									"Hemoperitoneo",
								],  

		"examenFisicoIngresoHUAPA": {
		
			"piel": ''' morena, normo térmica, llene capilar <3 seg,''',
			"cardiopulmonar": '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes, MV disminuido en hemitorax derecho, se evidencia HPAF en cuarto espacio intercostal derecho línea medio clavicular. Ruidos cardiacos rítmicos normofonéticos, no soplos. ''',
			"abdomen": '''Blando depresible doloroso a la palpación, se evidencia orificio de entrada de HPAF en fosa lumbar derecha sin orificio de salida''',
			"extremidades": '''	simétricas eutróficas sin edema.''',

		},  

		"diagnosticoIngresoHUAPA": [
				"Trauma abdominal penetrante por arma de fuego.",
				{"resumen":''' El paciente es llevado a mesa operatoria donde se realiza laparotomía xifopubica hallando 2500 cc de hemoperitoneo, lesión grado IV hepática de lóbulo derecho, lesión grado III de hemidiafragma derecho; realizando evacuación de hemoperitoneo, colocación de packing hepático, rafia de lesión de hemidiafragma, toracotomía minima en 5to espacio intercostal derecho mas colocación de tubo de drenaje torácico 36 fr. El paciente es evaluado por UCI quien por no tener cupo, conecta a ventilación mecánica en área de recuperación MA1 y hace sugerencias. El día de hoy se re evalua al paciente y por disponer de cupo se decide su ingreso a  UCI. Se recibe paciente en camilla de traslado, intubado, recibiendo oxigeno húmedo por ambu, se traslada a cama UCI, se conecta a monitor cardiaco continuo que reporta: Fc 141 lpm Fr: 20 rpm TA: 113/70 (82) mmHg SATO2: 100%.'''},			

		], 
		
	}, # 124

	{
		"IdHistoria": "52-62-03 ", 
		
		"nombre": "Brito Marquez Jesús Esteban", 		
		
		"edad": "57",
		
		"ci": "8.441.053 ", 
		
		"dirección": "Cumanacoa",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1957,9,1),

		"lugarNacimiento": "Cumanacoa", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,10,21),

		"fechaIngresoUCI": datetime(2014,10,21),

		"resumenIngreso": '''Se trata de paciente masculino de 57 años de edad conocido con Litiasis Vesicular, quien inicia enfermedad actual el  10/10/2014 cuando presenta dolor en Hipocondrio derecho de fuerte intensidad, irradiado hacia epigastrio, acompañado de náuseas y vómitos, posteriormente se anexa al cuadro aumento de la temperatura corporal cuantificado en 39ºC atenuado con acetaminofen, motivos por los cuales acude a este centro donde se evalúa e ingresa. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Paciente en malas condiciones generales, hemodinámicamente inestable, recibiendo Norepinefrina por infusión contínua, conectado a ventilación mecánica, se traslada a cama y se conecta a monitor cardíaco externo que reporta: SIGNOS VITALES: TA: 76/--mmHg FC: 184 lpm FR 11:rpm SPO2:--''',
			
			"piel" : 	'''	morena, hipotérmica, normoelastica, llenado capilar < 3 segundos, con acentuado tinte ictérico en piel y mucosas.''',
		
			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible, ruidos respiratorios presentes con crepitantes en base pulmonar izquierda, ruidos cardíacos rítmicos regulares, sin soplos.''',

			"abdomen": ''' globoso, blando, herida quirúrgica cubierta con apósitos sin secreciones, drenes con escasa salida de contenido hemático. ''',

			"neurologico": ''' no evaluable por sedación farmacológica, pupilas isocóricas con tendencia a la midriasis, no reactivas a la luz.''',
			"extremidades": '''simétricas, se evidencia edema en ambos miembros inferiores,''',

		}, 

		"diagnosticoIngresoUCI": [


						"Shock Séptico",
						"Sepsis punto de partida abdominal",
						"Postoperatorio Inmediato de Laparotomía para drenaje de Absceso Hepático.",
						"Insuficiencia Renal Crónica Reagudizada",
						"Síndrome Ictérico Obstructivo",
						"Litiasis Vesicular",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' El día 17/10/2104 se realiza Ecosonograma Abdominal que reporta: 1) Vesícula con paredes con doble contorno. 2) Microlitiasis Renal Bilateral. Paciente luce en aparentes regulares condiciones generales, eupneico, afebril, tolerando aire ambiente.  SIGNOS VITALES: FC: 78lpm FR: 17rpm ''',
			"piel": '''morena, normotérmica, normoelastica, llenado capilar < 3 segundos, tinte ictérico en piel y mucosas.''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes, sin agregados, ruidos cardíacos rítmicos regulares, sin soplos.''',
			"abdomen": '''panículo adiposo moderado, blando, ruidos hidroaéreos presentes, dolor en hipocondrio derecho, signo de Murphy positivo, sin megalias, sin signos de irritación peritoneal. ''',
			
			"neurologico": '''consciente, orientado en 3 planos, lenguaje coherente, fuerza muscular y reflejos osteotendinosos conservados.''',
		

		},  

		"diagnosticoIngresoHUAPA": [
						"Ictericia Obstructiva",
						"Síndrome Ictérico Obstructivo",
						{"resumen":''' El paciente permanece en el Área de Hospitalización recibiendo antibióticoterapia, presentando evolución no satisfactoria, retención de azoados motivos por los cuales solicitan la valoración por Nefrología y UCI quien acude a evaluar paciente y realiza sugerencias, se le realiza Ecosonograma Abdominal en donde se evidencia múltiples abscesos hepáticos por lo que plantean resolución quirúrgica para drenaje de dichos abscesos. En vista de que el paciente persiste en malas condiciones, con deterioro del estado general, deterioro del estado neurológico solicitan valoración y manejo postquirúrgico. El día de hoy (21/10/2014) el paciente es llevado a mesa operatoria donde bajo anestesia general se realiza laparotomía media, para supra e infraumbilical evidenciándose 200 cc de sangre en cavidad abdominal, 500cc de líquido seroso, absceso hepático en lóbulo derecho de aproximadamente 15x10cms en segmentos VI y VIII y bazo aumentado de tamaño, se toma como conducta evacuación de hemoperitoneo, de liquido seroso y drenaje de absceso hepático con salida de contenido purulento fétido. Lavado de cavidad, rafia, comprobación de hemostasia, se dejan dos drenes, dirigidos a lecho hepático y corrredera parieto-cólica derecha respectivamente, síntesis por planos y asepsia final.'''}
								

		], 
		
	},#125

	{
		"IdHistoria": "06–48–32", 
		
		"nombre": "Elba Rosa Bilmonte de Brito", 		
		
		"edad": "69",
		
		"ci": "3.337.518", 
		
		"dirección": "Muelle Cariaco, calle las Flores, casa S/N",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1944,9,4),

		"lugarNacimiento": "Cariaco, Edo. Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,3,2),

		"fechaIngresoUCI": datetime(2014,4,8),

		"resumenIngreso": '''Paciente femenina de 69 años de edad, natural y procedente de Cariaco, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual a principios del mes de febrero de 2014 aproximadamente cuando presenta movimientos tónico-clónicos generalizados, con relajación de esfínter vesical, motivo por el cual es llevada a ambulatorio de su localidad, de donde es referida a este centro asistencial el día 02/03/14 y previa valoración se ingresa por el servicio de Medicina Interna con los diagnósticos de EVC en evolución y síndrome convulsivo. Al momento del ingreso presenta desorientación en tiempo y espacio, lenguaje incoherente y hemiparesia izquierda. Permanece en área de emergencia y observación hasta el día 06/04/14 cuando es trasladada a piso de hospitalización. El día 02/03/14 se le realiza TAC simple cerebral que reporta efecto de masa frontal derecho, por lo que el 07/03/14 se le realiza RM cerebral con contraste paramagnético endovenoso, reportando lesión de aspecto tumoral, de aspecto extraaxial, probablemente meningioma fronto temporal derecho, con muy discreto edema perilesional y leve hernia subfalsina, solicitan valoración por el servicio de Neurocirugía, siendo evaluada por Dr. Acevedo (Neurocirujano) quien indica tener criterios de resolución quirúrgica por lo que se planifica para cirugía electiva. El día de hoy 08/04/14 es llevada a mesa operatoria donde bajo anestesia general se realiza incisión hemicoronal, disección por planos y disección de pericráneo hasta exponer órbita, osteotomía supraorbitaria, maxilar derecha y de arco cigomático, liberación de barra frontoorbitocigomática, craneotomía pterional y durotomía en “Y”, por falta de tiempo quirúrgico se difiere para culminación en un segundo tiempo quirúrgico. Previa autorización de Dra. Teresa Cortesía  se indica su ingreso a la UCI.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubada y conectada a ventilador mecánico de transporte, se pasa a cama UCI, se conecta a ventilación mecánica modo A/C, Vc: 560, FR: 12, FiO2: 60, Fl: 50, PEEP: 0 y se conecta a monitor cardíaco continuo que reporta: TA: 116/65(82) mmHg; FC: 105 lpm;  FR: 12 rpm; SatO2: 100%''',
			
			"piel" : 	'''	moderada palidez cutáneo-mucosa, hipotérmica al tacto, llenado capilar < 3seg.''',
	
			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, con roncus escasos bilaterales. Ruidos cardíacos rítmicos y regulares, taquicárdicos, sin soplo ni galope.''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico''',

			"neurologico": ''' no evaluable por efectos de sedación y relajación farmacológica. ''',

		}, 

		"diagnosticoIngresoUCI": [

						"POI DE CRANEOTOMIA FRONTO-ORBITO-CIGOMATICA PARA EXCERESIS DE LOE CEREBRAL EN 1/3 INTERNO DE ALA ESFENOIDAL DERECHO SUGESTIVO DE MENINGIOMA",
						"TRASTORNO HEMATOLOGICO:",
						"ANEMIA MODERADA",
						"TRASTORNO ACIDO-BASE:",
						"ACIDOSIS METABOLICA COMPENSADA CON ALCALOSIS RESPIRATORIA + HIPEROXEMIA",

									
								],  
	},# 126

	{
		
		"nombre": "Moris  Antabu", 		
		
		"edad": "74",
		
		"ci": "8.648.885", 
		
		"dirección": "Parcelamiento miranda sector D numero 34 Calle Vergatin ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1940,2,12),

		"lugarNacimiento": "Siria", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,11,5),

		"fechaIngresoUCI": datetime(2014,11,5),

		"resumenIngreso": '''Paciente masculino de 74 años de edad, natural de Siria y procedente de la localidad, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual el día 03/11/14 cuando presenta dolor abdominal difuso, motivo por el cual es llevado a centro asistencial privado donde es evaluado por especialistas (Internista, Gastroenterólogo, Cirujano General), se plantea diagnóstico de obstrucción intestinal y es llevado a mesa operatoria para resolución quirúrgica el día 04/11/14, se le realiza laparotomía exploratoria teniendo como hallazgos aproximadamente 500cc de exudado purulento libre en cavidad abdominal, tumor estenosante de aproximadamente 15x10cm de largo, con extensión hacia colon sigmoide y ascendente, tumor de 6cm de diámetro a nivel del ángulo esplénico de colon, fijado a retroperitoneo, bazo y epiplón mayor, con múltiples adenomegalias a nivel de colon transverso y 2 orificios de perforación de aproximadamente 0,5cm de diámetro, se toma como conducta evacuación y lavado de líquido libre en cavidad abdominal, se realiza colostomía tipo Hartman, ommentectomía mayor, constatación de hemostasia y cierre por planos dejando dren de látex a nivel de tejido subcutáneo. Paciente trasladado a la UCI de centro privado para manejo de postquirúrgico inmediato, al momento de su ingreso se mantiene intubado y se conecta a ventilación mecánica modo A/C, evoluciona tórpidamente llegando a la inestabilidad hemodinámica, ameritando Vasoactivos tipo Norepinefrina. El día de hoy 05/11/14, se procede a realizar extubación y por solicitud de familiares y previa autorización de Dra. Begglia Roa (Intensivista de Guardia), se decide su traslado a la UCI de este centro asistencial. Se recibe  paciente en camilla de traslado, inestable hemodinámicamente, recibiendo Levophed, sin monitor cardíaco, recibiendo O2 a través de sistema Ventury al 50%, se traslada a cama de UCI y se conecta monitor cardiaco continuo que reporta  signos vitales:  TA: 118/71(96) mmHg,  FC: 107 lpm, FR: 24 rpm, SATO2: 99%. ''', 


		"examenFisicoIngresoUCI": {

			"piel" : 	'''blanca, normotérmica al tacto, llenado capilar < 3 segundos.''',
			

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, taquicárdicos,  no se auscultan soplos ni galope.  ''',
			"abdomen": ''' globoso a expensas de panículo adiposo, ruidos hidroaéreos disminuidos, herida quirúrgica cubierta por apósitos con escasa secreción serohemática, se evidencia colostomía en flanco derecho funcionante, con bolsa de colostomía, blando, depresible, ligeramente doloroso a la palpación profunda, no megálico.''',

			"neurologico": '''Consciente, lenguaje coherente, pupilas isocóricas,  normorreactivas a la luz, Glasgow: 15/15 puntos. ''',
		}, 

		"diagnosticoIngresoUCI": [
									"POST-OPERATORIO MEDIATO DE LAPAROTOMIA EXPLORATORIA POR OBSTRUCION INTESTINAL DEBIDO A TUMOR ESTENOTICO DE COLON SIGMOIDE Y DESCENDENTE",
									"PERITONITIS PUNTO DE PARTIDA PERFORACION DE COLON TRANSVERSO",
									"SHOCK SEPTICO : SEPSIS PUNTO DE PARTIDA ABDOMINAL",
									"INFECCION RESPIRATORIA BAJA: NEUMONIA BILATERAL",
									"TRASTORNO HEMATOLOGICO:",
									"ANEMIA LEVE",
									"TRASTORNO ACIDO – BASE:",
									"ACIDOSIS METABOLICA COMPENSADA CON ALCALOSIS RESPIRATORIA MAS HIPEROXEMIA",

								],  
		
	},# 127

	{
		"IdHistoria": "54–27–10 ", 
		
		"nombre": "Juan Gabriel  Alzolar Perdomo", 		
		
		"edad": "40",
		
		"ci": "14.125.673 ", 
		
		"dirección": "barrió Campeche ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1975,12,18),

		"lugarNacimiento": "Cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,2,12),

		"fechaIngresoUCI": datetime(2015,2,13),

		"resumenIngreso": '''Paciente masculino de 40 años de edad, natural y procedente de la localidad, con  antecedentes patológicos de hipertensión arterial sistémica no controlado, refiere inicio de enfermedad actual  hace 1 semana aproximadamente cuando presenta aumento de la temperatura corporal cuantificado en 39 ºC, atenuado con acetaminofén posteriormente eritema generalizado, mialgia, artralgia y debilidad generalizada, el día 12/02/2016 se anexa al cuadro alteración del estado de consciencia, agitación psicomotriz y limitación para la marcha, por lo que acude a especialista Dr Aponte quien indica estudio por imagen TAC de cráneo, el cual reporta EDEMA CEREBRAL DISUSO , por lo que decide referir a nuestro asistencial, donde es ingresado por el servicio de medicina interna''', 


		"examenFisicoIngresoUCI": {
			
			"piel" : 	'''	Morena, normotérmica al tacto, llenado capilar <3 Seg.  ''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax, sin agregados. Ruidos cardiacos rítmicos, regulares, taquicardicos, sin soplos ni galope. ''',
			"abdomen": ''' ruidos hidroaéreos presentes, no doloroso a la palpación, no megálico.''',

			"neurologico": ''' consciente, lenguaje coherente, orientada en los 3 planos, pupilas isocóricas, reactivas a la luz, FM V/V en miembros inferiores y V/V en miembros superiores, ROT II/IV en miembros inferiores y superiores, Glasgow 15/15pts. ''',
			"extremidades": '''eutróficas, sin edema.''',

		}, 

		"diagnosticoIngresoUCI": ["Encefalitis viral complicada con edema cerebral difuso.",
									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' SIGNOS VITALES: TA: 150/100 mmHg FC: 82 LPM FR: 19 RPM. El paciente permanece durante 2 horas en el servicio de emergencia, recibiendo medidas anti edema cerebral, a base de Manitol al 10 %, Solicitan valoración por el servicio de Terapia Intensiva en vista de cuadro clínico, se evalúa y por disponibilidad de cupo, previa autorización de Dr Alpino  (Intensivista de Guardia) se decide su ingreso a la UCI. Se recibe paciente en silla de rueda, respirando aire ambiente, se conecta a monitor cardíaco continuo que reporta  TA: 131/85 (102) mmHg, FC: 120 lpm,  FR: 20 rpm, SatO2: 90%.''',
			"piel": ''' normotérmica al tacto, llenado capilar < 3 segundos.''',
			"cardiopulmonar": '''tórax simétrico, expandible, ruidos respiratorios presentes en ambos hemitórax, sin agregados. Ruidos cardiacos rítmicos regulares sin soplo ni galope ''',
			"abdomen": '''plano, ruidos hidroaéreos presentes, no doloroso a la palpación, no se palpación visceromegalias.''',
			"extremidades": '''simétricas, sin edema, ''',
			"neurologico": '''consciente, desorientado con cambios de conducta ''',
		},  

		"diagnosticoIngresoHUAPA": [

			"ESTADO CONFUSIONAL",
			"ENCEFALITIS VIRAL",
			"SINDROME DE HIPERTENSION ENDOCRANEANA",
			"EDEMA CEREBRAL DIFUSO",

								

		], 
		
	},# 128


	{
		"nombre": "Zoila Maza de Malavé ", 		
		
		"edad": "90",
		
		"dirección": "Cumana Calle Principal Cruz Roja casa 17 ",
		
		"fechaNacimiento":  datetime(1924,6,5),

		"lugarNacimiento": "Cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,4,27),

		"fechaIngresoUCI": datetime(2014,4,27),

		"resumenIngreso": ''' Se trata de paciente femenina de 90 años de edad con antecedentes de Hipertensión Arterial desde hace varios  años en tratamiento con Atacand 16 mg OD , inicia enfermedad actual el día 23-04-2015  caracterizado por vómitos de contenido alimentario al inicio luego oscuros (borra de café ) en repetidas oportunidades,  acompañado de dolor abdominal epigástrico opresivo sin irradiación , deterioro del estado  de consciencia, por lo que es llevada a centro privado de la localidad ''', 


		"examenFisicoIngresoUCI": {

			"piel" : 	'''	Normotérmica, deshidratada, llenado capilar <3segundos. ''',
		
			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible, con estertores crepitantes en ambasa bases pulmonares. Ruidos cardíacos rítmicos, regulares, no se auscultan soplos.''',
			"abdomen": ''' Blando, doloroso a la palpación superficial y  profunda en epigastrio , no visceromegalia''',

			"neurologico": ''' Glasgow 3  puntos dado por RM 1 RO 1 RV 1 pupilas isocóricas reactivas no signos meníngeos ''',
		

		}, 

		"diagnosticoIngresoPrivado": [
				"ECV DE POSIBLE ETIOLOGIA HEMORRAGICA ",
				"HEMORRAGIA DIGESTIVA INFERIOR",  
				"DESHIDRATACION SEVERA ",
				"HTA SISTEMICA ",
				{"resumen":''' La paciente permanece en centro privado ,a las 24 horas de su ingreso se constata hipotensión arterial que no responde a retos de líquidos por lo que amerita vasoactivos tipo Levophed  a razón de 55 mcg min , con deterioro progresivo del estado de consciencia ,debido a situación socioeconómica se decide su traslado a UCI HUAPA '''}

		],


		"diagnosticoEgresoPrivado":[
			"SHOCK SEPTICO ",
			"SEPSIS PUNTO PARTIDA TRACTO URINARIO vs RESPIRATORIO   ",
			"ECV DE POSIBLE ETIOLOGIA HEMORRAGICA ",
			"HEMORRAGIA DIGESTIVA SUPERIOR ",
			"DESHIDRATACION SEVERA ",
			"HTA SISTEMICA ",
			{"resumen":''' Se recibe paciente en camilla de traslado conectada  a monitor cardiaco, recibe oxigeno por mascarilla facial tipo Ventury al 50'%' se traslada a cama de UCI. SIGNOS VITALES:   FC 88 LPM    TA 40/23 MMHG  FR 34   SAT O2 100% '''}

		],

		"diagnosticoIngresoUCI": [
									"SHOCK SEPTICO ",
									"SEPSIS PUNTO PARTIDA TRACTO URINARIO vs RESPIRATORIO  ", 
									"ECV DE POSIBLE ETIOLOGIA HEMORRAGICA ",
									"HEMORRAGIA DIGESTIVA SUPERIOR ",
									"DESHIDRATACION SEVERA ",
									"HTA SISTEMICA ",
									"Postoperatorio Inmediato de Craneotomía Pterional Derecha para Exceresis de Tu de Hipófisis (no resecado)",
									"Macroadenoma de Hipófisis",
									"Hipertensión Arterial Sistémica.",

								],  

		"examenFisicoIngresoPrivado": {
	
			"piel": ''' Normotérmica, deshidratada, llenado capilar <3segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, con estertores crepitantes en bases pulmonares.  Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos.''',
			"abdomen": '''Blando,  doloroso a la palpación superficial y  profunda, no visceromegalia''',
			
			"neurologico": '''Glasgow 6 puntos dado por RM 4 RO 1 RV 1 pupilas isocóricas reactivas no signos meníngeos ni de focalización motora''',

		},

		"examenFisicoIngresoHUAPA": {

			"piel": ''' Normotérmica, deshidratada, llenado capilar <3segundos.''',
			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, con estertores roncus.  Ruidos cardíacos rítmicos, regulares, no se auscultan soplos. ''',
			"abdomen": '''globoso, blando, no doloroso a la palpación superficial ni profunda, no visceromegalias. ''',
			
			"neurologico": '''Conservado''',
		

		}, 

		"diagnosticoIngresoHUAPA": [

				{"resumen":''' La paciente permanece en Área de Hospitalización hasta el día de hoy cuando es llevada a mesa operatoria y bajo anestesia general inhalatoria se realiza craneotomía, retiro de flap óseo, disección subfrontal y temporal con evidencia de accidente de vasos sanguíneos, control de sangrado, síntesis por planos, asepsia final. Se mantiene durante acto operatorio hemodinámicamente estable con un sangrado estimado de 800 cc y se traslada a UCI. '''},				
				"Tu. Cerebral",
				"Hipertensión Arterial",
				"Deshidratación Leve",

		], 
		
	},#129

	{
		"IdHistoria": "52–11–80", 
		
		"nombre": "Julián José Peñalver ", 		
		
		"edad": "57",
		
		"ci": "11.600.430", 
		
		"dirección": "Cumanacoa, sector La Manga, casa S/N",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1957,1,3),

		"lugarNacimiento": "Cumanacoa, Edo. Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,5,30),

		"fechaIngresoUCI": datetime(2014,6,9),

		"resumenIngreso": ''' Paciente masculino de 57 años de edad, natural y procedente de Cumanacoa, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual a mediados del mes de mayo de 2014 aproximadamente cuando presenta disnea de medianos esfuerzos que progresa a pequeños esfuerzos, acompañado de edema en miembros inferiores, motivo por el cual, el día 30/05/14 acude a centro privado donde es evaluado por cardiólogo, realizan ecocardiograma que reporta derrame pericárdico severo, por lo que refieren a este centro asistencial donde es ingresado por el servicio de Medicina Interna con el diagnóstico de Derrama pericárdico severo complicaco con colapso cardíaco derecho; solicitan valoración por cirugía cardiovascular, es avaluado por Dr. Soto (Cirujano Cardiovascular) quien indica tener criterios para resolución quirúrgica; permanece en área de hospitalización hasta el día de hoy 09/06/14 cuando es llevad a mesa operatoria y bajo anestesia general se realiza toracotomía anterior en 5to espacio intercostal de 8cm aproximadamente hasta llegar a cavidad torácica, se evidencia lóbulo inferior pulmonar izquierdo con múltiples adherencias a pleura parietal, pericardio inflamatorio con tejido fibrótico, con aproximadamente 1000cc de líquido serohemático no fétido, se realiza pericardiectomía y toma muestra para diferentes estudios, verificación de hemostasia y se deja tubo de drenaje torácico conectado a pleurovac®, cierre por planos y asepsia final. Previa autorización de Dra. Teresa Cortesía  se indica su ingreso a la UCI.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubado y conectado a ventilador mecánico de transporte, se pasa a cama UCI, se conecta a ventilación mecánica modo A/C, Vc: 480, FR: 12, FiO2: 60, Fl: 50, PEEP: 0 y se conecta a monitor cardíaco continuo que reporta: TA: 116/65(82) mmHg; FC: 105 lpm; FR: 12 rpm;  SatO2: 100% ''',
			
			"piel" : 	'''moderada palidez cutáneo-mucosa, hipotérmica al tacto, llenado capilar < 3seg.''',
			
			"cardiopulmonar":  '''tórax asimétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, disminuidos en base pulmonar izquierda, con sibilantes bilaterales en ápices pulmonares. Ruidos cardíacos rítmicos y regulares, taquicárdicos, sin soplo ni galope.''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico''',

			"neurologico": ''' no evaluable por efectos de sedación y relajación farmacológica.''',
		}, 

		"diagnosticoIngresoUCI": [
									"POSTOPERATORIO INMEDIATO DE PERICARDIECTOMIA POR DERRAME PERICARDICO SEVERO COMPLICADO CON COLAPSO CARDIACO DERECHO",
									"TRASTORNO HEMATOLOGICO:",
									"ANEMIA LEVE",
									"TRASTORNO ACIDO-BASE:",
									"HIPEROXEMIA",
								],  
		
	},# 130

	{
		"IdHistoria": "54-00-06", 
		
		"nombre": "Rubén Rafael yeguez Goitia", 		
		
		"edad": "72",
		
		"ci": "2.659.728", 
		
		"dirección": "el peñón 3 era calle casa sin número.",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1943, 3, 20),

		"lugarNacimiento": "CUMANA", 
			 		
		"fechaIngresoHUAPA":  datetime(2015, 11,16),

		"fechaIngresoUCI": datetime(2015, 11, 22),

		"resumenIngreso": ''' Se trata de paciente masculino de 72 años de edad, natural y procedente de la localidad, con antecedentes de hipertensión arterial no controlada, diabetes mellitus tipo II en tratamiento con glucofage 500 mg OD, quien inicia enfermedad actual el día 15/11/2015 cuando presenta dolor precordial que se irradia a cuello y miembros superiores izquierdo que se intensifica el día 16/11/2015 por lo que acude a ambulatorio de la localidad donde realizan electrocardiograma evidenciando cambios en el mismo, motivo por el cual es referido a nuestro centro asistencial donde es evaluado por el servicio de medicina interna quien decide su ingreso. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, recibiendo oxigeno húmedo por bigote nasal, se traslada a cama de UCI, se conecta a monitor cardíaco externo que reporta: TA: 89/56(68) mmHg FC: 166 lpm FR: 27rpm SPO2: 95% Se realiza electrocardiograma evidenciando taquicardia supra ventricular con inestabilidad hemodinámica, se comunica caso con especialista de guardia doctor Guaimare quien indica cardiovertir, se administra midazolam dosis de sedación y se procede a realizar cardioversión con 100 yuls se realiza electrocardiograma post cardioversión evidenciando ritmo sinusal. Se procede a realizar catéter venoso yugular izquierda con catéter 6 FR monolumen sin complicaciones.''',
			
			"piel" : 	'''blanca, hipotermicatérmica al tacto, se evidencia ligera palidez cutánea mucosa, llenado capilar > 3 Seg.''',
			

			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible ruidos respiratorios presentes en ambos hemitorax con agregados crepitantes bibasales, Ruidos cardiacos arrítmicos taquicardicos, sin  soplo ni galope.	''',
			"abdomen": ''' globoso a expensa de panículo adiposo, Blando, no doloroso a la palpación, ruidos hidroaéreos presentes, no megalias ''',

			"neurologico": ''' Paciente somnoliento. Glasgow: 15/15pts, Respuesta Motora: 6pt, Apertura Ocular: 4pt.  Respuesta Verbal: 5pt. Pupilas isocóricas reactivas a la luz. ''',
			"extremidades": '''Simétricas, sin edema.''',

		}, 

		"diagnosticoIngresoUCI": [

										"Shock cardiogenico.",
										"Síndrome coronario agudo infarto  al miocardio con elevación del segmento ST en cara anteroseptal",
										"taquicardia supra ventricular.",
										"Hipertensión arterial no controlada",
										"Diabetes mellitus tipo II descompensada en hipoglicia",
									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 150/90() mmHg FC: 79pm FR: 19rpm SPO2: %. Paciente es evaluado por el servicio de cardiología Dra. María Ledesma el día 17/11/2015 quien replantea diagnostico a infarto agudo al miocardio con elevación del  segmento st no trombolizado, sugiriendo tratamiento a base de nitroglicerina en vista de paciente presentar dolor precordial, indica tratamiento a base de concor 2.5 mg OD, ecocardiograma y hollter cardiaco. Se anexa en horas de la noche dificultad respiratoria a pequeños esfuerzos con cifras de tensión arterial 200/100 mmHg por lo que administran dosis de lasix 40 mg stat. Con leve mejoría clínica, se plantea diagnóstico de edema agudo de pulmón  El día 18/11/2015 es reevaluado por el servicio de cardiología Dr. Khan quien realiza reajuste de tratamiento, permaneciendo en el área de choque durante 6 días con evolución clínica tórpida, el día 22/11/2015 se anexa al cuadro hipotensión arterial severa requiriendo soporte con vasoactivos levophed, se solicita valoración por el servicio de terapia intensiva evaluando paciente en condiciones clínicas de cuidado, por disponibilidad de cupo se decide su ingreso en la unidad de cuidados intensivos. ''',
			"piel": ''' blanca, normotermicatérmica al tacto, se evidencia ligera palidez cutánea mucosa, llenado capilar > 3 Seg. ''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible ruidos respiratorios presentes en ambos hemitorax sin agregados, Ruidos cardiacos rítmicos, sin  soplo ni galope.	''',
			"abdomen": '''globoso a expensa de panículo adiposo, Blando, no doloroso a la palpación, ruidos hidroaéreos presentes, no megalias''',
			"extremidades": '''Simétricas, sin edema.''',
			"neurologico": '''Paciente consciente. Glasgow: 15/15pts, Respuesta Motora: 6pt, Apertura Ocular: 4pt. Respuesta Verbal: 5pt. Pupilas isocóricas reactivas a la luz.''',
			

		},  

		"diagnosticoIngresoHUAPA": [
					"Síndrome coronario agudo infarto al miocardio sin elevación del segmento ST",
					"Isquemia sub endocardica en cara antero lateral ",
					"Hipertensión arterial sistémica no controlada.",
					"Diabetes mellitus tipo II",

		], 
		
	}, # 131

	{
		"IdHistoria": "19-41-61", 
		
		"nombre": "Zoraida Mercedes Rodríguez Valera", 		
		
		"edad": "48",
		
		"ci": "8.700.968", 
		
		"dirección": "Mariguitar, Sector Golindano, Calle Cuba, casa núm. 6 ",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1966,3,1),

		"lugarNacimiento": "Cumaná", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,1,9),

		"fechaIngresoUCI": datetime(2014,1,9),

		"antecedentes": '''Histerectomía hace 3 años aproximadamente.''', 

		"resumenIngreso": '''Se trata de paciente femenina de 48 años de edad, quien refiere inicio de enfermedad actual el día 07/01/14 cuando posterior a accidente de tránsito en automóvil (Autobús) tipo colisión presenta traumatismos múltiples motivos por los cuales es trasladada a este centro donde se ingresa con el diagnóstico de Traumatismo Craneoencefálico Severo con fractura fronto-parietal, se realiza TAC de Cráneo donde en vista de resultados es llevada a mesa operatoria el mismo día.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente en malas condiciones generales, hemodinámicamente inestable, recibiendo Norepinefrina a razón de 22,4 mic/min, conectada a ventilación mecánica y conectada a monitor cardíaco externo que reporta: TA: 112/70mmHg 	FC:135lpm; FR: 15rpm; SPO2: 100%''',
			
			"piel" : 	'''	blanca, hipotérmica, turgor disminuido, con acentuada pálidez cutáneo-mucosa, llenado capilar < 3 segundos.''',
			"cabeza": '''cubierta por apósitos limpios, no se evidencian secreciones. ''',
			"cara":''' blanca, con equimosis bipalpebral, herida en región frontal afrontada, sin secreciones.''',

			"cardiopulmonar":  ''' tórax simétrico, hipoexpansible, ruidos respiratorios presentes, se auscultan disminuidos en base derecha, ruidos cardíacos rítmicos, regulares, no se auscultan soplos.''',
			"abdomen": ''' globoso, blando, depresible, no doloroso a la palpación, se evidencia herida quirúrgica en región supra, para e infraumbilical cubierta por apósitos limpios, sin secreciones, ruidos hidroáereos presentes.''',

			"neurologico": '''Inconsciente, Glasgow: 3/15 pts, Respuesta Motora: 1pt, Respuesta Verbal: 1pt, Apertura Ocular: 1pt. Pupilas midriáticas, sin respuesta a la luz, reflejo tusígeno ausente, reflejo corneal ausente. ''',
			

		}, 

		"diagnosticoIngresoUCI": [

								"Postoperatorio Mediato de Craniectomía por Drenaje de Hematoma Epidural y Subdural Agudo Fronto-Temporal.",
								"Traumatismo Craneoencefálico Severo complicado con: ",
								"Hematoma Epidural",
								"Hematoma Subdural",
								"Fractura fronto-temporal", 
								"Inestabilidad Hemodinámica",
								"Insuficiencia Renal Aguda ",
								"Trastorno Hematológico: Anemia Moderada, Trombocitopenia.",
								"Trastorno Acido/Base: Acidosis Metabólica Compensada con Alcalosis Respiratoria e Hiperoxemia.",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente en malas condiciones generales. Se traslada a Quirófano donde bajo anestesia general balanceada  realizan drenaje de Hematoma Epidural y Subdural Temporo-Parietal Derecho, además se realiza laparotomía exploradora sin evidenciarse lesiones de órganos intra-abdominales, posterior a la intervención la paciente se traslada a el Área de Recuperación, es valorada por el Servicio de UCI quien en vista de no contar con cupo,  conecta a ventilación mecánica (Ventilador MA1), evidencia inestabilidad hemodinámica por lo que se indica Vasoactivos (Norepinefrina) llegando a recibir como dosis máxima 106 mic/min, se evidencia además Glasgow: 3/15pts, Respuesta Motora: 1pt, Respuesta Verbal: 1pt, Apertura Ocular: 1pt, pupilas midriáticas sin respuesta a la luz, sin reflejo córneal ni tusígeno  y se realizan sugerencias. El día de hoy en vista de disponibilidad de cupo se decide su ingreso.''',
			"piel": ''' Blanca, normotérmica, con acentuada palidez cutáneo-mucosa.''',
			
			"neurologico": '''Agitada, Glasgow: 8/15 pts, Respuesta Motora: 5pts, Respuesta Verbal: 2pts, Apertura Ocular: 1pt.''',
			"cabeza": ''' con herida externa en región parietal.''',

		},  

		
	},# 132
	{

		"nombre": "Roland Basmadji", 		
		
		"edad": "49",
		
		"ci": "8.975.727 ", 
		
		"dirección": "calle Monagas numero 24  ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1966,3,1),

		"lugarNacimiento": "Cumaná", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,12,9),

		"fechaIngresoUCI": datetime(2015,12,9),

		"resumenIngreso": '''Se trata de paciente masculino de 49 años de edad, natural y procedente de la localidad, con antecedentes de hipertensión arterial en tratamiento con benicar 40 mg OD, diabetes mellitus tipo II en tratamiento con glucobance 1 tableta BID, quien inicia enfermedad actual el día 08/11/2015 cuando presenta dolor precordial de fuerte intensidad y aparición súbita que se irradia a cuello y miembros superiores izquierdo, posteriormente se anexa al cuadro dificultad para respirar a moderados esfuerzos, por lo que acude el día 09/12/2015 a centro clínico privado(policlina sucre) constatando a la evaluación inicial cifras de tensión arterial elevadas 170/110 mmhg realizan paraclínicos evidenciando perfil isquémico positivo, por tal motivo es referido a nuestro centro asistencial donde se evalúa e ingresa por el servicio de medicina interna. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''TA: 100/70() mmHg; FC: 70pm; FR: 18rpm; SPO2: %. Se solicita valoración por el servicio de terapia intensiva, acudiendo al llamado  evaluando paciente en condiciones clínicas de cuidado, por disponibilidad de cupo se decide su ingreso en la unidad de cuidados intensivos.''',
			
			"piel" : 	'''	blanca, normotermicatérmica al tacto, se evidencia ligera palidez cutánea mucosa, llenado capilar > 3 Seg. ''',
	
			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible ruidos respiratorios presentes en ambos hemitorax sin agregados, Ruidos cardiacos rítmicos, sin soplo ni galope. ''',
			"abdomen": ''' globoso a expensa de panículo adiposo, Blando, no doloroso a la palpación, ruidos hidroaéreos presentes, no megalias''',

			"neurologico": ''' Paciente consciente. Glasgow: 15/15pts, Respuesta Motora: 6pt, Apertura Ocular: 4pt.  Respuesta Verbal: 5pt. Pupilas isocóricas reactivas a la luz.''',
			"extremidades": '''Simétricas, sin edema.''',

		}, 

		"diagnosticoIngresoUCI": [
									"Shock cardiogenico.",
									"Síndrome coronario agudo infarto  al miocardio con elevación del segmento ST en cara anteroseptal",
									"taquicardia supra ventricular.",
									"Hipertensión arterial no controlada",
									"Diabetes mellitus tipo II descompensada en hipoglicia",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se recibe paciente en camilla de traslado, recibiendo oxigeno húmedo por bigote nasal, se traslada a cama de UCI, se conecta a monitor cardíaco externo que reporta: TA: 89/56(68) mmHg; FC: 166 lpm; FR: 27rpm; SPO2: 95% Se realiza electrocardiograma evidenciando taquicardia supra ventricular con inestabilidad hemodinámica, se comunica caso con especialista de guardia doctor Guaimare quien indica cardiovertir, se administra midazolam dosis de sedación y se procede a realizar cardioversión con 100 yuls se realiza electrocardiograma post cardioversión evidenciando ritmo sinusal. Se procede a realizar catéter venoso yugular izquierda con catéter 6 FR monolumen sin complicaciones.''',
			"piel": ''' blanca, hipotermicatérmica al tacto, se evidencia ligera palidez cutánea mucosa, llenado capilar > 3 Seg. ''',
			"cardiopulmonar": '''Tórax simétrico, hipoexpansible ruidos respiratorios presentes en ambos hemitorax con agregados crepitantes bibasales, Ruidos cardiacos arrítmicos taquicardicos, sin  soplo ni galope ''',
			"abdomen": '''globoso a expensa de panículo adiposo, Blando, no doloroso a la palpación, ruidos hidroaéreos presentes, no megalias ''',
			"extremidades": '''Simétricas, sin edema.''',
			"neurologico": '''Paciente somnoliento. Glasgow: 15/15pts, Respuesta Motora: 6pt, Apertura Ocular: 4pt. Respuesta Verbal: 5pt. Pupilas isocóricas reactivas a la luz. ''',
		

		},  

		"diagnosticoIngresoHUAPA": [
								
			"Crisis hipertensiva expresada en Síndrome coronario agudo infarto al miocardio sin elevación del segmento ST cara anterior extensa.",
			"Hipertensión arterial sistémica.",
			"Diabetes mellitus tipo II",

		], 
		
	},# 133


	{
		
		"nombre": "Ray Gilbert Rodríguez  Andrade ", 		
		
		"edad": "17",
		
		"ci": "30.443.995", 
		
		"dirección": "la llanada sector 1 avenida 05 casa 06",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1938,8,31),

		"lugarNacimiento": "Cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,9,9),

		"fechaIngresoUCI": datetime(2015,9,9),

		"resumenIngreso": ''' Se trata de paciente masculino de 17 años de edad, natural y procedente de la localidad, quien inicia enfermedad actual el día 09/08/2015 cuando posterior a recibir múltiples heridas en región temporo parietal izquierda por objeto punzo penetrante es trasladado a nuestro centro asistencial donde es evaluado por el servicio de neurocirugía e ingresado.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubado recibiendo oxigeno por t de ayres,   se traslada a cama de UCI y se conecta a monitor cardíaco externo que reporta: TA: 98/76 mmHg; FC: 177 lpm; FR: 33rpm; SatO2: 99 % ''',
			
			"piel" : 	'''	morena, hipertérmica, llenado capilar < 3 segundos. Temp: 38.1ºC, se evidencia marcada palidez cutánea mucosa.''',
			"cabeza": ''' se evidencia apósito estéril que cubre herida, se evidencia edema más equimosis en ambos parpados que dificulta la apertura ocular y edema generalizada en cráneo.''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares,  con agregados tipo roncus bilaterales abundantes. Ruidos cardíacos rítmicos taquicardicos, sin soplos sin galope.''',
			"abdomen": ''' plano, se evidencia apósito que cubre herida de lavado peritoneal Rs Hs Ps, no doloroso a la palpación, no megálico. ''',

			"neurologico": ''' inconsciente, Glasgow: 4/15 ptos, Respuesta Motora: 2pts, Respuesta Verbal: 1pto, Apertura Ocular: 1pto. Pupila no evaluable por limitación en la apertura ocular debido a edema palpebral bilateral.''',
			"extremidades": '''simétricas, sin edema ''',

		}, 

		"diagnosticoIngresoUCI": [

								"Traumatismo cráneo encefálico severo complicado con:",
								"Fractura hundimiento en región temporo parietal izquierda.",
								"Edema cerebral",
								"Contusión en región parietal izquierda",
								"Trastorno Hematológico: anemia moderada, trombocitopenia",
								"Trastorno acido-base: alcalosis respiratoria descompensada + acidosis metabólica",
									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Signos Vitales: FR: 19 rpm Paciente en malas condiciones generales.''',
			"piel": ''' morena, Normotérmica al tacto, llenado capilar < 3 segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Rs Cs Rs Rs sin soplos, sin galope. ''',
			"abdomen": '''plano, Rs Hs Ps, blando depresible, no impresiona doloroso a la palpación, no megálico. ''',
			"extremidades": '''simétricas sin edema. ''',
			"neurologico": '''inconsciente, pupilas no evaluable por edema bipalpebral Glasgow: 4/15 pts RO: 1 pto RV: 1 pto RM: 2 ptos. ''',
			"cabeza": '''normocéfalo se evidencia múltiples soluciones de continuidad en cuero cabelludo en región temporo parietal izquierda.  ''',

		},  

		"diagnosticoIngresoHUAPA": [
					"traumatismo múltiples",
					"traumatismo craneal leve simple cerrado complicado con fractura hundimiento frontal.",
					"traumatismo tóraco abdominal cerrado.",

					{"resumen":''' Paciente a su ingreso se procede a realizar intubación endotraqueal y se conecta a t de ayres, permanece en el área de emergencia durante 16 horas, se le realiza en horas de la tarde tac de cráneo evidenciando fractura hundimiento de hueso temporal izquierdo con hematoma intraparenquimatoso y edema cerebral difusa, se solicita valoración por el servicio de terapia intensiva en vista de condiciones clínicas del paciente se acude al llamado valorando paciente en condiciones clínicas de cuidado en vista de disponibilidad de cupo se decide su ingreso en la unidad de cuidados intensivos.'''},

		], 
		
	}, # 134



	{
		
		"nombre": "Ramón Neptali Noguera Gamboa", 		
		
		"edad": "48",
		
		"ci": "6.952.835", 
		
		"dirección": "Guaraunos, Calle San José, Edo. Sucre",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1964,12,31),

		"lugarNacimiento": "El Pilar. Edo. Sucre.", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,5,15),

		"fechaIngresoUCI": datetime(2014,5,15),


		"resumenIngreso": ''' Paciente masculino de 48 años de edad, natural y procedente de Carúpano, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual el día 12/05/14 en horas de la noche, cuando presenta cefalea de aparición brusca y fuerte intensidad, mareos, con posterior pérdida de estado de consciencia, motivo por el cual es llevado a centro de salud de su localidad donde evalúan y solicitan TAC cerebral; dicho estudio se le realiza el día 13/05/14 y se evidencia hematoma intraparenquimatoso en región de ganglios basales derechos con drenaje a ventrículos, motivo por el cual refieren a este centro asistencial donde es evaluada e ingresado por el servicio de Neurocirugía, al momento del ingreso se encuentra inconsciente, con Glasgow de 8/15pts (RM: 4pts, RO: 2pts, RV: 2pts). En vista de estado general de la paciente, solicitan valoración por UCI, se acude a valorar paciente y previa autorización de Dra. Cortesía, por cuadro clínico antes descrito,  se decide su ingreso.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, recibiendo O2 por bigote nasal, se pasa a cama UCI, se conecta a monitor cardíaco continuo que reporta: TA: 208/149(177) mmHg;  FC: 132 lpm;  FR: 26 rpm; SatO2: 100%. En vista de cifras elevadas de TA se indica Nitropusiato de Sodio VEV por BIC a razón de 0,25µgr/Kg/min. Recibe O2 húmedo por mascarilla facial con sonda corrugada a razón de 10 LtrsX’. Previa asepsia y antisepsia, se realiza vía venosa central yugular derecha, con catéter 7Fr, bilumen, de 16cm, sifonaje positivo en ambos lúmenes, se fija a piel con Nylon 2 – 0, asepsia final y se cubre con apósitos limpios y secos, se solicita Rx AP de tórax control sin evidencia de complicaciones. ''',
			
			"piel" : 	'''	morena, normotérmica al tacto, llenado capilar < 3seg.''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, taquicárdicos, sin soplo ni galope.''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico''',

			"neurologico": ''' estuporoso, pupilas isocóricas, con tendencia a la miosis, hiporreactivas a la luz, reflejo tusígeno y corneal presentes, hemiparesia izquierda, Glasgow 9/15pts (RM: 5pts, RO: 2pts, RV: 2pto).''',

		}, 

		"diagnosticoIngresoUCI": [

						"CRISIS HIPERTENSIVA TIPO EMERGENCIA EXPRESADA EN EVC DE ETIOLOGIA HEMORRAGICA: ",
						"HEMATOMA INTRAPARENQUIMATOSO EN REGION DE GANGLIOS BASALES DERECHOS CON DRENAJE A VENTRICULOS",
						"TRASTORNO ACIDO-BASE:",
						"ALCALOSIS METABOLICA DESCOMPENSADA + HIPERMOXEMIA",

									
								],  

		
	},# 135

	{
		"IdHistoria": "47-19-29", 
		
		"nombre": "Luzmary del Carmen Segura Patiño", 		
		
		"edad": "29",
		
		"ci": "17.540.695", 
		
		"dirección": "Urbanización La llanada Barrio Universitario ",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1985,8,28),

		"lugarNacimiento": "Cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,10,4),

		"fechaIngresoUCI": datetime(2014,10,5),

		"antecedentes": '''ALERGIA NO REFIERE ''', 

		"resumenIngreso": '''Se trata de paciente femenina de 29 años de edad natural y procedente de la comunidad con antecedentes patológicos de enfermedad hipertensiva del embarazo (preeclampia) en primer embarazo. Inicia enfermedad actual cuando debido a su  segundo embarazo  (37 semanas) por eco  acude a servicio de ginecobstetricia refiriendo dolor en hipogastrio y vómitos  por lo que se decide su ingreso ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, tolerando aire ambiente, no conectada a monitor cardiaco. Se traslada a cama UCI, se conecta a monitor cardiaco que reporta: TA: 184/124 (123) mmHg FC: 92 lpm; FR: 22 rpm; SPO2: 99%''',
			
			"piel" : 	'''	Palidez cutáneo mucosa ligera, normo hídrica normotérmica.''',
		
			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes, sin agregados, ruidos cardíacos rítmicos, regulares, sin soplos.''',
			"abdomen": ''' Plano, depresible, doloroso a la palpación hipogastrio, no visceromegalia.Herida quirúrgica cubierta por apósito estéril limpia y seca.  Ruidos Hidroaéreos presentes loquios presentes abundantes sanguinolentos  ''',

			"neurologico": ''' Consciente, orientada no signos de focalización neurológica.''',
		

		}, 

		"diagnosticoIngresoUCI": [

									"TRASTORNO HIPERTENSIVO DEL EMBARAZO : ECLAMPSIA", 
									"PUERPERIO QUIRURGICO INMEDIATO DEBIDO A EMBARAZO GEMELAR",
									"ESTERILIZACION QUIRURGICA ", 
									"TRASTORNO HEMATOLOGICO ANEMIA LEVE",
									"TRASTORNO METABOLICO : HIPERGLICEMIA ",
									{"resumen":''' Se inicia tratamiento de inmediato con nitroprusiato de sodio mediante bomba de infusión continua.'''}

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 110/75 mmHg   Fr: 26 rpm   Fc: 81 lpm. ''',
			"piel": ''' normo hídrica, normotérmica, buen llene capilar''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes, sin agregados, ruidos cardíacos rítmicos, regulares, sin soplos.	''',
			"abdomen": '''Útero grávido AU 210 CM  DU 3/10   MF PRESENTES  FCF 1 140 X MIN  FCF2 142 X MIN ''',
		
			"neurologico": '''Consciente, orientada, no signos de focalización neurológica. ''',
			

		},  

		"diagnosticoIngresoHUAPA": [
				"SEGUNDA GESTA ",
				"EMBARAZO DE 37 SEMANAS POR ECO ",
				"ARO EMBARAZO GEMELAR BICORIAL BIAMNIOTICO ",
				"ANEMIA LEVE ",
				"TOXOPLASMOSIS ",
				{"resumen": ''' Paciente evaluada por servicio de obstetricia a la cual Se le realiza Cesárea segmentaria anterior sin complicaciones extrayéndose dos recién nacidos a termino  con peso adecuado para su edad gestacional, con evolución clínica favorable de la puérpera por lo que se decide subir a piso ,donde  presenta movimientos tónico clónicos generalizados que amerita la colocación de Valium y epaminizaciòn cediendo dicho cuadro se  traslada  a área de cuidados intermedios de sala de parto donde se evidencian cifras tensionales elevadas 230/140 mmHg se inicia tratamiento con sulfato de magnesio y antagonistas de los canales de calcio y se solicita evaluación por terapia intensiva ,se acude a evaluar y en vista de las condiciones ,cifras elevadas de tensión arterial se decide su ingreso '''}
				

		], 
		
	},# 136


	{
		"IdHistoria": "45-05-13", 
		
		"nombre": "MAIKOL JOSÉ MAIZ MAICAN", 		
		
		"edad": "13",
		
		"ci": "30.918.289 ", 
		
		"dirección": "SAN ANTONIO DEL GOLFO - Cachamaure, Sector las alegrías, casa sin número.",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(2002,9,14),

		"lugarNacimiento": "Cumaná - Estado Sucre.", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,11,13),

		"fechaIngresoUCI": datetime(2015,11,13),

		"resumenIngreso": '''Paciente masculino de 13 años de edad, natural de Cumaná, procedente de San Antonio del Golfo, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual el día 13/11/2015 en horas de la mañana (6:40 am) cuando posterior a  sufrir hecho vial  tipo arrollamiento por vehículo en marcha, presentando pérdida del conocimiento (no especifican el tiempo) vómitos precedidos de náuseas de contenido alimentario y en número de 4, además de movimiento tónico clónicos generalizados por lo que es trasladado al CDI de su localidad, donde indican tratamiento con Manitol al 20 % 250 cc VEV STAT, Diazepam 1 ampolla VEV STAT  y Atropina 1 ampolla VEV STAT, posteriormente es trasladado a este centro donde previa valoración, se ingresa por el servicio de Cirugía y Traumatología con los diagnósticos de: Signos Vitales: (Datos obtenidos de la Historia clínica) FR: 20 rpm  FC: 90 lpm''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' En vista del estado neurológico, se decide intubación endotraqueal previa sedación y relación con tubo endotraqueal 7,5 Fr y se conecta a ventilación mecánica con los parámetros: Modo: A/C, VC: 400, FR: 12, FiO2: 50, FL: 50, PEEP: 0. Se cateteriza vía venosa central yugular derecha con catéter monolumen 6.0 Fr, con xifonaje positivo, se realiza rayos x de tórax AP control sin complicaciones.''',
			
			"piel" : 	'''	Morena, normotérmica al tacto, turgor conservado, llenado capilar < 3 segundos, con leve palidez cutáneo. Temp: 36 ºC''',
			"cabeza": ''' Escoriaciones en hemicara izquierda, equimosis y aumento de volumen bipalpebral ipsilateral.''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, escasos roncus bilaterales; ruidos cardíacos taquicárdicos, regulares, sin soplos ni galope.''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación superficial y profunda, no megálico.''',

			"neurologico": ''' Estuporoso, Glasgow: RO: 1 pto RV: 2 ptos RM: 5 ptos 8/15 ptos, pupilas isocóricas,  normorreactivas a la luz, reflejo tusígeno presente. ''',
			"extremidades": '''simétricas, sin edema. No impresiona focalización neurológica. ''',

		}, 

		"diagnosticoIngresoUCI": [
									"POLITRAUMATIZADO.",
									"TRAUMATISMO CRANEOENCEFÁLICO MODERADO SIMPLE CERRADO. ",
									"TRAUMATISMO TORACO-ABDOMINAL CERRADO.",
									"TRAUMA FACIAL.",
									{"resumen":''' Se evalúa paciente por el servicio de Cirugía Blanda quien realiza controles hematológicos sin evidencia de descenso de cifras de hemoglobina, sin embargo al ingreso se evidencia Sonda Foley 16 Fr con balón inflado en uretra peneana, por lo que retiran y realizan lavado obteniéndose abundantes secreciones hemáticas, solicitando evaluación por UROLOGÍA, quien indica mantener vigilancia y conducta expectante en vista de que el paciente se mantiene con diuresis.  En horas de la tarde el paciente es trasladado  a centro privado para realizar TAC de cráneo la cual evidencia la presencia de contusiones hemorrágicas bi-frontales a predominio izquierdo, con edema perilesional asociado y Edema cerebral difuso, sin compromiso del sistema ventricular ni desviación de línea media. Se le notifican los hallazgos a Dr. Montaño quien indica mantener manejo médico y evaluación por Terapia Intensiva, quien acude al llamado y en vista de disponibilidad de cupo se decide su ingreso a UCI. Se recibe paciente en camilla de traslado, intubado y recibiendo O2 húmedo por mascarilla facial, se pasa a cama de UCI: TA: 103/73 mmHg, TAM: 84 mmHg, FC: 95 Lpm, FR: 11 rpm, SatO2: 100% '''},

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente en regulares condiciones generales, evaluado por Dr. Montaño Neurocirujano de Guardia quien indica Epamin 800 mg VEV STAT en 1 hora, TAC de Cráneo y Antibioticoterapia. ''',
			"piel": ''' Morena, turgente, hidratada.''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitórax, sin agregados,  ruidos cardíacos rítmicos, regulares, sin soplos. ''',
			"abdomen": '''blando, depresible, no impresiona dolor a la palpación, no megalias.''',
			"extremidades": '''dentro de límites normales.''',
			"neurologico": '''paciente bajo efectos farmacológico de diazepam (2 ampollas) y manitol al 20%. Estuporoso, sin respuesta ocular, respuesta verbal con sonidos incomprensibles, moviliza extremidades con agitación psicomotriz ocasional, normorreflexico, normotónico, Glasgow: 9/15 patos. RO: 1pto   RV: 2 RM: 6 ptos.''',
			"cabeza": ''' Normocéfalo, pupilas isocóricas reactivas a la luz, edema palpebral izquierdo.''',
			"boca":'''Salida de escasa secreción sanguinolenta.''',

		},  

		"diagnosticoIngresoHUAPA": [
									"Politraumatizado:",
									"Traumatismo Craneoencefálico Severo Simple Cerrado.",
									"Traumatismo Toraco-abdominal Cerrado.",
									"Traumatismo Facial.",
									"Traumatismo Uretral Postraumático (post-colocación de Foley)  ",
									"Trastorno acido base: ",
									"Acidosis metabólica compensada + Normoxemia. ",


		], 
		
	},# 137

	{
		"IdHistoria": "52-36-82", 
		
		"nombre": "Félix José Guevara López", 		
		
		"edad": "34",
		
		"ci": "15.112.703 ", 
		
		"dirección": "Cantarrana Villa Providencia ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1980,8,4),

		"lugarNacimiento": "Carúpano ", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,8,10),

		"fechaIngresoUCI": datetime(2014,8,10),


		"resumenIngreso": '''Se trata de paciente masculino de 34 años de edad natural de Carúpano y procedente de la localidad sin antecedentes patológicos conocidos quien inicia enfermedad actual hace aproximadamente 12 días caracterizado por dolor abdominal en región epigastrio tipo cólicos con irradiación a flanco izquierdo por lo que es hospitalizado en CDI de la localidad con diagnostico: Sx doloroso abdominal  indicándose los siguientes estudios y reportes: ECO ABDOMINAL (4-08-14): ESTEATOSIS HEPATICA, TAC ABDOMEN (5-08-14): ESPLENOMEGALIA, VIDEOENDOSCOPIA DIGESTIVA INFERIOR (07-08-14): PROCESO INFLAMATORIO INDETERMINADO DE COLON DERECHO,ESBOZOS DIVERTICULARES DE SIGMOIDES ,LESION ELEVADA DE RECTO ,HEMORROIDES INTERNAS  Posterior a la realización de último estudio el cuadro se reagudiza  refiriéndose a este centro para evaluación, se ingresa con diagnostico: ABDOMEN AGUDO QUIRURGICO: DIVERTICULITIS AGUDA  COMPLICADA  ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente en malas condiciones generales, hemodinámicamente inestable,  afebril, intubado ventilando espontáneamente, se conecta a Ventilación Mecánica con los parámetros: VC 560 FR 12 FIO2 90FL 50 PEEP 0. Signos Vitales: TA: 87/54mmHg; FC: 143pm; FR: 32rpm;  SPO2: 100Se realiza VVC yugular posterior izquierda con xifonaje positivo en los tres lúmenes, se realiza rayos x tórax control observándose la vía adecuadamente colocada.''',
			
			"piel" : 	'''normotérmica, hidratada, llenado capilar < 3''',

			"cardiopulmonar":  ''' tórax simétrico normo expansible, ruidos respiratorios disminuidos en ambos hemitorax sin agregados, ruidos cardíacos taquicárdicos, regulares, sin soplos.	''',
			"abdomen": ''' globoso depresible herida quirúrgica cubierta por apósito estéril impregnado en secreción hemática,  abdomen abierto con colocación de bolsa de Bogotá. ''',

			"neurologico": ''' Inconsciente Glasgow no evaluable por estar bajo efectos de sedantes  ''',
			

		}, 

		"diagnosticoIngresoUCI": [
									"POI LAPAROTOMIA EXPLORADORA DEBIDO A ",
									"INFARTO INTESTINAL COMPLICADO CON:",
									"SHOCK HIPOVOLEMICO",
									"HEMOPERITONEO ",
									"NECROSIS INTESTINAL ASAS DELGADAS ",
									"INSUFICIENCIA RENAL AGUDA PRERENAL ",
									"TTNO HEMATOLOGICO : ANEMIA MODERADA",
									"TTNO AB : ACIDOSIS METABOLICA DESCOMPENSADA E HIPEROXEMIA ",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente en aparentes malas  condiciones generales, afebril, eupneico. Sin Signos Vitales al ingreso Paciente que es llevada a quirófano de emergencia realizándose laparotomía media supra para  infra umbilical donde se observan : 100 cc de liquido inflamatorio libre en cavidad abdominal necrosis de asa delgada desde 60 cm hasta 180 cm de asa fija con presencia de trombos en vasos sanguíneos  sangrado en capa a nivel de raíz del mesenterio 2000 cc de hemoperitoneo , se toma como conducta drenaje de liquido resección de asa necrótica (160cm) cierre de cabos distales confección de packing hemostático con 2 compresas y bolsa de Bogotá en pared abdominal .Paciente se mantiene en malas condiciones en área de recuperación siendo evaluado por equipo de UCI y dejando sugerencias ,para el día de hoy debido a disponibilidad de cupo se decide su ingreso .  ''',
			"piel": ''' Blanca, normotérmica, hidratada, llenado capilar < 3 segundos.''',
			"cardiopulmonar": '''tórax simétrico normo expansible, sin agregados, ruidos cardíacos rítmicos, regulares, sin soplos.''',
			"abdomen": '''blando, depresible, doloroso a la palpación profunda en mesogastrio  flanco y fosa iliaca izquierda, no megalias.RHA presentes ''',
	
			"neurologico": '''consciente, somnoliento, orientado en TEP pupilas isocóricas reactivas reflejo corneal presente  ''',
		

		},  

	}, # 138


	{
		
		
		"nombre": "Miguel Angel Martínez", 		
		
		"edad": "57",
		
		
		"dirección": "Calle Arismendi casa número 26, Cumanacoa.",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1957,9,26),

		"lugarNacimiento": "Cumanacoa – Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,5,25),

		"fechaIngresoUCI": datetime(2014,5,25),

		"resumenIngreso": '''Se trata de paciente masculino con antecedentes de Hipertensión Arterial Crónica controlada con Adalat Oros, Hidroten, Concor, Coraspirina. 2 Eventos Cerebrovasculares sin secuelas. Refiere inicio de enfermedad actual el día 24/05/2014 cuando es encontrado inconsciente con pérdida de fuerza muscular en hemicuerpo derecho, por lo que es llevado a centro asistencial de la localidad donde evidencian cifras tensionales elevadas (220/110mmHg) por lo que colocan nifedipina sublingual y furosemida, posteriormente refieren a este centro hospitalario donde se evalúa y se decide su ingreso. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' En vista de estado neurológico del paciente se decide realizar intubación endotraqueal, se coloca tubo número 7 y se conecta a ventilación mecánica.''',
			
			"piel" : 	'''	Morena, normotérmica, turgor disminuido, llenado capilar < 3 segundos.''',

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes, se auscultan roncus bilaterales. Ruidos cardiacos arrítmicos normofonéticos, no soplos.''',
			"abdomen": ''' Globoso por panículo adiposo, blando depresible, no doloroso a la palpación, Rs Hs presentes sin megalias. ''',

			"neurologico": ''' Inconsciente, Glasgow: 7/15pts, Respuesta Motora: 5pts (limitado a hemicuerpo izquierdo), Respuesta Verbal: 1pt, Apertura Ocular: 1pt, pupilas isocóricas, normorreactivas a la luz.  ''',

		}, 

		"diagnosticoIngresoUCI": [
									"Emergencia Hipertensiva expresada en EVC",
									"Infección Respiratoria Baja: Neumonía por Broncoaspiración",
									"Fibrilación Auricular con respuesta ventricular variable",
									"Hipertensión Arterial Sistémica",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente evaluado en camilla de hospitalización, hemodinámicamente inestable, se conecta a monitor cardíaco externo que reporta: TA: 200/80mmHg	FC: 69lpm	FR: 16rpm	SPO2: 95%''',
			"piel": ''' Morena, normotérmica, turgor disminuido, llenado capilar < 3 segundos.''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes, S/A. Ruidos cardiacos rítmicos normofonéticos, no soplos ''',
			"abdomen": '''Globoso por panículo adiposo, blando depresible, no doloroso a la palpación, Rs Hs presentes sin megalias. ''',
			
			"neurologico": '''Inconsciente, Glasgow: 8/15pts, Respuesta Motora: 6pts, Respuesta Verbal: 1pt, Apertura Ocular: 1pt, pupilas isocóricas, normorreactivas a la luz. ''',

		},  

		"diagnosticoIngresoHUAPA": [
								"Emergencia Hipertensiva expresada en EVC",
								"Infección Respiratoria Baja: Neumonía por Broncoaspiración",
								"Fibrilación Auricular con respuesta ventricular variable",
								"Hipertensión Arterial Sistémica",
								{"resumen":''' En vista de condiciones clínicas del paciente, se solicita valoración por el Servicio de UCI quien en vista de disponibilidad de cupo se decide su ingreso.  Se recibe paciente en camilla de traslado, en regulares condiciones generales, ventilando espontáneamente, se conecta a monitor cardíaco externo que reporta: Signos Vitales: TA: 200/80mmHg	FC: 69lpm	FR: 16rpm	SPO2: 95%'''},


		], 
		
	},# 139

	{
		"IdHistoria": "14-91-36", 
		
		"nombre": "Rosa Elena Vallejo", 		
		
		"edad": "51",
		
		"ci": "9.285.295 ", 
		
		"dirección": "La llanada",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1964,2,1),

		"lugarNacimiento": "Maturín ", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,7,7),

		"fechaIngresoUCI": datetime(2015,8,12),

		"resumenIngreso": '''Se trata de paciente femenina de 51 años de edad con antecedentes de ingreso hace   8 meses con diagnóstico de Síndrome ictérico obstructivo debido a TU de cabeza de páncreas evidenciado en estudio tomografico que amerito la colocación de STENT biliar, inicia enfermedad actual el día 03/ 07/ 2015 caracterizado por la presencia de tinte ictérico en piel y mucosas, dolor abdominal difuso concomitantemente aumento de temperatura corporal  cuantificada de  40 grados motivo por lo cual acude a este centro donde se  ingresa  ''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''  Paciente es trasladado en camilla de transporte intubada recibiendo oxigeno húmedo mediante mascarilla autoinsuflable; se traslada a cama UCI, conectándose a ventilador mecánico EVITA 4 MODO AC FL 50 FIO2 50 VC 480 PEEP 0 y a  monitor cardiaco externo que reporta signos vitales:  TA: 50/26 mmHg   FC: 123; lpm; FR: 15 rpm; SPO2: 90   %Se realiza reposición hídrica con solución salina fisiológica sin lograr metas de TAM por lo que se inicia vasoactivos, infusión de Norepinefrina  a 21 mcg min ''',
			
			"piel" : 	'''	Tinte ictérico de piel mucosas y escleras llenado capilar menos de 3 seg ''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares con  agregados roncus aislados  Ruidos cardiacos rítmicos taquicardicos no soplos.''',
			"abdomen": ''' globoso blando depresible  doloroso a la palpación en banda a predominio de hipocondrio derecho, vesícula no palpable sin signos de irritación peritoneal, se palpa masa epigástrica de 6 cm, hepatomegalia de 4 cm por debajo del reborde costal  ''',

			"neurologico": ''' Inconsciente Glasgow no evaluable debido a sedación farmacológica  ''',
			"extremidades": '''eutróficas, simétrica sin edema''',

		}, 

		"diagnosticoIngresoUCI": [
									"SHOCK SEPTICO ",
									"SEPSIS PUNTO PARTIDA BILIAR ",
									"COLANGITIS AGUDA.",
									"ICTERICIA OBSTRUCTIVA POT TU CABEZA DE PANCREAS Y COLESISTOPATIA LITIASICA.",
									"TROMBOEMBOLISMO PULMONAR.",
									"INSUFICIENCIA RENAL AGUDA TIPO RENAL. ",
									"POT CPRE Y COLOCACCION DE STENT BILIAR.",
									"TRASTORNO HEMATOLOGICO ANEMIA LEVE.",
									"TRASTORNO ACIDO BASE ALCALOSIS MIXTA.",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Signos vitales de ingreso no colocados en historia  ''',
			"piel": '''Tinte ictérico de piel mucosas y escleras llenado capilar menos de 3 seg ''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares sin agregados Ruidos cardiacos rítmicos no soplos.''',
			"abdomen": '''globoso blando depresible  dolorosos a la palpación en banda a predominio de hipocondrio derecho, vesícula no palpable sin signos de irritación peritoneal, se palpa masa epigástrica de 6 cm, hepatomegalia de 4 cm por debajo del reborde costal ''',
			"extremidades": '''eutróficas, simétrica sin edema''',
			"neurologico": '''Consciente orientada en tres planos Glasgow 15/ 15 puntos, sin focalización neurológica. ''',
		

		},  

		"diagnosticoIngresoHUAPA": [
						"COLANGITIS AGUDA",
						"ICTERICIA OBSTRUCTIVA POT TU CABEZA DE PANCREAS",
						"COLESISTOPATIA LITIASICA ",
						{"resumen":''' Paciente que permanece hospitalizada siendo evaluada por servicio de  cirugía realizándose diferentes estudios y procedimientos los cuales describimos ,el día  06/07/15 se realiza Evaluación cardiovascular la cual reporta : No existencia de  evidencia de cardiopatías ASA III GOLDMAN MODERADO el  día 08/07/15 se realiza  Eco abdominal reportándose  coledococistopatia litiasica obstructiva,  13/07/15 se realiza otro   Eco abdominal reportando  coledocolitiasis obstructiva, colecistopatía litiasica, para el día  15/07/15 es llevada  a quirófano  realizándose CPRE la cual reporta  Colangitis, dilatación de vías biliares intra y extra hepáticas,coledocolitiasis por lo que se coloca STENT biliar plástico sin complicaciones. Paciente que presenta hemorragia digestiva superior posterior a colocación del STENT  por lo que se realiza endoscopia digestiva superior el día 20 reportando estudio sin alteraciones  sin eventos que justifican el sangrado ,permanece el descenso de hemoglobina por lo que se realiza colonoscopia observándose STENT biliar en transverso extrayéndose el mismo ,no se evidencia sangrado ,la paciente se mantiene en malas condiciones ,con descenso progresivo de hemoglobina y ascenso de azoados ameritando valoración por nefrología ,para el día 09/08/15 luego de la colocación de albumina humana presenta episodio de disnea acompañada de crepitantes bibasales por lo que es valorada por UCI y se sugiere traslado área de emergencia donde se mantiene hasta el día de hoy 12/08/15 que presenta episodio de disnea severa ,desaturación ,cianosis ,por lo que se decide intubación endotraqueal conectándose a ventilación mecánica con parámetros establecidos ,por disponibilidad de cupo se decide su ingreso a UCI '''}
		

		], 
		
	},# 140

	{
		"IdHistoria": "53-93-80", 
		
		"nombre": "Rosa María Rosa de León ", 		
		
		"edad": "69",
		
		"ci": "2.833.876", 
		
		"dirección": "margarita sector san griego calle principal ",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1946,1,19),

		"lugarNacimiento": "", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,10,28),

		"fechaIngresoUCI": datetime(2015,11,4),

		"resumenIngreso": '''Se trata de paciente femenina de 69 años de edad natural y procedente de Margarita  con antecedentes de Hipertensión Arterial  en tratamiento con Nifedipino 30 mg, olmersartan 40 mg, hidroclorotiazida 12.5 mg, diabetes mellitus tipo II en tratamiento con metformina 500 mg, antecedentes de sincopes durante el año 2015 en 4 oportunidades, quién refiere inicio de enfermedad actual el día 28/10/2015 cuando presenta perdida del estado de conciencia de manera súbita sin relajación de esfínter  durante aproximadamente 3 minutos con recuperación espontanea de la misma por lo cual es trasladado a nuestro asistencial donde es evaluado por el servicio de medicina interna constatando cifras tensionales elevadas 180/100 mmhg, por tal motivo deciden su ingreso. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en silla de ruedas se conectada  a monitor cardiaco, tolerando aire ambiente, se traslada a cama de UCI SIGNOS VITALES: FC: 59 LPM, TA:153/53(88) mmhg, FR:23, SAT O2 100% ''',
			
			"piel" : 	'''	Normotérmica, hidratada, llenado capilar <3segundos ''',
			
			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax sin agregados.  Ruidos cardíacos rítmicos, bradicardico,  no se auscultan soplos. ''',
			"abdomen": ''' Blando, no doloroso a la palpación superficial y  profunda en epigastrio , no visceromegalias ''',

			"neurologico": ''' consciente, orientada en tiempo espacio y persona, Glasgow 15/15 pts   ''',
		

		}, 

		"diagnosticoIngresoUCI": [
									"crisis hipertensiva tipo urgencia",
									"cardiopatía isquémica crónica (isquemia subepicardica anterior extensa)",
									"hipertensión arterial sistémica",
									"diabetes mellitus tipo II ",

								],  

		"examenFisicoIngresoHUAPA": {
	
			"piel": ''' Normotérmica, normo hidratada, llenado capilar <3segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios en ambos campos pulmonares sin agregado.  Ruidos cardíacos rítmicos, bradicardicos,  no se auscultan soplos. ''',
			"abdomen": '''Blando, no   doloroso a la palpación superficial y  profunda, no visceromegalia ''',
			
			"neurologico": '''Glasgow 15/15  lenguaje coherente orientada en tiempo espacio y persona.''',

		},  

		"diagnosticoIngresPrivado": [
								

								"Crisis hipertensiva tipo emergencia expresada en EVC en evolución",
								"Cardiopatía isquémica crónica",
								"Hipertensión arterial sistémica ",
								"Diabetes mellitus tipo II",
								{"resumen":''' La paciente es trasladada a estudio tomografico posteriormente se comunica caso a Neurólogo Dr. aponte quien en vista de imágenes sin alteraciones plantea diagnóstico de sincope vaso vagal vs crisis convulsiva, por lo que sugiere tratamiento con carbamazepina.es trasladada a área d observación en vista de condiciones clínicas estables. Se presenta resultados de holter cardiaco realizado previo ingreso que reporta bradicardia sinusal, es valorada por neurocirujano Dr. Acevedo el día 29/10/2015, quien indica realizar resonancia magnética con doble contraste, y evaluación por el servicio de cardiología el cual acude al llamado realizando reajustes en tratamiento antipertensivo, el día 30/11/2015 se realiza ecocardiograma .que reporta, anormalidad regional de la contracción del ventrículo izquierdo, fracción de eyección 55%, dilatación leve de la aurícula izquierda, disfunción diastólica grado I , lesión isquémica sub epicardica anterior extensa, hipocinesia ínfero posterior. En vista de persistir con cifras de tensión arterial elevadas se realiza ajuste de tratamiento antipertensivo en múltiples oportunidades, en vista de persistir hipertensa se decide trasladar a unidad de cuidados intensivos para monitoreo cardiaco continuo.'''}
		], 
		
	},#141

	{
		"IdHistoria": "49–42–35 ", 
		
		"nombre": "Nery Teresa Palomo", 		
		
		"edad": "73",
		
		"ci": "8.428.783", 
		
		"dirección": "Urb. Brasil, sector 3, vereda 4, casa #2, Cumaná, Edo. Sucre.",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1941,10,16),

		"lugarNacimiento": "Cumanacoa, Edo. Sucre.", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,8,17),

		"fechaIngresoUCI": datetime(2014,8,25),

		"resumenIngreso": '''Paciente femenina de 73 años de edad, natural de Cumanacoa y procedente de la localidad, con antecedentes patológicos de HTA sistémica controlada con Atacand® 16mg, Zanidip® 10mg y Coraspirina® 81mg, con ERC estadío V en diálisis peritoneal, cuyo familiar refiere inicio de enfermedad actual el día 17/08/14 en horas de la mañana, cuando presenta de manera súbita pérdida del estado de consciencia sin recuperación espontánea de la misma, motivo por el cual es llevado a CDI y refieren a éste centro asistencial donde se valora y es ingresado por el servicio de Medicina Interna. Al momento del ingreso al HUAPA presenta tórax simétrico, hipoexpansible, con crepitantes en base pulmonar derecha, deterioro neurológico caracterizado por somnolencia, desorientación, pupilas isocóricas, normorreactivas a la luz y Glasgow de 10/15pts (no discriminado), realizan paraclínicos y evidencian hipoglicemia severa. La paciente se mantienen en el servicio de choque y realiza hipoglicemias severas recurrentes, por lo que se indica infusión continua de solución dextrosa al 10% para 24 horas. El día 19/08/14 presenta mayor deterioro neurológico a pesar de cifras de glicemia de 188mg/dl y trabajo respiratorio, motivo por el cual realizan intubación endotraqueal y se conecta a ventilación mecánica. Se mantiene en el área de choque y en vista de estado general de la paciente, solicitan valoración por UCI quien acude en varias oportunidades a evaluar la paciente y el día de hoy 25/08/14, en vista de estado general del paciente y disponibilidad de cupo, previa autorización de Dra. Cortesía  decide su ingreso.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubada y recibiendo O2 por Ambú®, se pasa a cama UCI, se conecta a ventilación mecánica modo A/C, Vc: 600, FR: 12, FiO2: 90, Fl: 50, PEEP: 0 y se conecta a monitor cardíaco continuo que reporta: TA: 150/73(123) mmHg;  FC: 120 lpm; FR: 27 rpm; SatO2: 100%''',
			
			"piel" : 	'''	morena, normotérmica al tacto, llenado capilar < 3seg.''',
		
			"cardiopulmonar":  ''' tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, se auscultan crepitantes finos bibasales y sibilantes dispersos. Ruidos cardíacos arrítmicos y irregulares, taquicárdicos, sin soplo ni galope.''',
			"abdomen": ''' globoso a expensas de panículo adiposo, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico, se evidencia dren para diálisis peritoneal en flanco izquierdo limpio y seco.''',

			"neurologico": ''' estuporosa, pupilas isocóricas, normorreactivas a la luz, reflejo tusígeno y corneal presentes, Glasgow 9/15pts (RM: 4pts, RO: 4pts, RV: 1pto limitado por TET). ''',
			"extremidades": '''edema III/IV.''',

		}, 

		"diagnosticoIngresoUCI": [
									"EVC DE ETIOLOGIA A PRECISAR",
									"ENFERMEDAD RENAL CRONICA ESTADIO V EN DIALISIS PERITONEAL",
									"HTA SISTEMICA",
									"TRASTORNO METABOLICO:",
									"HIPOGLICEMIA",
									"TRASTORNO HEMATOLOGICO:",
									"ANEMIA MODERADA",
									"PROLONGACION DE PTT",
									"TRASTORNO HIDOELECTROLITICO:",
									"HIPONATREMIA",
									"HIPOKALEMIA",
									"TRASTORNO ACIDO-BASE:",
									"ACIDOSIS METABOLICA COMPENSADA CON ALCALOSIS RESPIRATORIA MAS HIPEROXEMIA",

								],  
		
	},#142

	{
		
		"nombre": "Moises Guevara", 		
		
		"edad": "15",
	
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1999,5,5),

		"lugarNacimiento": "cumanacoa", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,2,26),

		"fechaIngresoUCI": datetime(2014,2,26),


		"resumenIngreso": '''Se trata de paciente masculino de 15  años de edad natural de y procedente de cumanacoa sin antecedente patológicos de importancia, quien inicia enfermedad actual el día 26/2/2014 cuando posterior a contacto directo con llamas (no precisan tiempo de exposición) presenta lesiones en piel de tipo quemaduras de 3er grado, en cara, parte anterior del tronco, extremidades inferiores y superiores y genitales; así como dificultad para respirar e impotencia funcional, motivo por el cual es llevado a ambulatorio de la localidad donde es evaluado y referido a este centro asistencial donde se ingresa.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe  paciente en camilla de traslado intubado recibiendo oxigeno por ambu , se traslada  a cama UCI y se conecta monitor cardiaco continuo que reporta  signos vitales:  FC: 115  lpm   FR 22 rpm  TA128/86 mmHg ) mmHg    SATO2: 65%.''',
			
			"piel" : 	'''	morena, cubierta por gasas impregnadas en protosulfil, presencia de lesiones de quemaduras de 3er grado en parte anterior del tronco, cara, extremidades superiores e inferiores y genitales . ''',
			"cardiopulmonar":  ''' Tórax simétrico, expansible, ruidos respiratorios presentes MV conservado, sin agregados. Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos ni galope. ''',
			"abdomen": ''' plano , blando, no doloroso a la palpación, no megalias   ''',

			"neurologico": ''' consciente, pupilas isocóricas reactivas a la luz, glasgow RO: 4pto, RV: 5pto, RM: 6 ptos 15 /15 puntos reflejos conservados  ''',
		
		}, 

		"diagnosticoIngresoUCI": [
									"QUEMADURA DE 3er GRADO CON 80% DE SCQ.",
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' FC: 115lpm FR 22 rpm TA100/60 mmHg )mmHg ''',
			"piel": '''morena, presencia de lesiones de quemaduras de 3er grado en parte anterior del tronco, cara, extremidades superiores e inferiores y genitales . ''',
			"cardiopulmonar": '''Tórax simétrico, expansible, ruidos respiratorios presentes MV conservado, sin agregados. Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos ni galope.''',
			"abdomen": '''plano , blando, no doloroso a la palpación, no megalias ''',

			"neurologico": '''consciente, pupilas isocóricas reactivas a la luz, glasgow RO: 4pto, RV: 5pto, RM: 6 ptos 15 /15 puntos reflejos conservados  ''',
		

		},  

		"diagnosticoIngresoHUAPA": [
						"Quemaduras de 3er grado con 80 '%'' de SCQ",
						{"resumen":''' El paciente es evaluado por UCI en área de emergencia, donde se coloca vía femoral con catéter trilumen 7fr sin complicaciones y se procede a intubación endotraqueal con tubo 7 sin complicaciones y se conecta a T de Ayres, para posteriormente ingreso a UCI '''}


		], 
		
	},#143


	{
		
		
		"nombre": "Misleidy Chacon ", 		
		
		"edad": "12",
		
		"ci": "29.855.241", 
		
		"dirección": "Santa Fé",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(2002,1,22),

		"lugarNacimiento": "Santa Fé", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,12,7),

		"fechaIngresoUCI": datetime(2014,12,7),

		"resumenIngreso": ''' Se trata de paciente masculino de 12 años de edad, sin antecedentes patológicos conocidos, quien inicia enfermedad actual el día 07/12/2014 cuando posterior a accidente de tránsito tipo colisión (moto-camión) presenta escoriaciones y deterioro del nivel de consciencia, motivos por los cuales es trasladada a este centro hospitalario donde es ingresada con el diagnóstico de Traumatismo Craneoencéfalico Severo y en vista de estado neurológico deciden solicitar valoración por Servicio de Terapia Intensiva, acudiendo a valorar paciente en malas condiciones generales, con deterioro neurológico por lo que se decide ingresar al Servicio en vista de disponibilidad de cupo. ''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' SIGNOS VITALES: TA: 94/37mmHg, FC:115lpm, FR: 12rpm, SPO2: 99%. La paciente es valorada por el Neurocirujano de Guardia quien indica realizar TAC de Cráneo control para posteriormente decidir conducta. En vista de que la paciente al examen físico se evidencia abdomen duro, poco depresible, se solicita valoración por Servicio de Cirugía quienes realizan Ecosonograma Abdominal donde no se evidencian colecciones, en vista de edad de la paciente se plantea caso a Residente de Pediatría quien solicita valoración por Cirugía Pediátrica.  En vista de que por error de información por parte de los familiares con respecto a la edad de la paciente se presenta el caso a Servicio de Pediatria y Terapia Intensiva Pediátrica quien en vista de disponibilidad de cupo decide su ingreso y  traslado a Servicio de Terapia Intensiva Pediátrica para continuar manejo.''',
			
			"piel" : 	'''	Morena, normotérmica, turgor conservado, con herida en región maxilar.''',

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes, sin agregados, ruidos cardíacos, rítmicos, sin soplos''',
			"abdomen": ''' plano, blando, depresible, no doloroso a la palpación, sin megalias.''',

			"neurologico": ''' Inconsciente, Glasgow: 5/15pts, Respuesta Motora: 2pts, Respuesta Verbal: 2pts, Apertura Ocular: 1 pt. Pupilas anisocóricas, (pupila derecha con tendencia a la midriasis) reactivas a la luz.''',
		
		}, 

		

		"examenFisicoIngresoHUAPA": {
			
			"piel": ''' Morena, normotérmica, turgor conservado, con herida en región maxilar''',
			"cardiopulmonar": '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes, sin agregados, ruidos cardíacos, rítmicos, sin soplos.''',
			"abdomen": '''plano, blando, depresible, impresiona doloroso a la palpación, sin megalias. ''',
			
			"neurologico": '''Inconsciente, Glasgow: 7/15pts, Respuesta Motora: 4pts, Respuesta Verbal: 1pt, Apertura Ocular: 2 pts. Pupilas anisocóricas, (pupila derecha con tendencia a la midriasis) reactivas a la luz. ''',

		},  

		"diagnosticoIngresoHUAPA": [
								
			"Traumatismo Craneoencéfalico Severo.",
			"Trastorno Hematológico: Anemia Moderada.",
			{"resumen":''' Se recibe paciente en cama de traslado, en malas condiciones generales, se traslada a cama de UCI, se realiza intubación endotraqueal colocándole tubo número 6.5french y se conecta a ventilación mecánica. '''}

		],
		
	},#144

	{

		
		"nombre": "Mirian Lucich", 		
		
		"edad": "33",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1981,2,3),
			 		
		"fechaIngresoHUAPA":  datetime(2014,8,25),

		"fechaIngresoUCI": datetime(2014,8,25),

		"antecedentes": '''Diabetes Mellitus tratada con Insulina (Novorapid) 10 unidades y Levemir: 20unidades.  Hipotiroidismo en tratamiento con Euthyrox: 50mgOD.''', 

		"resumenIngreso": ''' Paciente femenina de 33 años de edad, natural y procedente de la localidad, con antecedentes de pancreatitis aguda hace 4 años y ooferectomía parcial bilateral por teratoma, cuyo familiar refiere inicio de enfermedad actual el día 22/08/14, cuando presenta de manera súbita dolor en epigastrio, de fuerte intensidad, continuo, irradiado a región dorsal, motivo por el cual es llevada a centro asistencial en Pto. La Cruz donde interpretan como pancreatitis aguda, indican tratamiento médico y egresan. El mismo día en horas de la noche, presenta pérdida del estado de consciencia sin recuperación espontánea de la misma, es trasladad a centro privado donde ingresa con cianosis peribucal y acrocianosis, además de TA: 80/40 mmHg, taquicardia, palidez cutáneo-mucosa y diaforesis, motivo por el cual es ingresada en la UCI de dicho centro asistencial, se le realiza ECO abdominal evidenciando líquido libre en cavidad abdominal, es valorada por cirujano de guardia y es llevada a mesa operatoria donde realizan laparotomía exploratoria con hallazgo de embarazo ectópico roto y 2000cc de hemoperitoneo, tomando como conducta salpingorrafia y ooferectomía, lavado de cavidad abdominal, control  de hemostasia y cierre por planos; se mantiene en la UCI y el día 24/08/14 presenta nueva descompensación, con signos de hipovolemia, por lo que es llevada nuevamente a mesa operatoria y se le realiza Relaparotomía con hallazgo de orificio y vaso sangrante en trompa uterina y sangrado esplénico con aproximadamente 1000cc de hemoperitoneo, toman como conducta rafia de lesión en trompa uterina, esplenectomía, lavado de cavidad con solución 0,9%, comprobación de hemostasia y cierre por planos, dejando dren rígido conectado a Hemovac, la paciente egresa de quirófano inestable hemodinámicamente, ameritando administración de Vasoactivos a altas dosis. Además por estado de hipovolemia severa presenta insuficiencia renal aguda que amerita hemodiálisis. El día de hoy 25/08/14, en vista de condiciones generales de la paciente y por trámites administrativos, por disponibilidad de cupo y previa autorización de Dra. Roa, se decide su ingreso a la UCI de este centro asistencial y dicta órdenes médicas.  Se recibe paciente en camilla de traslado, intubada y conectada a ventilador de transporte, recibiendo Levophed® a razón de 89,6 mcg/min e infusión de adrenalina, con sonda nasogástrica conectada a bolsa colectora evidenciándose gasto hemático, se pasa a cama UCI, se conecta a ventilación mecánica modo A/C, Vc: 560, FR: 12, FiO2: 70, Fl: 50, PEEP: 0 y se conecta a monitor cardíaco continuo que reporta: TA: 128/67(92) mmHg; FC: 153 lpm; FR: 12 rpm; SatO2: 95%. ''', 


		"examenFisicoIngresoUCI": {
			
			"piel" : 	'''	blanca, moderada palidez cutáneo-mucosa, hipotérmica al tacto, con acrocianosis, llenado capilar < 3seg.''',

			"cardiopulmonar":  ''' tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, taquicárdicos, sin soplo ni galope.''',
			"abdomen": ''' globoso a expensas de panículo adiposo, ruidos hidroaéreos disminuidos, blando, depresible, no impresiona doloroso a la palpación, no megálico, se evidencia dren rígido en fosa ilíaca izquierda conectado a Hemovac con moderado gasto serohemático.''',

			"neurologico": '''inconsciente, pupilas isocóricas, midriáticas, arreactivas a la luz, reflejo tusígeno y corneal ausentes, Glasgow 3/15pts (RM: 1pt0, RO: 1pts, RV: 1pto limitado por TET).''',
		}, 

		"diagnosticoIngresoUCI": [
									"POST-OPERATORIO MEDIATO DE LAPAROTOMIA EXPLORATORIA POR EMBARAZO ECTOPICO ROTO",
									"POST-OPERATORIO MEDIATO DE RELAPAROTOMIA EXPLORATORIA POR COLECCIÓN INTRAABDOMINAL",
									"SHOCK HIPOVOLEMICO",
									"INSUFICIENCIA RENAL AGUDA EN HEMODIALISIS",
									"HEMORRAGIA DIGESTIVA SUPERIOR",
									"TRASTORNO HEMATOLOGICO:",
									"TROMBOCITOPENIA",
									"TRASTORNO ACIDO-BASE:",
									"ACIDOSIS METABOLICA DESCOMPENSADA CON ALCALOSIS RESPIRATORIA MAS NORMOXEMIA",

								],  
	},#145

	{
		"IdHistoria": "51-86-41", 
		
		"nombre": "LUISA DEL VALLE CAMINO", 		
		
		"edad": "54",
		
		"ci": "5.695.696 ", 
		
		"dirección": "CUMANA",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1959,9,19),

		"lugarNacimiento": "CUMANA", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,4,21),

		"fechaIngresoUCI": datetime(2015,4,21),

		"antecedentes": '''Hipertiroisismo en tto medico con euthirox 50 mg od''', 

		"resumenIngreso": '''Se trata de paciente femenina de 54 años de edad natural de CUMANA con antecedentes de Hipertiroisismo en tto medico con euthirox 50 mg od .Inicia enfermedad actual el dia 21 del presente carcterizado por dolor cervical intenso ,tipo contractura leve que no mejora con automedicación ,luego de 48 horas presenta rigidez de musculos maseteros y miembros superiores por lo que es llevada a centro privado de la localidad y hospitalizada por traumatología ,debido a la presencia de trismo xialorrea disfagia ,insuficiencia respiratoria es evaluada por intensivista de guardia quien realiza intubación endotraqueal y coneccion a ventilación mecanica con parámetros establecidos en unidad de cuidados intensivos. Paciente que es tratada con antitoxina tetánica toxoide tetánico ,y por razones socioeconómicas se decide traslado a unidad de cuidados intensivos HUAPA ''', 
	
		"diagnosticoIngresoUCI": [

								"TETANOS GRAVE  ",
								"INSUFICIENCIA RESPIRATORIA AGUDA RESUELTA ",
								"IRB NEUMONIA POR BRONCOASPIRACION",
								"HTA CRONICA ",
								"HIPERTIROIDISMO ",
								{"resumen":''' La paciente se mantiene hospitalizada en el servicio de UCI con evolución satisfactoria, requiriendo de colchón antiescara. Informe que se expide a solicitud de la parte interesada en Cumana a los 16/05/2014.v  '''}

												
								],  
		
	},# 146

	{
		
		"nombre": "luisa Carmen Negrin de Sosa", 		
		
		"edad": "77",
		
		"ci": "8.424.753 ", 
		
		"dirección": "barrio bolívar nº 26   3 era calle. ",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1938,4,14),

		"lugarNacimiento": "Cumana Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,6,26),

		"fechaIngresoUCI": datetime(2015,6,26),

		"resumenIngreso": ''' Se trata de paciente femenina de 77 años de edad, natural y procedente de la localidad, con antecedentes de hipertensión arterial en tratamiento con losartan 50mg, pancitopenia en estudio (es espera de aspirado de medula ósea), quien refiere inicio de enfermedad actual 2 meses aproximadamente, cuando presenta debilidad generalizada, tos seca que posteriormente evoluciona  a productiva, aumento de la temperatura corporal cuantificada en 39 ºC intermitente, atenuada con acetaminofén, por lo cual acude en múltiples oportunidades a ambulatorios de la localidad donde tratan con tratamiento sintomático, para el día 9/06/2015 en vista de persistir sintomática es trasladado a centro clínico  privado donde ingresan con el diagnostico de infección respiratoria baja, permaneciendo ingresada durante 4 dias, egresando el día 13/06/2015 por mejoría clínica, anexándose posteriormente dificultad respiratoria a moderados esfuerzos persistiendo con debilidad generalizada y reaparición de cuadro febril y evacuaciones liquidas en multiples oportunidades, por lo que es reingresada el día 19/06/2015 constatando persistencia de cuadro infeccioso respiratorio por clínica y evidenciando en RX de tórax infiltrado basal derecho compatible con proceso neumónico, indicando tratamiento médico a base de (tazopril, aztreonam), además se evidencia retención de azoados por lo que se anexa a los diagnósticos insuficiencia renal, y se constata uro análisis patológico, paciente presenta evolución clínica tórpida, requiriendo la rotación de antibióticos a (zyvox y Dalacin), en vista de condiciones socioeconómicas de paciente, es trasladada a nuestro centro asistencial donde por disponibilidad de cupo y condiciones clínicas de cuidado del paciente se decide su ingreso en la unidad de cuidados intensivos.''', 

		"diagnosticoEgreso": [

			"Infección respiratoria baja",
			"Síndrome diarreico febril",
			"Infección urinaria severa",
			"Insuficiencia renal",
			"sepsis",

		],

		"diagnosticoIngresoUCI": [
									"Infección respiratoria baja neumonía bilateral ",
									"Insuficiencia renal crónica reagudizada ",
									"Infección del tracto urinario",
									"Trastorno hematológico: anemia moderada, trombocitopenia.",
									"Trastorno hidroelectrolítico: hipocalemia",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se recibe paciente respirando aire ambiente, se traslada a camilla de uci y se conecta a monitor cardiaco externo que reporta: TA: 164 /113 (138) mmHg FC: 103 lpm FR: 22 rpm SPO2:90% ''',
			"piel": ''' blanca,  Hidratada, Normotérmica al tacto, llenado capilar <3 segundos se evidencia ligera palidez cutáneo mucosa.''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible ruidos respiratorios presentes en ambos hemitorax con agregados roncus bilaterales y crepitantes en base pulmonar derecha.  Ruidos cardiacos normofonéticos rítmicos  no soplos. ''',
			"abdomen": '''globoso a expensa de panículo adiposo,  Blando depresible no doloroso a la palpación superficial ni profunda no megalias''',
			
			"neurologico": '''Paciente somnolienta, pupilas isocóricas normorreactivas a la luz, Glasgow 12/15 RM 6 pts RO 4 pts RV 2 pts. ''',
			

		},  

	},# 147

	{
		"IdHistoria": "27-54-94", 
		
		"nombre": "Irma Leonice de balbas  ", 		
		
		"edad": "76",
		
		"ci": "2.293.191 ", 
		
		"dirección": "Brasil A.V principal sector I nº 5  ",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1938,12,20),

		"lugarNacimiento": "Cumaná ", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,2,8),

		"fechaIngresoUCI": datetime(2015,2,9),


		"resumenIngreso": ''' Paciente femenino  de 79 años de edad natural y procedente de la localidad con antecedentes patológicos de hipertensión arterial sistémica en tratamiento con losartan potásico 50 mg OD, quien inicia enfermedad actual el día miércoles 4/2/15 en horas de la tarde cuando presenta dolor abdominal difuso de fuerte intensidad a predominio de epigastrio, distensión abdominal, concomitantemente vómitos.  Motivo por el cual acude a centro privado donde realizan paraclínicos reportando niveles de amilasas en 3000 mg/dl por lo que es valorado por Intensivista y Cirujano de guardia decidiendo su ingreso en UCI con diagnósticos:  Pancreatitis Aguda.  Cólico Biliar Persistente. Litiasis Biliar. Permaneciendo por 72 horas en dicha unidad de cuidados intensivos recibiendo tratamiento con Imipenem y Metronidazol, el día 7/02/2015 se realiza ecosonograma abdominal que reporta vesícula con múltiples litiasis en su interior además páncreas de bordes irregulares, mal definido, apreciándose colección peri pancreática. En vista de condiciones socioeconómicas del paciente se decide referir a nuestro centro asistencial el día 8/02/2015. Es evaluado por el servicio de medicina e ingresada con diagnósticos de: Pancreatitis Aguda de origen Biliar. Ascitis. Colecistitis Litiasica. Tromboembolismo pulmonar. Infección respiratoria baja: Neumonía Basal Izquierda Complicada con Derrame Pleural. Insuficiencia Renal Aguda . Hipertensión Arterial controlada''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, recibiendo oxígeno por mascarilla facial, se traslada a cama de UCI, se conecta a monitor cardíaco externo que reporta: TA: 63/42mmhg, FC: 113lpm, FR:12 rpm, SPO2:65%. Paciente que persiste hipoxemica, lo cual se constata por gases arteriales, se realiza intubación endotraqueal, evolucionando a la bradicardia progresando a la asistolia se realizan maniobras de  RCP básica y avanzada, evolucionando de forma satisfactoria  recuperando frecuencia cardiaca a ritmo sinusal, persistiendo hipotensa requiriendo la reposición de líquido con solución ringer hasta 1000cc evidenciando cifras de TA:110/73 (92)mmhg.''',
			
			"piel" : 	'''Morena, normotermica al tacto se evidencia moderada palidez cutáneo mucosa,  mucosa oral seca  llenado capilar >3seg.''',
			
			"cardiopulmonar":  '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes, disminuidos en base pulmonar izquierda. Ruidos cardíacos taquicárdicos regulares, sin soplo ni galope.''',
			
			"abdomen": ''' distendido, timpánico, ruidos hidroaéreos ausentes, se evidencia hematoma en hipocondrio y flanco derecho, impresiona dolor difuso  a la palpación.''',

			"neurologico": ''' inconsciente, Glasgow: 3/15pts, Respuesta Motora: 1pto, Respuesta Verbal: 1pto, Apertura Ocular: 1pto. Pupilas isocóricas, hiporreactivas a la luz.''',
	

		}, 

		"diagnosticoIngresoUCI": [
									"Estado post RCP",
									"Insuficiencia Respiratoria aguda",
									"Infección Respiratoria Baja: neumonía basal izquierda complicada con Derrame Pleural Izquierdo.",
									"Sepsis punto de partida abdominal: pancreatitis Aguda de origen Biliar",
									"Insuficiencia Renal Aguda (pre Renal)",
									"Hipertensión Arterial sistémica.",
									"Trastorno Hidroelectrolítico: Hipernatremia ",
									"Trastorno Acido/Base: acidosis metabólica descompensada con alcalosis respiratoria mas hipoxemia.",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 190 /110 mmHg; FC:80 lpm; FR: rpm. Permaneciendo durante 24 horas en área de choque presentando para el día 9/02/2015 en horas de la mañana trabajo respiratorio evolucionando en horas de la tarde con deterioro del estado neurológico dado por Glasgow de 8/15pts dado por RM: 5pts RO: 2 pts. RV: 1 pt,  en vista de disponibilidad de cupo se decide su ingreso en UCI.''',
			"piel": ''' blanca  normotermica, normohidratada, llenado capilar < de 3 seg.''',
			"cardiopulmonar": '''tórax simétrico, hipoexpansible, ruidos respiratorios disminuidos en ambos bases pulmonares, con agregados tipo crepitantes.''',
			"abdomen": '''globoso, ruidos hidroaéreos disminuidos, blando depresible doloroso a la palpación en hemiabdomen superior de moderada intensidad.''',
			"extremidades": '''simétricas, sin edema.''',
			"neurologico": '''consciente, orientada en 3 planos.''',

		},  

	},# 148

	{
		
		"nombre": "Douglas José Tremont Sánchez", 		
		
		"edad": "32",
		
		"ci": "17.135.253", 
		
		"dirección": "franja la llanada Antonio guzmán blanco",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1983,3,9),

		"lugarNacimiento": "CUMANA", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,4,23),

		"fechaIngresoUCI": datetime(2015,4,26),

		"resumenIngreso": '''Se trata de paciente masculino de 32 años de edad natural y procedente de la localidad sin antecedentes patológicos conocidos, quien inicia enfermedad actual el dia jueves 23/04/2015 en la localidad de araya cuando posterior a recibir herida por arma de fuego en región occipital es referido asistencial siendo evaluado por el servicio de Traumatología quien decide su ingreso con diagnóstico de.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubada, conectado a ventilador de traslado, se traslada a cama de UCI, se conecta a ventilación mecánica y a monitor cardíaco externo que reporta: Signos Vitales: TA: 169/95 mmHg; FC: 89 lpm; FR: 23 rpm; SPO2:98%''',
			
			"piel" : 	'''	morena, hidratada, con leve pálidez cutáneo-mucosa, llenado capilar < 3 segundos.''',
			"cabeza": ''' Se evidencia vendaje impregnado de secreción hemática  que cubre región de herida quirúrgica.''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax sin agregados, ruidos cardiacos rítmicos taquicárdicos, sin soplo ni galope. ''',
			
			"abdomen": ''' globoso a expensa de panículo adiposo ruidos hidroáreos presentes blando depresible sin megalias.''',

			"neurologico": ''' paciente bajo efectos de sedación farmacológica Glasgow no evaluable, pupilas isocóricas mioticas. ''',
			
		}, 

		"diagnosticoIngresoUCI": [
									"Post operatorio inmediato de limpieza quirúrgica de herida craneal parietal derecha ",
									"Traumatismo craneoencefálico leve por herida por proyectil de arma de fuego en región occipital ",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Signos Vitales: TA: mmHg; FC: lpm; FR: rpm. Se realiza tomografía el día 24/04/2015 siendo evaluado por servicio de Neurocirugía quien en vista de evidenciar imagen subjetiva de proyectil de arma de fuego en región parietal izquierda decide  llevar a mesa operatoria el día 26/04/2015 donde bajo anestesia general, retiro de puntos de sutura y ampliación de herida hasta llegar a plano óseo no se evidencia orificio de entrada de proyectil de arma de fuego en ambos parietales ni occipital, cierre por planos y asepsia final  se traslada a área de terapia intensiva para cuidados post operatorios. ''',
			"piel": ''' morena, llenado capilar < 3 seg ''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible ruidos respiratorios presentes en ambas hemitorax sin agregados .ruidos  cardiacos rítmicos regulares sin soplo ni galope. ''',
			
			"abdomen": '''globoso a expensa de panículo adiposo  ruidos hidroaéreos presentes sin megalias ''',
			
			"neurologico": '''paciente agitado desorientado en espacio y persona, pupilas isocóricas hipo reactivas, hemiparesia izquierda  a la luz   con Glasgow 10/15 pts (RM:5 pts RV: 3 pts RO: 2pt).''',
			"cabeza": ''' Se evidencia herida de 8 cm aproximadamente en región occipital de bordes irregulares''',

		},  

		"diagnosticoIngresoHUAPA": [
								"TEC moderado ",

		], 
		
	},# 149

	{
		
		"nombre": "Egdina Solangel Campos de Boada", 		
		
		"edad": "62",
		
		"ci": "3.872.734", 
		
		"dirección": "URB F e y Alegria",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1952,2,17),

		"lugarNacimiento": "cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,3,19),

		"fechaIngresoUCI": datetime(2014,3,19),

		"intervencionQuirurgica": True,

		"transfusion": True,

		"antecedentes": '''TU COLON 2012, APP:   TU COLON SIGMOIDES ''', 

		"resumenIngreso": '''Se trata de paciente femenino de 62  años de edad con antecedentes de Hemicolectomia Radical Izquierda con confección de Colostomía de Harman en el mes de marzo del año de 2013 por Cáncer de Colon  izquierdo obstruido, la cual recibió posteriormente quimioterapia coadyuvante 5Fu por 6 dosis ,comienza enfermedad actual hace aproximadamente 3 meses dado por la presencia de sangrado rectal abundante ameritando transfusiones sanguíneas en múltiples ocasiones ,se realiza seguimiento especializado por cirugía oncológica realizándose multiples studios dentro de los que se incluyen : Biopsia la cual informa ADC DE COLON ST IIIB ,Endoscopia digestiva baja ,Ecosonografia abdominal cuyos informes se anexan ,decidiéndose realizar Laparotomia exploradora por lo que se hospitaliza a cargo de cirugía blanda.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' TA: 125 /76 mmHg; FC: 75 lpm; FR: 12 rpm; SPO2: 100  %''',
			
			"piel" : 	'''Blanca, normotérmica al tacto, llenado capilar < 3 segundos. ''',
			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible , ruidos respiratorios presentes en ambos campos pulmonares, sin agregados estertores, ruidos cardíacos rítmicos, regulares,  hipofonéticos, sin soplos ni galope. ''',
			
			"abdomen": ''' blando, depresible, doloroso a la palpación superficial y profunda ,herida quirúrgica cubierta por apósito estéril drenes colocados en región de fondo de saco ,otro ubicado en espacio parieto cólico izquierdo  y citostomia  ruidos hidroáreos presentes, no megálico.''',

			"neurologico": '''bajo efectos de sedación ''',
		

		}, 

		"diagnosticoIngresoUCI": [
									"POI LAPAROTOMIA EXPLORADORA COMPLICADA CON ",
									"RESECCION DE ASA DELGADA ",
									"RAFIA VENA ILIACA DERECHA ",
									"TU SIGMOIDES ",
									"INESTABILIDAD HEMODINAMICA ",
									"ANEMIA MODERADA",
									"ACIDOSIS METABOLICA DESCOMPENSADA ",
									{"resumen": ''' PACIENTE QUE PERMANECE EN SERVICIO DE UCI POR 72 HORAS SIENDO EXTUBADA A LAS 6 HORAS DEL PERIODO POST QUIRURGICO TOLERANDO OXIGENO HUMEDO POR MASCARILLA FACIAL A RAZON DE 8 LT POR MINUTO , MANEJANDO CIFRAS DE TA CON TENDENCIA A HIPOTENSION QUE MEJORA CON REPOSICION DE FLUIDOS ,SE INICIO TRATAMIENTO ATB CON CIPROFLOXACINA Y METRONIDAZOL ,APRECIANDOSE AUMENTO PROGRESIVO DE CONTAGE DE BLANCOS POR LO QUE SE ROTA ATB A MEROPENEM Y MATENEMOS METRONIDAZOL , SE REALIZA ECOSONOGRAMA ABDOMINAL DONDE SE EVIDENCIA DILATACION CALICIAL IZQUIERDA , PACIENTE CON ASCENSO DE AZOADOS DEBIDO A DISMINUCION DE DIURESIS ,SE INDICA TRATAMIENTO CON LASIX MEJORANDO FUNCION RENAL ,PERMANECE POR 48 HORAS CON INESTABILIDAD HEMODINAMICA DEBIDO A SHOCK SEPTICO SEPSIS PUNTO DE PARTIDA ABDOMINAL MEJORANDO CON REPOSICION DE LIQUIDOS Y USO DE ESTERIODES ,DEBIDO A ESTABILIDAD HEMODINAMICA Y NO REQUERIR DE VENTILACION MECANICA SE DECIDE TRASLADO A SERVICIO DE CIRUGIA. .'''}

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente que es intervenida el día de hoy realizándose resección de asa delgada a 70 cm de asa fija y 110 cm de valvula iliocecal ,lesión iatrogénica de vena iliaca derecha con perdidas hematicas abundantes 1000 cc con inestabilidad hemodinámica que amerita transfusión de 1 udad de concentrado globular y sangre total por tal motivo se decide su ingreso a UCI. Recibimos paciente en  camilla de traslado recibiendo oxigeno mediante mascarilla autoinsuflable conectada  a reservorio, no conectado a monitor cardiaco. Se conecta a monitor cardiaco que reporta: TA: 125 /76 mmHg; FC: 86 lpm; FR: 12 rpm; SPO2: 100 % ''',
			"piel": ''' Blanca, normotérmica al tacto, llenado capilar < 3 segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible , ruidos respiratorios presentes en ambos campos pulmonares, sin agregados estertores, ruidos cardíacos rítmicos, regulares, hipofonéticos, sin soplos ni galope. ''',
			
			"abdomen": '''blando, depresible, doloroso a la palpación superficial y profunda ,herida quirúrgica cubierta por apósito estéril drenes colocados en región de fondo de saco ,otro ubicado en espacio parieto cólico izquierdo  y citostomia  ruidos hidroáreos presentes, no megálico.''',
		
			"neurologico": '''CONSCIENTE ORIENTADA EN TIEMPO ESPACIO Y PERSONA ,GLASGOW 13/15 PUNTOS RM 6 PUNTOS RO 4 PUNTOS RV 3 PUNTOS''',

		},  

		"diagnosticoIngresoHUAPA": ["TU COLON SIGMOIDES "], 
		
	},#150


	{
		"IdHistoria": "52-01-12 ", 
		
		"nombre": "Deison  Gregorio Blanco Urbáez", 		
		
		"edad": "18",
		
		"ci": "25.336.682", 
		
		"dirección": "San Antonio de IRAPA, Edo. Sucre.",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1995,8,31),

		"lugarNacimiento": "IRAPA", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,4,30),

		"fechaIngresoUCI": datetime(2014,4,30),

		"resumenIngreso": '''Paciente masculino de 18 años de edad, natural y procedente de San Antonio de Irapa, sin antecedentes patológicos, cuyo familiar refiere inicio de enfermedad actual el 29/04/20 14 en horas de la tarde cuando posterior a accidente de tránsito tipo colisión de vehículo en marcha contra objeto fijo (Camión), presentando traumatismos múltiples y aumento de volumen en pelvis dolor y limitación funcional de ambos miembros inferiores, motivo por el cual es trasladado al hospital de IRAPA y de ahí se traslada al Hospital de Carúpano, en donde evalúan  y se transfunden 2 uds de concentrado globular y por no contar con arco en C se traslada a este centro en donde ingresa el día 30/04/2014 en horas de la madrugada, por el servicio de Traumatología y Cirugía Blanda, al examen físico paciente consciente, orientado en 3 planos recibiendo hidratación parenteral a través de vía central subclavia izquierda bilumen 7.5 Fr, cuello móvil, Tórax simétrico normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares sin agregados, ruidos cardíacos rítmicos y regulares, taquicárdicos, sin soplo ni galope; Abdomen blando, Rs Hs disminuidos, depresible, sin megalias, sin signos de irritación peritoneal; Aumento de volumen en cadera derecha; Genitales externos con moderado edema escrotal derecho, uretra peneana permeable con Foley conectada a bolsa recolectora con 200cc de orinas concentradas, inmovilización de cadera, sensibilidad en miembros inferiores conservada, Neurológico: Glasgow 15/15ptos. Se realizan paraclínicos Rx de Tórax que evidencia neumotórax marginal bilateral, Rayos x de pelvis con fractura de Rama isquiopúbica derecha. Se le realiza toracostomía y colocan tubos de tórax bilateral con burbujeo positivo abundante.  Ingresa con los diagnósticos de 1) Traumatismo toracoabdominal cerrado 2) TCE leve, 3) Fractura de pelvis, 4) Trauma testicular. El día 30/04/2014 el paciente es llevado a mesa operatoria por el servicio de traumatología para la colocación de Shanz en espina ilíaca anterosuperior y transfixión tuberositaria en Tibia derecha. Posteriormente  se anexa en el postquirúrgico inmediato trabajo respiratorio y deterioro neurológico, siendo evaluado por terapia intensiva en el área de recuperación y se evalúa paciente en malas condiciones generales, recibiendo apoyo de O2 por mascarilla facial a 10 lts por min, conectado a monitor cardíaco externo que reporta TA: 67/45mmHg FC: 125 lpm Sat 68% FR: 50 rpm, taquipneico, taquicárdico, deshidratado, mucosas secas, frio al tacto, cardiopulmonar: toracostomía bilateral tórax simétrico hipoexpansible RsRsPs ambos Ht sin agregados, disminuidos en base derecha, Rs Cs Taquicárdicos, Neurológico: Estuporoso, pupilas isocóricas hiporreactivas a la luz, Glasgow RO: 2ptos RV: 3 ptos RM: 4ptos. Por disponibilidad de cupo y en vista de las condiciones generales del paciente y por autorización de Dra. Roa (Intensivista de guardia) se decide su ingreso a UCI y dicta órdenes médicas.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, recibiendo O2 por mascarilla facial, se pasa a cama de UCI y se conecta a monitor cardíaco continuo que reporta: TA: 95/38(57) mmHg; FC: 106 lpm; FR: 55 rpm; SatO2: 100% ''',
			
			"piel" : 	'''	morena, normotérmica al tacto, llenado capilar < 3seg. Temperatura: 36,4ºC, PVC: 11 cm3H2O ''',
			"cabeza": '''se evidencia herida en región parietal izquierda, lineal con puntos de sutura, sin tumoraciones ni reblandecimientos. ''',

			"cardiopulmonar":  ''' tórax simétricos, hipoexpansible, toracotomía bilateral con trampa de agua con burbujeo positivo, ruidos respiratorios presentes disminuidos en base derecha, sin agregados. Ruidos cardíacos arrítmicos, taquicardicos, sin soplo ni galope.''',
			"abdomen": '''  plano, blando, ruidos hidroaéreos presentes aumentados, con herida quirúrgica de sitio de punción de fijador con barra de arco en ambas espinas ilíacas antero-superiores, cubiertas por apósitos húmedos con secreción hemática escasa, no impresiona doloroso a la palpación, no megálico.''',

			"neurologico": ''' estuporoso, con agitación psicomotriz, desorientado en 3 planos, pupilas isocóricas normorreactivas a la luz, Glasgow 11/15pts (RM: 6pts, RO: 3pts, RV: 2pts).''',
			"extremidades": '''miembro inferior derecho aumento de volumen en muslo y con transfixión trasn-tuberositaria con tracción esquelética de 5kg de peso, sobre férula de Brown.''',

		}, 

		"diagnosticoIngresoUCI": [
									"POLITRAUMATIZADO:",
									"TRAUMATISMO CRANEOENCEFALICO LEVE.",
									"TRAUMATISMO TORACO-ABDOMINAL CERRADO.",
									"FRACTURA  DE PELVIS TILE IIA.",
									"TRAUMA TESTICULAR.",
									"FRACTURA DE ACETÁBULO DE CADERA DERECHA",
									"CONTUSIÓN CARDÍACA.",
									"NEUMOTÓRAX BILATERAL.",
									"SHOCK HIPOVOLÉMICO.",
									"RABDOMIÓLISIS.	",
									"INSUFICIENCIA RENAL AGUDA",
									"TRASTORNO HEMATOLOGICO:",
									"ANEMIA MODERADA",
									"TRASTORNO ACIDO-BASE:",
									"ALCALOSIS METABOLICA COMPENSADA + HIPEROXEMIA",
									"TRASTORNO HIDROELECTROLÍTICO: ",
									"HIPERCALEMIA.",
									{"resumen":''' al ingreso el paciente se intuba y se conecta a ventilación mecánica por trabajo respiratorio (FR: 55rpm) parámetros Modo AC, FR: 12, Fio2: 90, FL 50, VC: 560 (7cc x kg), Tinsp 0,95, Peep: 0. Se le coloca sonda nasogástrica obteniéndose contenido sanguinolento (traumático) que posteriormente se hace alimentario, se le colocan 1000cc de solución Ringer lactato sin mejoría de cifras tensionales se le coloca Levophed a dosis de 36 mcg/min. Se indica por orden de Dra Roa sedación y relajación, con analgesia.'''},

								],  
		
	},# 151


	{
		
		
		"nombre": "Dionicio Eleazar Carvajal Rodríguez", 		
		
		"edad": "20",
		
		"ci": "24.401.890 ", 
		
		"dirección": "Campeche sector II.  ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1995,2,3),

		"lugarNacimiento": "CUMANA", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,3,20),

		"fechaIngresoUCI": datetime(2015,3,25),

		"resumenIngreso": '''Se trata de paciente masculino de 20 años de edad quien inicia enfermedad actual el día 20/03/2015 cuando posterior a recibir heridas por proyectil de arma de fuego en hemitorax derecho y región lumbar es llevado a centro privado siendo referido a nuestro centro asistencial y previa evaluación por Servicio de Cirugía se decide su ingreso  ''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, intubada, recibiendo oxígeno a través de ambú, se traslada a cama de UCI, se conecta a ventilación mecánica y a monitor cardíaco externo que reporta: Signos Vitales: TA: 125/55 mmHg; FC: 80 lpm; FR: 21 rpmSPO2:95%''',
			
			"piel" : 	'''morena, hidratada, con leve pálidez cutáneo-mucosa, llenado capilar < 3 segundos.''',

			"cardiopulmonar":  ''' tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos hemitorax y disminuidos en base pulmonar izquierda ,se evidencia tubo de tórax conectado a trampa de agua con salida de secreción hemática escasa,  con agregados roncos bilaterales moderados, Ruidos cardíacos rítmicos regulares, sin soplos''',
			
			"abdomen": '''globoso a expensa de panículo adiposo, se evidencia apósito estéril que cubre herida quirúrgica limpia y seca ruidos hidroaéreos presentes.se evidencia sonda nasogástrica con salida de secreción bilioenterica, blando, depresible no impresiona dolor a la palpación, sin megalias.''',

			"neurologico": ''' paciente inconsciente, Glasgow no evaluable por efecto de sedación farmacológica Pupilas isocóricas  hiporreactivas a la luz. Reflejo tusígeno presente''',
		
		}, 

		"diagnosticoIngresoUCI": [

									"Post operatorio inmediato de laparotomía exploradora por traumatismo Toraco abdominal penetrante por proyectil de arma de fuego con lesión grado III se segmento hepático VII y Lesión grado III de colon ascendente.",
									"Insuficiencia respiratoria aguda.",
									"Insuficiencia renal aguda (pre-renal)",
									"Infección respiratoria baja neumonía por broncoaspiración ",
									"Trastorno hematológico: anemia moderada ",
									"Trastorno Hidroelectrolítico: Hiperkal",
									"Trastorno acido base: ",
									"Post operatorio inmediato de laparotomía exploradora por traumatismo toracoabdominal penetrante por proyectil de arma de fuego.",
									"Lesión grado III se segmento hepático VII",
									"Lesión grado III de colon ascendente. ",
									{"resumen":''' El día 21/03/2015 en horas de la noche presenta cuadro de insuficiencia respiratoria severa (referido por residente de cirugía) dado por cianosis distal y acrocianosis y dificultad respiratoria, motivo por el cual realiza intubación endotraqueal con tubo 6.5 FR. solicitando valoración por equipo de terapia intensiva, acudiendo al llamado  evaluando paciente en piso 7 intubado no conectado a monitor cardiaco recibiendo oxigeno por ambú.se traslada a are de recuperación de quirófano donde se conecta a ventilación mecánica y en vista de no contar con disponibilidad de cupo se realizan sugerencias. Para el día 23/03/2015 se solicita valoración por servicio d nefrología en vista de que paciente cursa con oliguria además retención de azoados el cual se cumple por Nefrólogo de guardia Dra. Nervis González   quien realiza sugerencias entre ellas revaloración por su servicio en 24 horas. siendo evaluado el día 24/03/2015 decidiendo brindar soporte dialítico (hemodiálisis).es evaluado el día 25/03/2015  por el Servicio de UCI quien  por disponibilidad de cupo se decide su ingreso.'''}

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente es llevado a mesa operatoria a su ingreso donde bajo anestesia general realizan laparotomía exploradora drenando hemoperitoneo, lesión grado III del segmento hepático y lesión grado III de colon ascendente los cuales se rafia con crómico. Y lavado de cavidad con 2000 cc de solución 0,9%. Es trasladado a área de recuperación de quirófano permaneciendo 6 horas y luego trasladado  a área de piso 7 cirugía blanda con diagnostico:''',
			"piel": '''morena, normotermica, normoelastica, llenado capilar < 3 Seg ''',
			"cardiopulmonar": '''tórax simétrico, ruidos respiratorios disminuidos  en ambas bases pulmonares,se evidencia orificio por proyectil de arma de fuego a nivel de 8vo espacio intercostal con línea media axilar.''',
			"abdomen": '''globoso a expensa de panículo adiposo, ruidos hidroaéreos presentes, blando depresible, doloroso a la palpación difusa en región lumbar se evidencia orificio por proyectil de arma de fuego a nivel de L5-S1.''',
			"extremidades": '''se evidencia orificio por proyectil de arma de fuego en cara anterior de hombro izquierdo. Fuerza muscular abolida en miembros inferiores ''',
			"neurologico": '''paciente orientado en3 planos.''',
			

		},  

		"diagnosticoIngresoHUAPA": ["Traumatismo Toraco abdominal penetrante"], 
		
	},# 152


	{
		"IdHistoria": "06–48–32 ", 
		
		"nombre": "Elba Rosa Bilmonte de Brito", 		
		
		"edad": "69",
		
		"ci": "3.337.518", 
		
		"dirección": "Muelle Cariaco, calle las Flores, casa S/N",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1944,9,4),

		"lugarNacimiento": "Cariaco, Edo. Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,3,2),

		"fechaIngresoUCI": datetime(2014,4,8),

		"resumenIngreso": '''Paciente femenina de 69 años de edad, natural y procedente de Cariaco, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual a principios del mes de febrero de 2014 aproximadamente cuando presenta movimientos tónico-clónicos generalizados, con relajación de esfínter vesical, motivo por el cual es llevada a ambulatorio de su localidad, de donde es referida a este centro asistencial el día 02/03/14 y previa valoración se ingresa por el servicio de Medicina Interna con los diagnósticos de EVC en evolución y síndrome convulsivo. Al momento del ingreso presenta desorientación en tiempo y espacio, lenguaje incoherente y hemiparesia izquierda. Permanece en área de emergencia y observación hasta el día 06/04/14 cuando es trasladada a piso de hospitalización. El día 02/03/14 se le realiza TAC simple cerebral que reporta efecto de masa frontal derecho, por lo que el 07/03/14 se le realiza RM cerebral con contraste paramagnético endovenoso, reportando lesión de aspecto tumoral, de aspecto extraaxial, probablemente meningioma fronto temporal derecho, con muy discreto edema perilesional y leve hernia subfalsina, solicitan valoración por el servicio de Neurocirugía, siendo evaluada por Dr. Acevedo (Neurocirujano) quien indica tener criterios de resolución quirúrgica por lo que se planifica para cirugía electiva. El día de hoy 08/04/14 es llevada a mesa operatoria donde bajo anestesia general se realiza incisión hemicoronal, disección por planos y disección de pericráneo hasta exponer órbita, osteotomía supraorbitaria, maxilar derecha y de arco cigomático, liberación de barra frontoorbitocigomática, craneotomía pterional y durotomía en “Y”, por falta de tiempo quirúrgico se difiere para culminación en un segundo tiempo quirúrgico. Previa autorización de Dra. Teresa Cortesía  se indica su ingreso a la UCI.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubada y conectada a ventilador mecánico de transporte, se pasa a cama UCI, se conecta a ventilación mecánica modo A/C, Vc: 560, FR: 12, FiO2: 60, Fl: 50, PEEP: 0 y se conecta a monitor cardíaco continuo que reporta: TA: 116/65(82) mmHg; FC: 105 lpm; FR: 12 rpm; SatO2: 100%''',
			
			"piel" : 	'''moderada palidez cutáneo-mucosa, hipotérmica al tacto, llenado capilar < 3seg.''',
		
			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, con roncus escasos bilaterales. Ruidos cardíacos rítmicos y regulares, taquicárdicos, sin soplo ni galope.''',
			"abdomen": ''' plano,ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico''',

			"neurologico": '''no evaluable por efectos de sedación y relajación farmacológica. ''',
		}, 

		"diagnosticoIngresoUCI": [

								"POI DE CRANEOTOMIA FRONTO-ORBITO-CIGOMATICA PARA EXCERESIS DE LOE CEREBRAL EN 1/3 INTERNO DE ALA ESFENOIDAL DERECHO SUGESTIVO DE MENINGIOMA",
								"TRASTORNO HEMATOLOGICO:",
								"ANEMIA MODERADA",
								"TRASTORNO ACIDO-BASE:",
								"ACIDOSIS METABOLICA COMPENSADA CON ALCALOSIS RESPIRATORIA + HIPEROXEMIA",

									
								],  
		
	},# 153


	{
		"IdHistoria": "48-005-09", 
		
		"nombre": "Erika Josefina Maican Ramos", 		
		
		"edad": "19",
		
		"ci": "25.654.156", 
		
		"dirección": "San Juan sector Guaranache I",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1944,12,22),

		"lugarNacimiento": "Maturín", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,11,7),

		"fechaIngresoUCI": datetime(2014,11,7),


		"resumenIngreso": '''Paciente femenina de 19 años de edad sin antecedentes patológicos importante, gesta II, cesárea anterior, quien cursa con embarazo actual de 38 sem + 5 días por eco, cuyo familiar refiere que presenta convulsiones tónico – clónicas generalizadas desde las 5 am en múltiples ocasiones, por lo que es trasladada a este centro, donde se evalúa por servicio de Ginecología y se decide ingreso; presentando cifras tensionales elevadas y nuevo episodio convulsivo por lo que es llevada a mesa operatoria donde se realiza cesárea segmentaria obteniendo recién nacido atermino masculino de 3400 gr.''', 


		"examenFisicoIngresoUCI": {
			
			"piel" : 	'''Morena, normotérmica al tacto, llenado capilar <3 segundos.''',

			"cardiopulmonar":  '''Tórax simétrico, expansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados pulmonares, ruidos cardíacos normofonéticos, sin soplos ni galope.''',
			"abdomen": ''' herida quirúrgica cubierta por apósito estéril, útero tónico a nivel umbilical ''',

			"neurologico": '''Agitación psicomotriz, desorientada, pupilas isocóricas, reactivas a la luz.''',
			

		}, 

		"diagnosticoIngresoUCI": [

								"Post operatorio inmediato de cesárea segmentaria",
								"Trastorno hipertensivo del embarazo tipo Eclampsia.",
								"Trastorno Hidroelectrolítico: hipokalemia.",
								"Trastorno acido base: acidosis metabólica descompensada con alcalosis respiratoria más hiperoxemia.",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 180/120mmHg  Fr: 25 rpm  Fc: 120 lpm ''',
			"piel": ''' Morena, normotérmica al tacto, llenado capilar <3 segundos.''',
			"cardiopulmonar": '''Tórax simétrico, expansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados pulmonares, ruidos cardíacos normofonéticos, sin soplos ni galope. ''',
			"abdomen": '''Útero grávido, con feto único, longitudinal, cefálico ''',
			"extremidades": '''Simétricas, edema grado I en ambos miembros inferiores''',
			"neurologico": '''Consciente, desorientada, lenguje incoherente, pupilas reactivas a la luz.''',

		},  

		"diagnosticoIngresoHUAPA": [
								"II Gesta",
								"Embarazo de 38 sem + 5 días",
								"ARO por: Trastorno hipertensivo del embarazo tipo Eclampsia.",
								"Cesárea anterior.",
								"Anemia leve ( Hb 10.5)",
								"Domicilio lejano.  ",
								{"resumen":''' La paciente es llevada a cuidados intermedios y  se solicita evaluación por UCI. Se evalúa paciente en cama recibiendo oxigeno húmedo por mascarilla facial, conectada a monitor cardiaco que reporta Fc 87 lpm TA 140/60 mmHg Fr 24 rpm, desorientada, con agitación psicomotriz, decidiéndose su ingreso  UCI. Se recibe paciente en camilla de traslado, recibiendo oxigeno húmedo por mascarilla facial a 5lts por minutos, se traslada a cama UCI, se conecta a monitor cardiaco que reporta Fr: 17rpm Fc:93 lpm TA 106/67 (77)mmHg SATO2 93 %. Se procede a intubación endotraqueal previa sedación con Midazolam colocando tubo 7.5 sin complicaciones y se conecta a ventilación mecánica AC Vc 600 Fr 12 FiO2 50 TI 1:4 Fl 50 PEEP 0. '''}

		], 
		
	},# 154


	{
		"IdHistoria": "52–42–55 ", 
		
		"nombre": "Fernando Javier Gómez Vera", 		
		
		"edad": "18",
		
		"ci": "25.467.289 ", 
		
		"dirección": "San Antonio del Golfo, Edo. Sucre",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1995,9,23),

		"lugarNacimiento": "Cumaná, Edo. Sucre.", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,8,24),

		"fechaIngresoUCI": datetime(2014,8,25),

		"resumenIngreso": '''Paciente masculino de 18 años de edad, natural y procedente de la localidad, sin antecedentes patológicos conocidos, cuyo familiar refiere inicio de enfermedad actual el día de hoy 25/08/14 en horas de la madrugada, cuando posterior a accidente de tránsito tipo colisión (moto – moto) presenta traumatismos múltiples y pérdida del estado de consciencia sin recuperación espontánea de la misma, motivo por el cual es llevado a CDI de donde es referido a éste centro asistencial donde se valora y es ingresado por el servicio de Neurocirugía. Al momento del ingreso presenta deterioro neurológico caracterizado por inconsciencia, pupilas isocóricas, hiporreactivas a la luz y Glasgow de 9/15pts (RM: 5pts, RO: 2pts, RV: 2pts) por lo que se realiza intubación endotraqueal y se conecta a T de Ayres con O2 húmedo a 10LtrsX’. En vista de estado general de la paciente, solicitan valoración por UCI y en vista de estado general del paciente, previa autorización de Dra. Cortesía  decide su ingreso.''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubado y recibiendo O2 por Ambú, se pasa a cama UCI, se conecta a ventilación mecánica modo A/C, Vc: 560, FR: 12, FiO2: 90, Fl: 50, PEEP: 0 y se conecta a monitor cardíaco continuo que reporta: TA: 93/47(77) mmHg;     FC: 126 lpm;      FR: 18 rpm;      SatO2: 99% Se realiza TAC cerebral simple donde se evidencia pequeño hematoma intraparenquimatoso temporal izquierdo, edema cerebral difuso, fractura de hueso propio nasal y maxilar del lado izquierdo y sinusopatía postraumática etmoido-maxilar bilateral.''',
			
			"piel" : 	'''	morena, normotérmica al tacto, con escoriaciones múltiples a nivel de cara, miembros superiores y miembro inferior derecho, con equimosis y edema bipalpebral derecho, rafia a nivel supraciliar derecha cubierta por apósitos con escasa secreción serohemática, llenado capilar < 3seg.''',
			

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, taquicárdicos, sin soplo ni galope.''',
			
			"abdomen": '''plano, ruidos hidroaéreos presentes, herida quirúrgica infraumbilical cubierta por apósitos con moderada secreción serohemática, blando, depresible, no impresiona doloroso a la palpación, no megálico.''',

			"neurologico": '''inconsciente, pupilas isocóricas, mióticas, arreactivas a la luz, reflejo tusígeno y corneal presentes, Glasgow no evaluable por efectos de sedación farmacológica.''',
			"extremidades": '''férula braquio – palmar derecha funcionante, con abundante secreción serohemática, aumento de volumen en rodilla derecha, cubierta por apósitos con escasa secreción serohemática. ''',

		}, 

		"diagnosticoIngresoUCI": [

									"TRAUMATISMO CRANEOENCEFALICO SEVERO COMPLICADO CON:",
									"HEMATOMA INTAPARENQUIMATOSO TEMPORAL IZQUIERDO",
									"EDEMA CEREBRAL DIFUSO",
									"FRACTURA DE HUESO PROPIO NASAL Y MAXILAR DEL LADO IZQUIERDO",
									"SINUSOPATIA POSTRAUMATICA ETMOIDO-MAXILAR BILATERAL",
									"TRAUMATISMO TORACOABDOMINAL CERRADO",
									"FRACTURA DE CUBITO Y RADIO DERECHO POR CLINICA",
									"TRASTORNO HEMATOLOGICO:",
									"ANEMIA MODERADA",
									"PROLONGACION DE PT",
									"TRASTORNO ACIDO-BASE:",
									"ACIDOSIS METABOLICA COMPENSADA MAS HIPEROXEMIA",

									
								],  

		
	},#155

	{
		"IdHistoria": "54-08-65", 
		
		"nombre": "Luis Guillermo Montaño Marcano", 		
		
		"edad": "34",
		
		"ci": "15.743.964", 
		
		"dirección": "Barrio Venezuela calle 1 No 271 ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1981,9,21),

		"lugarNacimiento": "La Guaira", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,12,13),

		"fechaIngresoUCI": datetime(2015,12,13),

		"resumenIngreso": '''Se trata de paciente masculino de 34 años de edad, natural de la Guaira, procedente de la localidad, con antecedentes de HIV positivo según refiere familiar, en control y tratamiento en la cuidad de Caracas. Quien inicia enfermedad actual el día de hoy en horas de la madrugada cuando recibe múltiples heridas por arma blanca, motivo por el cual es traído a este centro asistencial donde es evaluado y hospitalizado por servicio de cirugía.''', 


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, intubado recibe oxigeno húmedo por ambu, se traslada a cama UCI, se conecta a ventilador mecánico modo A/C Vc: 360 Fr: 12 Fl: 50 FiO2: 60 TI: 1:4 PEEP: 0 Y a monitor cardiaco que reporta Fc: 161 lpm TA 66/48 (51) mmHg Fr: 38 rpm SATO2: 100 %  PVC: 12 cmH2O''',
			
			"piel" : 	'''	Normotérmica, llenado capilar <3segundos. Se evidencia palidez cutánea mucosa.''',
		

			"cardiopulmonar":  '''Tórax simétrico, normoexpansible, Ruidos respiratorios disminuidos en base izquierda sin agregados Ruidos cardíacos rítmicos, taquicardicos,  no se auscultan soplos. Tubo de drenaje torácico conectado a trampa de agua con gasto hemático.''',
			"abdomen": ''' plano, depresible,  se evidencia apósito estéril que cubre herida quirúrgica limpio y seco, no drenes, ruidos hidroaéreos abolidos.''',

			"neurologico": ''' no evaluable por sedación farmacológica.''',
			
		}, 

		"diagnosticoIngresoUCI": [
						"Post operatorio inmediato de laparotomía exploratoria media supra para e infraumbilical debido a: Traumatismo tóraco abdominal penetrante por arma blanca . ",
						"shock Hipovolémico.",
						"Insuficiencia Renal Aguda pre renal",
						"HIV positivo",
						"Trastorno hematológico: anemia severa, ptt prolongado",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' SIGNOS VITALES: FC LPM TA MMHG FR''',
			"piel": ''' morena, llenado capilar <3segundos. ''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, Ruidos respiratorios presentes en ambos hemitorax sin agregados Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos. Se evidencian múltiples heridas por arma blanca en región dorsal y una herida en 8vo espacio intercostal derecho con línea medio clavicular''',
			"abdomen": '''Depresible, no doloroso a la palpación superficial y profunda.''',
			
			"neurologico": '''Consciente orientada en tiempo espacio y persona.''',

		},  

		"diagnosticoIngresoHUAPA": [
								"Traumatismo tóraco abdominal penetrante por arma blanca en 8vo espacio intercostal derecho. ",
								{"resumen":''' El paciente es llevado a mesa operatoria donde se realiza laparotomía exploratoria media supra para e infraumbilical con hallazgo de 2500 cc de hemoperitoneo, lesión grado III de segmento V yVI hepático, lesión grado II diafragmática izquierda, lesión grado II en curvatura mayor de estómago, hematoma en zona II retroperitoneal derecha expansivo, no pulsátil. Tomando como conducta evacuación del hemoperitoneo, rafias de Estómago y lesión en hemidiafragma izquierdo, comprobación de hemostasia y síntesis de pared por planos, en segundo tiempo se coloca tubo de drenaje torácico 34 fr en 5to EIC con LMA izquierda, obteniendo burbugeo y gasto hemático de 100 cc aproximadamente. El paciente es evaluado por UCI acudiendo ha llamado y por no disponer de cupo se deja en ventilación mecánica en área de recuperación de quirófano y hace sugerencias. El paciente permanece en dicha área donde recibe 2 uds de concentrado globular y 2 reposiciones de Sol Ringer y Sol 0.9% hasta horas de la tarde cuando por disponibilidad de cupo y las malas condiciones del paciente se decide su ingreso a UCI.  '''}
		], 
		
	},# 156

	{
		"IdHistoria": "53-37-52", 
		
		"nombre": "Santiago Miguel Muñoz", 		
		
		"edad": "13",
		
		"ci": "28.044.729", 
		
		"dirección": "Urbanización Lomas de Ayacucho. Cumana Edo. Sucre ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(2001,8,26),

		"lugarNacimiento": "Cumaná - Edo. Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,5,11),

		"fechaIngresoUCI": datetime(2015,5,11),

		"resumenIngreso": '''Se trata de paciente masculino de 13 años de edad sin antecedentes patológicos conocidos, quien inicia enfermedad actual hace aproximadamente 1mes cuando comienza a presentar pérdida de peso y hace aproximadamente 2 semanas comienza con poliuria y polidipsia, motivo por el cual es traído el día de hoy en la mañana a este centro asistencial donde realizan exámenes de laboratorio evidenciando cifras de glicemia elevadas y orientan repetir en otro centro, por lo que el paciente es llevado a su casa donde en horas de la noche presenta dolor abdominal, vómitos y  dificultad respiratoria, por lo que es traído nuevamente a este centro donde previa evaluación se ingresa; se realiza glicemia capilar reportando HI. Se realizan paraclínicos que reportan Glic: 691 mg/dl, cuerpos cetónicos ++, creatinina: 1.4 mg/dl gases arteriales Ph: 7.09 PCO2:13 PO2: 172 HCO3: 3.9 EB: -23.9 SATO2: 99%. TA: 130/70mmHg;  FC: 130 lpm; FR: 30 rpm	''', 


		"examenFisicoIngresoUCI": {

			"piel" : 	'''	normotermica, normoelástica, llenado capilar < 3 seg''',
	

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos ni galope''',
			"abdomen": ''' plano, blando, no doloroso a la palpación, ruidos hidroaéreos presentes, sin megalias.''',

			"neurologico": '''consciente con tendencia a la somnolencia, orientado en tres planos, normoreflextico, Glasgow 15/15 ''',
			"extremidades": '''simétricas, no edemas, eutróficas ''',

		}, 

		"diagnosticoIngresoUCI": [
									"CETOACIDOSIS DIABÉTICA",
									"DIABETES MELLITUS TIPO 1 DE DEBUT.",
									{"resumen":''' Se solicita valoración por UCI presentando caso a Dra. Cortesía especialista de guardia quien  decide su ingreso. Se recibe paciente en camilla de traslado ventilando espontáneamente, tolerando aire ambiente,  se traslada  a cama UCI y se conecta monitor cardiaco continuo que reporta:  TA: 128/74 (91)mmHg	       FC: 131 lpm; FR: 30 rpm; SPO2: 100%'''}

								],  

		"examenFisicoEgresoUCI": {
			
			"piel": ''' blanca, normotérmica, hidratado, llenado capilar <3segundos.''',
			
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos, regulares, no se auscultan soplos ni galope.''',
			
			"abdomen": '''plano, blando, no doloroso a la palpación, ruidos hidroaéreos presentes, sin megalias.''',
		
			"neurologico": '''Consciente, orientado en tres planos, Glasgow 15/15 puntos, pupilas isocóricas reactivas a la luz, no signos de focalización neurológica. ''',
			
		},  

		"diagnosticoIngresoHUAPA": [
								"CETOACIDOSIS DIABÉTICA.",
								"DIABETES MELLITUS TIPO 1 EN DEBUT",
								"ACIDOSIS METABÓLICA DESCOMPENSADA + ALCALOSIS RESPIRATORIA CON HIPEROXEMIA.",
								{"resumen":''' Paciente que permanece en servicio de terapia intensiva recibiendo Insulina Cristalina mediante bomba de infusión continúa a razón de 0,1 Ud. /h e hidratación parenteral a razón de 80 cckg primeras 24 horas y luego Reducción progresiva de líquidos en dependencia de  parámetros hemodinámicos  ,se reduce dosis de insulina por bomba de infusión continua apreciándose compensación acido básica ,se inicia tratamiento con Lantus 12 U  noche e Insulina cristalina 3 Uds. en Desayuno ,Almuerzo y Cena ,debido a evolución favorable se decide egreso '''}

		], 

		"diagnosticoEgreso": ["DIABETES MELLITUS TIPO 1  DEBUT"],
	},#157

	{
		"IdHistoria": "52-94-13", 
		
		"nombre": "NIXON JESUS CARIAS CHACON  ", 		
		
		"edad": "43",
		
		"ci": "11.416.483", 
		
		"dirección": "SANTA FE SECTOR LA BOCA CALLE LOS PRIMOS S/N",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1971,2,5),

		"lugarNacimiento": "cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,1,19),

		"fechaIngresoUCI": datetime(2015,1,19),


		"resumenEgreso": '''Paciente masculino de 43 años de edad, natural y procedente de santa fe, sin antecedentes patológicos conocidos, inicia enfermedad actual el día 6/01/2015 cuando presenta artralgia y aumento de la temperatura corporal cuantificado en 39 y 40 ºC precedida de escalofríos,  atenuada con acetaminofen. Para el día 7/01/2015 se anexa al cuadro cefalea continua de fuerte intensidad, motivo por el cual acude a ambulatorio de la localidad, realizan paraclínicos que reporta: leucocitosis con neutrofilia, transaminasas elevadas, bilirrubinas elevadas a expensa de la indirecta y examen de orina patológico,  egresan con tratamiento ambulatorio a base de  Ciprofloxacina  y Genurin el cual cumple por 7 días. Para el día 18/01/2015 se anexa al cuadro ictericia  coluria, somnolencia, bradipsiquia,  además de persistencia del cuadro febril, acudiendo el día 19/01/2015 a centro privado donde refieren a este centro asistencial, previa evaluación se ingresa por el servicio de medicina interna con  los diagnósticos de : Síndrome febril prolongado de etiología A/P. Infección del tracto urinario: litiasis renal A/D. Encefalopatía hepática. Esplenomegalia A/D''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' FR: 27 rpm, FC: 119 lpm, TA: 112/64 (86) mmHg,SatO2: 100% ''',
			
			"piel" : 	'''Morena, con marcado tinte ictérico en piel y mucosas, normotérmica al tacto, panículo adiposo aumentado, llenado capilar <3 seg.''',
	

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, se auscultan crepitantes bibasales. Ruidos cardiacos arrítmicos y taquicárdicos, sin soplos ni galope.''',
			"abdomen": ''' globoso a expensas de panículo adiposo, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación. ''',

			"neurologico": '''no evaluable por efectos de sedación farmacológica ''',
			"extremidades": '''simétricas, eutróficas, sin edema.''',

		}, 

		"diagnosticoIngresoUCI": [
									"SÍNDROME FEBRIL EN ESTUDIO.",
									"SEPSIS PUNTU DE PARTIDA DEL SISTEMA NERVIOSO CENTRAL A DESCARTAR.",
									"INFECCIÓN REPIRATORIA BAJA: NEUMONÍA POR BRONCOASPIRACION.",
									"TRASTORNO ACIDO-BASE: ACIDOSIS METABOLICA COMPENSADA CON ALCALOSIS. RESPIRATORIA MAS HIPER-OXEMIA.",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' El día 20 es evaluado por el Servicio de Terapia Intensiva por solicitud del servicio tratante quien en vista de presentar deterioro neurológico y rigidez de nuca se realiza punción lumbar siendo traumática por lo que se difiere procedimiento. Se realizan sugerencias en vista de no contar con cupo en UCI,  Por lo que se mantiene en el área de choque recibiendo antibióticoterapia. Para el día de hoy 22/1/15 es evaluado nuevamente por el servicio de terapia intensiva y en vista de presentar franco trabajo respiratorio y desaturación por monitor se procede a realizar intubación endotraqueal con tubo # 8.5 Fr y se conecta a ventilación mecánica con parámetros establecidos  EVITA modo IPPV, Vc: 640 (8cc X Kg), FL: 50Lt/min, FiO2:60%,  PEEP: 5 Cm2 H2O, Fr: 14rpm. Especialista del área realiza nuevamente punción lumbar que se obtiene líquido xantocròmico, se procede a tomar muestra para diferentes estudios   (pendientes resultados) y Por disponibilidad de cupo es ingresado al servicio de terapia intensiva. Se recibe paciente en camilla de traslado, intubado recibiendo oxigeno por Ambú ®, se pasa a cama UCI, se conecta a ventilación mecánica modo A/C, Vc: 600, Fr: 12rpm, FiO2: 60%, Fl: 50, PEEP: 0, se conecta a monitor cardiaco externo que reporta TA: 121 /71mmHg, FC: 124lpm,FR: 26 rpm, SatO2: 99%''',
			
			"piel": ''' piel morena, se evidencia marcada palidez cutáneo, mucosa oral seca. ''',
			"cardiopulmonar": ''' tórax simétrico, expandible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardiacos rítmicos y regulares, taquicárdicos, sin soplos ni galope.''',
			"abdomen": '''globoso, ruidos hidroaéreos presentes, depresible, no doloroso a la palpación superficial y profunda,  se palpa ligero aumento (hepatomegalia)+- 2 centímetros de reborde costal flanco derecho ''',
			"extremidades": '''simétricas, sin alteraciones. ''',
			"neurologico": '''Consiente, somnoliento bradilalico, no rigidez de nuca.''',

		},  
		
	},# 158

	{
		"IdHistoria": "52–22–96", 
		
		"nombre": "Mary Dannys Jimenez Bastardo", 		
		
		"edad": "19",
		
		"ci": "22.628.509", 
		
		"dirección": "Caiguire, calle La Marina, casa S/N, Cumana, Edo. Sucre.",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1955,4,4),

		"lugarNacimiento": "Cumana, Edo. Sucre.", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,7,3),

		"fechaIngresoUCI": datetime(2014,7,3),

		"resumenIngreso": '''Paciente femenina de 19 años de edad, natural y procedente de la localidad, I gesta, con embarazo de 35 semanas + 5 días por FUR, cuyo familiar refiere inicio de enfermedad actual hace aproximadamente un mes cuando presenta cefalea de leve a moderada intensidad en repetidas oportunidades que atenuaba con analgésicos (no precisa cuales), debilidad generalizada y mareos, acude el día de hoy 03/07/14 a este centro asistencial donde es evaluada por el servicio de Ginecología y Obstetricia evidenciando cifras elevadas de presión arterial y dentro del examen practicado presenta movimientos tónico-clónicos generalizados y sialorrea, motivo por el cual es trasladada a quirófano para realización de cesárea segmentaria de emergencia por eclampsia, se obtiene RNAT/AEG vivo femenino, en el transoperatorio persiste con cifras elevadas de presión arterial y realiza nuevo episodio de movimientos tónico-clónicos generalizados a pesar de estar recibiendo sulfato de Mg durante todo el acto quirúrgico, realizan alumbramiento manual completo, histerorrafia, comprobación de hemostasia y cierre por planos, al tener signos de ventilación espontanea se realiza reversión de bloqueo neuromuscular, sin embargo la paciente persiste con depresión neurológica y se mantiene en ventilación mecánica, solicitan valoración por UCI, acudo a quirófano de sala de parto a valorar paciente y en vista de cuadro clínico antes descrito y disponibilidad de cupo, previa autorización de Dra. Roa, se decide su ingreso a la UCI. Se recibe paciente en camilla de traslado, intubada y recibiendo O2 húmedo por Ambú®, se pasa a cama UCI, se conecta a monitor cardíaco continuo que reporta: TA: 111/74(83) mmHg; FC: 101 lpm; FR: 13 rpm; SatO2: 100%''', 


		"examenFisicoIngresoUCI": {

			
			"piel" : 	'''hipotérmica al tacto, ligera palidez cutáneo mucosa, llenado capilar < 3seg.''',
			

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos, regulares, taquicárdicos, sin soplo ni galope.''',
			"abdomen": ''' globoso a expensas de panículo adiposo, ruidos hidroaéreos presentes, blando, depresible, útero tónico a nivel de cicatriz umbilical, herida quirúrgica cubierta por apósitos limpios y secos.''',

			"neurologico": '''inconsciente, pupilas puntiformes, arreactivas a la luz, reflejos corneal y tusígeno presentes, Glasgow 3/15pts (RM: 1pts, RO: 1pto, RV: 1pts). ''',
			
			"genitales": ''' de aspecto y configuración normal, con sonda de Foley conectada a bolsa recolectora con aproximadamente 200cc de orinas, escasos loquios a través de genitales externos.''',

		}, 

		"diagnosticoIngresoUCI": [
									"POSTOPERATORIO INMEDIATO DE CESAREA SEGMENTARIA POR TRASTORNO HIPERTENSIVO DEL EMBARAZO TIPO ECLAMPSIA",
									"TRASTORNO ACIDO-BASE:",
									"ACIDOSIS METABOLICA DESCOMPENSADA CON ALCALOSIS RESPIRATORIA MAS HIPEROXEMIA",

								],  
		
	},# 159

	{
		"IdHistoria": "53-25-62", 
		
		"nombre": "Lazaro Antonio Diaz", 		
		
		"edad": "56",
		
		"ci": "6.657.893", 
		
		"dirección": "muelle de cariaco calle principal palo sano frente al comedor",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1958,12,16),

		"lugarNacimiento": "cariaco", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,4,20),

		"fechaIngresoUCI": datetime(2014,4,30),

		"resumenIngreso": '''Se trata de paciente masculino, de 56 años de edad, natural y procedente de la localidad de cariaco, sin antecedentes patológicos conocidos, quien inicia enfermedad actual el día 19/04/2015 cuando posterior a caída desde sus propios pies presenta perdida del estado de conciencia y posteriormente lenguaje disartrico y hemiparesia izquierda por lo que es llevado a ambulatorio de la localidad, siendo referido a nuestro centro asistencial, es evaluado porel servicio de medicina interna e ingresado con diagnóstico de:''', 


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente es trasladado en camilla de transporte,  intubado conectado a ventilador de traslado,; se traslada a cama UCI, conectándose a ventilación mecánica y a monitor cardiaco externo que reporta signos vitales: TA: 131/72 mmHg(97) FC: 65 lpm FR: 12 rpm SPO2: 100 %''',
			
			"piel" : 	'''	morena, Normotérmica al tacto, llenado capilar <3 segundos, con ligera pálidez cutáneo mucosa.''',
			"cabeza": ''' se evidencia herida quirúrgica cubierta con apósitos esteril limpio y seco.''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos rítmico regulares, sin soplos ni galope. ''',
			"abdomen": ''' blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes. ''',

			"neurologico": '''Paciente bajo efectos de sedación farmacológica, Glasgow no evaluable. Pupilas mióticas, no reactivas a la luz.''',

		}, 

		"diagnosticoIngresoUCI": [
									"Post-operatorio inmediato de Craneotomía para drenaje de  hematoma intraparenquimatoso  Frontoparietal derecha",
									"Hematoma intraparenquimatoso temporoparietal izquierda.",
									"Trastorno hematológico: anemia leve",
									"Trastorno hidroelectrolítico",
									"Trastorno Acido Base: Acidosis metabólica descompensada más hiperoxemia.",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 170/80 mmHg FC: 65 lpm FR: 15 rpm SPO2: %. Paciente permanece en el servicio de emergencia 48 horas. Recibiendo tratamiento médico a base de enalapril, amlodipino, somacina posteriormente es trasladado a área de hospitalización en piso donde persiste con alteración del sensorio motivo por el cual deciden realizar estudio por imágenes TAC de cráneo  el día 24/04/2015 con hallazgos de hematoma intraparenquimatoso frontoparietal derecho y hematoma intraparenquimatoso temporoparietal izquierdo , se solicita valoración por el Servicio de Neurocirugía, se cumple valoración el día 30/04/2015 y en vista de hallazgos ya mencionados es llevado a mesa operatoria donde bajo anestesia general se realiza craniotomia  drenando hematoma intraparenquimatoso frontoparietal derecha de 210 cc aproximadamente  de contenido hemático, se realiza comprobación de hemostasia. Cierre por plano y es trasladado a unidad de cuidados intensivos para cuidados post operatorios.''',
			"piel": '''Normotérmica al tacto, llenado capilar <3 segundos. ''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, no agregados. ''',
			"abdomen": '''blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes.''',
			"extremidades": '''eutróficas, simétrica sin edema''',
			"neurologico": '''Paciente somnoliento lenguaje disartrico.''',
			

		},  

		"diagnosticoIngresoHUAPA": [
							"Síndrome de abstinencia alcohólica ",
							"ACV en evolución ",
							"Traumatismo craneoencefálico moderado",  
	

		], 
		
	},# 160

	{
		"IdHistoria": "51-08-95", 
		
		"nombre": "Luis José Suarez  ", 		
		
		"edad": "45",
		
		"ci": "14.671.774 ", 
		
		"dirección": "AV las palomas sector las quintas (detrás del terminal de pasajeros) ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1969,12,13),

		"lugarNacimiento": "Cumaná ", 		
			 		
		"fechaIngresoHUAPA":   datetime(2015,2,13),

		"fechaIngresoUCI": datetime(2015,2,2),

		"resumenIngreso": '''Paciente masculino de 45 años de edad natural y procedente de la localidad con antecedentes patológicos de hipertensión arterial sistémica en tratamiento con catapresan, Nifedipino 30 mg BID  guayaten (minoxidil) 1 tableta OD,  Enfermedad renal crónica en diálisis peritoneal hace 1 año, inicia enfermedad actual el día 26/01/2015 cuando presenta dolor abdominal difuso de predominio localización de inserción de catéter de tenckhoff  motivo por el cual  acude a consulta de Nefrología donde indican tratamiento médico a base de ampicilina sulbactam, Fluconazol los  cuales se cumplen durante 8 días además de  vancomicina 2 dosis sin mejoría clínica. El día 2/02/2015 se anexa al cuadro salida de secreción purulenta, aumento de volumen, calor y rubor de zona de inserción de catéter de tenckhoff.  Es trasladado a control de Nefrología quien decide su ingreso en el Servicio de Medicina Interna con los diagnosticos Peritonitis punto de partida catéter de tenckhoff''',

		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, recibiendo oxígeno por mascarilla facial, se traslada a cama de UCI, se conecta a monitor cardíaco externo que reporta: TA: 63/42mmhg, FC: 113lpm, FR:12 rpm, SPO2:65%. Paciente que persiste hipoxemica, lo cual se constata por gases arteriales, se realiza intubación endotraqueal, evolucionando a la bradicardia progresando a la asistolia se realizan maniobras de  RCP básica y avanzada, evolucionando de forma satisfactoria  recuperando frecuencia cardiaca a ritmo sinusal, persistiendo hipotensa requiriendo la reposición de líquido con solución ringer hasta 1000cc  evidenciando cifras de TA:110/73 (92)mmhg.''',
			
			"piel" : '''Morena, normotermica al tacto se evidencia moderada palidez cutáneo mucosa,  mucosa oral seca  llenado capilar >3seg.''',

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes, disminuidos en base pulmonar izquierda. Ruidos cardíacos taquicárdicos  regulares, sin soplo ni galope.''',
			"abdomen": '''distendido, timpánico, ruidos hidroaéreos ausentes, se evidencia hematoma en hipocondrio y flanco derecho, impresiona dolor difuso  a la palpación.''',

			"neurologico": '''inconsciente, Glasgow: 3/15pts, Respuesta Motora: 1pto, Respuesta Verbal: 1pto, Apertura Ocular: 1pto. Pupilas isocóricas, hiporreactivas a la luz.''',

		}, 

		"diagnosticoIngresoUCI": [
									"Estado post RCP",
									"Insuficiencia Respiratoria aguda",
									"Infección Respiratoria Baja: neumonía basal izquierda complicada con Derrame Pleural Izquierdo.",
									"Sepsis punto de partida abdominal: pancreatitis Aguda de origen Biliar",
									"Insuficiencia Renal Aguda (pre Renal)",
									"Hipertensión Arterial sistémica.",
									"Trastorno Hidroelectrolítico: Hipernatremia ",
									"Trastorno Acido/Base: acidosis metabólica descompensada con alcalosis respiratoria mas hipoxemia.",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": '''TA: 140 /80 mmHg;FC:80 lpm; FR: 19 rpm. Permanece en el are de emergencia durante 48 horas recibiendo tratamiento médico a base de tazocin 2.5 gr cada 12 horas para el día 4/02/2015 es trasladado al are de observación anexándose al tratamiento médico vancomicina 1 gr stat y luego 1 dosis cada 72 horas. Para el día 5/02/2015 se realiza diálisis peritoneal sin complicaciones, el día 6/02/2015 es reevaluado por servicio de nefrología quien decide indicar tazocin 1gr cada 8 horas en vista evolución tórpida, para el día 12/02/2015 es llevado a diálisis peritoneal en horas de la mañana  siendo diferido el procedimiento en vista de evidenciar obstrucción del catéter de tenckhoff. Presentando en horas de la noche hipertensión arterial TA: 270/130 mmhg episodio de congestión pulmonar, hipoxemia evolucionando a parada cardio respiratoria, realizan RCP  con evolución satisfactoria comunican caso con especialista de guardia quien indica valoración por UCI. Se realiza valoración por Servicio de UCI quien en vista de paciente presentar  trabajo respiratorio además de salida de secreción asalmonada atravez de cavidad oral, hipoxemia constatada por gases arteriales  , deterioro del estado neurológico dado por Glasgow 6/15 pts. RM 1 pt RO 4 pts. RV 1 pt se decide intubación endotraqueal con tubo.''',
			"piel": '''blanca  normotermica, normohidratada, llenado capilar < de 3 seg.''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax, con agregados tipo roncos bilaterales, ruidos cardiacos rítmicos regulares sin soplo ni galope.''',
			"abdomen": '''plano, ruidos hidroaéreos presentes, se evidencia catéter de diálisis peritoneal en hemiabdomen izquierdo blando depresible doloroso a la palpación superficial y profunda, no visceromegalia.''',
			"extremidades": '''simétricas, con  edema grado 3.''',
			"neurologico": '''consciente, orientada en 3 planos. ''',

		},  

		"diagnosticoIngresoHUAPA": ["Peritonitis punto de partida catéter de tenckhoff"], 
		
	}, #161

	{
		"IdHistoria": "49-43-57", 
		
		"nombre": "Marlis Margarita Sanez ", 		
		
		"edad": "19",
		
		"ci": "25.657.173 ", 
		
		"dirección": "Sector Caiguire, detrás del Estadium",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1994,6,30),

		"lugarNacimiento": "", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,1,24),

		"fechaIngresoUCI": datetime(2014,1,24),


		"resumenEgreso": '''Se trata de paciente femenina gestante de 19 años de edad, sin antecedentes patológicos conocidos, quien refiere inicio de enfermedad actual el día de hoy cuando presenta cefalea de fuerte intensidad localizada a nivel frontal, mareos y escotomas motivos por los cuales acude a al Servicio de Sala de Parto de este centro hospitalario donde se evalúa y se evidencia cifras tensionales de 175/115 mmHg motivos por los cuales se ingresa con los diagnósticos de: II Gesta. Embarazo de 30 semanas por ECO. ARO: Trastorno Hipertensivo del Embarazo: Preeclampsia Severa. Disfunción Renal''', 


		"examenFisicoIngresoUCI": {

			
			"piel" : 	'''Morena, normotérmica, con ligera pálidez cutáneo mucosa.''',
			
			"ojos": ''' Se evidencia edema bipalpebral.''',

			"cardiopulmonar":  '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes, se auscultan sibilantes bilaterales, no se auscultan agregados, ruidos cardíacos rítmicos regulares, taquicárdicos, sin soplos.	''',
			"abdomen": ''' Globoso, blando, depresible, no doloroso a la palpación, ruidos hidroáreos ausentes. ''',

			"neurologico": '''Inconsciente, Glasgow: 7/15pts, Respuesta Motora: 5pts, Respuesta Verbal: 2pts, Apertura Ocular: 1pt, pupilas isocóricas, hiporreactivas a la luz.''',
			"extremidades": '''Simétricas, eutróficas, se evidencia edema en ambos miembros inferiores grado II, frío, que deja fóvea.''',
			"genitales": ''' de aspecto y configuración normal, se evidencia edema vulvar. ''',

		}, 


		"diagnosticoIngresoUCI": [
									"Postoperatorio Inmediato de Cesárea Segmentaria por Eclampsia",

									"Trastorno Hipertensivo del Embarazo: Preeclampsia Severa",

									"Trastorno Acido/Base: Acidosis Metabólica Descompensada con Alcalosis Respiratoria",
									{"resumen": '''La paciente permanece en el Servicio durante 72 horas, donde evoluciona de forma satisfactoria, el día 25/01 se le realiza Tomografía de Cráneo donde no se evidencian alteraciones, en vista de mejoría del estado neurológico y de gases arteriales adecuados se realiza extubación el día 26/01,  se coloca mascarilla facial recibiendo oxígeno húmedo a  8 litros por minuto tolerándolo sin complicaciones. En vista de evolución clínica satisfactoria se decide su egreso y traslado a Servicio de Gineco-Obstetricia para continuar manejo. '''},


								],
								
		"diagnosticoEgresoUCI": [
									"Postoperatorio Mediato de Cesárea Segmentaria por Eclampsia",
									"Trastorno Hipertensivo del Embarazo: Preeclampsia Severa",
									"Trastorno Hematológico: Anemia Leve",
									"Trastorno Acido/Base: ",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se evalúa paciente en aparentes buenas condiciones generales, eupneica. Signos Vitales: TA: 175/115mmHg. FC: 79lpm. FR: 17rpm. Se traslada paciente a Área de Cuidados Intermedios recibiendo antihipertensivos (Sulfato de Magnesio, Aldomet) además de esteroides para maduración pulmonar, durante su estancia la paciente  presenta movimientos tónico-clónicos generalizados, sialorrea, desviación de la comisura labial, motivos por los cuales es llevada a mesa operatoria para realización de Cesárea Segmentaria, durante abordaje a cavidad se evidencia de salida de aproximadamente 4000cc de líquido ascítico, se drena y se realiza limpieza de cavidad abdominal y se realiza cierre por planos, se evidencia además cifras tensionales de 80/50mmHg, y persistencia de deterioro neurológico, motivos por los cuales se solicita valoración por UCI. Se acude a evaluar paciente en área de quirófano en malas condiciones generales, ventilando espontáneamente, hemodinámicamente estable, conectada a monitor cardíaco externo que reporta: TA: 109/64 mmHg. FC: 125lpm FR: 29rpm. SPO2:96%''',
			"piel": ''' Morena, normotérmica, con ligera pálidez cutáneo mucosa.''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes sin agregados, ruidos cardìacos rítmicos regulares, sin soplos.''',
			"abdomen": '''grávido a expensas de feto único, longitudinal, cefálico, movimientos fetales presentes.''',
			"extremidades": '''Simétricas, eutróficas, se evidencia edema en ambos miembros inferiores grado III.''',
			"neurologico": '''Consciente, orientada en 3 planos, Hiperreflexica.''',
			

			"ojos": ''' Se evidencia edema bipalpebral.''',

			"genitales": ''' de aspecto y configuración normal, se evidencia edema vulvar. Tacto: vagina, normotérmica, normoelástica, cuello central, largo, permeable en OCE.''',

		},  

	},# 162


	{
		
		"nombre": "JUAN BRUZUAL", 		
		
		"edad": "20",
		
		"ci": "24.690.260", 
		
		"dirección": "las palomas",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1995,5,2),

		"lugarNacimiento": "cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,5,31),

		"fechaIngresoUCI": datetime(2015,6,1),


		"resumenIngreso": '''Se trata de paciente masculino de 20 años de edad natural y procedente de la localidad con antecedentes patológicos de farmacodependencia, quien inicia enfermedad actual el dia domingo  31/05/2015 en horas de la mañana, cuando posterior a recibir herida por arma de fuego en región temporo parietal izquierda presenta perdida del estado de conciencia   es trasladado a nuestro centro  asistencial siendo evaluado por el servicio de Traumatología  quien decide su ingreso ''',


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, intubada recibiendo O2 por ambu, se traslada a cama de UCI, se conecta a ventilación mecánica y a monitor cardíaco externo que reporta: Signos Vitales: TA: 118/64 (95) mmHg; FC: 93 lpm; FR: 14 rpm; SPO2:100%''',
			
			"piel" : 	'''	blanca, hidratada, con moderada pálidez cutáneo-mucosa, llenado capilar < 3 segundos.''',
			"cabeza": ''' Se evidencia vendaje impregnado de secreción hemática  que cubre herida por proyectil de arma de fuego. Y apósito que cubre conducto auditivo externo.''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax con agregados roncus bilaterales a predominio de hemitorax derecho, ruidos cardiacos rítmicos regulares, sin soplo ni galope. ''',
			"abdomen": ''' plano, ruidos hidroáreos presentes blando depresible no impresiona a la palpación  sin megalias.''',

			"neurologico": ''' paciente bajo efectos de sedación farmacológica Glasgow no evaluable, pupilas isocóricas hiporreactivas a la luz.''',
		}, 



		"diagnosticoIngresoUCI": [
									"Traumatismo craneoencefálico severo por herida por proyectil de arma de fuego en región temporo parietal izquierda.",
									"Trastorno hematológico ",
									"Anemia moderada",
									"Trombocitopenia",
									"Trastorno hidroelectrolítico:",
									"Hipokalemia",
									"Trastorno acido base",
									"Acidosis metabólica compensada  más hiperoxemia.",
									{"resumen": ''' Paciente permanece durante 13  días en la unidad de cuidados intensivos recibiendo tratamiento a base de ceftaxidima , vancomicina, epamin  (13 días), meropenem (3 días), acetab (2 días), intubado y conectado a ventilación mecánica, siendo transfundido en múltiples oportunidades en vista de presentar cifras de hemoglobina bajas (HB: 6.5), para posteriormente ser llevado a mesa operatoria para resolución quirúrgica, la cual se cumple el día 10/06/2015 donde bajo anestesia general se realiza craniectomía fronto temporo parietal  izquierda, limpieza quirúrgica cierre por planos y asepsia final. Trasladando nuevamente a unidad de cuidados intensivos, evidenciando 24 horas posteriores a acto quirúrgico salida de LCR por herida quirúrgica y conducto auditivo ipsilateral, que impregna cura quirúrgica persistiendo hasta la actualidad, en vista de estado neurologico se decide iniciar plan de destete ventilatorio, hasta alcanzar extubación el día 12/06/2015 sin complicaciones, por mejoría clínica y paraclínicas se decide su egreso a área de hospitalización a cargo de servicio de Neurocirugía. '''}

								],

		
		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente presenta deterioro del estado neurológico por lo que es intubado por el servicio de traumatología y conectado a T de ayres, solicitan valoración por el servicio de terapia intensiva quien acude al llamado evaluando paciente en área de quirofanito, intubado recibiendo oxigeno por T de ayres, se realiza verificación de entubación endotraqueal constatando tubo en vías digestivas, por lo que se procede a  re intubar con tubo 7.5 FR sin complicaciones, se realizan sugerencias en vista de no contar con disponibilidad de cupo. Paciente es trasladado a área de recuperación de quirófano permaneciendo durante 12 horas  conectado a ventilación mecánica, en vista de disponibilidad de cupo se decide ingresar en el servicio de Terapia intensiva.''',
			"piel": '''blanca, llenado capilar < 3 seg ''',
		
			"cardiopulmonar": '''tórax simétrico, normoexpansible ruidos respiratorios presentes en ambas hemitorax con agregados roncus bilaterales .ruidos  cardiacos rítmicos regulares sin soplo ni galope.	''',
			"abdomen": '''plano  ruidos hidroaéreos presentes sin megalias''',
			
			"neurologico": '''paciente estuporoso con periodos de agitación psicomotriz, pupilas isocóricas normo reactivas, Glasgow 7/15 pts. (RM:4 pts RV: 1 pts RO: 2pt). ''',
			"cabeza": ''' Se evidencia solución de continuidad en región temporo parietal izquierda con salida de masa encefálica y otorragia con salida de masa encefálica a través de conducto auditivo.   ''',

		},  

		"diagnosticoIngresoHUAPA": [
					"TEC severo",	
					"Post operatorio mediato de craniectomía fronto temporo parietal izquierda debido a herida por proyectil de arma de fuego complicada con:",
					"edema cerebral e isquemia perilesional",
					"fractura conminuta de temporal izquierdo",
					"infección respiratoria baja : neumonía asociado a ventilación mecánica mecánica",
					"infección del tracto urinario de origen micotico",
					"trastorno hematológico :anemia leve",
					"trastorno acido base ",
		], 
		
	},# 163

	{
		
		
		"nombre": "Francisca Véliz de Carvajal", 		
		
		"edad": "77",
		
		"ci": "2.294.371", 
		
		"dirección": "San Lorenzo, calle principal, #89-26, Cumanacoa.",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1937,6,16),

		"lugarNacimiento": "Cumanacoa, Edo. Sucre.", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,10,26),

		"fechaIngresoUCI": datetime(2014,10,26),

		"resumenIngreso": '''Paciente femenina de 77 años de edad, natural y procedente de Cumanacoa, con antecedentes patológicos de HTA de larga data, en tratamiento con Cozaar® 50mg OD y trastorno hematológico tipo trombocitopenia, cuyo familiar refiere inicio de enfermedad actual el día 26/10/14 en horas de la mañana,  cuando posterior a caída de sus propios pies presenta traumatismo craneoencefálico y herida a nivel parietal izquierda con, aproximadamente 12 horas posterior, pérdida del  nivel de consciencia sin recuperación espontánea, es traída a este centro donde es evaluada y se ingresa por el servicio de neurocirugía. ''',


		"examenFisicoIngresoUCI": {


			"piel" : 	'''	morena, normotérmica, con equimosis en aéreas de venopunción, llenado capilar < 3seg.''',
			"cabeza": ''' hematoma de aproximadamente 8cm de diámetro en región parietal derecha''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, normofonéticos, sin soplo ni galope.''',
			"abdomen": ''' globoso a expensas de panículo adiposo, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, sin signos de irritación peritoneal, no megálico.''',

			"neurologico": '''inconsciente, pupilas anisocóricas, arreactivas a estímulo luminoso, Glasgow 6/15pts (RM: 4pts, RO: 1pto, RV: 1pto), sin aparentes focalidad, no clonus, no babinsky, sin clínica de meningismo ni de hipertensión endocraneana, FM III/V en MsIs y II/V en MsSs, normotónica y normorrefléxica.  ''',
			"extremidades": '''simétricas, sin edema, movimientos activos de 4 extremidades.''',
			
		}, 

		"diagnosticoIngresoUCI": [
								"TRAUMATISMO CRANEOENCEFALICO SEVERO  Vs. EVC DE ETIOLOGIA A PRECISAR.",
								"HIPERTENSION ARTERIAL SISTEMICA",
								"TRASTORNO HEMATOLOGICO:",
								"ANEMIA MODERADA",
								"TROMBOCITOPENIA",
								"TRASTORNO ÁCIDO-BASE: ",
								"ACIDOSIS METABOLICA COMPENSADA CON ALCALOSIS RRSPIRATORIA + HIPEROXEMIA. ",
	
								],

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' FC: 94 lpm; FR: 26 rpm; TA: 126/98 mmHg. En vista de estado neurológico del paciente solicitan evaluación por UCI al momento de su ingreso, se evalúa paciente en área de quirofanito, en vista de deterioro neurológico se procede a realizar intubación endotraqueal con tubo 7 Fr y por disponibilidad de cupo se ingresa a la UCI. Se recibe paciente en camilla de traslado, intubado y recibiendo apoyo de oxigeno húmedo por ambú® a 10 litros por minutos, se pasa a cama UCI, se conecta a monitor cardíaco continuo que reporta: TA: 168/92 (138) mmHg;  FC: 129 lpm;  FR: 18 rpm;  SatO2: 100%''',
		
		
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, normofonéticos, sin soplo ni galope.''',
			"abdomen": '''globoso a expensas de panículo adiposo, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, sin signos de irritación peritoneal, no megálico''',
			
			"neurologico": '''inconsciente, pupilas anisocóricas, arreactivas a estímulo luminoso, Glasgow 6/15pts (RM: 4pts, RO: 1pto, RV: 1pto), sin aparentes focalidad, no clonus, no babinsky, sin clínica de meningismo ni de hipertensión endocraneana, FM III/V en MsIs y II/V en MsSs, normotónica y normorrefléxica. ''',
			"cabeza": ''' hematoma de aproximadamente 8cm de diámetro en región parietal derecha.''',

		},  

		"diagnosticoIngresoHUAPA": ["TRAUMATISMO CRANEOENCEFALICO SEVERO  COMPUESTO CERRADO.", "TRASTORNO HEMATOLOGICO: TROMBOCITOPENIA EN ESTUDIO."], 
		
	},# 164

	{
		"IdHistoria": "53-25-62 ", 
		
		"nombre": "Lazaro Antonio Diaz", 		
		
		"edad": "56",
		
		"ci": "6.657.893", 
		
		"dirección": "muelle de cariaco calle principal palo sano frente al comedor",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1958,12,16),

		"lugarNacimiento": "Cariaco", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,4,20),

		"fechaIngresoUCI": datetime(2015,4,30),



		"resumenIngreso": '''Se trata de paciente masculino,  de 56 años de edad, natural y procedente de la localidad de cariaco, sin antecedentes patológicos conocidos, quien inicia enfermedad actual el día 19/04/2015 cuando posterior a caída desde sus propios pies presenta perdida del estado de conciencia y posteriormente lenguaje disartrico y hemiparesia izquierda por lo que es llevado a ambulatorio de la localidad, siendo referido a nuestro centro asistencial, es evaluado porel servicio de medicina interna e ingresado con diagnóstico de:''',

		"examenFisicoIngresoUCI": {

			"resumen": '''Paciente es trasladado en camilla de transporte,  intubado conectado a ventilador de traslado,; se traslada a cama UCI, conectándose a ventilación mecánica y a monitor cardiaco externo que reporta signos vitales: TA: 131/72 mmHg(97) FC: 65 lpm FR: 12 rpm SPO2: 100% ''',
			
			"piel" : 	'''	morena, Normotérmica al tacto, llenado capilar <3 segundos, con ligera pálidez cutáneo mucosa.''',
			"cabeza": ''' se evidencia herida quirúrgica cubierta con apósitos esteril limpio y seco.''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos rítmico regulares, sin soplos ni galope. ''',
			"abdomen": '''blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes.''',

			"neurologico": ''' Paciente bajo efectos de sedación farmacológica, Glasgow no evaluable. Pupilas mióticas, no reactivas a la luz.''',
		

		}, 

		"diagnosticoIngresoUCI": [
								"Post-operatorio inmediato de Craneotomía en región frontal para drenaje de  hematoma subdural  Frontal",
								"Hematoma subdural occipital.",
								"Trastorno hematológico: anemia leve",
								"Trastorno hidroelectrolítico",
								"Trastorno Acido Base: Acidosis metabólica descompensada más hiperoxemia.",
									
								],

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 170/80 mmHg FC: 65 lpm	FR: 15 rpm SPO2: %. Paciente permanece en el servicio de emergencia 48 horas. Recibiendo tratamiento médico a base de enalapril, amlodipino, somacina posteriormente es trasladado a área de hospitalización en piso donde persiste con alteración del sensorio motivo por el cual deciden realizar estudio por imágenes TAC de cráneo  el día 24/04/2015 con hallazgos de hematoma subdural frontal y occipital, se solicita valoración por el Servicio de Neurocirugía, se cumple valoración el día 30/04/2015 y en vista de hallazgos ya mencionados es llevado a mesa operatoria donde bajo anestesia general se realiza craniotomia en región frontal drenando hematoma subdural de región frontal de 210 cc aproximadamente  de contenido hemático, se realiza comprobación de hemostasia. Cierre por plano y es trasladado a unidad de cuidados intensivos para cuidados post operatorios.''',
			"piel": ''' Normotérmica al tacto, llenado capilar <3 segundos. ''',
		
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, no agregados. ''',
			"abdomen": '''blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes.''',
			"extremidades": '''eutróficas, simétrica sin edema''',
			"neurologico": '''Paciente somnoliento lenguaje disartrico.''',
			
		},  

		"diagnosticoIngresoHUAPA":[
			"Síndrome de abstinencia alcohólica ",
			"ACV en evolución ",
			"Traumatismo craneoencefálico moderado  ",

		], 

		
	},# 165

	{
		
		"nombre": "José Salvador Rodríguez Gamboa    ", 		
		
		"edad": "27",
		
		"ci": "18.099.771", 
		
		"dirección": "La Campiña calle principal Guiria. ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1986,12,5),

		"lugarNacimiento": "Carúpano ", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,7,31),

		"fechaIngresoUCI": datetime(2014,7,31),

		"resumenIngreso": '''Se trata de paciente masculino de 27 años de edad procedente de la localidad sin antecedentes patológicos personales quien inicia enfermedad actual hace 24 horas cuando posterior a accidente  de tránsito tipo colisión a bordo de moto y presenta múltiples traumatismos acompañado de pérdida de la consciencia siendo trasladado al hospital de Carúpano donde es evaluado e inmediatamente trasladado hacia la ciudad de cumana. Al momento del ingreso presenta TA: 114/69 mmHg, FC: 98 lpm y FR: 24 rpm, al examen físico de ingreso presenta piel y mucosas húmedas y normo coloreadas tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares sin agregados Ruidos cardiacos rítmicos no soplos abdomen blando depresible no doloroso palpación superficial ni profunda no megalias Neurologico , Glasgow 7/15pts (RM: 5pts, RO: 1pto, RV: 1pto)pupilas isocóricas reactivas reflejo corneal presente .Se ingresa con diagnosticos de : TCE SEVERO ,TX TORACOABDOMINAL CERRADO  En vista de malas condiciones generales de paciente solicitan valoración por UCI y por disponibilidad de cupo se decide su ingreso a Unidad de Cuidados Intensivos . ''',


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, estable hemodinámicamente, no intubado y recibiendo O2 por canula nasal a razón se 5 lt por minuto , se pasa a cama UCI se procede a realizar intubación endotraqueal con TET 7.5 F  sin complicaciones es conecta a VM modo  AC con parámetros VC 560 FIO2 50 FL 50 PEEP 0 FR 12 y se conecta a  monitor cardíaco continuo que reporta:  TA: 115/70(61) mmHg;     FC: 86  lpm;      FR: 12 rpm;      SatO2: 99%. Se realize VVC derecha Via Yugular posterior sin complicaciones con xifonaje positive en ambos lumenes se realize rayos x control. Se observa TAC de CRANEO realizada en carupano donde se identifica hematoma epidural fronto parietal izquierdo con contusiones hemorrágicas fronto temporales ,se comunica a Servicio de Neurocirugia .''',
			
			"piel" : '''hipertérmica al tacto, llenado capilar < 3seg.''',
			

			"cardiopulmonar":  '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados . Ruidos cardíacos rítmicos y regulares, taquicardicos, sin soplo ni galope.''',
			"abdomen": '''ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico.	''',

			"neurologico": ''' Inconsciente Glasgow 7/15 puntos RM 5 RV 1 RO 1 Pupilas isocóricas reactivas reflejo corneal presente.''',
			"extremidades": '''eutróficas, simétricas, sin edema.''',
			

		}, 


		"diagnosticoIngresoUCI": [
									"TRAUMATISMO CRANEOENCEFALICO SEVERO C/C",
									"HEMATOMA EPIDURAL FRONTO PARIETAL IZQUIERDO",
									"EDEMA CEREBRAL DIFUSO",
									"HEMORRAGIA SUBARACNOIDEA POST TRAUMATICA ",

								],

	},# 166

	{
		"IdHistoria": "43-41-01", 
		
		"nombre": "Juan Segundo Yegres Contreras ", 		
		
		"edad": "73",
		
		"ci": "2.920.929 ", 
		
		"dirección": "Las Colinas Cumanacoa ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1940,5,6),

		"lugarNacimiento": "Cumanacoa ", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,10,25),

		"fechaIngresoUCI": datetime(2014,10,25),

		"resumenIngreso": '''Paciente masculino de 73 años de edad natural y procedente de la localidad con antecedentes patológicos personales de Insuficiencia Cardiaca además de trastorno del ritmo Fibrilacion auricular crónica , lleva tratamiento con Lasix 40 mg OD ,Aldactone 25 mg OD ,Pradaxa 150 mg OD ,Digoxina 0.25 mg OD .Inicia enfermedad actual hace 48 horas debido a la presencia de disnea súbita progresiva acompañado de palpitaciones  por lo cual es llevado a clínica de la localidad donde se administran Lasix 40 mg y es referido a este centro asistencial ''',

		"examenFisicoIngresoUCI": {

			"piel" : 	'''	hipotérmico al tacto, llenado capilar < 3seg.''',

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, disminuidos globalmente con estertores crepitantes universales  taquipneico. Ruidos cardíacos taquicárdicos  y regulares, sin soplo ni galope.''',
			"abdomen": '''plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico ''',

			"neurologico": ''' consciente, orientado, pupilas isocóricas, reactivas a la luz.''',

		}, 


		"diagnosticoIngresoUCI": [
									
										"INSUFICIENCIA CARDIACA DESCOMPENSADA EN EDEMA AGUDO DE PULMON ",
										"TRASTORNO DEL RITMO : FIBRILACION AURICULAR CRONICA ",
										"BLOQUEO COMPLETO RAMA IZQUIERDA DEL HAS DE HISS",
										"INSUFICIENCIA RENAL CRONICA REAGUDIZADA",
										"HTA SISTEMICA CONTROLADA ",
										"TRASTORNO HEMATOLOGICO : ",
										"PT Y PTT PROLONGADO ",
										"TRASTORNO ACIDO BASE : ACIDOSIS METABOLICA DESCOMPENSADA + ALCALOSIS RESPIRATORIA", 
										"TRASTORNO HIDROELECTROLITICO:HIPERKALEMIA ",

								],


		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 150/90 mmHg; FC: 56 lpm; FR: 32 rpm; SatO2: 99%''',
			
			"piel": ''' hipotérmico al tacto, llenado capilar < 3seg.''',
			
			"cardiopulmonar": '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares,disminuidos globalmente con estertores crepitantes universales taquipneico. Ruidos cardíacos taquicárdicos y regulares, sin soplo ni galope.''',
			
			"abdomen": '''plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico''',
	
			"neurologico": '''consciente, orientado , pupilas isocóricas, reactivas a la luz.''',
		

		},  

		"diagnosticoIngresoHUAPA": [
							"INSUFICIENCIA CARDIACA DESCOMPENSADA EN EDEMA AGUDO DE PULMON ",
							"FARVR",
							"HTA SISTEMICA CONTROLADA ",
							{"resumen": ''' Paciente que es evaluado por servicio de terapia intensiva y debido a disponibilidad de cupo se decide su ingreso. Se recibe paciente en camilla de traslado tolerando oxigeno húmedo mediante cánula nasal a 3 lt por minuto se conecta a monitor cardiaco que reporta. FC 112 LPM    FR 34 RPM       TA 124/67 MMHG      SAT O2 99 % '''}
	
		], 
		
	},# 167

	{
		
		"nombre": "Luis Jose Riera Lara ", 		
		
		"edad": "32",
		
		"ci": "16.311.785  ", 
		
		"dirección": "Santa Fe, brisas de cuchapal calle principal casa sin numero frente al ambulatorio",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1981,7,5),

		"lugarNacimiento": "cumana", 		
			 		
		"fechaIngresoHUAPA": datetime(2014,3,26),
		"fechaIngresoUCI": datetime(2014,3,26),

		"resumenIngreso": '''Se trata de paciente masculino de 32 años de edad con diagnostico de Diabetes Mellitus tipo 2 desde Enero 2013 tratado con Metformina (no espicifica dosis), sin control por especialista cuyo familiar refiere abandono de tratamiento hace aproximadamente 1 mes. Inicia enfermedad actual el día 21/03/14, cuando presenta disnea de aparición progresiva a medianos esfuerzos, persistiendo síntomas hasta el día 22/03/14 , anexándose al cuadro en horas de la tarde perdida de consciencia, por lo que es llevado a centro asistencial de la localidad donde es evaluado y referido a este centro donde se decide su ingreso ''',


		"examenFisicoIngresoUCI": {

			"piel" : 	'''	morena, normotermica al tacto, deshidratado. ''',
	

			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible, ruidos respiratorios presentes MV disminuido en base derecha, sin agregados, ruidos cardíacos rítmicos, regulares, sin soplos ni galope. ''',
			"abdomen": ''' globoso, blando, depresible, ruidos hidroaéreos presentes, no megálico.''',

			"neurologico": ''' Paciente somnoliento, desorientado  Glasgow 11/15 puntos ( RM 5 RO 4 RV 2)''',
		}, 

		"diagnosticoIngresoUCI": [

							"Diabetes Mellitus descompensada en cetoacidosis diabética",
							"Inestabilidad hemodinámica",
							"Deshidratación severa.",
							"Pancreatitis aguda",
							"Trastorno hematológico: Anemia moderada, Trombocitopenia",
							"Trastorno Metabolico: hipertrigliceridemia",
							"Trastorno HIdro electrolítico: Hipernatremia",
							"Trastorno acido básico: acidosis metabólica descompensada",

									
								],


		"examenFisicoIngresoHUAPA": {
			"resumen": '''TA: 130 /90 mmHg FC: 120 lpm FR: 16 rpm SPO2: 99''',
			"piel": '''morena, normotermica al tacto, deshidratación moderada, signo del pliegue positivo. ''',
		
			"cardiopulmonar": '''Tórax simétrico, hiperexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos taquicárdicos rítmicos, regulares, sin soplos ni galope. ''',
			"abdomen": '''globoso, blando, depresible, ruidos hidroaéreos presentes, no megálico.''',
	
			"neurologico": '''Paciente desorientado en tiempo y espacio Glasgow 11 puntos''',

		},  

		"diagnosticoIngresoHUAPA": [
								
		"Diabetes Mellitus tipo 2 descompensada en Cetoacidosis Diabética",
		{"resumen":''' Paciente que fue evaluado por residente de guardia de UCI quien por disponiblidad de cupo y estado del paciente se decide su ingreso. Recibimos paciente en  camilla de traslado recibiendo oxigeno mediante mascarilla autoinsuflable  conectada  a reservorio, no conectado a monitor cardiaco. Se traslada a cama UCI y se conecta a monitor cardiaco que reporta:FR:13 rpm FC:80 lpm TA:82/49(65) mmHg SATO2: 100%'''}
		], 
		
	},# 168

	{
		
		"nombre": "Elvis Daniel Suárez Benítez", 		
		
		"edad": "18",
		
		"ci": "25.700.102", 
		
		"dirección": "CUMANA",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1995,7,19),

		"lugarNacimiento": "Cumaná – Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,5,18),

		"fechaIngresoUCI": datetime(2014,6,16),


		"resumenIngreso": '''Se trata de paciente masculino 18 años de edad, natural y procedente de la localidad, sin antecedentes de patológicos de importancia, cuyo familiar refiere  inicio de enfermedad actual el día 18 de mayo de 2014, cuando presenta traumatismo toraco-abdominal penetrante posterior a recibir herida por arma de fuego con orificio de entrada a nivel de 10º  EIC con línea axilar posterior izquierda y orificio de salida en hipocondrio derecho,  es trasladado a este centro de Salud e ingresa al Servicio de Cirugía Blanda. ''',


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente que se recibe en camilla de transporte, tolerando aire ambiente, se traslada a cama de UCI, conectándose a monitor cardiaco externo que reporta signos vitales: TA: 153/110mmHg FC: 123 lpm FR: 24 rpm SatO2: 100%''',
			
			"piel" : 	'''	Morena, normotérmica, deshidratada, con moderada palidez cutáneo mucosa, llenado capilar < 3 segundos. ''',
		

			"cardiopulmonar":  '''Estable hemodinámicamente, tórax simétrico hipoexpansible, no se observa tirajes subcostal ni intercostal. Ruidos cardiacos regulares taquicárdicos, sin soplos ni galope; ruidos respiratorios presentes disminuidos en ambas bases, sin agregados. ''',
			"abdomen": ''' Plano, blando, depresible,  apósitos estériles que cubren herida quirúrgica de laparotomía con puntos de tensión, con secreción serohemática,  se evidencian 4 drenes: un tubo de tórax 28 fr dirigido a lecho pancreático, 2 en ambas correderas parietocólicas y un dren de Nelaton 20 Fr en fondo de saco, conectados a  su bolsa recolectora con gasto hemático. Presenta evacuaciones líquidas abundantes fétidas y expulsando flatos.''',

			"neurologico": '''consciente, orientado, pupilas isocóricas normorreactivas a la luz, Glasgow: RO: 4 ptos RV: 5 ptos RM: 6 ptos  15/15 ptos. Sin signos de focalización neurológica ni signos de irritación meníngea.''',
			"extremidades": '''simétricas sin edema, movimientos activos y pasivos conservados.''',

		}, 
		"diagnosticoIngresoUCI": [
								
								"Sepsis Severa con Falla de Múltiples Órganos.",
								"Postoperatorio Mediato de Relaparotomía por colección hemática intrabdominal y adherensiolisis. ",
								"Postoperatorio Tardío de Laparotomía Exploradora por Traumatismo toraco-abdominal izquierdo penetrante por herida por proyectil por arma de fuego complicada con:",
								"Lesión grado II en: Hemidiafragma izquierdo, Antro gástrico,  Segmento VII hepático, cuerpo y cola de páncreas.",
								"Lesión grado IV de bazo y Riñon izquierdo.",
								"Fistula Pancreática de Alto gasto.",
								"Esplenectomía.",
								"Nefrectomía Izquierda.",
								"Insuficiencia Renal Aguda.",
								"Trastorno hematológico:",
								"Anemia Severa",
								"Trombocitopenia. ",
								"Trastorno Acido Base:",
								"Alcalosis metabólica descompensada con acidosis respiratoria mas hiperoxemia.",

	
								],

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' No reportan signos vitales de ingreso a sala de emergencias: Ingresa en As Rs Cs Gs eupneico, tolerando aire ambiente.''',
			"piel": ''' Morena, hipotérmica al tacto, palidez cutánea y mucosa leve y llenado capilar >3 segundos. ''',
		
			"genitales": '''Normoconfigurados, con sonda de Foley conectada a bolsa recolectora con orinas claras.   ''',
			"cardiopulmonar": '''Tórax simétrico, normo expansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos normofonéticos,  sin soplos ni galope.''',
			"abdomen": '''Blando, plano, depresible, doloroso a la palpación profunda, sin signos de irritación peirtoneal, se evidencian herida por proyectil por arma de fuego con orificio de entrada en 10º EIC posterior izquierdo y orificio de salida en hipocondrio derecho, con Sonda nasogástrica funcionante conectada a bolsa recolectora con gasto hemático''',
			"extremidades": '''Simétricas sin edema, pulsos periféricos presentes.''',
			"neurologico": '''Consciente, conservado.''',

		},  

		"diagnosticoIngresoHUAPA": [
					"Traumatismo toraco-abdominal izquierdo penetrante por herida por proyectil por arma de fuego.",
					{"resumen":''' Al ingreso el paciente es llevado a quirófano y se realiza laparotomía exploradora encontrándose los siguientes hallazgos: 500 cc de hemoperitoneo libre en cavidad, lesión grado II en: Hemidiafragma izquierdo, Antro gástrico,  Segmento VII hepático, cuerpo y cola de páncreas y Lesión grado IV de bazo y Riñon izquierdo, tomándose como conducta: evacuación del hemoperitoneo y lavado de cavidad con 1000 cc de sol 0,9%, Toracotomía izquierda con tubo 36 fr obteniéndose 600 cc de contenido hemático, se realiza rafia de las lesiones de hemidiafragma izquierdo, estómago, segmento VII del hígado y páncreas, Nefrectomía izquierda, Esplenectomía y se dejan 2 drenes uno de ellos dirigido a lecho pancreático y otro en fondo de saco.  Se mantiene en el área hospitalización de cirugía blanda con los  diagnósticos de Postoperatorio Mediato de Laparotomía Exploradora por Traumatismo toraco-abdominal izquierdo penetrante por herida por proyectil por arma de fuego complicada con las lesiones descritas y Fístula pancreática de alto gasto, recibiendo antibioticoterapia con Imipenem  y Metronidazol durante 12 días,  sin embargo se mantiene febril con temperaturas que oscilan entre 39 y 40 ºC,  se asocia al cuadro clínico leucocitosis por lo que se indica Cefoperazona Sulbactan y Fluconazol, omitiéndose Imipenem el día 30/05/2014 por sugerencia de Infectología; posteriormente mejoría del gasto de drenaje torácico el día 31/05/2014 se retira el tubo de tórax. Se realizan estudios Imagenológicos Eco abdominal y Tac de abdomen que reportan dentro de límites normales.  Se toman muestras para hemo y urocultivo además de cultivo de punta de catéter y de secreción pancreática al inicio que reportaron negativos.  Para el día 09/06/2014 el paciente presenta dolor abdominal y signos de irritación peritoneal por lo que se realiza Eco Abdominal que reporta colección intrabdominal a nivel inferior de la cola del páncreas y probable colección en lóbulo izquierdo del hígado segmento IV; en vista de ello el día 10/06/2014 es llevado a mesa operatoria bajo anestesia general se realiza laparotomía supra para e infraumbilical, encontrándose adherencias firmes y laxas interasas,  a peritoneo y epiplón, evidenciándose trayecto fistuloso de pácreas a fosa ilíaca derecha dirigido con drenaje rígido sin evidencia de colección.  Se toma como conducta adherensiolisis roma y cortante y lavado de cavidad con 3000 cc de solución fisiológica,  se dejan dos drenes rígidos uno dirigido a fístula pancreática y otro en fondo de saco. En el postoperatorio inmediato el paciente permanece en el área de recuperación  presentando descenso en los controles de hemoglobina y signos de hipovolemia, por lo que solicitan reevaluación por UCI, se sugiere optimizar cifras de hemoglobina y realizar  ECO FAST el cual reporta  líquido libre en cavidad no cuantificado, el día 11/06/2014 le realizan relaparotomía xifopúbica evidenciándose Hemoperitoneo de aproximadamente 2500cc (coágulos) en cavidad  más  colección pancreática de 40 cc,  sangrado en capas  a nivel del peritoneo parietal y adherencia a hígado, se toma como conducta evacuación de coágulos y secreción pancreática fétida,  lavado de cavidad con 4000 cc de solución 0,9 %, se dejan 4 drenes un tubo de tórax 28 fr dirigido a lecho pancreático, 2 en ambas correderas parietocólicas y un dren de Nelaton 20 Fr en fondo de saco,  en vista de no disponer de cupo en UCI se mantiene en el área de recuperación intubado conectado a ventilación mecánica  durante 24 horas y posteriormente se extuba por mejoría de gasometría arterial y estabilidad hemodinámica, siendo evaluado  diariamente por el servicio. El día domingo 15 de junio,  presenta en 2 oportunidades movimientos tónicos clónicos generalizados por lo que solicitan reevaluación por el servicio de UCI y se indica Diazepam 10mg stat ameritando impregnación con Epamín, el día 16/06/2014 por disponibilidad de cupo se discute caso con Dra. Begglia Roa intensivista de  guardia y se ingresa.'''}	
		], 
		
	},# 169

	{
		"IdHistoria": "53-20-07", 
		
		"nombre": "Fredy José Cordero", 		
		
		"edad": "64",
		
		"ci": "4.189.616 ", 
		
		"dirección": "Urbanización tres picos, sector las azucenas. ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1951,2,20),

		"lugarNacimiento": "Cumaná - Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,6,9),

		"fechaIngresoUCI": datetime(2015,6,9),


		"resumenIngreso": '''Se trata de paciente masculino de 64 años de edad, natural y procedente de la localidad con antecedentes de hipertensión arterial en tratamiento con valsartan 160 mg OD, Nifelan 60 mg OD, y EVC isquémico en 2014, quien el día 19/05/2015 es llevado a mesa operatoria donde realizan remplazo de válvula mitral por prótesis mecánica ats número 20 mm, mas plastia de válvula aortica por insuficiencia aortica + cierre de comunicación interauricular, siendo trasladado a unidad de cuidados intensivos para cuidados post operatorios presentando complicación operatoria inmediata dada por regurgitación para valvular severa, ameritando nuevo tiempo en bomba cardiaca extra corpórea con tiempo total de 5 horas, manteniéndose inestable durante 24 horas con requerimientos elevados de vasoactivos, y signos de enfermedad  renal aguda requiriendo la administración de diuréticos de asa con adecuada depleción, requiriendo posteriormente la colocación de marcapaso provisional epicardico ante presencia de ritmo de la unión, ameritando durante 48 horas soporte con ventilación mecánica a  través de tubo endotraqueal por  sobrecarga hídrica  siendo posteriormente extubado.es egresado de unidad de cuidados intensivos el día 23/05/2015 permaneciendo durante 24 horas en área de hospitalización, presentando crisis hipertensiva tipo emergencia expresada en edema agudo de pulmón ameritando reingreso en unidad de cuidados intensivos, siendo reintubado y conectado a ventilación mecánica, iniciando tratamiento hipotensor y depleción de líquidos, además, uso de vasodilatadores endovenoso tipo Nitropusiato de sodio el cual requiere durante 48 horas, presentando posteriormente cuadro compatible con infección respiratoria nosocomial asociado a la ventilación mecánica, se aísla germen Gram negativo (E coli) sensible a carbapenemicos, presenta mejoría clínica y paraclínicos por lo que el día 31/05/2015 es egresado a área de hospitalización. Permanece durante 6 días presentando cambios de coloración y dolor de fuerte intensidad en miembro inferior izquierdo, se realiza eco doppler  arterial en miembros inferiores con evidencia de enfermedad ateromatosa difusa, con cambios hemodinámicos en los segmentos infrapopliteo izquierdo, el día 06/06/2015 presenta cuadro caracterizado por taquipnea, desaturación y trastornos del ritmo (FARVR) y edema agudo de pulmón, iniciando apoyo ventilatorio con BIPAP, tratamiento con diuréticos (lasix 120 mg) sin respuesta satisfactoria, por lo que es trasladado a UCI donde permanece durante 4 días, con mejoría clínica y es egresado nuevamente a área de hospitalización, donde permanece por 4 días en regulares a malas condiciones generales, presentando PO2 limitrofes, requiriendo su reingreso en unidad de cuidados intensivos el día 12/06/2015 presentando parada cardiaca secundaria a hipoxemia severa, se realiza RCP avanzado durante 4 minutos saliendo con (FARVA) siendo conectado nuevamente a ventilación mecánica, con apoyo de Vasopresores e inotrópicos de tipo dopamina, adrenalina y Dobutamina. Paciente permanece durante 6 días en unidad de cuidados intensivos,  en vista de ser natural y procedente de la localidad se decide su traslado a UCI HUAPA''',


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, traqueostomizado, conectado a ventilador mecánico de transporte, se traslada a cama de UCI, se conecta a monitor cardíaco externo que reporta: TA: 91/61(72) mmHg	FC: 98 lpm	FR: 12rpm SatO2: 95%''',
			
			"piel" : 	'''	negra, normotérmica, normoelastica, con llenado capilar > 3 Seg. ''',
	
			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible se evidencia herida quirúrgica en región esternal, ruidos respiratorios presentes en ambos hemitorax con agregados roncus bilaterales y sibilantes dispersos, Ruidos cardiacos arrítmicos, con  soplo sistólico en foco mitral y aórtico ''',
			"abdomen": ''' globoso a expensa de panículo adiposo  Blando, no doloroso a la palpación, ruidos hidroaéreos presentes, no megalias ''',

			"neurologico": ''' Paciente somnoliento. Glasgow: 9/15 pts, Respuesta Motora: 4pt, Apertura Ocular: 4pt (no conectado con el medio externo).  Respuesta Verbal: 1pt. Pupilas isocóricas reactivas a la luz. Impresiona hemiplejia derecha. ROT II/IV  ''',
			"extremidades": '''Simétricas, con edemas grado I, se evidencian lesiones en dedos de miembros inferiores con necrosis digital. ''',
		

		},

		"diagnosticoIngresoUCI": [
									"Estado Post RCP",
									"Encefalopatía post hipoxica",
									"Shock cardiogenico por disfunción ventricular severa (R)",
									"POT de :",
									"Reemplazo de válvula mitral con prótesis mecánica",
									"Plastia de válvula aortica ",
									"Cierre de comunicación interauricular ", 
									"Enfermedad renal crónica reagudizada",
									"Valvulopatia",
									"Insuficiencia mitral severa",
									"Insuficiencia aortica moderada",
									"Comunicación interauricular",
									"Trastorno del ritmo:",
									"FARVA",
									"Enfermedad vascular cerebral AD",
									"Enfermedad arterial periférica",
									"Hipertensión arterial sistémica",
									"POM de traqueostomía  ",
									"Trastorno hematológico:",
									"Anemia moderada ",
									"Trastorno hidroelectrolítico:",
									"Trastorno acido base ",
									"Alcalosis respiratoria descompensada mas hiperoxemia",


								],

		"diagnosticoEgresoPrivado": [
									
											"Condición post paro cardiaco",
											"Shock cardiogenico complicado con falla renal:",
											"Disfunción ventricular severa",
											"Enfermedad renal crónica reagudizada (clearance: 21 ml/min) secundario a :",
											"Pre- renal: disminución del volumen circulante efectivo.",
											"Renal por nefropatía hipertensiva.",
											"Trastorno del ritmo cardiaco: ritmo auricular ectópico.",
											"POM de remplazo valvular aórtico + cierre de CIA con  técnica CEC.",
											"Valvulopatia: insuficiencia mitral severa, insuficiencia aortica moderada + comunicación interauricular.",
											"Enfermedad arterial periférica.",
											"Hematuria macroscópica de EAP. ",
											{"resumen":"Paciente es trasladado en Unidad de Aero-ambulancia hasta el aeropuerto de la ciudad de Cumaná, donde se recibe en malas condiciones generales conectado a ventilador de trasporte, sin utilización de inotrópicos o vasoactivos se traslada a HUAPA, previa disponibilidad de cupo se decide su ingreso en la unidad de cuidados intensivos.", "fecha":datetime(2015,6,19)}

								],  

		
	}, #170

	{
	
		"nombre": "GEORGETE NAHAS ", 		
		
		"edad": "71",
	
		
		"dirección": "Parcelamiento miranda sector c",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1944,8,14),

		"lugarNacimiento": "Cumaná", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,12,12),

		"fechaIngresoUCI": datetime(2015,12,12),
		"antecedentes": " hipertensión arterial",


		"resumenIngreso": ''' Se trata de paciente femenina de 71 años de edad procedente de la localidad, con antecedentes de en tratamiento con Nimodipino 30 mg BID atacan (no precisan dosis ),diabetes mellitus tipo en tratamiento con insulina lantus 25 unds VSC hora sueño e insulina cristalina en dependencia de glicemia capilar, antecedentes quirúrgicos de derivación ventrículo peritoneal por hidrocefalia debido a EVC hemorrágico en el año 2012,quien inicia enfermedad actual el día miércoles 26/11/2015 en horas de la tarde cuando presenta debilidad generalizada motivo por el cual es trasladado a centro privado policlínica sucre es evaluada e indican tratamiento con solución 0,9% y somacina 500 mg vev stat, posteriormente egresando sin tratamiento médico, presentando en horas de la noche perdida del estado de conciencia motivo por el cual es trasladado a centro privado clínica oriente donde es valorado por intensivista de guardia , quien decide su ingreso. solicitan valoración por el servicio de neurocirugía, quien indica realizar estudio por imágenes TAC de cráneo el cual se realiza el día 27/11/2015 reportando hidrocefalia obstructiva aguda con la presencia de válvula de DVP de aspecto disfuncional por dilatación evaluada del sistema ventricular. Por lo que se decide resolución quirúrgica, la cual se lleva a cabo el día 1/12/2015 donde bajo anestesia general realizan extracción de de derivación ventricular con salida de secreción hemática y  recambio de sistema de derivación ventrículo peritoneal derecho y posteriormente se traslada a unidad de cuidados intensivos de dicha institución para cuidados post operatorios, donde permanece durante 24 horas sin evidenciar mejoría del estado neurológico, por lo que se decide realizar TAC control y trasladar a unidad de cuidos intensivos del HUAPA por razones socioeconómicas.''',

		"examenFisicoEgreso": {

			"resumen": ''' Se recibe paciente en camilla de traslado, intubada recibiendo oxigeno húmedo por ambu, se traslada a cama de UCI y se conecta a monitor cardíaco externo que reporta: TA: 153/46 (79) mmHg; FC: 89 lpm; FR: 20rpm; SPO2: 94% ''',
			
			"piel" : 	'''	blanca, normotérmica al tacto, llenado capilar < 3 segundos se evidencia ligera palidez cutáneo mucosa.''',
		
			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos normofonéticos, rítmicos, regulares sin soplos ni galope.''',
			"abdomen": ''' globoso, a expensa de panículo adiposo, Rs Hs Ps, no doloroso a la palpación, no megálico.''',

			"neurologico": '''inconsciente, pupilas isocóricas con lenta respuesta a la luz, Glasgow: 6/15ps, Respuesta Motora: 4pts, Respuesta Verbal: 1pts, Apertura Ocular: 1pts.  ''',
			"extremidades": '''simétricas, eutróficas, sin edema.''',

		}, 

		"diagnosticoIngresoUCI": [
								"Post operatorio inmediato de recambio de sistema de derivación ventrículo peritoneal derecho por hidrocefalia debido a disfunción valvular.",
								"Post operatorio inmediato de colocación de sistema ventricular externa.",
								"Hipertensión arterial sistémica ",
								"Evc hemorrágico secuelar",
								"Diabetes mellitus tipo II descompensada en hiperglicemia ",
								"Trastorno hematológico:",
								"Trombosistosis",
								"Anemia leve",
									
								],
		"diagnosticoEgresoPrivado":[
			"(centro privado clínica Oriente)"
			"Post operatorio inmediato por recambio de sistema de derivación ventrículo peritoneal derecho por disfunción",
			"EVC hemorrágico operado",
			"Diabetes mellitus tipo II ",
			"HTA sistémica.", 

		]
		
	},# 171

	{
	
		
		"nombre": "Gregorina del Carmen Garcia Jimenez ", 		
		
		"edad": "22",
		
		"ci": "24.754.780", 
		
		"dirección": "La Montañita. ",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1992,6,25),

		"lugarNacimiento": "Cumaná", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,9,20),

		"fechaIngresoUCI": datetime(2014,9,20),


		"resumenIngreso": ''' Se trata de paciente femenina de 22 años de edad sin antecedentes patológicos importantes; primigesta con embarazo controlado en red ambulatoria de 34 sem + 3 días por eco (FUR incierta). Quien inicia  enfermedad actual en horas de la madrugada del día de hoy 20/09/14 cuando presenta según refiere el esposo sangramiento vaginal abundante de color rojo, vómitos, sudoración, palidez y frialdad y pérdida de consciencia; motivo por el cual es traslada a este centro donde se evalúa e ingresa por servicio de Ginecología con diagnósticos ''',


		"examenFisicoEgreso": {

			"resumen": ''' Se recibe paciente en cama de traslado, intubada, recibiendo oxigeno húmedo por ambú; se traslada a cama de uci y se conecta a ventilación mecánica AC Vc 400 Fr: 12 Fl: 50 FiO2: 50 PEEP: 0 y a monitor cardíaco externo que reporta: TA: 127/90mmHg FC: 74 lpm FR: 15 rpm	SPO2: 100%''',
			
			"piel" : 	'''	Palidez cutáneo mucosa, normohídrica nomotérmica.''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes, sin agregados, ruidos cardíacos rítmicos, regulares, sin soplos.''',
			"abdomen": ''' Plano, depresible, útero tónico a nivel umbilical, Ruidos Hidroaereos disminuidos. ''',

			"neurologico": ''' Incosciente, no evaluable por efectos de sedación y relajación farmacológica''',

		}, 

		"diagnosticoIngresoUCI": [
								"POST OPERATORIO MEDIATO DE CESARA SEGMENTARIA. ",
								"DESPRENDIMIENTO PREMATURO DE PLACENTA",
								"HIPOVOLEMIA SEVERA.",
								"TRASTORNO HEMATOLOGICO: ANEMIA SEVERA.",
									
								],

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 60/40 mmHg Fr: Fc: 93 lpm. La paciente es llevada a mesa operatoria de emergencia, donde se realiza cesárea segmentaria obteniendo feto muerto masculino de 2360 gr; desprendimiento prematuro de placenta 40%; revisión de cavidad uterina, histerorrafia en 2 planos, comprobación de hemostasia. Debido a que la paciente presenta hipotensión severa se solicita valoración por UCI, donde se evalúa paciente en quirófano, con palidez cutáneo mucosa intubada, conectada a monitor que reporta Fr: 16 rpm Fc: 101 lpm TA: 80/60 mmHg. Por disponibilidad de cupo y estado de la paciente se decide ingreso a UCI.  ''',
			"piel": '''Palidez cutáneo mucosa, normohídrica nomotérmica.''',
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes, sin agregados, ruidos cardíacos rítmicos, regulares, sin soplos.''',
			"abdomen": '''Útero grávido feto único DU irregular, AU: 32 cm,  FCF 20 x.''',
			
			"neurologico": '''Consciente, orinetada, no signos de focalización neurológica  ''',
			

		},  

		"diagnosticoIngresoHUAPA": [
								
			"I GESTA.",
			"EMBARAZO DE 34 SEM + 3 DIAS POR ECO",
			"ARO DEBIDO A:", 
			"DESPRENDIMIENTO PREMATURO DE PLACENTA",
			"BRADICARDIA FETAL",
			"EMBARAZO MAL CONTROLADO",
			"SHOCK HIPOVOLÉMICO.",

		], 
		
	},# 172

	{

		"nombre": "ISAMAR CORONADO", 		
		
		"edad": "23",
		
		"ci": "21.096.251", 
		
		"dirección": "Mu Negro Cumanacoa",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1990,9,29),

		"lugarNacimiento": "Cumana- Edo Sucre ", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,3,20),

		"fechaIngresoUCI": datetime(2014,3,20),

		"resumenIngreso": '''Se trata de paciente femenina de 23 años de edad con antecedentes de Lupus Eritematoso Sistémico diagnosticado hace 8 años controlado con cellcept tab 1gr cada 8 horas, Hipertensión Arterial controlada con cozaar 50 mg BID, adalat oros 30 mg VO 8am,  carvedilol 25 mg VO OD. Quien inicia enfermedad actual el día 6/03/14 cuando presenta cuadro febril acompañado de malestar general,  disnea y dolor abdominal,  motivo por el cual acude en varias ocaciones a servicio de emergencia donde trataban de forma ambulatoria, por persistencia de síntomas es llevada a centro privado donde permanece por 48 horas y por falta de recursos es traslada a este centro donde se ingresa.''',

		"examenFisicoIngresoUCI": {

	
			"piel" : 	'''	normohidrica, afebril al tacto.''',
		

			"cardiopulmonar":  ''' Tórax simétrico, expandible; ruidos cardiacos rítmicos, normo fonéticos, sin soplos ni galope. Ruidos respiratorios presentes MV conservado, se auscultan crepitantes en hemitorax derecho y base pulmonar izquierda''',
			"abdomen": ''' Globuloso, depresible, doloroso a la palpación, hepatomegalia de 2 cm, RHA presentes. ''',

			"neurologico": ''' Consciente, orientada en 3 planos, pupilas isocóricas reactivas a la luz ''',
			
		}, 

		"diagnosticoIngresoUCI": [
									"Lupus Eritematosa Sistémico en actividad.",
									"Nefritis lupica",
									"Hepatomegalia en estudio",
									"Ascitis en estudio.",
									"Infección Respiratoria Baja: neumonía derecha adquirida en la comunidad",
										
								],
		"examenFisicoIngresoHUAPA": {
			
			"piel": ''' morena, normotermica llenado capilar <3 seg.''',
			
			"cardiopulmonar": '''tórax simétrico, normo expansible, ruidos respiratorios presentes, se auscultan crepitantes basales.''',
			"abdomen": '''globuloso, blando depresible no doloroso a la palpación.''',
			"extremidades": '''simétricas eutróficas sin edema.''',
			"neurologico": '''consiciente ubicada en los 3 planos ROT II/IV, FM V/V.''',

		},  

		"diagnosticoIngresoHUAPA": [
								
			"Lupus Eritematoso.",
			"Nefropatía Lupica.",
			"Hepatomegalia en estudio",
			"Ascitis en estudio",
			"IRB: neumonía basal",
			"Anemia severa (6.4 g/dl)",
			{"resumen":''' Se recibe paciente en camilla de traslado, que recibe oxigeno húmedo por bigote nasal a 5 lts por minuto, se traslada a cama UCI, se conecta a monitor cardiaco continuo que reporta: Fc 86 lpm Fr: 38 rpm TA: 96/54 (70) mmHg SATO2: 91%.'''}

		], 
		
	},# 173

	{
		"nombre": "Julia Sifontes de Muñoz", 		
		
		"edad": "92",
		
		"ci": "542185", 
		
		"dirección": "Urbanización fe y alegría",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1923,7,5),

		"lugarNacimiento": "Cumaná", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,4,17),

		"fechaIngresoUCI": datetime(2015,4,17),

		"resumenIngreso": '''Se trata de paciente femenina de 92 años de edad,  natural y procedente de la localidad. Con antecedentes patológicosde hipertensión arterial y diabetes mellitus tipo II sin tratamiento médico, así como antecedentes de Hemorragia subaracnoidea +clipaje de aneurisma cerebral hace 20 años , cuyo familiar refiere inicio de enfermedad actual  el día 17/04/2015 en horas de la mañanacuando presenta cefalea intensa ,posteriormente se anexa al cuadro perdida del estado de conciencia y relajación de esfínter vesical, motivopor el cual es trasladada a ambulatorio de la localidad donde constatan cifras de tensión arterial elevadas 200/90 mmhg refiriendo a nuestrocentro asistencial donde es evaluada por el servicio de medicina interna, se ingresa con los diagnósticos''',


		"examenFisicoIngresoUCI": {

			"resumen": '''Paciente es trasladado en camilla de transporte, recibiendo oxigeno por mascarilla facial se conecta  a monitor cardiaco externo que reporta signos vitales: TA: 170/70 mmHg FC: 55 lpm FR: 24 rpm  SPO2: 95% ''',
			
			"piel" : 	'''	morena, Normotérmica al tacto, llenado capilar <3 segundos, con pálidez cutáneo mucosa''',
			

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, con  agregados roncos bilaterales moderados, ruidos cardíacos rítmicos bradicardico,  sin soplos ni galope. ''',
			"abdomen": ''' blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes. ''',

			"neurologico": ''' inconsciente pupilas anisocoricas con midriasis derecha arreactivas a la luz Glasgow 3/15 pts RM 1 RO 1 RV 1 ,reflejo corneal presente''',
			"extremidades": '''eutróficas, simétrica sin edema ''',
			
		}, 

		"diagnosticoIngresoUCI": [
						"Crisis hipertensiva tipo emergencia expresada en EVC hemorrágico",
						"Hemorragia subaracnoidea con  componente hemático en valle silviano derecho con drenaje ventricular.",
						"Hipertensión arterial sistémica",
						"Diabetes mellitus tipo II ",
						"Trastorno hematológico : trombocitopenia",
									
								],

		"examenFisicoIngresoHUAPA": {
			"resumen": '''TA: 150/80 mmHg FC: 100 lpm FR: 18 rpm SPO2: % Paciente es trasladada para realización de estudio por imágenes (TAC) de cráneo que reporta hemorragia subaracnoidea masiva con mayor componente hemático en valle silviano derecho con drenaje ventricular abundante, a descartar origen carotideo interno o en la arteria cerebral media ipsilateral. Se solicita valoración por el servicio de terapia intensiva dada las condiciones clínicas del paciente y en vista de disponibilidad de cupo se decide su ingreso en UCI     ''',
			"piel": ''' morena, Normotérmica al tacto, llenado capilar <3 segundos. ''',
			
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, no agregados, ruidos cardiacos rítmicos regulares sin soplo ni galope.''',
			"abdomen": '''blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes.''',
			"extremidades": '''eutróficas, simétrica sin edema''',
			"neurologico": '''estuporosa, no responde al llamado desviación de la comisura labial a la izquierda.''',

		},  

		"diagnosticoIngresoHUAPA": [
								
				"Crisis hipertensiva tipo emergencia expresada en EVC en evolución",
				"Hipertensión arterial no controlada ",
				"Diabetes mellitus tipo II descompensada en hiperglicemia ",

		], 
		
	},# 174


	{
		
		"nombre": "Lilia del Valle Marcano de Mujica", 		
		
		"edad": "84",
		
		"ci": "524.437", 
		
		"dirección": "Urb. El Peñón Calle los Ricos casa # 5775. ",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1930,9,8),

		"lugarNacimiento": "Cumanacoa.", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,11,11),

		"fechaIngresoUCI": datetime(2014,11,11),

		"antecedentes": '''Hipertensión Arterial Sistémica de larga data y Cardiopatía Isquémica Crónica en tratamiento con Aprovel ® 150mg OD, lasix® 20 mg, Corazem® 120mg, Lipitor® 80 mg OD y Plavix® 75mg OD Diábetes Mellitus tipo 2 desde hace 15 años tratada con Insulina Cristalina pre-pandrial (de acuerdo esquema indicado por Dr. Toledo Endocrinólogo tratante) y Lantus 30 Uds VSC 8am OD, Hipotiroidismo tratada con Euthyrox 50mg OD y Alergia al Adalat Oros y Captopril. Familiar niega antecedentes de Asma. Niega hábitos tabáquicos. Fumadora Pasiva, (Esposo fallecido con hábitos tabáquicos acentuados)''', 

		"resumenIngreso": ''' Se trata de paciente femenina de 84 años de edad, natural de Cumanacoa y procedente de la localidad quien cursa con antecedentes personales de Hipertensión Arterial Sistémica de larga data y Cardiopatía Isquémica Crónica en tratamiento con Aprovel ® 150mg OD, lasix® 20 mg, Corazem® 120mg, Lipitor® 80 mg OD y Plavix® 75mg OD Diábetes Mellitus tipo 2 desde hace 15 años tratada con Insulina Cristalina pre-pandrial (de acuerdo esquema indicado por Dr. Toledo Endocrinólogo tratante) y Lantus 30 Uds VSC 8am OD, Hipotiroidismo tratada con Euthyrox 50mg OD y Alergia al Adalat Oros y Captopril. Cuyo familiar refiere inicio de Enfermedad actual el 04/11/2014 cuando presenta disnea de aparición súbita a medianos esfuerzos, concomitante tos húmeda con expectoración blanquecina y elevación de la temperatura corporal no cuantificada; para el día 05/11/2014 permanece sintomática por lo que se traslada a la emergencia de centro clínico privado en donde es evaluada por endocrinólogo e internista quien decide su ingreso a Sala de Hospitalización con IDx de Sepsis de Punto de partida Respiratorio,  Infección Respiratoria Baja. La paciente en horas de la noche presenta disnea acentuada, sibilantes universales, estridor laríngeo, tiraje intercostal y subcostal, diaforesis y signos de hipoperfusión tisular dado por Cianosis distal, por lo que solicitan evaluación por UCI, siendo evaluada por Intensivista de Guardia de dicho centro y se decide ingreso a la UCI. Permanece con evolución tórpida, afebril, disneica con tiraje subcostal e intercostal recibiendo Oxigeno húmedo por Sistema Ventury al 50%, ameritando de intubación endotraqueal el día sábado 08/11/2014 y se conecta a Ventilación Mecánica con parámetros Modo A/C, VC: 600 (8cc/Kg), Fl: 50; FiO2: 60, recibiendo esteroides endovenosos y diuréticos de asa en infusión continua, Antibióticoterapia: Zyvox (7 días), Vorcum (3 días) e Imipenem (2 días). Se evidencia posteriormente elevación de azoados y se asocia el diagnóstico de Insuficiencia Renal Crónica Reagudizada, solicitándose evaluación por Nefrología, siendo evaluada por Nefrólogo de guardia el día 11/11/2014 quien en vista de las condiciones y de azoemia persistente decide dar apoyo de diálisis, sin embargo por decisión del familiar, la paciente  se traslada a la Unidad de Diálisis del HUAPA, se conecta a monitor cardíaco externo y a ventilación mecánica, se le coloca Catéter Femoral derecho, recibiendo soporte de hemodiálisis durante dos horas, posteriormente se ingresa a la Unidad de Cuidados Intensivos.''',

		"examenFisicoIngresoUCI": {

			"resumen": ''' Se traslada a la paciente en camilla de traslado en regulares condiciones generales, con monitor cardíaco, intubada con apoyo de oxigeno por ambú, se traslada a cama de UCI y se conecta monitor cardiaco continuo que reporta  signos vitales:   TA: 133/82 mmHg,  TAM: 103mmHg,   FC: 98 lpm,   FR: 24 rpm,  SATO2: 94%. ''',
			
			"piel" : 	'''	blanca, normotérmica al tacto, hidratada, llenado capilar < 3 segundos.''',

			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible, sibilantes bilaterales universales,  Ruidos cardíacos taquicárdicos,  no se auscultan soplos ni galope.  ''',
			"abdomen": ''' blando, globoso a expensas de panículo adiposos, distendido, no impresiona doloroso. No se palpan visceromegalias.''',

			"neurologico": ''' Somnolienta, pupilas isocóricas,  normorreactivas a la luz, Glasgow: RO: 3 ptos, RV: 1 ptos, RM: 6 ptos 10/15 puntos, reflejos osteotendinosos presentes. ''',
			"extremidades": '''Simétricas,  edema en miembros inferiores III/IV.''',
			"genitales": ''' Se evidencia salida pared vaginal por prolapso irreductible. ''',

		}, 

		"diagnosticoIngresoUCI": [
									

									"Sepsis de punto de partida Respiratoria.",
									"Infección Respiratoria Baja: Neumonía Adquirida en la comunidad.",
									"Enfermedad Renal Crónica Reagudizada en Hemodiálisis.",
									"Diábetes Mellitus tipo 2.",
									"Hipertensión Arterial Sistémica.",
									"Cardiopatía Isquémica Crónica.",
									"Hipotiroidismo.",
									"Alergia a Captopril y Adalat.",
									"Prolapso Vaginal Irreductible.",
									"Trastorno Hematológico:",
									"Anemia Leve.",
									"Trastorno Acido-Base:",
									"Acidosis metabólica descompensada.",

								],
		
	},# 175


	{
		"IdHistoria": "42-30-43", 
		
		"nombre": "Jhonny José Sucre Belonis", 		
		
		"edad": "25",
		
		"ci": "25.622.067", 
		
		"dirección": "CUMANA",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1988,9,12),

		"lugarNacimiento": "Guiria – Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,7,18),

		"fechaIngresoUCI": datetime(2014,8,14),


		"antecedentes": '''Niega Diabetes, asma, HTA y alergias a medicamentos. Quirúrgicos: reducción cruenta más osteosíntesis de tibia y peroné izquierdo. ''', 

		"resumenIngreso": '''Se trata de paciente masculino 25 años de edad, natural y procedente de Guiria, sin antecedentes de patológicos de importancia, cuyo familiar refiere  inicio de enfermedad actual el día 20 de Junio de 2014, cuando posterior a traumatismo por proyectil por arma de fuego con impactos múltiples (perdigones) en hemitórax izquierdo presentando dolor y disnea, motivo por el cual acude a Hospital de Carúpano, en donde evalúan y por evidenciar clínica y radiología compatible hemo-tórax deciden la colocación de tubo de drenaje torácico en 5to EIC con LMC, obteniéndose 250 cc de gasto hemático en pleuroevac. Paciente permanece hospitalizado en dicho centro requiriendo reposicionamiento del tubo de drenaje en dos oportunidades; en vista de no presentar mejoría del gasto a través de sistema de drenaje y por persistencia de imagen radiológica compatible hemo-neumotórax se refiere a este centro de Salud en donde se ingresa por el Servicio de Cirugía Blanda.  ''',

		"examenFisicoIngresoUCI": {

			"resumen": '''  Paciente que se recibe en camilla de transporte, intubado con apoyo de oxígeno por ambú, se traslada a cama de UCI, conectándose a monitor cardiaco externo que reporta signos vitales: TA: 105/62mmHgFC: 77 lpm FR: 19 rpm   SatO2: 100% ''',
			
			"piel" : 	'''	Morena, normotérmica, hidratada, con moderada palidez cutáneo mucosa, llenado capilar < 3 segundos. ''',
			

			"cardiopulmonar":  ''' Estable hemodinámicamente, tórax simétrico hipoexpansible,  Ruidos cardiacos regulares taquicárdicos, sin soplos ni galope; ruidos respiratorios presentes, sin agregados. Se evidencia tubo de tórax anterior y posterior en hemitórax izquierdo 5to EIC y LMC, con gasto hemático escaso y burbujeo positivo.	''',
			"abdomen": ''' Plano, blando, depresible, Rs Hs disminuidos, sin megalias''',

			"neurologico": ''' Incosciente bajo sedación y relajación, con pupilas isocóricas con tendencia a la midriásis, normorreactivas a la luz, Glasgow no evaluable. Sin signos de focalización neurológica ni signos de irritación meníngea.''',
			"extremidades": '''Simétricas sin edema.''',
			
		}, 

		"diagnosticoIngresoUCI": [
									"Postoperatorio Inmediato de toracotomía Posterolateral izquierda por traumatismo torácico penetrante por proyectil de cargas múltiples complicado con pulmón atrapado y Neumotórax apical.",
									"Trastorno hematológico:",
									"Anemia Moderada.",
									"Trastorno Acido Base:",
									"Acidosis metabólica compensada  más hiperoxemia.",

								],

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente luce en As Rs Cs Gs, afebril, eupneico. Signos vitales: TA: 120/80mmHg FR: 20rpm FC: 82 lpmTraumatismo torácico penetrante por proyectil por arma de fuego complicado con hemotórax coagulado + Neumotórax izquierdo. Al ingreso el paciente es evaluado en conjunto a Dr. Sotillet Cirujano de Tórax quien evalúa estudios radiológicos y Tomografía de Tórax, impresionando condensación pulmonar y Neumotórax apical sin signos de derrame pleural, por lo que indica terapia fibrinolítica con Estreptoquinasa 300.000 uds vía intrapleural por 3 días. Permanece en el área de  la  emergencia con gasto post-terapia de 500 cc  y 350 cc hemato-purulento. Se le realizó TAC de tórax el día 09/07/2014 que reporta Atelectasia Pulmonar izquierda, contusión parenquimatosa hemorrágica izquierda, hemotórax moderado y la presencia de múltiples cuerpos extraños. Espirometría 01/08/2014 que reporta  patrón restrictivo grave.  El día 13/07/2014  es reevaluado por Dr. Sotillet quien indica como plan  Toracotomía Posterolateral izquierda más decorticación. El día 14/08/2014 es llevado a quirófano bajo anestesia general encontrándose los siguientes hallazgos: tubo de drenaje torácico intraparenquimatoso, fístula broncopleural,  pulmón con múltiples adherencias a pleura parietal, cámara néumica apical y lesión diafragmática iatrogénica. Tomándose como conducta decorticación pulmonar, cura de fístula broncopleural, liberación  de cámara néumica apical, rafia con seda 1-0 de la lesión iatrogénica diafragmática, se deja tubo de drenaje torácico de 34Fr anterior y posterior. En el postoperatorio inmediato se solicitan evaluación y cupo por UCI, en vista de disponibilidad se ingresa,  con Dra. Begglia Roa intensivista de  guardia.''',
			"piel": ''' Morena, hipotérmica al tacto, palidez cutánea y mucosa leve y llenado capilar >3 segundos. ''',
			
			"genitales": '''Normoconfigurados, con sonda de Foley conectada a bolsa recolectora con orinas claras.   ''',
			"cardiopulmonar": '''Se evidencia tubo de drenaje pleural conectado a pleuroevac, no funcionante con gasto hematopurulento, Tórax simétrico, normo expansible, ruidos respiratorios presentes disminuidos en hemitorax izquierdo sin agregados, ruidos cardíacos normofonéticos,  sin soplos ni galope. ''',
			"abdomen": '''Plano Rs Hs presentes, blando, depresible, no doloroso a la palpación profunda, sin signos de irritación peritoneal.''',
			"extremidades": '''Simétricas sin edema, pulsos periféricos presentes.''',
			"neurologico": '''Consciente, conservado.''',

		},  
		
	},# 176

	{
		"IdHistoria": "41-71-45", 
		
		"nombre": "María del Valle  Vera Cardiet", 		
		
		"edad": "25",
		
		"ci": "21.093.794 ", 
		
		"dirección": "comunidad el huapo numero 224 ",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1990,4,2),

		"lugarNacimiento": "", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,12,9),

		"fechaIngresoUCI": datetime(2015,12,9),
		"resumenIngreso": ''' SIGNOS VITALES: FC 75 LPM TA 110/70 MMHG  FR 17. Se trata de paciente femenina de 25 años de edad natural y procedente de la localidad con antecedentes patológicos personales de litiasis coraliforme diagnosticado hace 1 año aproximadamente en control por el servicio de cirugía para resolución quirúrgica (Dr. Carlos Figuera), quien inicia enfermedad actual hace 15 días aproximadamente cuando presenta dolor en fosa lumbar izquierda que se irradia a extremidad inferior ipsilateral, posteriormente se anexa al cuadro aumento de la temperatura corporal cuantificada en 39 ºC y aumento del perímetro abdominal además de persistir clínica de dolor, por lo que decide 4/12/2015 acudir al médico tratante quien  refiere a nuestro centro asistencial  para su ingreso y resolución quirúrgica.''',


		"examenFisicoIngresoUCI": {


			"piel" : 	'''	Normotérmica, normo hidratada, llenado capilar <3segundos. ''',
			
			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, Ruidos respiratorios presentes en ambos hemitorax sin agregados Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos.''',
			"abdomen": ''' globoso,  doloroso a la palpación superficial y  profunda, puño percusión positiva ''',

			"neurologico": '''  Consciente orientada en tiempo espacio y persona ''',
			
		}, 


		"diagnosticoIngresoUCI": [
								"PIELONEFRITIS IZQUIERDA ",
								"TRASTORNO HEMATOLOGICO :ANEMIA MODERADA ",
								{"resumen": ''' El paciente a su ingreso es evaluado por el servicio de cirugía blanda (urología) quien indica planificar para quirófano el día domingo 6/12/2015, con plan de realizar pielolitotomia izquierda versus nefrectomía izquierda, es llevada a mesa operatoria donde bajo anestesia general se realiza laparotomía para rectal izquierda con hallazgos de riñón izquierdo de 20x15 cm con capsula renal engrosada e indurada, con 50 cc aproximadamente de secreción purulenta espesa no fétida tomándose como conducta drenaje de colección purulenta intrarenal mas nefrectomía subcapsular izquierda, se deja dren rígido 18 fr dirigido a lecho quirúrgico, cierre por planos, y en segundo tiempo quirúrgico bajo abordaje endoscópico se retira catéter doble j. posteriormente se traslada a área de hospitalización a cargo del servicio de Medicina Interna. Permaneciendo durante 48 horas con evolución clínica tórpida, persistiendo febril, en paraclínicos persistiendo leucocitosis con neutrofilia, el día 09/12/2015 se anexa al cuadro dificultad respiratoria a moderados esfuerzos, por tal motivo deciden solicitar valoración por el servicio de terapia intensiva, quien acude al llamado evaluando paciente en condiciones clínicas de cuidados en vista de disponibilidad de cupo se decide su ingreso a UCI.   '''}
	
								],

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' SIGNOS VITALES:  FC 110 LPM TA 95/65 (78) MMHG FR 42 rpm SATO2: 88 %''',
			"piel": '''Normotérmica, normo hidratada, llenado capilar <3segundos. Se evidencia marcada palidez cutánea mucosa.''',
			
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, Ruidos respiratorios presentes en ambos hemitorax sin agregados Ruidos cardíacos rítmicos, taquicardicos,  no se auscultan soplos.''',
			"abdomen": '''globoso, poco depresible,   doloroso a la palpación  profunda, se evidencia apósito estéril que cubre heridas quirúrgica limpio y seco, con presencia de dren rígido conectado a bolsa recolectora con presencia de secreción serohemática en moderada cantidad''',
			
			"neurologico": '''Consciente orientada en tiempo espacio y persona, pupilas isocóricas normorreactivas  la luz, Glasgow 15/15 pts. ROT II/IV. ''',
		

		},  

		"diagnosticoIngresoHUAPA": [
						"SEPSIS PUNTO DE PARTIDA RENAL",
						"POST OPERATORIO MEDIATO DE NEFRECTOMIA IZQUIERDA DEBIDO A ABSCESO RENAL IZQUIERDO.",
						"TRASTORNO HEMATOLOGICO : ANEMIA LEVE",
						"TRASTORNO HIDROELECTROLITICO: HIPOKALEMIA ",
							
		], 
		
	},# 177

	{
		"IdHistoria": "51–79–65", 
		
		"nombre": "Gabriel Alejandro Rivas Ortiz", 		
		
		"edad": "23",
		
		"ci": "19.707.169 ", 
		
		"dirección": "Calle La Belleza, Carúpano.",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1990,6,19),

		"lugarNacimiento": "Carúpano, Edo. Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,3,3),

		"fechaIngresoUCI": datetime(2014,3,4),

		"resumenIngreso": '''Paciente masculino de 23 años de edad, natural y procedente de Carúpano, sin antecedentes patológicos, cuyo familiar refiere inicio de enfermedad actual el 02/03/2014 cuando posterior a accidente de tránsito tipo colisión en moto, presenta múltiples escoriaciones y traumatismo en región temporo-parietal izquierda, es trasladado a ambulatorio de su localidad y posteriormente al hospital de Carúpano, se le realiza TAC cerebral evidenciándose edema cerebral difuso a predominio de hemisferio cerebral izquierdo, contusión hemorrágica frontal izquierda, por lo que deciden referir a este centro asistencial el día 03/03/14 donde se evidencia al examen físico paciente  con TA: 110/70mmHg, FC: 90X’, FR: 17X’, somnoliento, con respuesta a estímulos dolorosos, Glasgow 9/15pts (RM: 5pts, RO: 2pts, RV: 2pts) por lo que es ingresado por el servicio de Neurocirugía y Traumatología con los diagnósticos de Traumatismo Craneoencefálico Moderado y Escoriaciones Múltiples. En vista de estado neurológico del paciente solicitan valoración por UCI, siendo evaluado en área de quirofanito de emergencia, por deterioro neurológico a 7pts se decide intubación endotraqueal y se conecta a T de Ayres con O2 húmedo a 10ltrsX’ y se hacen sugerencias. El día de hoy, en vista de condiciones generales del paciente y por autorización de Dra. Roa (Intensivista de Guardia) se decide su ingreso a UCI y dicta órdenes médicas. ''',


		"examenFisicoIngresoUCI": {

			"resumen": '''Se recibe paciente en camilla de traslado, intubado y recibiendo O2 por Ambú®, se pasa a cama UCI y se conecta a ventilación mecánica modo A/C, Vc: 560, FR: 12, FiO2: 50, Fl: 50, PEEP: 0, se conecta además a monitor cardíaco continuo que reporta: TA: 126/75(87) mmHg; FC: 117 lpm; FR: 19 rpm; SatO2: 99%''',
			
			"piel" : 	'''	morena, con múltiples escoriaciones en cara, miembro superior izquierdo y rodilla izquierda, normotérmica al tacto, llenado capilar < 3seg.''',
			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, taquicardicos, sin soplo ni galope.''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, blando, depresible, no impresiona doloroso a la palpación, no megálico ''',

			"neurologico": ''' no evaluable por efectos de sedación farmacológica. ''',
			"extremidades": '''eutróficas, simétricas, sin deformidades.''',
			

		}, 

		"diagnosticoIngresoUCI": [

						"TRAUMATISMO CRANEOENCEFALICO SEVERO",
						"TRASTORNO HIDROELECTROLITICO:",
						"HIPOKALEMIA",
						"TRASTORNO ACIDO-BASE:",
						"ACIDOSIS METABOLICA COMPENSADA CON ALCALOSIS RESPIRATORIA + HIPEROXEMIA",

									
								],
	},# 178

	{
		"IdHistoria": "52-45-23", 
		
		"nombre": " Hernán Rafael  García Portillo", 		
		
		"edad": "62",
		
		"ci": "3.956.000 ", 
		
		"dirección": "Avenida Cajigal numero 101 Cumana ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1952,10,12),

		"lugarNacimiento": "Barcelona ", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,9,9),

		"fechaIngresoUCI": datetime(2014,9,9),

		"resumenIngreso": ''' Se trata de paciente masculino de 62 años de edad natural de Barcelona  y procedente de la localidad con antecedentes patológicos conocidos de Enfermedad Broncopulmonar obstructiva Crónica , con tratamiento médico que no refieren los familiares .Inicia enfermedad actual hace 15 días (23-08-14) presentando disnea a pequeños esfuerzos acompañado de tos seca motivo por el cual es llevado a ambulatorio de la localidad y referido a este centro donde fue ingresado y tratado , a las 72 horas a petición del paciente es llevado a clínica de la localidad donde fue hospitalizado recibió tratamiento que no precisa por 48 horas ,es dado de alta médica posteriormente (24 horas ) continua con disnea, tos y expectoración por lo que es  traído por segunda ocasión  a servicio de emergencia HUAPA donde es reingresado''',


		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente en malas condiciones generales, hemodinámicamente estable,  afebril, intubado disneico trasladado en camilla de transporte recibiendo oxigeno por cánula nasal a razón de 3 lt porminuto  Signos Vitales: TA: 127/74mmHg FC: 93pm FR: 32rpm  SPO2: 87Debido a desaturación disnea intensa utilización de músculos accesorios de la respiración se decide realizar intubación endotraqueal con TET 8 F sin complicaciones se conecta a ventilación mecánica con los siguientes parámetros VC 420 FR 10 FIO2 50 FL 60 PEEP O.''',
			
			"piel" : 	'''	normotérmica, hidratada, llenado capilar < 3 segundos.''',
			

			"cardiopulmonar":  ''' tórax simétrico hipoexpansible, ruidos respiratorios disminuidos en ambos hemitorax  abolidos en ambas bases pulmonares, ruidos cardíacos taquicárdicos, regulares, sin soplos.''',
			"abdomen": ''' globoso depresible no doloroso  a la palpación superficial ni profunda no megalias RHA presentes y normales.''',

			"neurologico": ''' consciente somnoliento  orientado en tiempo espacio y persona no signos meníngeos ni de focalización motora  ''',

		}, 

		"diagnosticoIngresoUCI": [
								

								"ENFERMEDAD BRONCOPULMONAR OBSTRUCTIVA CRONICA DESCOMPENSADA ",
								"INFECCION RESPIRATORIA BAJA ",
								"INESTABILIDAD HEMODINAMICA ",
								"TRASTORNO METABOLICO : HIPERGLICEMIA",
								"TRASTORNO ACIDO BASICO : ACIDOSIS RESPIRATORIA  DESCOMPENSADA +ALCALOSIS METABOLICA ",
								"TRASTORNO HIDROELECTROLITICO : HIPOKALEMIA ",
	
								],

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente en aparentes malas  condiciones generales, afebril, disneico. Signos Vitales al ingreso. FC 91  LPM T 36.5  FR 24  RPM  TA 130 /90 MMHG ''',
			"piel": ''' Blanca, normotérmica, hidratada, llenado capilar < 3 segundos.''',
		
			"cardiopulmonar": '''tórax simétrico hipoexpansible, ruidos respiratorios presentes, estertores sibilantes y roncos diseminados, ruidos cardíacos rítmicos, regulares, sin soplos.''',
			"abdomen": '''blando, depresible, no doloroso a la palpación superficial y  profunda, no megalias.RHA presentes  ''',
			
			"neurologico": '''consciente,  orientado en TEP pupilas isocóricas reactivas reflejo corneal presente ''',
		
		},  

		"diagnosticoIngresoHUAPA": [
								"EBPOC : ENFISEMA PULMONAR", 
								"CRISIS DE ASMA LEVE",
								{"resumen":''' Paciente que permanece en área de emergencia recibiendo oxigeno por cánula nasal a razón de 3 lt por minuto y antibióticoterapia con Ceftriaxone evolucionando desfavorablemente  por lo que se solicita valoración por terapia intensiva observándose paciente disneico que no tolera el decúbito y con gases arteriales que reportan Acidosis respiratoria descompensada, alcalosis metabólica e hipoxemia por lo que se decide ingreso en UCI .'''}


		], 
		
	},# 179

	{
		"IdHistoria": "52–61–92", 
		
		"nombre": "Jackson Josue Rodríguez Lanza", 		
		
		"edad": "26",
		
		"ci": "19.082.326", 
		
		"dirección": "Paraíso. Zona Industrial. San Luis. Cumana",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1988,12,11),

		"lugarNacimiento": "Cumaná - Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,2,23),

		"fechaIngresoUCI": datetime(2015,2,24),

		"resumenIngreso": '''Se trata de paciente masculino de 26 años de edad, natural y procedente de la localidad, con antecedentes de Diabetes Mellitus tipo 1 controlado con insulina Lantus® 30 uds en la noche e Insulina cristalina 3 uds pre desayuno, pre almuerzo, pre cena. Quien inicia enfermedad actual el día de ayer 23/02/2015 cuando comienza a presentar vómitos en número de 10 de contenido bilioso y luego con sangre, acompañado de dolor abdominal de poca intensidad; acude a ambulatorio de la localidad donde evalúan, y refieren a este centro asistencial, siendo ingresado por servicio de medicina interna.  ''',

		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente recibido  en silla de ruedas respirando aire ambiente, se traslada a cama UCI y se conecta a monitor cardiaco continuo que reporta Fr:28 rpm Fc:126 lpm TA  125/78 (90) mmHg SATO2:100 %. Se reciben Amilasas que reportan 812 ui/l''',
			
			"piel" : 	'''	Deshidratada, Normotérmica al tacto, llenado capilar <3 segundos.''',

			"cardiopulmonar":  ''' Plano, doloroso a la palpación en epigastrio e hipocondrio derecho, ruidos hidroaéreos presentes, no megalias''',

			"neurologico": ''' Paciente consciente orientado en tres planos, lenguaje coherente.''',
			"extremidades": '''Simétricas sin edemas''',
			

		}, 

		"diagnosticoIngresoUCI": [
								
									"Diabetes Mellitus tipo 1 descompensada en Cetoacidosis diabética",
									"Pancreatitis aguda AD",
									"Trastorno Hidro electrolítico: Deshidratación Severa.",
									"Trastorno Metabólico: Hiperglicemia",
									"Trastorno acido – base: Acidosis Metabólica descompensada más alcalosis respiratoria con  hiperoxemia.",
								], 

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se realizan paraclínicos que reportan Leuc: 37.9 Seg: 69 Linf: 31% Hb: 15.2 Hto: 48.1% PLT: 400 Glic: 684 Creat: 1.8 Na: 146 K:4.2 gases arteriales Ph:7.0 PCO2: 19  PO2: 50 HCO3: 4.7 EB: -26.6 SATO2:  ''',
			"piel": ''' Moreno, normotérmico, normoelástico, con llenado capilar < 3 seg''',

			"cardiopulmonar": '''Tórax simétrico, ruidos respiratorios presentes, murmullo vesicular conservado sin agregados pulmonares. Ruidos cardiacos rítmicos, sin soplos	''',
			"abdomen": '''Plano, doloroso a la palpación en epigastrio e hipocondrio derecho, ruidos hidroaéreos presentes, no megalias''',
			"extremidades": '''Simétricas sin edemas''',
			"neurologico": ''' Paciente consciente orientado en tres planos, lenguaje coherente.''',

		},  

		"diagnosticoIngresoHUAPA": [
								"Cetoacidosis diabética.",
								{"resumen":''' El paciente es evaluado por servicio de cirugía quien realiza paneo ecosonográfico abdominal que reporta como hallazgo parénquima pancreático heterogéneo a predomino de cuerpo y cola, Rx de abdomen simple de pie sin evidencia de neumoperitoneo. El paciente es evaluado por UCI en área de consulta de cirugía; quien evalúa paciente deshidratado, en malas condiciones generales, con dificultad respiratoria decidiendo su traslado a sala de UCI.'''}
		], 
		
	},# 180

	{
		
		"nombre": "Jesús Alberto Aguilera Marin ", 		
		
		"edad": "18",
		
		"ci": "25.479.300 ", 
		
		"dirección": "Urbanización Eduardo González, Calle Principal ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1996,7,15),

		"lugarNacimiento": "Chacopata ", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,12,2),

		"fechaIngresoUCI": datetime(2014,12,2),

		"resumenIngreso": '''Se trata de paciente masculino de 18 años de edad sin antecedentes patológicos conocidos, quien inicia enfermedad actual el día 30/11/2014 cuando posterior a accidente de tránsito tipo colisión (carro-poste) presenta pérdida de la consciencia, otorragia bilateral, motivos por los cuales es trasladado a Hospital de Carúpano donde es ingresado, se solicita valoración por Servicio de Neurocirugía quien indica valoración por UCI quien en vista de no contar con cupo refieren a este centro para valoración y conducta. Se recibe paciente en Área de Emergencia y se ingresa. El paciente es evaluado por el Servicio de Terapia Intensiva quien en vista de disponibilidad de cupo decide su ingreso al Servicio. Recibiendo paciente en cama de traslado, en malas condiciones generales, febril,  ventilando espontáneamente, recibiendo oxígeno húmedo por bigote nasal, se traslada a cama de UCI, en vista de estado neurológico se realiza intubación endotraqueal, colocando tubo Nº 7french, sin complicaciones, se conecta a ventilación mecánica con parámetros establecidos, posteriormente se procede a cateterizar Vía Venosa Central monolumen, en vena yugular derecha, con prueba de xifonaje positivo, se realiza radiografía control, evidenciándose correcta colocación de la misma.''',


		"diagnosticoIngresoUCI": [
										"Contusión Cerebral",
										"Hemorragia Subaracnoidea Fisher III",
										"Hematoma Subdural",
										"Neumoencéfalo ",
										"Fractura Bilateral del Peñasco del Temporal",
										"Fractura de Rama Ileo-Púbica Derecha",
										"Fractura Distal de Tibia Derecha",
										"Fractura del 1er metatarsiano derecho.",


									
								],

	

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente en malas condiciones generales, ventilando espontáneamente, recibiendo oxígeno húmedo por cánula nasal, se traslada a cama de UCI, se conecta a monitor cardíaco externo que reporta: TA: 141/50mmHg FC: 158lpm; FR:48rpm; SPO2: 99%  En vista de evidenciarse radiografías de ambas extremidades con alteraciones y además radiografía de pelvis con trazo de fractura, se solicita valoración por el Servicio de Traumatología quienes acuden al Servicio evalúan al paciente y deciden colocar fijador externo en pierna derecha para fijar fractura de tibia derecha y se coloca férula suropédica en miembro inferior izquierdo para pie traumático, planteándose además posterior resolución quirúrgica y solicitan TAC de Cadera.''',
			"piel": ''' Morena, hipertérmica al tacto, turgor conservado, con marcada palidez cutáneo-mucosa, llenado capilar < 3 segundos''',
			"cardiopulmonar": '''Tórax simétrico, hipoexpansible, ruidos respiratorios presentes con abundantes roncus bilaterales, disminuidos en tercio medio de hemitórax derecho, ruidos cardíacos rítmicos, regulares, taquicárdicos, sin soplos.''',
			"abdomen": '''plano, blando, depresible, no impresiona dolor a la palpación, ruidos hidroaéreos presentes. ''',
			"extremidades": '''Se evidencia inmovilización tipo férula en ambos miembros inferiores''',
			"neurologico": '''Inconsciente, Glasgow: 10/15pts, Respuesta Motora: 6pts (limitado a apertura ocular), Respuesta Verbal: 1pt, Apertura Ocular: 3pts. Pupilas isocóricas, reactivas a la luz.''',

		},  

		"diagnosticoIngresoHUAPA": [
								
			"Politraumatizado",
			"Traumatismo Craneoencefálico Severo complicado con Hemorragia Subaracnoidea",
			"Fractura de tercio medio y distal de tibia derecha",
			"Fractura transversa de Acétabulo derecho",
			"Fractura de 1er metatarsiano, cabeza de 1er y 4to metatarsiano (Luxo-Fractura de Lisfranc)",
			"Infección Respiratoria Baja: Neumonía por Broncoaspiración",
			"Rabdomiolisis",
			"Trastorno Hematológico: Anemia Moderada, Trombocitopenia",
			"Trastorno Hidroelectrolítico: Hipokalemia, Hipernatremia.",
			"Trastorno Acido/Base: Hiperoxemia",

		], 
		
	},# 181

	{
		
		"nombre": "Jesús Antonio García López", 		
		
		"edad": "17",
		
		
		"dirección": "Tronconal calle 4, Barcelona - Estado Anzoátegui.",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1997,12,16),

		"lugarNacimiento": "Puerto la Cruz", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,9,30),

		"fechaIngresoUCI": datetime(2015,9,30),

		"antecedentes": '''Alergia a la Gentamicina. Episodio convulsivo hace 1 año durante episodio febril, niega antecedentes de Asma, Diabetes e hipertensión arterial. Padre fallecido. Hábito alcohólico tipo social. Niegan tabáquicos y drogas,''', 

		"resumenIngreso": '''Se trata de paciente masculino de 17 años de edad, natural de Puerto la Cruz, procedente de Mariguitar, con antecedentes de episodio convulsivo hace 1 año (datos aportados por familiar que no precisan). El cual, refiere inicio de enfermedad actual el día 29/09/2015 cuando presenta cefalea de moderada a fuerte intensidad, sin atenuantes, posterior aumento de la temperatura corporal, no cuantificado, el día 30/09/2015 en horas de la mañana se anexa al cuadro deterioro progresivo de la consciencia y relajación del esfínter vesical, por lo que es trasladado al ambulatorio de la localidad donde evalúan y refieren a este centro donde ingresa por el Servicio de Medicina Interna.''',


		"examenFisicoIngresoUCI": {

			"resumen": '''  Se recibe paciente en camilla de traslado recibiendo  Oxígeno húmedo por Mascarilla facial a10 litros por minuto. Se traslada a cama de UCI y se conecta a monitor cardiaco que reporta signos vitales: TA: 81/50 mmHg  (68) mmHg   FC: 116 lpm   FR: 16 rpm  SatO2: 75%. Se evidencia franca hipoexpansibilidad torácica, por lo que se decide colocar tubo endotraqueal 8 Fr. Evidenciándose la salida de secreciones bronquiales con restos de contenido gástrico. Se conecta a Ventilación Mecánica con los siguientes parámetros: MODO: A/C  Fr: 12/ FiO2: 60/Vc: 480/ FL: 50/PEEP: 0.''',
			
			"piel" : 	'''	Morena, normotérmica al tacto, turgor y elasticidad disminuidos.''',

			"cardiopulmonar":  ''' tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares disminuidos en base derecha,  Ruidos cardiacos regulares, rítmicos sin soplos, ni galopes.	''',
			"abdomen": ''' plano, Rs Hs Ps, blando, depresible, no doloroso a la palpación, no megalias. ''',

			"neurologico": ''' Inconsciente, pupilas mióticas puntiformes, con escasa respuesta a estímulos luminosos.''',
			"extremidades": '''simétricas, eutróficas, sin edema.''',

		}, 


		"diagnosticoIngresoUCI": [
								"Evento cerebrovascular de probable etiología hemorrágica.",
								"Estado Post RCP.",
								"Neumonía por Broncoaspiración.",
								"Inestabilidad hemodinámica.",
								"Trastorno Hidroeléctrico: Hipokalemia.",
								"Trastorno Acido-Base: Acidosis respiratoria descompensada más hipoxemia.",
									
								],
		"diagnosticoActual": [

			"HIPOVENTILACION ALVEOLAR IDIOPATICA ",
			"ESTADO POST RCP",
			"IRB NEUMONIA POR BRONCOASPIRACION ",
			"TRASTORNO HEMATOLOGICO :ANEMIA MODERADA ", 
			"TRASTORNO ACIDO BASE : ACIDOSIS RESPIRATORIA COMPENSADA +ALCALOSIS METABOLICA ",

		],

		

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se traslada al paciente al área de choque, se conecta a monitor cardiaco externo donde se evidencia cifras de tensión arterial 40/20 mmHg FC:115 Lpm FR: 18 rpm, al examen físico neurológico paciente estuporoso, Glasgow RO: 1 pto RV: 1pto RM: 1pto, pupilas puntiformes con escasa respuesta a la luz, se procede a administrar fluidoterapia con solución 0,9 %  3000 cc en 3 horas, lasix 40 mg VEV STAT, Flumazenil 1 ampolla VEV STAT, Oxígeno por mascarilla facial a 10 lts por minuto, se realizan gases arteriales que reportan   pH: 6,96 PCO: bajo (no calculado) PO2: 79 mmHg HCO3, EB y SatO2 no calculados por la máquina, se le coloca Foley 14 fr, obteniéndose orinas claras 2700 cc. Se solicita evaluación por Terapia Intensiva quien acude al llamado, se repite gasometría que reporta pH: 6,94 PCO2: 97 mmHg PO2: 55 mmHg HCO3: 20,8 mmHg EB: -11,5 mmol/L  SATO2:64% por lo que se consulta caso a Dra. Cortesía quien en vista de disponibilidad de cupo se decide su ingreso a UCI.''',
			"piel": ''' Morena, hidratada, afebril, turgor y elasticidad conservada, cianosis distal y peribucal.''',
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presente en ambos campos pulmonares, sin agregados, ruidos cardiacos rítmicos no soplos.''',
			"abdomen": '''plano, Rs Hs Ps, blando, depresible, no doloroso a la palpación, no megalias.  ''',
			"extremidades": '''simétricas, eutróficas, sin edema.''',
			"neurologico": '''Inconsciente, pupilas mióticas puntiformes, con escasa respuesta a estímulos luminosos.''',
		},  

		"diagnosticoIngresoHUAPA": [
								
		"Intoxicación por drogas ilícitas",
		"SCA: IMSEST cara antero-septal.",
		"Trastorno Acido-Base: Acidosis Respiratoria.",
		"Inestabilidad hemodinámica.",
		{"resumen":''' Al ingreso el paciente presenta bradicardia que progresa a la asistolia ameritando de reanimación cardiopulmonar básica y avanzada, con posterior recuperación del ritmo cardíaco con taquicardia sinusal 136 lpm, saturación de O2: 69% que se corrobora en gasometría arterial con hipoxemia que mejora con la colocación de Peep: 8 Vc: 420, posteriormente se evidencia hipotensión 45/32 mmHg, que amerita la colocación de Levophed a dosis de 32 mcg/min, se le cateteriza vía central yugular derecha con catéter 6.0 Fr, xifonaje positivo el cual se corrobora con Rayos X de torax AP, a su vez con el hallazgo de infiltrado pulmonar en base derecha, por lo que se plantea el diagnóstico de Neumonía por Broncoaspiración por lo que se asocia Clindamicina: 900 mg cada 8 horas. Se realizan controles electrocardiográficos que evidencian ondas T negativas desde V1 a V4, desviación del Eje a la derecha con Hemibloqueo de Rama derecha del haz de His. Paciente que se mantiene intubado conectado a ventilación mecánica EVITA MODO AC VC 480 FL 50 FIO2 50 FR 12 PEEP 0, se logra estabilidad hemodinámica iniciándose tratamiento médico con cefotaxima, vancomicina a dosis meníngeas así como dexametasona, se realiza TAC de cráneo donde se evidencia edema cerebral difuso asi como imagen sugestiva de LOE cerebral en fosa posterior se inicia tratamiento con manitol al 18 % por tres días logrando recuperación de estado neurológico llegando a ECG 11/15 puntos RM 6 RO 4 RV 1 limitado por TET con destete ventilatorio progresivo hasta T de AYRES con oxígeno húmedo a 10 LT por minuto ,siendo el mayor inconveniente la hipoventilacion del paciente con gases arteriales que reportan pco2 mayor a 60 con síntomas carecteristicos de narcolepsia por lo que pensamos en algún trastorno compresivo o isquémico en tallo por lo que se solicita RMN contrastada la cual no se ha realizado por permanecer intubado el paciente.Se realiza RMN sin contraste con resultados normales por lo que se descarta el diagnostico de LOE cerebral ,se realiza protocolo de extubación lográndose con éxito manteniéndose por 72 horas tolerando mascarilla facial con oxígeno  a 10 lt por minuto ,cabe destacar que se mantiene con acidosis respiratoria compensada con valores de co2 por  encima de 70 mmhg ,por su evolución favorable se decide egreso a observación y se remite informe para BIPAP. FC 87 LPM    FR 15  RPM  TA  123/75 MMHG    SATOHG  99 % '''}

		], 
		
	},# 182

	{
		"IdHistoria": "51–83–36 ", 
		
		"nombre": "Jesús Gregorio Jiménez Guerra", 		
		
		"edad": "29",
		
		"ci": "19.041.966 ", 
		
		"dirección": "Sector 5 de Julio, casa S/N, Carúpano, Edo. Sucre.",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1984,8,9),

		"lugarNacimiento": "San Félix", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,3,16),

		"fechaIngresoUCI": datetime(2014,3,19),


		"resumenIngreso": '''Paciente masculino de 29 años de edad, natural de San Félix y procedente de Carúpano, sin antecedentes patológicos, cuyo familiar refiere inicio de enfermedad actual el 16/03/2014 cuando posterior a accidente de tránsito tipo colisión en moto contra objeto fijo (Carro), presenta traumatismos múltiples, pérdida del estado de consciencia por varios minutos y aumento de volumen en muslo derecho con deformidad y limitación funcional, motivo por el cual es trasladado al hospital de Carúpano donde se le coloca férula lumbopédica y posteriormente referido a este centro asistencial donde es valorado e ingresado por el servicio de Traumatología y Neurocirugía; al momento del ingreso se realiza lavado peritoneal que resulta negativo, al examen físico se evidencia tórax simétrico, normoexpansible, con ruidos respiratorios presentes en ambos campos pulmonares con roncus bilaterales, ruidos cardíacos rítmicos y regulares, taquicárdicos, sin soplo ni galope, abdomen blando, depresible, que no impresiona doloroso, sin megalias, en extremidades se evidencia miembro inferior derecho con férula lumbopédica con apósitos con secreción hemática, neurológicamente estuporoso, pupilas isocóricas con respuesta a la luz, FM V/V limitada en MID, ROT II/IV, Glasgow 8/15pts (RM: 5pts, RO: 1pto, RV: 2pts). Se ingresa con los diagnósticos de 1) Traumatismos Múltiples: a) TCE moderado simple cerrado, b) Traumatismo Tóraco-abdominal cerrado, 2) Fractura trifragmentaria de tercio medio de fémur derecho. Solicitan valoración por UCI, siendo evaluado en área de quirofanito de emergencia y se hacen sugerencias. El día de hoy 19/03/14 es trasladado al área de choque donde es atendido por Dra. Vásquez (Intensivista) quien realiza vía venosa subclavia derecha sin complicaciones, en vista de condiciones generales del paciente y por autorización de Dra. Roa (Intensivista) se decide su ingreso a UCI y dicta órdenes médicas.''',


		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, recibiendo O2 por bigote nasal a 5LtrsX’, se pasa a cama UCI y se conecta a monitor cardíaco continuo que reporta: TA: 130/84(93) mmHg; FC: 85 lpm; FR: 14 rpm; SatO2: 98%''',
			
			"piel" : 	'''	morena, normotérmica al tacto, llenado capilar < 3seg.''',
			"cabeza": ''' sin tumoraciones ni reblandecimientos.''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados. Ruidos cardíacos rítmicos y regulares, taquicardicos, sin soplo ni galope.''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, con herida quirúrgica de lavado peritoneal cubierta por apósitos limpios y secos, blando, depresible, no impresiona doloroso a la palpación, no megálico.''',

			"neurologico": ''' estuporoso, con agitación psicomotriz, desorientado en tiempo y espacio, orientado en persona, pupilas isocóricas, hiporreactivas a la luz, ROT II/IV, , Glasgow 11/15pts (RM: 5pts, RO: 4pts, RV: 2pts).''',
			"extremidades": '''miembro inferior derecho con equimosis en muslo y tobillo, con aumento de volumen y deformidad en muslo, con tracción esquelética transtuberositaria derecha sobre férula de Brown.''',
		}, 

		"diagnosticoIngresoUCI": [
								"TRAUMATISMO CRANEOENCEFALICO MODERADO ",
								"TRAUMATISMO TORACO-ABDOMINAL CERRADO",
								"FRACTURA TRIFRAGMENTARIA DE FEMUR DERECHO",
								"RABDOMIOLISIS",
								"TRASTORNO HEMATOLOGICO:",
								"ANEMIA SEVERA",
								"TRASTORNO ACIDO-BASE:",
								"ALCALOSIS METABOLICA COMPENSADA + HIPEROXEMIA",
	
								],
		
	},# 183

	{
		"IdHistoria": "52-86-27", 
		
		"nombre": "Jesús  Ramón Marval López ", 		
		
		"edad": "25",

		"dirección": "Guayacán, Calle principal s/n  Güiria  ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1989,3,23),

		"lugarNacimiento": "Güiria ", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,12,29),

		"fechaIngresoUCI": datetime(2014,12,29),

 

		"resumenIngreso": '''Se trata de paciente masculino de 25 años de edad sin antecedentes patológicos conocidos, quien inicia enfermedad actual el día 28/12/2014 cuando posterior a accidente de tránsito tipo colisión  contra objeto fijo presenta pérdida de la consciencia y traumatismos múltiples , motivo por el cual es trasladado al Hospital de Carúpano donde se evidencia deterioro neurológico dado por Glasgow de 6/ 15 puntos RM 4 RO 1 RV 1 se solicita valoración por Servicio de Neurocirugía quien indica referir a este centro donde llega en malas condiciones y se ingresa con los diagnósticos :  TRAUMATISMO CRANEOENCEFALICO SEVERO. FRACTURA DE CLAVICULA IZQUIERDA ''',



		"examenFisicoIngresoUCI": {

			"resumen": ''' Recibimos paciente en cama de traslado, en malas condiciones generales, recibiendo oxígeno húmedo por bigote nasal, se traslada a cama de UCI,  se realiza intubación endotraqueal, colocando tubo Nº 8 french, sin complicaciones, se conecta a ventilación mecánica con parámetros establecidos EVITA 4 MODO AC VC 560 FIO2 50 FL 50 PEEP 0 TA: 165/80mmHg	FC: 138lpm	 FR:38rpm SPO2: 89% Se evidencia Vía venosa subclavia derecha procedemos a realizar rayos x para verificar posición de la misma. Paciente que permanece ingresado 16 días en nuestro servicio con los diagnósticos 1. Politraumatizado:1.1 traumatismo craneoencefálico severo complicado con edema cerebral además de hemorragia Subaracnoidea  por lo cual cumplió tratamiento anti edema cerebral con manitol durante 6 días ,solución hipertónica al 20% durante 4 días con mejoría del estado neurológico. Recibe actualmente tratamiento antibiótico con Imipenem 500mg vev /6h  en vista de recibir resultados de cultivo de secreción bronquial que reporta (klebsiella pneumoniae) demás de uro cultivó que reporta (acinetobanter especies) ambos sensibles al fármaco ya descrito. Para el día de hoy dada la mejoría clínica del paciente, en revista médica con Dra. cortesía y Dr. Guaimare se decide su egreso del servicio de uci y traslado a piso 8 a cargo de traumatología y cirugía blanda.''',
			
			"piel" : 	'''	Morena, normotérmica al tacto, turgor conservado, con marcada palidez cutáneo-mucosa, llenado capilar < 3 segundos. Múltiples escoriaciones a nivel del hombro derecho tipo quemadura por fricción, flictenas a nivel de miembro inferior derecho.''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes con abundantes roncus bilaterales, ruidos cardíacos rítmicos, regulares, taquicárdicos, sin soplos.''',
			"abdomen": ''' plano, blando, depresible, no impresiona dolor a la palpación, ruidos hidroaéreos presentes. ''',

			"neurologico": ''' Inconsciente, Glasgow: 6/15pts, Respuesta Motora: 4pts, Respuesta Verbal: 1pt, Apertura Ocular: 1pts. Pupilas isocóricas, reactivas a la luz. Reflejo corneal presente, reflejos osteotendinosos presentes II/IV ,impresiona hemiparesia braquial izquierda  ''',
			"extremidades": '''Se evidencia aumento de volumen en región clavicular izquierda, férula inguinopelvica izquierda y férula braquial derecho''',
		}, 

		"examenFisicoEgreso": {

			"resumen": ''' Paciente consiente con traqueostomo conectado a T de ayres con O2 húmedo a 10 litros, conectado a monitor cardiaco que reporta  FC:72 lpm FR:22rpm TA:139/81 mmHg TAM(89)mmHg  SAO2:100% ''',
			
			"piel" : 	'''	turgor y elasticidad conservado llenado capilar menor de 10s, se evidencia moderada palidez cutánea mucosa, además de curas en muslo derecho y hombro ibsilateral y escoriaciones en fase de resolución en antebrazo contra lateral.''',

			"cardiopulmonar":  ''' tórax simétrico hipoexpansible, ruidos respiratorios presentes con agregados roncos en ambos ápices, ruidos cardiacos rítmicos regulares sin soplo ni galope''',
			"abdomen": ''' plano, ruidos hidroaéreos presentes, no impresiona dolor a la palpación, no visceromegalia.  ''',

			"neurologico": ''' paciente consiente, pupilas isocóricas normorreactivas a la luz, Glasgow 10/15 pts. Dada por RM:5pts. RV:1pt limitado por traqueostomo RO:4pts. ,   ''',
			"extremidades": '''simétricas, se evidencia fijadores externos en muslo de miembro inferior  izquierdo, y férula antebraquipalmar en miembro superior derecho, sin edemas. ''',
		}, 

		"diagnosticoIngresoUCI": [

									"Politraumatizado",
									"Traumatismo Craneoencefálico Severo complicado con:",
									"Hemorragia Subaracnoidea post traumática ",
									"Edema cerebral ",
									 "Fractura de tercio medio de clavícula izquierda ",
									"Fractura diafisaria de fémur izquierdo",
									"Fractura 1 2 y 3 metacarpiano derecho ",
									"Traumatismo Toraco abdominal cerrado ",
									"Infección Respiratoria Baja: Neumonía por Broncoaspiración",
									"Hidroneumotorax ",
									"Rabdomiolisis",
									"Trastorno Acido/Base: Acidosis metabólica +alcalosis respiratoria compensada",

									
								],

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' NO SE REPORTAN SIGNOS VITALES AL INGRESO. El paciente es evaluado por el Servicio de Terapia Intensiva quien en vista de disponibilidad de cupo decide su ingreso al Servicio. ''',
			"piel": ''' Morena, normotérmica al tacto, turgor conservado, con marcada palidez cutáneo-mucosa, llenado capilar < 3 segundos. Múltiples escoriaciones a nivel del hombro derecho tipo quemadura por fricción, flictenas a nivel de miembro inferior derecho ''',
		
			
			"cardiopulmonar": '''Tórax simétrico, normoexpansible, ruidos respiratorios presentes con abundantes roncus bilaterales, ruidos cardíacos rítmicos, regulares, taquicárdicos, sin soplos.''',
			"abdomen": ''' plano, blando, depresible, no impresiona dolor a la palpación, ruidos hidroaéreos presentes.''',
			"extremidades": '''Se evidencia aumento de volumen en región clavicular izquierda, férula inguinopelvica izquierda y férula braquial derecha ''',
			"neurologico": '''Inconsciente, Glasgow: 6/15pts, Respuesta Motora: 4pts, Respuesta Verbal: 1pt, Apertura Ocular: 1pts. Pupilas isocóricas, reactivas a la luz. Reflejo corneal presente, reflejos osteotendinosos presentes II/IV  ''',


		},  

		"diagnosticoIngresoHUAPA": [
								"Politraumatizado",
								"Traumatismo Craneoencefálico Severo complicado con:",
								"Hemorragia Subaracnoidea post traumática ",
								"Edema cerebral ",
								"Fractura de tercio medio de clavícula izquierda ",
								"Fractura diafisaria de fémur izquierdo",
								"Fractura 1 2 y 3 metacarpiano derecho", 
								"Traumatismo Toraco abdominal cerrado (R)",
								"Infección Respiratoria Baja: Neumonía asociada a ventilación mecánica",
								"Infección del tracto urinario bacteriana.",
								"Hidroneumotorax (R)",
								"Rabdomiolisis (R)",
								"Trastorno hematológico:",
								"Anemia moderada",
								"trombositosis",
		], 
		
	},# 184

	{
		"IdHistoria": "53-09-32", 
		
		"nombre": "Edgar Rafael Arismendi ", 		
		
		"edad": "66",
		
		"ci": "4.689.958", 
		
		"dirección": "calle principal boca de sabana casa sin número",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1949,1,1),

		"lugarNacimiento": "cumana-estado sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,3,2),

		"fechaIngresoUCI": datetime(2015,3,2),

		"resumenIngreso": '''Se trata de paciente masculino de 66 años de edad natural y procedente de la localidad, con antecedentes de hipertensión arterial sistémica en tratamiento con enalapril 10 mg cada 12 horas, Diabetes Mellitus tipo II en tratamiento con euglucon (glibenclamida) 5 mg. inicia enfermedad actual el día 01/03/2015 cuando es hallado por familiares inconsciente con desviación de la comisura labial hacia la izquierda, motivo por el cual es traslado a nuestro centro asistencial donde es evaluado por servicio de medicina interna y es ingresado con diagnostico: Emergencia hipertensiva tipo ACV hemorrágico. Hipertensión arterial sistémica. Diabetes Mellitus   ''',


		"examenFisicoIngresoUCI": {

			"resumen": ''' Fc 95 lpm Fr: 15 rpm TA: 190/100 mmHg SATO2: %. En vista de condiciones clínicas de paciente comunican caso a especialista de guardia DR Camino quien indica solicitar valoración por UCI. Se acude al llamado evaluando paciente en área de choque en condiciones clínicas de cuidados constatando deterioro del estado neurológico, trabajo respiratorio además de desaturación por monitor constatado posteriormente por gases arteriales se decide a su intubación endotraqueal con tubo 8.0 Fr. sin complicaciones evidenciando salida de secreción con contenido alimentario a través de tubo endotraqueal se conecta a ventilación mecánica y en vista de no contar cupo en el servicio se realizan sugerencias. Paciente permanece durante 24 horas en área de choque siendo evaluado el día 02/03/2015 quien decide rotar antibióticoterapia, dosis stat de manitol al 18%  de 500 cc, indica tratamiento antipertensivo y solicita valoración por el servicio de Neurocirugía. En vista de contar con cupo en UCI se decide su ingreso.''',
			
			"piel" : 	'''	morena, normo térmica, normohidratada llenado capilar <3 Seg.''',

			"cardiopulmonar":  ''' tórax simétrico, normo expansible, ruidos respiratorios presentes, no se  auscultan  .ruidos cardiacos rítmicos taquicárdicos normofonéticos, no soplos.''',
			"abdomen": ''' globuloso, a expensa de panículo adiposo, ruidos hidroaéreos presentes.''',

			"neurologico": ''' nconsciente desorientado, irritable Glasgow 6/15 ptos. ''',

			"extremidades": '''simétricas  sin edema.''',
		}, 

		"examenFisicoEgreso": {
			
			"piel" : 	'''	normo hídrica, afebril al tacto, dedos con uña en vidrio reloj.''',
			
			"cardiopulmonar":  '''Tórax simétrico, expandible; ruidos cardiacos rítmicos, normo fonéticos, soplo sistólico III-IV/VI. Ruidos respiratorios presentes MV conservado, sin agregados .''',
			"abdomen": ''' Plano, depresible, no doloroso a la palpación, no visceromegalia RHA presentes. ''',

			"neurologico": ''' Consciente orientado en TEP  Glasgow 14/15 ptos  (RM5 RV1 RO2), pupilas isocóricas normorreactivas a la luz.''',
		}, 

		"diagnosticoIngresoUCI": [
									"Cardiopatía congénita tipo CIV.",
									"Infección Respiratoria Baja: neumonía derecha adquirida en la comunidad",
									"Hipertensión pulmonar.",
									{"resumen":''' Paciente que permanece en UCI 7 días recibiendo a su ingreso ATB con levofloxacina e imipenem en el contexto de IRB : Neumonia derecha ,debido a  la presencia de convulsiones previas al ingreso se solicita TAC de cráneo donde se evidencia Absceso cerebral frontal por lo que se decide llevar a mesa operatoria para drenaje de absceso la cual fue satisfactoria drenándose 20 cc de pus el cual fue cultivado creciendo germen patógeno  escherichia coli , en tal contexto (infección del SNC ) se inicio tratamiento con metronidazol,cefotaxima y vancominina con evolución clínica favorable lográndose extubación endotraqueal sin complicaciones manteniéndose por 48 horas recibindo oxigeno húmedo por mascarilla facial a razón de 8 lt por minuto ,se realiza TAC control donde se evidencia reabsorción parcial de absceso cerebral ,por evolución favorable se decide egreso .Recibe tratamiento con sildenafil en el contexto de HT pulmonar'''}

								],

		"diagnosticoEgresoUCI": [

									"Cardiopatía congénita tipo CIV.",
									"Infección del SNC Absceso cerebral", 
									"POM craneotomía para drenaje de absceso cerebral ",
									"Infección Respiratoria Baja: neumonía derecha adquirida en la comunidad resuelta ",
									"Hipertensión pulmona",

									
								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Se recibe paciente en camilla de traslado, intubado, recibiendo oxigeno húmedo por ambu, se traslada a cama UCI, se conecta a monitor cardiaco continuo que reporta: Fc 93 lpm   Fr: 18 rpm  TA: 163/108 (125) mmHg  SATO2: 95%.''',
			"piel": ''' normo hídrica, afebril al tacto, dedos con uña en vidrio reloj.''',
			
			"cardiopulmonar": '''Tórax simétrico, expandible; ruidos cardiacos rítmicos, normo fonéticos, soplo sistólico III-IV/VI. Ruidos respiratorios presentes MV conservado, se auscultan crepitantes en hemitorax derecho y base pulmonar izquierda.	 ''',
			"abdomen": '''Plano, depresible, no doloroso a la palpación, no visceromegalia RHA presentes.''',
			
			"neurologico": '''estuporoso, Glasgow 8/15 ptos (RM5 RV1 RO2), pupilas isocóricas hiporreactivas a la luz. ''',
		},  
		
	}, # 185

	{
		
		"nombre": "Jesus Maria Urbaneja", 		
		
		"edad": "62",
		
		"ci": "4.188.222", 
		
		"dirección": "calle Caiguire calle el cementerio s/n. Cumana",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1951,12,19),

		"lugarNacimiento": "cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,3,19),

		"fechaIngresoUCI": datetime(2014,3,19),

		"resumenIngreso": '''Paciente masculino natural y procedente de la localidad, de  62 años de edad con antecedentes de cardiopatía isquémica, hipertensión artrerial con tratamiento de Losartan potásico 100 mg OD, Atorvastatina 80 mg OD, Clopidogrel 75 mg OD y Aspirina OD, quien inicia enfermedad actual el dia 18/03/14 presenta sincope, posteriormente disartria, hemiparesia, desviación de la comisura labial y somnolencia, por lo que es trasladado a este centro asistencial donde es evaluado y se decide su ingreso. ''',

		"examenFisicoIngresoUCI": {
			
			"piel" : 	'''	normohidratada, febril al tacto''',

			"cardiopulmonar":  ''' Tórax simétrico, expansible, ruidos respiratorios presentes MV conservado , sin agregados, ruidos cardíacos  rítmicos, regulares, sin soplos ni galope. ''',
			"abdomen": ''' Blando, depresible, ruidos hidroaéreos presentes, no megálico.''',

			"neurologico": ''' inconsciente, Glasgow 4/15 puntos (RM 2 RO 1 RV 1).''',
		}, 

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 150 /70 mmHg FC: 53 lpm FR: 26 rpm''',
			
			"piel" : 	'''	palidez cutáneo mucosa leve, buen llenado capilar''',

			"abdomen": ''' Blando, depresible, no doloroso a la palpación, RH presentes''',

			"neurologico": ''' Inconsciente, pupilas anisocóricas, Glasgow 8/15 puntos''',
		}, 


		"diagnosticoIngresoUCI": [
									"Emergencia Hipertensiva expresada en ACV Hemorragico",
									"Hipertensión Arterial",
									"Hemorragia Digestiva Superior",
									"Trastorno Hidro-Electrolitico: Hipokalemia.",
								],


		"diagnosticoIngresoHUAPA": [
				"ECV en evolución ",
				"Emergencia Hipertensiva",
				"Hipertensión Arterial",
				{"resumen":''' El paciente es evaluado por UCI quien por no disponer de cupo hace sugerencias. El día de hoy es re evaluado en área de observación y por disponibilidad de cupo se decide su ingreso a UCI. Recibimos paciente en  camilla de traslado, intubado, recibiendo oxigeno mediante ambu  conectado  a reservorio, no conectado a monitor cardiaco. Se traslada a cama UCI y se conecta a monitor cardiaco que reporta: FR: 14 rpm FC: 106 lpm TA:54/38(49) mmHg  SATO2: 98%'''}
		], 
		
	},#186


	{
		"IdHistoria": "52-80-36 ", 
		
		"nombre": "Luiggy Rafael Gómez Rodriguez", 		
		
		"edad": "19",
		
		"ci": "23.433.298", 
		
		"dirección": "Calle Ezequiel Zamora “El Peñon” ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1995,12,6),

		"lugarNacimiento": "Cumaná - Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,12,8),

		"fechaIngresoUCI": datetime(2014,12,8),

		"antecedentes": '''ALERGIA A LA NOVALCINA''', 

		"resumenIngreso": '''Se trata de paciente masculino de 14 años natural y procedente de la localidad, sin antecedentes patológicos importantes, fumador (familiar no precisa cantidad de cigarrillos diarios). Quien inicia enfermedad actual el día 8/12/14 cuando posterior a herida por arma blanca en región de zona 2 del cuello del lado izquierdo, motivo por el cual es traído a este centro donde se evalúa e ingresa por servicio de cirugía blanda ''',

		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente es trasladado en camilla de transporte, conectado a monitor cardíaco externo que reporta signos vitales: TA: 98/48mmHg  FC: 90 lpm FR: 25rpm SatO2: 99%, intubado recibiendo oxigeno por ambu; se traslada a cama UCI, conectándose a ventilación mecánica AC Vc: 600 FiO2: 50 Fl: 50 Fr: 12 PEEP: 0 y  a monitor cardiaco externo que reporta signos vitales:  TA:  mmHg   FC:   lpm	FR: rpm    	SPO2: 99   %''',
			
			"piel" : 	'''	Blanca, normotérmica al tacto, llenado capilar <3 segundos.''',
			"cuello": '''Presencia de herida quirúrgica en región lateral izquierda del cuellocubierta por apósito estéril limpia y sin secreciones. ''',

			"cardiopulmonar":  '''tórax simétrico, expandible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos normofonéticos, taquicárdicos,  sin soplos ni galope. ''',
			"abdomen": ''' blando, plano, depresible, no impresiona doloroso a la palpación, ruidos hidroaéreos presentes, no megalias.  ''',

			"neurologico": ''' bajo efectos de sedación y relajación, pupilas anisocóricas, hiporreactivas a respuesta a la luz, Glasgow: no evaluable por sedación. ''',
		}, 


		"diagnosticoIngresoUCI": ["Herida por arma blanca de zona 2 del cuello lado izquierdo."],

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' En vista de que el paciente presenta palidez cutáneo mucosa, y sangrado por la herida en región de zona 2 del cuello es llevado a mesa operatoria donde se evidencia lesión de arteria carótida común a nivel de la emergencia de la carótida externa en 100%; se realiza pinzamiento sección y ligadura de arteria carótida externa izquierda, comprobación de hemostasia y síntesis por planos. El paciente es llevado a recuperación donde solicitan valoración por UCI. Se evalúa paciente en cama en malas condiciones generales, recibiendo oxigeno húmedo por mascarilla facial a 10 litros por minutos, conectado a monitor cardiaco que reporta Fc: 118 lpm Fr: 36 rpm TA: 88/37 mmHg SATO2: 98%; pálido, sudoroso, frio, pupilas anisocóricas, midriasis izquierda no reactiva a la luz. Se procede a realizar intubación endotraqueal con tubo 7.0 Fr sin complicaciones; se presenta caso a especialista de guardia Dr Alpino quien decide su ingreso a la UCI.''',
			
			"piel": ''' Blanca, fría, sudorosa, pálida ''',
			
			"cuello": '''Se evidencia herida de aproximadamente 4 cm en zona 2 izquierda. ''',

			"cardiopulmonar": '''Tórax simétrico, normo expansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos normofonéticos, taquicárdicos,  sin soplos ni galope.''',

			"abdomen": '''blando, plano, depresible, no doloroso a la palpación, ruidos hidroaéreos presentes, no megalias ''',
			
			"extremidades": '''simétricas sin edema.''',

			"neurologico": '''Estuporoso.''',
		

		},  

		"diagnosticoIngresoHUAPA": [
					"Postoperatorio Inmediato de Herida por arma blanca en zona 2 del cuello lado izquierdo complicada con lesión vascular arteria carótida externa.",
					"Anemia Moderada.",

		], 
		
	},#187


	{
		"IdHistoria": "53-35-35", 
		
		"nombre": "José Miguel Rodríguez Segura", 		
		
		"edad": "15",
		
		"ci": "27.208.255", 
		
		"dirección": "Tumiriquire El bajo ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1999,12,31),

		"lugarNacimiento": "cumana", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,5,10),

		"fechaIngresoUCI": datetime(2015,5,13),

		"resumenIngreso": '''Se trata de paciente masculino,  de 15  años de edad, natural del Estado  Miranda y procedente de los Valles del Tuy , sin antecedentes patológicos conocidos, quien inicia enfermedad actual el día 10/05/2015 cuando posterior a accidente tipo colisión vehículo moto  presenta múltiples traumatismos en cráneo ,pelvis y pierna izquierda además deterioro del estado de consciencia por lo que es traído a nuestro centro asistencial, es evaluado por el servicio de traumatología siendo ingresado con los siguientes diagnósticos.''',


		"examenFisicoIngresoUCI": {

			"resumen": '''  Paciente es trasladado en camilla de transporte, sin recibir oxigeno no  conectado a ventilador de traslado, se traslada a cama UCI, conectándose a monitor cardiaco externo que reporta signos vitales: TA: 131/72 mmHg (97)   FC: 65   lpm FR: 12 rpm    SPO2: 100%. Se realiza intubación endotraqueal con TET 8 F sin complicaciones y se conecta a ventilación mecánica modo AC VC 560 FL 50 FIO2 50 FR 12 PEEP 0 ,se realiza además colocación de VVC yugular posterior izquierda con catéter mono lumen 6 f sin complicaciones con xifonaje positivo, se realiza rayos x de tórax comprobándose adecuada colocación de la vía ''',
			
			"piel" : 	'''	morena, Normotérmica al tacto, llenado capilar <3 segundos, con ligera palidez cutáneo mucosa. Escoriaciones a nivel de ambos miembros superiores tipo quemadura por fricción ''',
			"cabeza": ''' Escoriaciones a nivel facial y región temporal craneal ''',

			"cardiopulmonar":  ''' tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin agregados, ruidos cardíacos rítmico regulares,  sin soplos ni galope. ''',
			"abdomen": ''' blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes. ''',

			"neurologico": ''' Paciente bajo efectos de sedación farmacológica, Glasgow 7/15 RM 5 RO 1 RV 1. Pupilas isocóricas reactivas reflejo corneal presente  ''',
			"extremidades": '''Fractura abierta de tibia y peroné izquierda fijada con tutores externos.''',
			
		}, 

		"diagnosticoIngresoUCI": [
										"POLITRAUMATIZADO ",
										"TRAUMATISMO CRANEOENCEFALICO SEVERO COMPLICADO CON", 
										"EDEMA CEREBRAL DIFUSO ",
										"HEMORRAGIA SUBARACNOIDEA POSTRAUMATICA ",
										"TRAUMATISMO TORACO ABDOMINAL CERRADO",
										"FRACTURA ABIERTA DE TIBIA Y PERONE IZQUIERDO ",
										"TRASTORNO HIDROELECTROLITICO DESHIDRATACION ISOTONICA SEVERA", 
	
								],

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Paciente evaluado por servicio de neurocirugía evidenciando deterioro neurológico dado por Glasgow de 12/15 puntos RM 5  RO 4 RV 3 ,pupilas isocóricas reactivas a la luz reflejo corneal presente ,se indica TAC de cráneo en la cual se evidencia HEMORRAGIA SUBARACNOIDEA POSTRAUMATICA Y EDEMA CEREBRAL DIFUSO ,solicitándose valoración por UCI la cual se cumple anexando sugerencias. Para el día de hoy 13/05/2015 el paciente es llevado a mesa operatoria donde se realiza Fijación de la fractura  con tutor externo  en miembro inferior izquierdo  presentando  deterioro neurológico evidenciándose Glasgow 7/15 puntos dado por RM 5 RO 1  RV 1 por lo que es evaluado por servicio de terapia intensiva y debido a disponibilidad de cupo se decide su ingreso TA: 120/80 mmHg FC: 95 lpm FR: 15 rpm SPO2:%''',
			"piel": '''Normotérmica al tacto, llenado capilar <3 segundos. ''',
			
			"cardiopulmonar": '''tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, no agregados.''',
			"abdomen": '''blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes. ''',
			"extremidades": '''eutróficas, simétrica sin edema''',
			"neurologico": '''Consciente.''',

		},  

		"diagnosticoIngresoHUAPA": ["FRACTURA DE TERCIO MEDIO DE TIBIA Y PERONE IZQUIERDA"], 
		
	},# 188

	{
		"IdHistoria": "33-28-93", 
		
		"nombre": "Henry Vicente Montes Figueroa", 		
		
		"edad": "59",
		
		"ci": "4.190-846 ", 
		
		"dirección": "Barrio malariologia",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1956,2,20),

		"lugarNacimiento": "Cumaná - Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,1,31),

		"fechaIngresoUCI": datetime(2015,2,2),

		"resumenIngreso": '''Se trata de paciente masculino de 59años de edad  natural y procedente de la localidad, con antecedentes de Hipertensión Arterial en tratamiento con Amlodipina 5mgOD y Bisoprolol 5mgOD y Diabetes Mellitus tipo 2 tratada con Glucofage, quien inicia enfermedad actual el día 31/01/2015  cuando posterior a accidente de tránsito tipo arrollamiento presenta traumatismos múltiples, aumento de volumen y deformidad en pierna derecha, perdida de la conciencia por lo que es traído a esta institución, donde previa valoración se ingresa.''',

		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente es trasladado en camilla de transporte,  intubado recibiendo oxigeno por ambu; se traslada a cama UCI, conectándose a ventilación mecánica y a monitor cardiaco externo que reporta signos vitales: TA: 156/78 mmHg FC: 115   lpm	FR: 25 rpm    	SPO2: 94   %''',
			
			"piel" : 	'''	Blanca, pálida normotérmica al tacto, llenado capilar <3 segundos, con pálidez cutáneo mucosa.''',
			

			"cardiopulmonar":  '''tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, se auscultan crepitantes en ambas bases pulmonares, ruidos cardíacos normofonéticos, taquicárdicos,  sin soplos ni galope.''',
			"abdomen": ''' blando, plano, depresible, no impresiona dolor, no se palpan megalias, ruidos hidroaéreos presentes.''',

			"neurologico": ''' paciente en estado comatoso, Glasgow: RM: 4pts, RV:1pto, RV:1pto 6/15ptos. Pupilas isocóricas con tendencia a la miosis hiporreactivas a la luz''',
			"extremidades": '''se evidencia férula suropédica funcionante en miembro inferior derecho, pulso pedio presente.''',
	

		}, 

		"diagnosticoIngresoUCI": [
									"Politraumatizado",
									"Traumatismo Craneoencefálico Severo",
									"Traumatismo Toraco¬-Abdominal Cerrado",
									"Fractura distal de Fémur Derecho",
									"Infección Respiratoria Baja: Neumonía por Broncoaspiración",
									"Trastorno Hematológico: Anemia Severa, Trombocitopenia",

								],

		"diagnosticoIngresoHUAPA": [
								"Impresión Diagnóstica de Ingreso HUAPA :",
								"Traumatismo craneoncefálico ",
								"Traumatismo Toraco-Abdominal cerrado",
								"Fractura distal de Fémur",
								"Hipertensión arterial",
								"Diabetes Mellitus",
		], 
		
	},# 189

	{
		
		"nombre": "Jose del Valle Cordova ", 		
		
		"edad": "22",
		
		"ci": "20.991.892", 
		
		"dirección": "calle Buenos aires, detrás del Teide. Cumana ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1991,7,24),

		"lugarNacimiento": "CUMANA", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,4,8),

		"fechaIngresoUCI": datetime(2014,4,8),

		

		"resumenIngreso": '''Paciente masculino de 22 años de edad sin antecedentes patológicos importantes, quien inicia enfermedad actual el dia 31/03/14 cuando posterior a caída de vehículo en marcha presenta traumatismo craneo encefálico con deterioro del nivel de consciencia por lo que es traido a este centro donde se evalúa y se decide su ingreso ''',

		"examenFisicoIngresoUCI": {

			"resumen": ''' PACIENTE QUE SE MANTUVO EN NUESTRO SERVICIO POR ESPACIO DE 6 DIAS INTUBADO CONECTADO A VENTILACION MECANICA MODO AC VC 500 FIO2 50 FL 50 PEEP 0, SIN MEJORIA DESDE PUNTO DE VISTA NEUROLOGICO POR LO QUE AMERITO REALIZACION DE TRAQUEOSTOMIA SIN COMPLICACIONES Y COLOCACION DE TRAQUESTOMO 7 F, DESDE EL INICIO RECIBIENDO ANTIBIOTICOTERAPIA CON CEFTAZIDIMA VANCOMICINA Y DEBIDO A ASCENSO DE GLOBULOS BLANCOS SE DECIDE ROTAR A IMIPENEM Y MANTENER VANCOMICINA REPLANTEANDO DISGNOSTICO DE IRB NEUMONIA ASOCIADA A VENTILACION MECANICA Y SE EVIDENCIA MEJORA SIGNIFICATIVA EN PARACLINICOS POR LO QUE SE MANTIENE EL MISMO TRATAMIENTO A PESAR DE RECIBIRSE CULTIVO DE SECRECION BRONQUIAL CON PRESENCIA DE PSEUDOMONA AURINOSA , SE OBSERVA DISMINUCION DE SECRECIONES ASPIRADAS POR TRAQUEOSTOMO ASI COMO SE OBSERVAN MAS FLUIDAS ,SE REALIZA TAC DE CRANEO EVOLUTIVA EVIDENCIANDOSE EDEMA CEREBRAL DIFUSO EN MENOR CUANTIA COMPARADO CON ESTUDIO ANTERIOR ASI COMO REABSORCION PARCIAL DE LESIONES HEMATICAS A NIVEL DE TEMPORAL IZQUIERDO Y MESENCEFALO ,DEBIDO A SU ESTADO NEUROLOGICO DE 4/15 PUNTOS DE ECG A PESAR DE MEJORA DESDE EL PUNTO DE VISTA TOMOGRAFICO SE PLANTEA DIAGNOSTICO DE : LESION AXONAL DIFUSA , POR NO REQUERIR VENTILACION MECANICA Y ESTABILIDAD HEMODINAMICA SE DECIDE EGRESO A SALA OBSERVACION.''',
			
			"piel" : 	'''	morena, normotermica al tacto, deshidratado. ''',
			

			"cardiopulmonar":  ''' Tórax simétrico, expansible, ruidos respiratorios presentes MV conservado , sin agregados, ruidos cardíacos  rítmicos, regulares, sin soplos ni galope. 	''',
			"abdomen": ''' Blando, depresible, ruidos hidroaéreos presentes, no megálico.''',

			"neurologico": ''' 	inconsciente, Glasgow 4/15 puntos ( RM 2 RO 1 RV 1).''',
		

		}, 

		"diagnosticoIngresoUCI": [

								"TRAUMATISMO CRANEO ENCEFALICO SEVERO COMPLICADO CON :",
								"HEMATOMA INTRAPARENQUIMATOSO",
								"HEMORRAGIA SUBARACNOIDEA CON DRENAJE A VENTRICULO",
								"EDEMA CEREBRAL",
								"IRB: NEUMONIA NOSOCOMIAL.",
								 "HIPOCALEMIA.",

									
								],

		"diagnosticoEgresoUCI": [
									"TRAUMATISMO CRANEO ENCEFALICO SEVERO COMPLICADO CON :",
									"HEMATOMA INTRAPARENQUIMATOSO",
									"HEMORRAGIA SUBARACNOIDEA CON DRENAJE A VENTRICULO",
									"EDEMA CEREBRAL",
									"LESION AXONAL DIFUSA ",
									"IRB: NEUMONIA NOSOCOMIAL.",

								],  

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' TA: 124 /67 mmHg FC: 89 lpm FR: 16 rpm SPO2: 100%. Paciente en malas condiciones generales, afebril, eupneico, hidratado. Se evidencia herida de aproximadamente 7 cm en región parietal derecha sin evidencia de línea de fractura. Neurológico: Estuporoso, pupilas anisocóricas derecha 3mm, izquierda 7 mm arreactivas a la luz Glasgow 9/15 puntos ( RM 5 RV 2 RO 2). Fuerza muscular III/V en miembros superiores, II/V en miembros inferiores, no clonus, no babinsky. No clínica de meningismo ni HTE.''',
		},  

		"diagnosticoIngresoHUAPA": [
						"TRAUMATISMO CRANEO ENCEFALICO MODERADO COMPUESTO CERRADO",
						"ETILISMO AGUDO",
						{"resumen":''' Paciente que fue evaluado por residente de guardia de UCI quien por deterioro neurológico decide realizar intubación endotraqueal con tubo endotraqueal Nº 7 y se conecta a T de Ayres; por no constar con cupo en UCI; se hacen sugerencias. El paciente permanece en área de choque, donde el día 6/4/14 se conecta a ventilación mecánica en vista de deterioro neurológico del pcte. El dia de hoy por disponibilidad de cupo se decide traslado e ingreso a UCI.    Recibimos paciente en  camilla de traslado recibiendo oxigeno mediante ambu  conectado  a reservorio, no conectado a monitor cardiaco. Se traslada a cama UCI y se conecta a monitor cardiaco que reporta: FR: 20 rpm FC:124 lpm TA:106/69(78) mmHg SATO2: 100%'''}
		

		], 
		
	},# 190

		{
		"IdHistoria": "53-96-76", 
		
		"nombre": "Fernando bautista Ayala Malavé  ", 		
		
		"edad": "78",
		
		"ci": "4.683.708", 
		
		"dirección": "Cumanacoa calle Carabobo sin número ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1953,5,31),	
			 		
		"fechaIngresoHUAPA":  datetime(2015,11,6),

		"fechaIngresoUCI": datetime(2015,11,10),

		"resumenIngreso": '''	Se trata de paciente masculino de 78 años de edad natural y procedente de la localidad de Cumanacoa, con antecedentes de Hipertensión Arterial no controlado,  quien inicia enfermedad actual el día 06/11/2015 cuando presenta perdida súbito del estado de consciencia y caída de sus propios pies por tal motivo es traslado a nuestro centro asistencial, ingresando inconsciente, es valorado por el servicio de medicina interna constatando cifras tensionales elevadas 220/110 mmHg siendo ingresado con diagnóstico ''',

		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla, intubado recibiendo oxigeno por ambu se traslada a cama de UCI SIGNOS VITALES: FC 98 LPM TA178/78(99) MMHG  FR 34  SAT O2 93% ''',
			
			"piel" : 	'''	blanca  hipertérmica, hidratada, llenado capilar <3segundos ''',

			"cardiopulmonar":  ''' Tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos hemitorax con estertores roncus bilaterales moderados a predominio derecho.  Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos. ''',
			"abdomen": '''  Blando, ruidos hidroaéreos presentes, no doloroso a la palpación superficial y  profunda, no visceromegal ''',

			"neurologico": ''' estuporoso, pupilas isocóricas hiporreactivas a la luz, Glasgow 6/15 pts.  puntos dado por RM 4 RO 1 RV 1 limitado por TET, no signos meníngeos ''',
	
		}, 

		"examenFisicoIngresoPrivado": {

			"resumen": ''' FC 80 LPM TA220 /120() MMHG FR 21 rpm SAT %  Paciente en malas condiciones generales, hipertenso, diaforético, El  paciente permanece en área de choque recibiendo oxigeno húmedo por bigote nasal, en vista de persistir hipertenso se inicia tratamiento a base de Nitropusiato de sodio por cuenta gota, a razón de 10 cc hora, es trasladado a estudio tomografico, quien en vista de reportar hemorragia intraparenquimatoso fronto temporal izquierdo y hemorragia sub aracnoidea Fisher 4, deciden solicitar valoración por el servicio de neurocirugía quien en vista de hallazgos tomografico decide conducta quirúrgica, solicitan valoración por el servicio de terapia intensiva se acude al llamado evaluando paciente en condiciones clínicas de cuidado en vista de deterioro de estado neurológico, trabajo respiratorio y desaturación por monitor se decide realizar maniobras de intubación endotraqueal con tubo 7.5 FR evidenciando salida de secreción de contenido alimentario por tubo fétida, se conecta a ventilación mecánica en modo A/C FR 12 VC 560 FL 50 FIO2 60 PEEO 0  y en vista de no contar con cupo en la unidad de cuidados intensivos se realizan sugerencias . El día 07/11/2015 es llevado a mesa operatoria donde bajo anestesia general, craneotomía parieto temporal izquierdo con 5 agujero, observándose duramadre violácea tensa y sin latidos, se realiza durotomia, realizando posteriormente drenaje de hematoma subdural mas hematoma intraparenquimatoso por aspirado con gran volumen de coagulo, se realiza hemostasias, y se procede a cierre por planos. Posteriormente  es trasladado a área de recuperación de quirófano donde permanece durante 4 días y en vista del día 10/11/2015 contar con cupo se decide ingresar en UCI adulto. ''',
			
			"piel" : 	'''	blanco,  Normotérmica, llenado capilar <3segundos. ''',

			"cardiopulmonar":  ''' Tórax simétrico, hipoexpansible, ruidos respiratorios presentes en ambos hemitorax sin agregados.  Ruidos cardíacos rítmicos, regulares,  no se auscultan soplos. ''',
			"abdomen": ''' Blando, no  doloroso a la palpación superficial y  profunda, no visceromegalia''',

			"neurologico": ''' estuporoso desviación de comisura labial, pupilas anisocóricas, poco reactivas a la luz,  Glasgow 6/15 puntos dado por RM 4 RO 1 RV 1.''',
		

		}, 

		"diagnosticoIngresoUCI": [
										"post operatorio mediato de  craniotomia fronto-temporal  izquierda para drenaje de",
										"hematoma intraparenquimatoso fronto- temporal izquierda de gran volumen",
										 "hematoma subdural agudo",
										"EVC fronto-temporal izquierdo de etiología hemorrágica  ", 
										"Infección respiratoria baja neumonía por bronco aspiración ",
										"Hipertensión arterial sistémica no controlada",
										"Diabetes mellitus tipo 2 ",
										"Trastorno hematológico",
										"anemia moderada",


								],

		"diagnosticoIngresoHUAPA": [
								"Crisis hipertensiva expresada en EVC de posible etiología hemorrágica",
								"Infección respiratoria baja neumonía por bronco aspiración.",
								"Hipertensión arterial sistémica no controlada ",
								"Diabetes mellitus tipo 2 descompensada en hiperglicemia ",
	

		], 

	},# 191

	{
		"IdHistoria": "", 
		
		"nombre": "ARELIS JOSEFINA CASTRO FUENTES", 		
		
		"edad": "57",
		
		"ci": "4.688.789  ", 
		
		"dirección": "Urb. Fe y Alegría, Bloque 5-1, Apto 00-04",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1956,7,28),

		"lugarNacimiento": "Cumanacoa, Edo. Sucre.", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,4,9),

		"fechaIngresoUCI": datetime(2014,4,9),

		"resumenIngreso": '''Paciente femenina de 57 años de edad, con antecedentes de hipertensión arterial sistémica de larga data y Diabetes Mellitus tipo 2 no controladas, cuyo familiar refiere inicio de enfermedad actual el día 02/04/14 cuando presenta cuadro caracterizado por cefalea de fuerte intensidad, vómitos en incontables oportunidades y disminución de la fuerza muscular en hemicuerpo derecho, motivo por el cual es evaluada en centro privado, se evidencian cifras de TA elevadas cuantificadas en 190 /100 mmHg, se contacta cardiólogo de guardia quien decide su ingreso en sala de hospitalización con diagnóstico de Crisis hipertensiva  y Diabetes Mellitus tipo 2 descompensada, siendo evaluado además por internista de guardia quienes indican la realización de TAC cráneo que reporta : hallazgos sugestivos de HSA con mayor representación entre lóbulos frontales y cisura interhemisferica frontal donde hay colección hemática y con discreto componente asociado a IV ventrículo y asta occipital izquierda, edema cerebral difuso, se mantiene hospitalizada en habitación recibiendo Nimotop®, antihipertensivos que no precisan,  insulina Lantus® e hidratación parenteral, el día 08/04/14 presenta deterioro neurológico con Glasgow de 8/15 puntos, disartria y hemiplejia derecha, se practica estudio tomográfico que revela hallazgos sugestivos de isquemia secundaria a vasoespasmo de localización frontoparietal izquierda y reabsorción parcial del componente hemorrágico subaracnoideo, motivo por el cual se decide ingreso a terapia intensiva de centro privado donde se realiza intubación endotraqueal y se conecta a ventilación mecánica, ameritó Vasoactivos tipo Norepinefrina por 24 horas, posteriormente es trasladada a la UCI del HUAPA; permanece conectada a ventilación mecánica hasta el día 15/04/14 cuando por mejoría de estado neurológico se realiza extubación y recibe oxígeno húmedo por mascarilla facial tolerándolo satisfactoriamente. Se asocia neumonía nosocomial que progresa a insuficiencia respiratoria y el día 20/04/14 amerita reintubación y se conecta nuevamente a ventilación mecánica hasta la actualidad. Se realiza TAC cerebral simple control el día 22/04/14 que reporta Hipodensidad difusa, con alteración arquitectural a nivel interhemisférico anterior, en relación con hematoma parenquimatoso en resolución, adecuada relación de la sustancia blanca y gris, con surcos prominentes de acuerdo con la edad de la paciente, sistema ventricular simétrico, aumentado discretamente de volumen, sin desplazamiento de línea media. Actualmente recibe tratamiento con Levofloxacina (14 días), Imipenem (7 días), Fluconazol (3 días), Difenilhidantoína (20 días), Nimodipino, Hyzaar® 100mg/12,5mg, Hidroten® 25mg y Clonidina 0,075mg VSNG cada 6 horas.''',

		"examenFisicoIngresoUCI": {

			"resumen": ''' Paciente estable hemodinámicamente, afebril, en condiciones clínicas de cuidado, intubada y conectada a ventilación mecánica modo SIMV + ASB con Vc: 560, FiO2: 50, FR: 8, FL: 50 y PASB: 15, conectada a monitor cardíaco continuo que reporta:TA: 120/87(98) mmHgFC: 82 lpm FR: 14 rpm SatO2: 100%''',
			
			"piel" : 	'''	normotérmica al tacto, ligera palidez cutáneo mucosa, llenado capilar < 3segundos.''',
			
			"cardiopulmonar":  ''' tórax simétrico normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, roncus abundantes bilaterales, ruidos cardíacos rítmicos, regulares, normofonéticos, sin soplo ni galope.''',
			"abdomen": ''' globoso a expensas de panículo adiposo, ruidos hidroaéreos presentes, blando, depresible, no doloroso a la palpación superficial ni profunda, no megálico.''',

			"neurologico": ''' 	somnolienta, pupilas isocóricas, normorreactivas a la luz, hemiplejia derecha, Glasgow 10/15pts (RM: 6pts, RO: 3pts, RV: 1pto limitado por TET)  ''',
			
		}, 

		"diagnosticoIngresoUCI": [
									"HEMORRAGIA SUBARACNOIDEA Fisher III, H-H IV ",
									"ANEURISMA DE ARTERIA COMUNICANTE ANTERIOR",
									"INFECCION RESPIRATORIA BAJA: NEUMONIA NOSOCOMIAL",
									"INFECCION DEL TRACTO URINARIO MICOTICA",
									"HIPERTENSION ARTERIAL SISTEMICA",
									"DIABETES MELLITUS TIPO 2",

								],

		
	},# 192

	{
		"IdHistoria": "33-81-26", 
		
		"nombre": "Sorveidi  Josefina Díaz Andrade ", 		
		
		"edad": "21",
		
		"ci": "24.690.249 ", 
		
		"dirección": "Barrio El pinar  Sector E casa numero 27 ",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1993,5,25),

		"lugarNacimiento": "Cumaná", 		
			 		
		"fechaIngresoHUAPA":  datetime(2015,3,10),

		"fechaIngresoUCI": datetime(2015,3,10),


		"resumenIngreso": '''Se trata de paciente femenina de 21 años de edad natural y procedente de la comunidad  con antecedentes patológicos personales de Diabetes Mellitus TIPO I  desde la infancia para lo cual lleva tratamiento habitual con Insulina Lantus®10 unidades 8:00 pm el cual es suspendido desde hace 1 mes aproximadamente. e Insulina cristalina 15 unidades para 24 horas repartidas en 5 Uds. Desayuno ,5 Uds. Almuerzo  y 5 Uds. en la Cena ,además antecedentes de nefropatía diabética en seguimiento por consulta externa e hipertensión arterial sistémica en tratamiento con Amlodipino 1o mg diarios, quien inicia enfermedad actual el día 06/03/15  en horas de la mañana cuando presenta dolor abdominal localizado en región epigástrica, persistiendo sintomática hasta el día 07/03/15  anexándose  al cuadro clínico vómitos en numero de 12  por lo que acude a nuestro centro asistencial medicando con Irtopam® hidratación parenteral y egresan, para el día de hoy 10/03/15 en horas de la madrugada (3:00 am) se reanuda cuadro clínico de vómitos en innumerables oportunidades por lo que acuden a emergencia donde es evaluado por el servicio de medicina interna e ingresan con los diagnósticos de: ''',

		"examenFisicoIngresoUCI": {

			"resumen": ''' Se recibe paciente en camilla de traslado, procedente del servicio de emergencia. Se traslada a cama UCI y se conecta a monitor cardiaco continuo que reporta Fr: 16rpm   Fc: 99 lpm    TA: 116/70 mmHg   SATO2: 98%. GASES ARTERIALES PH 7.17 PO2 185 mmHg PCO2 18 mmHg  HCO3 13.1mmol/L EB -9.8mmol/L  SATO2100 % ''',
			
			"piel" : 	'''	palidez cutáneo mucosa marcada, afebril al tacto, deshidratada, sequedad de mucosa oral, se evidencia edema facial,  llenado capilar <3seg. ''',
			

			"cardiopulmonar":  ''' Tórax simétrico normoexpansible Ruidos respiratorios presentes en ambos hemitorax, no se auscultan agregados. Ruidos cardiacos rítmicos, se ausculta soplo sistólico grado II-III/VI''',
			"abdomen": ''' blando depresible, ruidos hidroaéreos presentes, doloroso a la palpación superficial y profunda en toda su extensión. ''',

			"neurologico": ''' consciente orientada en tiempo, espacio y persona, lenguaje coherente, Glasgow 15/15ptos. Fuerza muscular 5/5pts.  Sensibilidad conservada. ROT: II/IV. ''',
			"extremidades": '''se evidencia edema en ambos miembros inferiores grado I.''',
			

		}, 
		"diagnosticoIngresoUCI": [
									
								"Diabetes Mellitus tipo I descompensada en Cetoacidosis  diabética. ",
								"Nefropatía diabética. ",
								"Hipertensión arterial sistémica.",
								"Vulvovaginitis Micótica ",
								"Trastorno Hematológico: Anemia moderada.",
								"Trastorno Hidroelectrolítico: Deshidratación Isotónica Severa ",
								"Trastorno Acido Base : Acidosis metabólica descompensada + alcalosis respiratoria ",
								"Trastorno Acido – Base: acidosis metabólica descompensada con alcalosis respiratoria mas hiperoxemia", 



								],

		"examenFisicoIngresoHUAPA": {
			"resumen": ''' Fr: 23 rpm  Fc: 99 lpm TA: 130/70 mmHg . Paciente es evaluada por el servicio de terapia intensiva en horas de la mañana  y en vista de no contar con  disponibilidad de cupo en  la unidad se realizan sugerencias.  Es reevaluada en horas de la tarde por Servicio de UCI  decidiendo su ingreso por disponibilidad de cupo ''',
			"piel": ''' blanca deshidratada, turgor y elasticidad ligeramente disminuidos llenado capolar <3seg  Edema bipalpebral.''',

			"cardiopulmonar": '''Tórax simétrico normoexpansible Ruidos respiratorios presentes en ambos hemitorax, no se auscultan agregados. Ruidos cardiacos rítmicos regulares no ausculto soplo.''',
			"abdomen": '''globoso, ruidos hidroaéreos presentes, blando, depresible no doloroso a la palpación.''',
			"extremidades": '''se evidencia edema grado II en miembro inferior derecho, duro que deja fóvea y edema grado I en miembro inferior izquierdo.''',
			"neurologico": '''Paciente consciente, orientada con lenguaje coherente. ''',

		},  

		"diagnosticoIngresoHUAPA": [
							"DIABETES MELLITUS TIPO 1 DESCOMPENSADA EN CETOACIDOSIS ",
							"HIPERTENSIÒN ARTERIAL SISTEMICA",
							"ANEMIA LEVE 9.8 gr/dl",
								

		], 
		
	},# 193

	{
		"IdHistoria": "01–02–66", 
		
		"nombre": "Matilde del Valle Rivero de Márquez", 		
		
		"edad": "60",
		
		"ci": "5.078.605", 
		
		"dirección": ": Av. Perimetral, detrás del Teide",
		
		"sexo": "",	
		
		"fechaNacimiento":  datetime(1953,4,6),

		"lugarNacimiento": "Cumaná, Edo. Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,1,22),

		"fechaIngresoUCI": datetime(2014,1,22),

		"resumenIngreso": ''' Paciente femenina de 60 años de edad, natural y procedente de la localidad, con antecedente de artritis reumatoide diagnosticada hace 2 años aproximadamente, en tratamiento regular que no precisa, cuyo familiar refiere inicio de enfermedad actual hace aproximadamente tres meses cuando comienza a presentar aumento de la temperatura corporal, continua, cuantificada en 39ºC, atenuada con acetaminofen, motivo por el cual el día 05/11/13 es traída e ingresada al HUAPA por el servicio de medicina interna, seguidamente se anexa al cuadro clínico dolor abdominal difuso, tipo cólico, exacerbado con la palpación, de 15 días de duración aproximadamente, se le realiza ECO y TAC abdominal sin evidencia de lesión alguna. Permanece en piso de hospitalización sin diagnóstico preciso hasta el día 30/12/13, cuando es egresada. El día 08/01/14, comienza a presentar períodos de desorientación transitoria y persiste estado febril, por lo que el día 16/01/14 reingresa en esta institución presentando piel hipertérmica al tacto, con tórax simétrico, normoexpansible, ruidos respiratorios presentes en ambos campos pulmonares, sin  agregados, ruidos cardíacos rítmicos y regulares sin soplo ni galope, abdomen plano, blando, no doloroso a la palpación, no megálico, ruidos hidroaéreos presentes, extremidades dolorosas a la movilización, con puntos álgidos, se ingresa con el diagnóstico de Síndrome febril de origen desconocido, Neo Oculto y Síndrome de desgaste orgánico. El día 17/01/14 la paciente presenta franco deterioro del estado neurológico, ptosis palpebral y hemiparesia derecha, permanece en hospitalización de medicina interna hasta el día de hoy 22/01/14 cuando por evolución tórpida solicitan valoración por UCI. Se evalúa en conjunto con Dra. Teresa Cortesía  y por malas condiciones de la paciente se decide su ingreso a la UCI. Actualmente la paciente se encuentra en condiciones clínicas de cuidado, intubada y conectada a ventilación mecánica con parámetros preestablecidos, neurológicamente inconsciente, pupilas isocóricas, midriáticas, arreactivas a la luz, reflejo corneal y tusigeno presentes, hemiparesia derecha, arreflexica, Glasgow 6/15pts (RM: 4pts, RO: 1pto, RV: 1 pto limitado por TET). Se le realiza TAC cerebral que reporta HIDROCEFALIA CUADRIVENTRICULAR CON EDEMA PERIEPENDIMARIO, es evaluada por el servicio de neurocirugía quien indica que amerita resolución quirúrgica de emergencia y colocación de VALVULA DE DERIVACION VENTRICULO-PERITONEAL PROGRAMABLE TIPO HAKIM MARCA CODMAN. ''',

		"diagnosticoIngresoUCI": [
									"HIDROCEFALIA CUADRIVENTRICULAR CON EDEMA PERIEPENDIMARIO.",
									"HIPERTENSION ENDOCRANEAL.",

								],
	}, # 194

	{
		"IdHistoria": "52-14-83", 
		
		"nombre": "Cesar Castañeda", 		
		
		"edad": "14",
		
		"ci": "28.188.194 ", 
		
		"dirección": "Sabilar villa el progreso ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(2001,2,2),

		"lugarNacimiento": "Cumaná-Estado Sucre", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,11,6),

		"fechaIngresoUCI": datetime(2015,3,19),


		"resumenIngreso": '''Se trata de paciente masculino de 14 años de edad natural y procedente de la localidad, sin antecedentes patológicos conocidos, refiere inicio de enfermedad actual en julio del 2014 caracterizado por tos seca, fiebre cuantificada en 39 ºC y disnea que progresa de de grandes esfuerzos a moderados esfuerzo, motivo por el cual acude a médico especialista Neumonólogo quien indica TAC de tórax y en vista de hallazgos de aumento de la densidad de ambos pulmones por lesión en forma de vidrio deslumbrado ocupante de la mayor parte del pulmón derecho, e enfermedad intersticial crónica . Refiere a este centro donde es  evaluado por el servicio de cirugía blanda  y se ingresa: Enfermedad pulmonar intersticial en estudio. Permanece en área de de hospitalización durante aproximadamente 4 meses a cargo del servicio de cirugía y el día de hoy 19/03/2015 es llevado a mesa operatoria donde bajo anestesia  general realizan toracotomía antero lateral derecha y mediante videofibrobroncoscopio se evidencia pulmón de aspecto fibrotico. Se toma como conducta lavado y aspirado bronquial y toma de biopsia de bronquio principal derecho. Se coloca también tubo de drenaje torácico número 32 FR.  Solicitan  valoración por el servicio de UCI. En vista de contar con cupo se decide su ingreso. Actualmente se encuentra ingresado en el servicio de terapia intensiva en condiciones clínicas de cuidados.''',


		"diagnosticoIngresoUCI": [
								"Post operatorio inmediato de toracotomía antero lateral derecha para toma de biopsia.", 
								"Enfermedad pulmonar intersticial en estudio.",
								"Edema agudo del pulmón ",
								"Trastorno acido base: acidosis respiratoria descompensada más hiperoxemia.",

	
								],
		
	},#195

	{

		"nombre": "WILLIANA PORRELLO", 		
		
		"edad": "47",
		
		"ci": "8.339.584", 
		
		"dirección": "CDI FE Y ALEGRA ",
		
		"sexo": "M",	
		
		"fechaNacimiento":  datetime(1967,1,2),

		"lugarNacimiento": "CUMANA", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,6,6),

		"fechaIngresoUCI": datetime(2014,6,6),

		"resumenIngreso": '''Paciente femenina de 47 años de edad, natural  y procedente de la localidad, con antecedentes patológicos de Asma Bronquial desde la infancia, Hipertensión Arterial diagnosticada hace 15 años aproximadamente, en tratamiento con Ziac® 2.5mg OD y Norvasc®  5 mg OD, cuyo familiar refiere inicio de enfermedad actual el día 12/05/14 cuando presenta fiebre y cefalea que atenúa con Acetaminofen, es tratada de forma ambulatoria con Ampicilina-Sulbactam 750 mg cada 12 horas, sin obtener mejoría  clínica, por lo que acude a centro privado donde es evaluada presentando al examen físico adenomegalias gigantes en región axilar, submaxilar  e inguinal; disneica y se auscultan roncus en ACP, Glasgow 15/15 puntos. Paraclínicos leuc: 38.000 seg: 98%; Rx tórax pequeño infiltrado parahiliar derecho motivo por el cual se ingresa con diagnóstico de Sepsis punto de partida respiratorio, Síndrome adenomegálico, Adenitis submaxilar. Recibe tratamiento con Avelox® y Zienam®. La paciente es evaluada por hematología quien al frotis evidencia granulaciones tóxicas, la paciente continua febril y se asocia Vancomicina mejorando el cuadro febril. Se realiza TAC de cráneo sin contraste que reporta normal, la paciente presenta mejoría clínica con descenso de cuenta blanca. El viernes 23/05/14 presenta mareos, nauseas y vómitos en proyectil, convulsión con deterioro neurológico, constatando cifras de tensión de 170/100mmHg, Glasgow 10/15 ptos (RM: 5pts RV: 2pts RO: 3pts); es trasladada a UCI donde por progresión del deterioro neurológico a 7/15 ptos (RM: 5pts RV: 1pto RO: 1pto) y trabajo respiratorio se intuba y se conecta a ventilación mecánica. Posteriormente la paciente presenta sangramiento nasal y lesiones petequiales en cara; el sábado 24/06/14 se realiza TAC de cráneo que informa hemorragia cerebral derecha a nivel de ganglios basales, es llevada a mesa operatoria por neurocirugía con Glasgow 4/15 ptos, realizando hemicraniectomía derecha y drenaje de hematoma. La paciente llega a UCI sedada y relajada con pupilas midriáticas (10 mm) bilateral, se mantiene así durante 4 días con posterior mejoría de los cambios pupilares, reflejo corneal y tusigeno presentes; se realiza TAC control que reporta hidrocefalia  iniciando Acetazolamida, se realiza Eco Doppler Transcraneal que reporta vasoespasmo izquierdo  iniciando Nimodipino, se realiza TAC control que reporta mejoría de hidrocefalia y hernia subfalcina. La paciente recibió tratamiento con Manitol 18% y Solución Hipertónica mejorando el Glasgow a 6/15 ptos por lo que se reinicia tratamiento con Manitol. El día 05/06/2014 se realiza Traqueostomía sin complicaciones. El día 06/06/14 es trasladada a la UCI del HUAPA. La Paciente  se mantiene durante 46 días en el área de terapia intensiva del HUAPA, con apoyo de ventilación mecánica modo ASB/ PS 15/ FIO2 50'%' alternándose con T de Ayres y Oxígeno Húmedo  a 10 lts por min a través de traqueostomo.  Recibió tratamiento con cefoperazona- sulbactan en el contexto de IRB asociada a ventilación mecánica y Voriconazol (Vorcum®) debido a ITU Micótica. Actualmente con mejoría clínica y paraclínica, con cultivos negativos del 14 de julio 2014. Hemodinámicamente estable, afebril,  con nutrición enteral vía sonda nasogástrica. Por tratarse de paciente de larga estancia en unidad de cuidados intermedios  y se requiere servicio de fisiatría y rehabilitación  se solicita su colaboración para traslado a centro  de salud de Barrio Adentro; lugar donde será además atendido por Neurocirugía Dr.  Yesid  Acevedo.''',

		"diagnosticoIngresoUCI": [

		"POT de hemicraniectomía por drenaje de hematoma parietal derecho",
		"ACV hemorrágico en ganglios basales",
		"POM de Traqueostomía",
		"Diabetes Insípida Central (resuelta)",
		"Hipertensión Arterial Sistémica",
		"Sepsis punto de partida respiratorio (resuelto).",

									
								],

	}, #196

	{
		"IdHistoria": "49–42–35 ", 
		
		"nombre": "Nely Teresa Palomo", 		
		
		"edad": "73",
		
		"ci": "8.428.783 ", 
		
		"dirección": "Urb. Brasil, sector 3, vereda 4, casa #2, Cumaná, Edo. Sucre.",
		
		"sexo": "F",	
		
		"fechaNacimiento":  datetime(1941,10,16),

		"lugarNacimiento": "cumanacoa", 		
			 		
		"fechaIngresoHUAPA":  datetime(2014,8,17),

		"fechaIngresoUCI": datetime(2014,8,25),

		"antecedentes": '''SI''', 

		"resumenIngreso": ''' Paciente femenina de 73 años de edad, natural de Cumanacoa y procedente de la localidad, con antecedentes patológicos de HTA sistémica controlada con Atacand® 16mg, Zanidip® 10mg y Coraspirina® 81mg, con ERC estadío V en diálisis peritoneal, cuyo familiar refiere inicio de enfermedad actual el día 17/08/14 en horas de la mañana, cuando presenta de manera súbita pérdida del estado de consciencia sin recuperación espontánea de la misma, motivo por el cual es llevado a CDI y refieren a éste centro asistencial donde se valora y es ingresado por el servicio de Medicina Interna. Al momento del ingreso al HUAPA presenta tórax simétrico, hipoexpansible, con crepitantes en base pulmonar derecha, deterioro neurológico caracterizado por somnolencia, desorientación, pupilas isocóricas, normorreactivas a la luz y Glasgow de 10/15pts (no discriminado), realizan paraclínicos y evidencian hipoglicemia severa. La paciente se mantienen en el servicio de choque y realiza hipoglicemias severas recurrentes, por lo que se indica infusión continua de solución dextrosa al 10% para 24 horas. El día 19/08/14 presenta mayor deterioro neurológico a pesar de cifras de glicemia de 188mg/dl y trabajo respiratorio, motivo por el cual realizan intubación endotraqueal y se conecta a ventilación mecánica. Se mantiene en el área de choque y en vista de estado general de la paciente, solicitan valoración por UCI quien acude en varias oportunidades a evaluar la paciente y el día de hoy 25/08/14, en vista de estado general del paciente y disponibilidad de cupo, previa autorización de Dra. Cortesía  decide su ingreso.''',


		"diagnosticoIngresoUCI": [
									"EVC DE ETIOLOGIA A PRECISAR",
									"ENFERMEDAD RENAL CRONICA ESTADIO V EN DIALISIS PERITONEAL",
									"HTA SISTEMICA",
									"TRASTORNO METABOLICO:",
									"HIPOGLICEMIA",
									"TRASTORNO HEMATOLOGICO:",
									"ANEMIA MODERADA",
									"PROLONGACION DE PTT",
									"TRASTORNO HIDOELECTROLITICO:",
									"HIPONATREMIA",
									"HIPOKALEMIA",
									"TRASTORNO ACIDO-BASE",
									"ACIDOSIS METABOLICA COMPENSADA CON ALCALOSIS RESPIRATORIA MAS HIPEROXEMIA",
									{"resumen":''' La paciente durante su estancia en el servicio además de recibir tratamiento médico, requirió de la realización de varios exámenes de laboratorio entre ellos química sanguínea, electrolitos séricos, hematología completa, marcadores serológicos para hepatitis A, B y C; así como de tomografía axial computadorizada de cráneo. Informe que se expide a solicitud de la parte interesada el día 04/09/14 en  UCI SAHUPA, Cumaná. Edo. Sucre      '''}

								],
		
	},# 197















] # FIN DE LA LISTA DE REGISTROS





















