import math

vectorR = ()

def Ecuacion_Continua(punto, vector):
	print "Ecuacion continua de la recta: ", "x -",punto[0],"/", vector[0], " = " , "y -",punto[1],"/", vector[1]

def Ecuacion_General(punto,vector):

	A =  vector[1]
	B =  -1*vector[0]
	C =  punto[1]*vector[0]-punto[0]*vector[1]

	print "A = ", A
	print "B = ", B
	print "C = ", C
	print "Ecuacion General de la recta es: " , A,"X +", B,"Y +", C, "= 0"


print "punto 1","\n"
Numero= raw_input("Digite el primer punto: ").split(" ")
punto = (int (Numero[0]),int(Numero[1]))

print "Vectorr","\n"
Numero2= raw_input("Ingrese un vector: ").split(" ")
vector = (int (Numero2[0]),int(Numero2[1]))


Ecuacion_Continua(punto,vector)
Ecuacion_General(punto,vector)