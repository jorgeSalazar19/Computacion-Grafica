import math

def normaVector (vector):
	norma = math.sqrt(pow(vector[0],2) + pow(vector[1],2))
	return norma

def ProductoPunto(vector1,vector2):
	producto = vector1[0]*vector2[0] + vector1[1]*vector2[1]
	return producto

#Angulo entre dos vectores
def AnguloVector (vector1,vector2):
	norma2vectores= normaVector(vector1)*normaVector(vector2)
	Producto = math.fabs(ProductoPunto(vector1,vector2))
	angulo = math.degrees(math.acos(Producto/norma2vectores))
	return angulo

def Crear_Vector (A,B):
	vector1 = (-1*B, A)
	return vector1


print "Recta 1","\n"
A= int (raw_input("Digite La componente A de la recta: "))
B= int (raw_input("Digite La componente B de la recta: "))
C= int (raw_input("Digite La componente C de la recta: "))

vectorR1 = Crear_Vector (A,B)

print "Recta 2","\n"
A1= int (raw_input("Digite La componente A de la recta: "))
B2= int (raw_input("Digite La componente B de la recta: "))
C3= int (raw_input("Digite La componente C de la recta: "))

vectorR2 = Crear_Vector (A1,B2)

print "El Angulo Entre Las Dos Rectas es = ",AnguloVector(vectorR1,vectorR2)

