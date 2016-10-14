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
	Sp1 = pygame.image.load("Squirtle.png")
	Sp2 = pygame.image.load("Warturtle.png")
	Sp1_X = 100
	Sp1_Y = 100
	Sp2_X = 10
	Sp2_Y = 10
	pantalla.blit(fondo,(0,0))
	pantalla.blit(Sp1,[Sp1_X,Sp1_Y])
	pantalla.blit(Sp2,[Sp2_X,Sp2_Y])
	reloj = pygame.time.Clock()

	pygame.display.flip()

	Aux = False

	while 1:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit() 
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RIGHT: 
					print "Tecla"
					Sp2_X+=10
					pantalla.blit(fondo,(0,0))
					pantalla.blit(Sp2,[Sp2_X,Sp2_Y])

				if event.key==pygame.K_LEFT: 
					print "Tecla"
					Sp2_X-=10
					pantalla.blit(fondo,(0,0))
					pantalla.blit(Sp2,[Sp2_X,Sp2_Y])

				if event.key==pygame.K_DOWN: 
					print "Tecla"
					Sp2_Y+=10
					pantalla.blit(fondo,(0,0))
					pantalla.blit(Sp2,[Sp2_X,Sp2_Y])

				if event.key==pygame.K_UP: 
					print "Tecla"
					Sp2_Y-=10
					pantalla.blit(fondo,(0,0))
					pantalla.blit(Sp2,[Sp2_X,Sp2_Y])


		if Sp1_X < ANCHO-44 and Aux != True:
			Sp1_X+=1

		else:
			Aux = True

		if Aux:
			Sp1_X-=1
			
		if Sp1_X == -10:
			Aux = False 

		pantalla.blit(fondo,(0,0))	
		pantalla.blit(Sp2,[Sp2_X,Sp2_Y])
		pantalla.blit(Sp1,[Sp1_X,Sp1_Y])
		pygame.display.flip()
		reloj.tick(60)
