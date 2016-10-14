import pygame
import Libreria

ANCHO = 500
ALTO = 400
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]


if __name__ == "__main__":

	pygame.init()
	pantalla=pygame.display.set_mode((ANCHO,ALTO))
	centro=(250,250)
	pantalla.fill(BLANCO)
	Libreria.Dibujarejes(centro,pantalla,ALTO,ANCHO,NEGRO)
	cont = 0
	puntos = []
	pygame.display.flip()

	while 1:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				cont = cont + 1
				posicion = pygame.mouse.get_pos()

				if cont <= 3 or cont > 0:	
					puntos.append(posicion)
				"""	
				if cont == 2:
					print puntos
					Libreria.PintarPuntosYVector(centro,puntos,pantalla,NEGRO)
					print puntos
					puntos = []
					cont = 0
				"""
				if cont == 3:
					Libreria.DibujarPoligono(puntos,pantalla,NEGRO)
					Libreria.AngulosInternosTriangulo(puntos)
					puntos = []
					cont = 0


