import pygame
import math

ALTO=400
ANCHO=400
BLANCO=(255, 255, 255)
ROJO=(255, 0, 0)
AZUL=(0, 0, 255)
NEGRO=(0, 0, 0)

pygame.init()
screen=pygame.display.set_mode([ANCHO, ALTO])
screen.fill(BLANCO)
pygame.display.flip()

#Dibuja plano cartesiano dado una pantalla y un centro
def cartPlane(scr, c):
    pini=(0, c[1])
    pfin=(ANCHO, c[1])
    pygame.draw.line(scr, NEGRO, pini, pfin)
    pini=(c[0], 0)
    pfin=(c[0], ALTO)
    pygame.draw.line(scr, NEGRO, pini, pfin)
    pygame.display.flip()

#Traslación de una lista
def Move(pts, c):
    Mpts=[]
    for pt in pts:
        x=c[0]+pt[0]
        y=c[1]-pt[1]
        Mpt=[x,y]
        Mpts.append(Mpt)
    return Mpts

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
def drawRegPoly(scr, n):
    d=360/n
    pts=[]
    angle=0
    for i in range (0,n):
        rAngle=math.radians(angle)
        x=190*math.cos(rAngle)
        y=190*math.sin(rAngle)
        pt=[x,y]
        pts.append(pt)
        angle=angle+d
    Mpts=Move(pts, [200,200])
    pygame.draw.polygon(scr, NEGRO, Mpts, 1)
    pygame.display.flip()

#Escala con respecto a un punto fijo (recibe una lista de puntos y la escala)
def scaleFixedPoint(scr, pts, s):
    Mpts=Move(pts, [200,200])
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
def rotateFixedPoint(scr, pts, angle):
    Mpts=Move(pts, [200,200])
    pygame.draw.polygon(scr, NEGRO, Mpts, 1)
    tx=pts[0][0]
    ty=pts[0][1]
    Rpt=[]
    angle=math.radians(angle)
    for pt in pts:
        x=((pt[0]-tx)*(math.cos(angle))-(pt[1]-ty)*(math.sin(angle)))+tx
        y=((pt[0]-ty)*(math.sin(angle))+(pt[1]-ty)*(math.cos(angle)))+ty
        rpt=[x,y]
        Rpt.append(rpt)
    Mpts=[]
    Mpts=Move(Rpt, [200,200])
    pygame.draw.polygon(scr, NEGRO, Mpts, 1)
    pygame.display.flip()

#drawRegPoly(screen, 50)
rotateFixedPoint(screen, [[20,20],[50,20],[50,40]], 90)

fin=False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin=True
