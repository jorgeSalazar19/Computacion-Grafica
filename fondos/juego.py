import pygame
ANCHO=600
ALTO=400

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
    #fondo=pygame.image.load('terrenogen.png').convert_alpha()
    fondo=Cargar_fondo('terrenogen.png',32,32)
    pantalla.blit(fondo[8][9],(0,0))
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True
