import pygame


centro = (250,250)
ANCHO = 600 
ALTO = 500
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]
MORADO=[102,15,130]


def figuraPatronHorizontal(l):
	lt=[]
	lAux = []
	for i in l:
		x=i[0]+ 40
		y=i[1]
		punto=[x,y]
		lAux.append(punto)	
		#pygame.draw.polygon(pantalla,azul,lt,1)
	return lAux

def figuraPatronVertical(l):
	lt=[]
	lAux = []
	for i in l:
		x=i[0]
		y=i[1] + 40
		punto=[x,y]
		lAux.append(punto)	
		#pygame.draw.polygon(pantalla,azul,lt,1)
	return lAux

def figuraPatron(l):
	lt=[]
	lAux = []
	for i in l:
		x=i[0] - 40
		y=i[1] 
		punto=[x,y]
		lAux.append(punto)	
		#pygame.draw.polygon(pantalla,azul,lt,1)
	return lAux

def figuraPatron2(l):
	lt=[]
	lAux = []
	for i in l:
		x=i[0]  
		y=i[1] -40 
		punto=[x,y]
		lAux.append(punto)	
		#pygame.draw.polygon(pantalla,azul,lt,1)
	return lAux


def DibujarPatron(patron):
	nA = ANCHO / 50
	nAL = ALTO / 50
	posAncho = 0
	posAlto = 0
	if posAncho < ANCHO:
		for x in range(nA+1):
			PatronAux = figuraPatronHorizontal(patron)
			pygame.draw.polygon(pantalla,ROJO,PatronAux,0)
			patron = PatronAux
			posAncho += 50
		posAncho = 0

	if posAlto < ALTO:
		for x in range(nAL+1):
			PatronAux = figuraPatronVertical(patron)
			pygame.draw.polygon(pantalla,ROJO,PatronAux,0)
			patron = PatronAux
			posAlto += 50
		posAlto = 0

	if posAncho < ANCHO  and posAlto == 0:
		for x in range(nA+1):
			PatronAux = figuraPatron(patron)
			pygame.draw.polygon(pantalla,ROJO,PatronAux,0)
			patron = PatronAux
			posAncho += 50
		posAncho = 0 

	if posAlto < ALTO  and posAncho == 0:
		for x in range(nAL+1):
			PatronAux = figuraPatron2(patron)
			pygame.draw.polygon(pantalla,ROJO,PatronAux,0)
			patron = PatronAux
			posAncho += 50
		
		
	


pygame.init()
pantalla= pygame.display.set_mode([ANCHO,ALTO])
pantalla.fill(BLANCO)
patron=[[10,10],[40,10],[40,30],[60,30],[60,40],[30,40],[30,20],[10,20]]
reloj = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			exit()
	DibujarPatron(patron)
	pygame.display.flip()
	reloj.tick(60)

