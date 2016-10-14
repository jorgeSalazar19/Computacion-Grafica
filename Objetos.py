import pygame
import random

ANCHO = 640
ALTO = 480
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]

class Jugador(pygame.sprite.Sprite):
	
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([20,20])
		self.image.fill(ROJO)
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.cambiox=0
		self.cambioy=0

	def update(self):
		self.rect.x+=self.cambiox
		self.rect.y+=self.cambioy

class Enemigo(pygame.sprite.Sprite):
	
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([20,20])
		self.image.fill(AZUL)
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.cambiox=0
		self.cambioy=0

	def update(self):
		self.rect.x+=self.cambiox
		self.rect.y+=self.cambioy


if __name__ == "__main__":
	

	pygame.init()
	pantalla=pygame.display.set_mode((ANCHO,ALTO))
	pantalla.fill(BLANCO)

	jp = Jugador(100,100)
	todos=pygame.sprite.Group()

	enemigos = pygame.sprite.Group()

	for i in range(50):
		x = random.randrange(ANCHO-20)
		y = random.randrange(ALTO-20)
		en = Enemigo (x,y)
		enemigos.add(en)
		todos.add(en)

	todos.add(jp)
	puntos = 0
	pygame.display.flip()

	reloj = pygame.time.Clock()



	while 1:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					jp.cambiox=5
				if event.key == pygame.K_LEFT:
					jp.cambiox=-5
				if event.key == pygame.K_UP:
					jp.cambioy=-5
				if event.key == pygame.K_DOWN:
					jp.cambioy=5
				if event.key == pygame.K_SPACE:
					jp.cambiox=0
					jp.cambioy=0

		if jp.rect.x == ANCHO - jp.rect.width:
			#jp.cambiox=0
			#jp.rect.x=ANCHO-jp.rect.width
			#jp.rect.x=0
			jp.cambiox=-5

		if jp.rect.y == 0:
			#jp.cambiox=0
			#jp.rect.x=ANCHO-jp.rect.width
			#jp.rect.x=0
			jp.cambioy=5

		if jp.rect.x == 0:
			#jp.cambiox=0
			#jp.rect.x=ANCHO-jp.rect.width
			#jp.rect.x=0
			jp.cambiox=5

		if jp.rect.y == ALTO - jp.rect.height:
			#jp.cambiox=0
			#jp.rect.x=ANCHO-jp.rect.width
			#jp.rect.x=0
			jp.cambioy=-5

		l_choque = pygame.sprite.spritecollide(jp,enemigos,False)
		for ecol in l_choque:
			puntos+=1
			print puntos

		pantalla.fill(BLANCO)
		todos.draw(pantalla)
		jp.update()
		pygame.display.flip()
		reloj.tick(60)