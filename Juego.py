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
		self.ancho = 20
		self.alto = 20
		self.image=pygame.Surface([self.ancho,self.alto])
		self.image.fill(ROJO)
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.Aumentar = False
		self.cambiox=0
		self.cambioy=0

	def update(self):
		pass

	def Cambio(self,x,y):
		if self.Aumentar:
			self.ancho+= self.cambiox
			self.alto+= self.cambioy
			self.image= pygame.Surface([self.ancho,self.alto])
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y
			self.image.fill(ROJO)
			self.Aumentar = False

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
		pass


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

			if event.type == pygame.MOUSEMOTION:
				pos = pygame.mouse.get_pos()
				jp.rect.x = pos[0]
				jp.rect.y = pos[1]


		l_choque = pygame.sprite.spritecollide(jp,enemigos,True)
		for ecol in l_choque:
			jp.cambioy = 1
			jp.cambiox = 1
			jp.Aumentar = True
			jp.Cambio(pos[0],pos[1])
			#puntos+=1
			#print puntos

		pantalla.fill(BLANCO)
		todos.draw(pantalla)
		jp.update()
		pygame.display.flip()
		reloj.tick(60)