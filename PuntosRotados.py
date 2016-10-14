import pygame
import Libreria
import math

ANCHO = 700
ALTO = 700
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]

  
if __name__ == "__main__":
	

	pygame.init()
	pantalla=pygame.display.set_mode((ANCHO,ALTO))
	centro=(350,350)
	pantalla.fill(BLANCO)
	Libreria.Dibujarejes(centro,pantalla,ALTO,ANCHO,NEGRO)

	"""
	puntos = [[100,50],[150,50],[125,100]]
	PuntoTrasladados = Libreria.PuntosTrasladados(centro,puntos)
	Libreria.DibujarPoligono(PuntoTrasladados,pantalla,VERDE)
	
	puntosRotados = Libreria.RotarPuntos(puntos,centro,90)
	puntosRotadosYTrasladados = Libreria.PuntosTrasladados(centro,puntosRotados)
	Libreria.DibujarPoligono(puntosRotadosYTrasladados,pantalla,ROJO)
	
	"""
	punto = [30,10]
	Libreria.DibujarVectorDesdeOrigen(pantalla,VERDE,centro,punto)
	puntoR = Libreria.RotarPunto(punto,centro,180)
	Libreria.DibujarVectorDesdeOrigen(pantalla,ROJO,centro,puntoR)
	print puntoR
	
	"""
	puntos = [[100,100],[0,200],[100,300],[200,300],[300,200],[200,100]]
	PuntoTrasladados = Libreria.PuntosTrasladados(centro,puntos)
	pygame.draw.polygon(pantalla,ROJO,PuntoTrasladados)
	#puntosRotadosYTrasladados = Libreria.PuntosTrasladados(centro,puntosRotados)
	#pygame.draw.polygon(pantalla,ROJO,puntosRotadosYTrasladados,4)
	reloj = pygame.time.Clock()
	"""
	pygame.display.flip()



	while 1:

		    for event in pygame.event.get():
		        if event.type == pygame.QUIT:
		        	exit()
		        	
		        """if event.type == pygame.MOUSEBUTTONDOWN:
		        	pantalla.fill(BLANCO)
		        	Libreria.Dibujarejes(centro,pantalla,ALTO,ANCHO,NEGRO)
		        	#print puntos
		        	puntosRotados = RotarPuntos(puntos,centro,45)
		        	#print puntos
		        	puntosRotadosYTrasladados = Libreria.PuntosTrasladados(centro,puntosRotados)
		        	pygame.draw.polygon(pantalla,ROJO,puntosRotadosYTrasladados)
		        	puntos = puntosRotados
		        	pygame.display.flip()
				reloj.tick(20)
"""