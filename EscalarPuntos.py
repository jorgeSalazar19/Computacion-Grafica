import pygame
import Libreria

ANCHO = 600 
ALTO = 500
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]
MORADO=[102,15,130]


listaPuntos = [[50,50],[75,75],[175,75],[125,50]]
Escala1 = [0.5,0.5]
Escala2 = [2,2]
Escala3 = [3,3]





if __name__ == "__main__":
	pygame.init()
	pantalla=pygame.display.set_mode((ANCHO,ALTO))

	centro=(250,250)

	#puntos = Libreria.EscalarPunto(listaPuntos,Escala,centro)
	#puntosT = Libreria.PuntosTrasladaDos(centro,puntos)
	#listaPuntosT = Libreria.PuntosTrasladados(centro,listaPuntos)

	puntoEscala1 = Libreria.EscalarPunto(listaPuntos,Escala1,centro)
	puntosEcsyT1 = Libreria.PuntosTrasladados(centro,puntoEscala1)

	puntoEscala2 = Libreria.EscalarPunto(listaPuntos,Escala2,centro)
	puntosEcsyT2 = Libreria.PuntosTrasladados(centro,puntoEscala2)

	puntoEscala3 = Libreria.EscalarPunto(listaPuntos,Escala3,centro)
	puntosEcsyT3 = Libreria.PuntosTrasladados(centro,puntoEscala3)

	puntoOrigin = Libreria.PuntosTrasladados(centro,listaPuntos)


	pantalla.fill(BLANCO)
	Libreria.Dibujarejes(centro,pantalla,ALTO,ANCHO,NEGRO)
	

	pygame.draw.polygon(pantalla,MORADO,puntoOrigin)
	pygame.draw.polygon(pantalla,ROJO,puntosEcsyT1)
	pygame.draw.polygon(pantalla,AZUL,puntosEcsyT2)
	pygame.draw.polygon(pantalla,NEGRO,puntosEcsyT3)

	pygame.display.flip()

	"""
	Libreria.DibujarPoligono(listaPuntos,pantalla,VERDE)
	Libreria.DibujarPoligono(puntos,pantalla,AZUL)
	Libreria.DibujarPoligono(listaPuntosT,pantalla,NEGRO)
	Libreria.DibujarPoligono(puntosT,pantalla,ROJO)

	print puntosT
"""
	while 1:

		    for event in pygame.event.get():
		        if event.type == pygame.QUIT:
		        	exit()
	        	