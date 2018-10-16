# Definición de variables
minimos = [0,0,12] # minimos 
maximos = [41,133,92] # maximos 
medias = [10.60, 4.86, 46.25] # medias
desviaciones = [6.22, 16.00, 21.11] # desviaciones estandar
resultados = []; # Lista de resultados

def procesar():
    """Realizar el cálculo de x' = (x - media) / desviacion  """
    # Generar los conjuntos
    conjuntos = list(zip(minimos,maximos,medias,desviaciones))
    for c in conjuntos: # recorrer los conjuntos creados
        # Realiza los calculos para cada conjunto en su rango completo antes de pasar al siguiente.
        listaTemporal = list() # lista vacia para guardar datos temporalmente
        for r in range(c[0],c[1]): # rango de datos de cada conjunto
            prima = (r - c[2]) / c[3]; # formula aplicada
            listaTemporal.append(prima); # agregar los resultados del calculo a la lista temporal.
        resultados.append(listaTemporal); # agregar las listas a la lista de resultados


def acotarRango(datos=[], minimoNuevo=0, maximoNuevo=1):
    """Acotar el rango de la función"""
    resultado = [] # Memoria temporal
    for x in datos: # Recorrido por el rango de datos
        # Acotación del rango de valores
        proceso = (((x- min(datos)) * (maximoNuevo - minimoNuevo)) / (max(datos) - min(datos))) + minimoNuevo 
        resultado.append(proceso) # Agregar resultados de la transformación a la memoria
    return resultado # Retornar resultados obtenidos


matriz = [
	# DESDE EL MIN HASTA EL MAX
    list(range(0,42)), # SALIDA DEL SISTEMA
    list(range(0,134)), # ESTADIA HOSPITALARIA INGRESO A HUAPA - INGRESO A UCI EN DIAS CANTIDAD TOTAL
    list(range(12,93)), # # EDAD DEL PACIENTE 
]

for indice,lista in enumerate(matriz):
    print("RANGO ANTIGUO::","(",min(lista),"," ,max(lista), ")")
    print("\n")
    print(indice,"TRANSFORMADO AL RANGO::","(",min(acotarRango(lista)),"," ,max(acotarRango(lista)), ")")
    print(acotarRango(lista))
    print("\n")

input()








