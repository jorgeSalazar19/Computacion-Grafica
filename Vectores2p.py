import math

vectorR = ()

#FUncion para obtener un vector apartir de dos puntos
def Vector2p (punto1, punto2):
	vector = [punto2[0]-punto1[0],punto2[1]-punto1[1]]
	return vector

#norma de un vector 
def normaVector (vector):
	norma = math.sqrt(pow(vector[0],2) + pow(vector[1],2))
	return norma

#Distancia entre dos puntos determinados
def distanciaEntre2Puntos (punto1,punto2):
	distancia = math.sqrt(pow(punto2[0]-punto1[0],2) + pow(punto2[1]-punto1[1],2))
	return distancia

#producto punto entre dos vectores
def ProductoPunto(vector1,vector2):
	producto = vector1[0]*vector2[0] + vector1[1]*vector2[1]
	return producto

#Angulo entre dos vectores determinados.
def AnguloVector (vector1,vector2):
	norma2vectores= normaVector(vector1)*normaVector(vector2)
	Producto = math.fabs(ProductoPunto(vector1,vector2))
	angulo = math.degrees(math.acos(Producto/norma2vectores))
	return angulo

