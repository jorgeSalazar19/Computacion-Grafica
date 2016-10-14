import pygame
import math
import Libreria

ALTO=400
ANCHO=400
BLANCO=(255, 255, 255)
ROJO=(255, 0, 0)
AZUL=(0, 0, 255)
NEGRO=(0, 0, 0)
centro = [200,200]

pygame.init()
screen=pygame.display.set_mode([ANCHO, ALTO])
screen.fill(BLANCO)
Libreria.Dibujarejes(centro,screen,ALTO,ANCHO,NEGRO)
pygame.display.flip()


#Escala un punto
def scale(pts, sx, sy):
    Spts=[]
    for pt in pts:
        x=sx*pt[0]
        y=sy*pt[1]
        Spt=[x,y]
        print Spt
        Spts.append(Spt)
    return Spts

#Rota un punto
def rotate(pt, angle):
    Rpt=[]
    angle=math.radians(angle)
    x=pt[0]*(math.cos(angle))-pt[1]*(math.sin(angle))
    y=pt[0]*(math.sin(angle))+pt[1]*(math.cos(angle))
    Rpt=[x,y]
    return Rpt

#Rota una lista de puntos
def rotateList(pts, angle):
    Rpts=[]
    for pt in pts:
        rpt=rotate(pt,angle)
        Rpts.append(rpt)
    return Rpts

#Dibuja poligono regular de N lados
def drawRegPoly(scr, n,c):
    d=360/n
    pts=[]
    angle=0
    for i in range (0,n):
        rAngle=math.radians(angle)
        x=100*math.cos(rAngle)
        y=100*math.sin(rAngle)
        pt=[x,y]
        pts.append(pt)
        angle=angle+d
    return pts
    #Mpts=Move(pts, c)
    #pygame.draw.polygon(scr, NEGRO, Mpts, 1)
    #pygame.display.flip()

#Escala con respecto a un punto fijo (recibe una lista de puntos y la escala)
def scaleFixedPoint(scr, pts, s,c):
    Mpts=Move(pts,c)
    pygame.draw.polygon(scr, NEGRO, Mpts, 1)
    tx=pts[0][0]
    ty=pts[0][1]
    Spt=[]
    for pt in pts:
        x=((pt[0]-tx)*s)+tx
        y=((pt[1]-ty)*s)+ty
        spt=[x,y]
        Spt.append(spt)
    Mpts=[]
    Mpts=Move(Spt, [200,200])
    pygame.draw.polygon(scr, NEGRO, Mpts, 1)
    pygame.display.flip()

#Rota respecto a un punto fijo
def rotateFixedPoint(scr, pts, angle,c):
    Mpts=Libreria.PuntosTrasladados(c, pts)
    tx=pts[0][0]
    ty=pts[0][1]
    Rpt=[]
    angle=math.radians(angle)
    for pt in pts:
        x=((pt[0]-tx)*(math.cos(angle))-(pt[1]-ty)*(math.sin(angle)))+tx
        y=((pt[0]-ty)*(math.sin(angle))+(pt[1]-ty)*(math.cos(angle)))+ty
        rpt=[int (x),int (y)]
        Rpt.append(rpt)
    return Rpt

PTriangulo = drawRegPoly(screen, 3,centro)
PTrianguloYT = Libreria.PuntosTrasladados(centro,PTriangulo)
pygame.draw.polygon(screen, ROJO, PTrianguloYT, 1)
pygame.display.flip()

puntos = [[20,20],[50,20],[50,40]]
puntosT = Libreria.PuntosTrasladados(centro,puntos)
pygame.draw.polygon(screen, ROJO, puntosT, 1)

fin=False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin=True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            puntosR = rotateFixedPoint(screen, puntos , 90,centro)
            puntosRyT = Libreria.PuntosTrasladados (centro,puntosR)
            pygame.draw.polygon(screen, AZUL, puntosRyT, 1)
            puntos = puntosR
            print puntos
            pygame.display.flip()


