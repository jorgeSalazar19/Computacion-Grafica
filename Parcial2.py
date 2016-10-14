import pygame
import Libreria
import math

centro = (250,250)
ANCHO = 600 
ALTO = 500
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]
MORADO=[102,15,130]

#Funcion para calcular el radio , de las coordenadas polares 
def CalcularRadioPolares(Vector):
	R = math.sqrt(pow(Vector[0],2)+pow(Vector[1],2))
	return R

#funcion para calcular el angulo de las coordenadas polares 
def AnguloPolarVector(Vector):
	y = math.radians(Vector[1])
	x = math.radians(Vector[0])
	return math.degrees(math.atan2(y,x))

#funcion que dado un vector , me calcula una recta que pasa a 45 grados de el , con ayuda de coordenadas polares 
def RectaVector(Vector):
	R = CalcularRadioPolares(Vector) # Se calcula el radio (coordenas polares) del vector
	angulo = AnguloPolarVector(Vector) # se calcula el angulo (coordenadas polares) del vector

	anguloRecta = angulo + 45 # se calcula el angulo que tendra la recta (sera 45 grados mayor al angulo del vector previamente calculado)

	x = R * math.cos(math.radians(anguloRecta)) # se obtiene la corrdenada x cartesiana de la recta (sera el mismo radio o puede ser cualquiera, lo que importa es el angulo)
	y = R * math.sin(math.radians(anguloRecta)) # se ontiene la coordenada y al igual que la coordenada x

	punto = (x,y) # creo el punto con las coordendas , este sera un punto de la recta 
	return punto # retorno el punto 



Vector = [50,50] # creo un vector cualquiera 
#print AnguloPolarVector(Vector)
#print CalcularRadioPolares(Vector)
puntoRecta = RectaVector(Vector) # le saco el punto a la recta que pasa a 45 grados del vector 
punto2Recta =  [-1*puntoRecta[0],-1*puntoRecta[1]] # segundo punto de la recta , se multiplica por escalar -1 

#se trasladasn los puntos con respecto al centro (eje en la pantalla)
puntoRectaT = Libreria.PuntoTrasladado(puntoRecta,centro) 
punto2RectaT = Libreria.PuntoTrasladado(punto2Recta,centro)


if __name__ == "__main__":
	pygame.init()
	pantalla=pygame.display.set_mode((ANCHO,ALTO))
	pantalla.fill(BLANCO)
	Libreria.Dibujarejes(centro,pantalla,ALTO,ANCHO,NEGRO)
	pygame.draw.line(pantalla,MORADO,punto2RectaT,puntoRectaT,2) # dibujo la recta que pasa a 45 grados del vector
	Libreria.DibujarVectorDesdeOrigen(pantalla,ROJO,centro,Vector) # dibujo el vector creado anteriormente , desde el origen
	#Libreria.DibujarVectorDesdeOrigen(pantalla,VERDE,centro,puntoRecta) # deibujo la recta que pasa a 45 grados del vector , desde el origen hasta el punto calculado 
	print "El Angulo entre la reta y el vector es = ",Libreria.AnguloVector(Vector,puntoRecta) # para verificar saco el angulo entre la recta y el vector , debe ser 45
	pygame.display.flip()
	reloj = pygame.time.Clock()


	while 1:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()