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
    fondo=Cargar_fondo('animales.png',32,32)


    reloj=pygame.time.Clock()
    con=0
    var_y=5
    pos_y=0
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin =True

        pantalla.fill((0,0,0))
        if con<=2:
            pos_y+=var_y
            pantalla.blit(fondo[9+con][0],[0,pos_y])
            con+=1
        else:
            con=0
            pos_y+=var_y
            pantalla.blit(fondo[9+con][0],[0,pos_y])


        pygame.display.flip()
        reloj.tick(10)
