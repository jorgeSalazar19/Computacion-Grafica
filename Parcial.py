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

#Funcion Para Graficar R = 2 - 2sen(angulo) -> cardioide
def GraficarPolar ():
	ListaPuntos = []
	angulo = 0 #Angulo varia de 0 a 360 grados
	while(angulo <= 360): 
		rAngle = angulo
		#Angle=math.radians(rAngle) #se pasa el angulo a radianes 
		R =  (50*rAngle) #se calcula R
		x = (R)*math.cos(angulo) # se alla componente x en cooredeandas cartesianas , (se multiplica por 60 para que sea mas grande)
		y = (R)*math.sin(angulo) # se alla componente y en cooredeandas cartesianas , (se multiplica por 60 para que sea mas grande)
		punto = (int (x), int (y)) #se crean un punto con cada componente
		angulo += 0.01 # se incrementa el angulo
		ListaPuntos.append(punto) # se agrega el punto a una lista de puntos
	return ListaPuntos # se retorna la lista de puntos




if __name__ == "__main__":
	pygame.init()
	pantalla=pygame.display.set_mode((ANCHO,ALTO))
	pantalla.fill(BLANCO)
	Libreria.Dibujarejes(centro,pantalla,ALTO,ANCHO,NEGRO)

	Puntos = GraficarPolar() # llamado a la funcion graficar polar , retorna lista de puntos a graficar

	"""Con este ciclo se grafican cada uno de los puntos de la lista, con un vector desde el origen al centro.
	Nota: (tambien se pueden graficar solo los puntos) """
	for aux in Puntos:
		punto = Libreria.PuntoTrasladado(aux,centro)
		pantalla.set_at(punto,NEGRO)
		#Libreria.DibujarVectorDesdeOrigen(pantalla,ROJO,centro, aux)

	pygame.display.flip()
	reloj = pygame.time.Clock()



while 1:
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		