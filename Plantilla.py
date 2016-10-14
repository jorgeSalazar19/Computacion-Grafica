import pygame
import Libreria

centro = (250,250)
ANCHO = 600 
ALTO = 500
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]
MORADO=[102,15,130]


if __name__ == "__main__":
	pygame.init()
	pantalla=pygame.display.set_mode((ANCHO,ALTO))
	pantalla.fill(BLANCO)
	Libreria.Dibujarejes(centro,pantalla,ALTO,ANCHO,NEGRO)
	pygame.display.flip()
	reloj = pygame.time.Clock()


	while 1:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		
				
