import pygame
import random 
import PLano
import Vectores2p


ANCHO = 500
ALTO = 500
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]


def DibujarCirculo(pantalla,punto,color):
	pygame.draw.circle(pantalla,color,punto,50,2)

#FUnciona para dibujar circulos de una lista de ountos determinados
def DibujarCirculos(pantalla,puntos,color):
	for cont in range (len (puntos)):
		punto = puntos[cont]
		pygame.draw.circle(pantalla,color,puntos[cont],50,2)

#Funcion para gwenerar una lista de puntos aleatroios (el numero de puntos biene dado por el parametro de la funcion)
def GenerarPuntos(num):
	Puntos = []
	for cont in range (num):
		valor =  random.randrange(200)
		valor2 = random.randrange(200)
		punto = [valor,valor2]
		#print punto
		Puntos.append(punto)
	return Puntos

#funcion que dibuja en la pantalla la lista de ountos que pasamos como parametro
def DibujarPuntos(c,pantalla,puntos,color):
	for cont in range(len (puntos)):
		punto = puntos[cont]
		pantalla.set_at(punto,color)

#funcion que a partir de una lista de puntos, los traslada a su posicion trasladada con respecto al centro de la pantalla
def PuntosTrasladasos(c,puntos):
	puntosT =[]
	for cont in range(len(puntos)):
		#print len(puntos)
		punto  = puntos[cont]
		puntox = c[0] + punto[0]
		puntoy = c[1] - punto[1]
		puntoTrasladado = [puntox,puntoy]
		puntosT.append(puntoTrasladado)
	return puntosT

def PuntoTrasladado (punto,c):
	puntox = c[0] + punto[0]
	puntoy = c[1] - punto[1]
	punto = [puntox,puntoy]
	return punto
		
#Funcion que me dibuja dos puntos dados , me crea un vector con dichos puntos y lo grafica en el plano (pantalla) , con respecto a un centro dado
def DibujarPuntosYVector(punto1 ,punto2,pantalla,c):
	PLano.DibujarPunto(c,pantalla,BLANCO,punto1,punto2)
	vector = Vectores2p.Vector2p(punto1,punto2)
	PLano.Cartesiano(pantalla,BLANCO,c,vector)

#lista1 = GenerarPuntos(3)

#pygame.init()
#pantalla=pygame.display.set_mode((ANCHO,ALTO))
#centro=(250,250)
#pantalla.fill(NEGRO)
#PLano.Dibujarejes(centro,pantalla,ALTO,ANCHO)
#DibujarPuntosYVector([10,50],[80,30],pantalla,centro)
#DibujarPuntos(centro,pantalla,lista1,VERDE)
#DibujarCirculos(pantalla,lista1,BLANCO)
#Npuntos = PuntosTrasladasos(centro,lista1)
#DibujarPuntos(centro,pantalla,Npuntos,ROJO)
#DibujarCirculos(pantalla,Npuntos,ROJO)
#DibujarCirculo(pantalla,(100,100),VERDE)
#pygame.display.flip()


#while 1:

#    for event in pygame.event.get():
#        if event.type==pygame.QUIT:
#            exit()