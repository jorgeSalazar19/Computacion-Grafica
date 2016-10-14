import pygame

ANCHO = 640
ALTO = 480
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]


if __name__ == "__main__":
	

	pygame.init()
	pantalla=pygame.display.set_mode((ANCHO,ALTO))
	fondo = pygame.image.load("Fondo.jpg")
	Sp = pygame.image.load("Warturtle.png")
	Sp_X = 100
	Sp_Y = 100
	pantalla.blit(fondo,(0,0))
	pantalla.blit(Sp,[Sp_X,Sp_Y])


	pygame.display.flip()



	while 1:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RIGHT: 
					print "Tecla"
					Sp_X+=5
					pantalla.blit(fondo,(0,0))
					pantalla.blit(Sp,[Sp_X,Sp_Y])

				if event.key==pygame.K_LEFT: 
					print "Tecla"
					Sp_X-=5
					pantalla.blit(fondo,(0,0))
					pantalla.blit(Sp,[Sp_X,Sp_Y])

				if event.key==pygame.K_DOWN: 
					print "Tecla"
					Sp_Y+=5
					pantalla.blit(fondo,(0,0))
					pantalla.blit(Sp,[Sp_X,Sp_Y])

				if event.key==pygame.K_UP: 
					print "Tecla"
					Sp_Y-=5
					pantalla.blit(fondo,(0,0))
					pantalla.blit(Sp,[Sp_X,Sp_Y])

		pygame.display.flip()