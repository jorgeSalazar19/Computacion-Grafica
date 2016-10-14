import math

vectorR = ()

def Vector2p (punto1, punto2):
	vector = [punto2[0]-punto1[0],punto2[1]-punto1[1]]
	return vector

print "punto 1 primer vetor","\n"
Numero= raw_input("Digite el primer punto: ").split(" ")
vector1 = (int (Numero[0]),int(Numero[1]))

print "punto 2 primer vector","\n"
Numero2= raw_input("Digite el primer punto 2: ").split(" ")
vector2 = (int (Numero2[0]),int(Numero2[1]))

vectorR = Vector2p(vector1,vector2)

print "Ecuacion Vectorial es = ", "(x,y) = " , vector1 , " + k *", vectorR

print "Ecuacion Parametrica es ="
print "x = " , vector1[0] , "+ k *" , vectorR[0]
print "y = " , vector1[1] , "+ k *" , vectorR[1]