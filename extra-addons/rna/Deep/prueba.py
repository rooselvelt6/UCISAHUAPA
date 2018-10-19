from mlp import Agente
a = Agente();
m = a._cargarCompilar()
#print(dir(m))
m._make_predict_function()
lista = [0,0,1,0,1,0,1,0,1]
r = a._estimar(atributos=lista, modelo=m)
print(r)
