import pygame

VectorR = {}
VectorM =()
ANCHO = 500
ALTO = 500
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]
MORADO = [230,240,210]


#Funcion Para dibujar los ejes cartesianos, en la pantalla
def Dibujarejes(c,p,al,an):
    pygame.draw.line(p,NEGRO,(0,c[1]),(an,c[1]),2)
    pygame.draw.line(p,NEGRO,(c[0],0),(c[0],al),2)

#Dibuja un punto y recibe , un centro de pantalla, una pantalla , y dos puntos
def DibujarPunto(c,p,color,punto1,punto2):
    punto1x = c[0] + punto1[0] 
    punto1y = c[0] - punto1[1] 

    FPunto = [punto1x,punto1y]

    punto2x = punto2[0] + c[0]
    punto2y = c[0] - punto2[1]  

    SPunto = [punto2x,punto2y]

    p.set_at(FPunto,color)
    p.set_at(SPunto,color)

#Funcion para dibujar un vector desde el origen a un punto determinado en el eje cartesiano
def DibujarVectorDesdeOrigen(pantalla,color,c,p):
    px=c[0]+p[0]
    py=c[1]-p[1]
    np=[px,py]
    pygame.draw.line(pantalla,color,c,np,2)

#Funcion Para dibujar un vector resultado de la suma de dos vectores , desde el origen 
def DibujarSumaVectores (pantalla,color,c,v1,v2):
    VectorR[0] = v1[0] + v2[0]
    VectorR[1] = v1[1] + v2[1]
    VectorM = (VectorR[0],VectorR[1])
    px = c[0] + VectorR[0]
    py = c[1] - VectorR[1]
    Nv =(px,py)
    pygame.draw.line(pantalla,color,c,Nv,2)
    return VectorM
