import pygame
import random

ANCHO=800
ALTO=500
BLANCO=(255,255,255)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
NEGRO=(0,0,0)
GATO=0
PALOMA_T=3
PALOMA_V=6
RATON=9


class Jugador(pygame.sprite.Sprite):
    def __init__(self, imagen_sp):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagen_sp
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=100
        self.var_x=0
        self.var_y=0
        self.con=0
        self.dir=0

    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y
        if self.con<=2:
            self.con+=1
        else:
            self.con=0

def Cargar_fondo(archivo, ancho_corte, alto_corte):
    imagen=pygame.image.load(archivo).convert_alpha()
    img_ancho,img_alto =imagen.get_size()
    print img_alto, ' ', img_ancho
    matriz_fondo=[]
    for fila in range(0, img_ancho/ancho_corte):
        linea=[]
        matriz_fondo.append(linea)
        for columna in range(0, img_alto/alto_corte):
            cuadro=(fila*ancho_corte, columna*alto_corte, ancho_corte, alto_corte)
            linea.append(imagen.subsurface(cuadro))

    return matriz_fondo


if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.mouse.set_visible(False)

    fondo=Cargar_fondo('animales.png',32,32)
    jp=Jugador(fondo[0][1])
    #ANIMAL=GATO
    ANIMAL=PALOMA_V

    todos=pygame.sprite.Group()
    todos.add(jp)
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jp.var_x=-5
                    jp.var_y=0
                    jp.dir=1
                if event.key == pygame.K_RIGHT:
                    jp.var_x=5
                    jp.var_y=0
                    jp.dir=2
                if event.key == pygame.K_DOWN:
                    jp.var_x=0
                    jp.var_y=5
                    jp.dir=0
                if event.key == pygame.K_UP:
                    jp.var_x=0
                    jp.var_y=-5
                    jp.dir=3
                if event.key == pygame.K_SPACE:
                    jp.var_x=0
                    jp.var_y=0

        jp.image=fondo[ANIMAL+jp.con][jp.dir]
        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)
