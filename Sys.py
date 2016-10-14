import os,sys 
import pygame

BLANCO = [250,250,250]
ROJO = [250,0,0]
AZUL = [0,0,250]


class boton (pygame.sprite.Sprite):
	def __init__(self,archivo,xi,yi,nombre):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(archivo).convert_alpha()
		self.rect = self.image.get_rect()
		self.nombre = nombre
		self.rect.x = xi
		self.rect.y = yi


class Cuadro(pygame.sprite.Sprite):
	def __init__(self,archivo,xi,yi):
		pygame.sprite.Sprite.__init__(self)
		self.image  = pygame.image.load(archivo).convert_alpha()
		self.rect = self.image.get_rect()
		self.click = False
		self.rect.x = xi
		self.rect.y = yi		

	def update(self,surface):
		if self.click :
			self.rect.center = pygame.mouse.get_pos()
		surface.blit(self.image,self.rect)



def BarMenu(alto,pantalla,color):
	puntos = [[0,600],[0,600-alto],[1000,600-alto],[1000,600]]
	pygame.draw.polygon(pantalla,color,puntos)

def GenerarBloques(listabloques,listabotones,listatodos):
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			for b in listabotones:
				if b.rect.collidepoint(event.pos) and b.nombre == "caja":
					bloqueT = Cuadro("cajita.png",300,300)
					listabloques.add(bloqueT)
					listatodos.add(bloqueT)
				if b.rect.collidepoint(event.pos) and b.nombre == "roca":
					bloqueT = Cuadro("roca.png",100,300)
					listabloques.add(bloqueT)
					listatodos.add(bloqueT)
				if b.rect.collidepoint(event.pos) and b.nombre == "caja2":
					bloqueT = Cuadro("caja.png",200,300)
					listabloques.add(bloqueT)
					listatodos.add(bloqueT)
			for bloque in listabloques:
				if bloque.rect.collidepoint(event.pos):
					bloque.update(pantalla)
					bloque.click = True
		elif event.type == pygame.MOUSEBUTTONUP:
				for bloque in listabloques:
					bloque.update(pantalla)
					bloque.click = False
		if event.type == pygame.QUIT:
				pygame.quit(); sys.exit()
		pantalla.fill(0)
		BarMenu(100,pantalla,BLANCO)
		listatodos.draw(pantalla)
		pygame.display.update()
		listatodos.update(pantalla)
		#reloj.tick(60)

	

if __name__ == "__main__":
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	pantalla = pygame.display.set_mode((1000,600))
	botonCaja = boton("cajita.png",20,500,"caja")
	botonRoca = boton("roca.png",120,500,"roca")
	botonCaja2 = boton("caja.png",220,500,"caja2")

	todos = pygame.sprite.Group()
	botones= pygame.sprite.Group()
	bloques = pygame.sprite.Group()

	botones.add(botonCaja)
	botones.add(botonRoca)
	botones.add(botonCaja2)

	todos.add(botonCaja)
	todos.add(botonRoca)
	todos.add(botonCaja2)

	reloj = pygame.time.Clock()	


	while 1:
		GenerarBloques(bloques,botones,todos)
			
	

