import pygame
import math
import random

#Funcion Para dibujar los ejes cartesianos, en la pantalla
def Dibujarejes(c,p,al,an,color):
    pygame.draw.line(p,color,(0,c[1]),(an,c[1]),2)
    pygame.draw.line(p,color,(c[0],0),(c[0],al),2)

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

#funcion que dibuja en la pantalla la lista de puntos que pasamos como parametro
def DibujarPuntos(c,pantalla,puntos,color):
    for cont in range(len (puntos)):
        punto = puntos[cont]
        pantalla.set_at(punto,color)

#funcion que a partir de una lista de puntos, los traslada a su posicion trasladada con respecto al centro de la pantalla
def PuntosTrasladados(c,puntos):
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
    vector = VectorApartir2Puntos(punto1,punto2)
    DibujarVectorDesdeOrigen(pantalla,BLANCO,c,vector)

#Funcion Para rotar un punto en el angul requerido
def RotarPunto(punto,angulo):

    Conv = math.radians(angulo)
    Cos = math.cos(Conv)
    Sen = math.sin(Conv)
    
    puntoxR = punto[0]*Cos - punto[1]*Sen
    puntoyR = punto[0]*Sen + punto[1]*Cos

    #punto  = [int ( puntoxR), int  (puntoyR)]
    punto  = [puntoxR, puntoyR]
    return punto

#Funcion para rotar una lista de puntos en el angulo determinado
def RotarPuntos (Lpuntos,angulo):
    Lrot = []
    aux = len(Lpuntos)
    for cont in range(aux):
        ListaAux = Lpuntos[cont]
        Lrot.append (RotarPunto(ListaAux,angulo))
    return Lrot

#Funcion que retorna la posicion real del mause con respecto al plano
def PosicionReal (puntos,centro):
    aux = len(puntos)
    for cont in range(aux):
        ListaAux = puntos[cont]
        ListaAux[0] = ListaAux[0] - centro[0]
        ListaAux[1] = centro[1] - ListaAux[1]
        puntos[cont] = ListaAux
    return puntos  

#Funcion para escalar una lista de puntos en una escala determianda
def EscalarPunto (puntos,Escala,centro):
    Laux = []
    lRes = []
    aux2 = len(puntos)
    PuntosEscalados =[]
    aux = len(Escala)
    for cont1 in range(aux2):
        for cont in range(aux):
            Laux = puntos[cont1]
            lRes.append(Laux[cont]*Escala[cont])
        PuntosEscalados.append(lRes)
        lRes=[]
    return PuntosEscalados

#FUncion para obtener un vector apartir de dos puntos
def VectorApartir2Puntos(punto1, punto2):
    vector = [punto2[0]-punto1[0],punto2[1]-punto1[1]]
    return vector

#norma de un vector 
def normaVector (vector):
    norma = math.sqrt(pow(vector[0],2) + pow(vector[1],2))
    return norma

#Distancia entre dos puntos determinados
def distanciaEntre2Puntos (punto1,punto2):
    distancia = math.sqrt(pow(punto2[0]-punto1[0],2) + pow(punto2[1]-punto1[1],2))
    return distancia

#producto punto entre dos vectores
def ProductoPunto(vector1,vector2):
    producto = vector1[0]*vector2[0] + vector1[1]*vector2[1]
    return producto

#Angulo entre dos vectores determinados.
def AnguloVector (vector1,vector2):
    norma2vectores= normaVector(vector1)*normaVector(vector2)
    Producto = math.fabs(ProductoPunto(vector1,vector2))
    angulo = math.degrees(math.acos(Producto/norma2vectores))
    return angulo

#Funcion Para Pintar dos puntos y el vectror de esos dos puntos
def PintarPuntosYVector(centro,puntos,pantalla,color):
    punto1x = puntos[0][0] + centro[0]
    punto1y = centro[1] - puntos[0][1] 

    punto1 = (punto1x,punto1y)

    punto2x = puntos[1][0] + centro[0]
    punto2y = centro[1] -puntos[1][1]  

    punto2 = (punto2x,punto2y)

    pygame.draw.line(pantalla,color,puntos[0],puntos[1])
    vectorR = VectorApartir2Puntos(punto1,punto2)
    DibujarVectorDesdeOrigen(pantalla,color,centro,vectorR)
    pygame.display.flip()


#Funcion para dibujar un poligono regular de N lados
def DibujarPoligono(puntos,pantalla,color):
    pygame.draw.polygon(pantalla,color,puntos)
    pygame.display.flip()

#Funcion para sacar los angulos internos de un triangulo
def AngulosInternosTriangulo(puntos):
    vector1 = VectorApartir2Puntos(puntos[0],puntos[1])
    vector2 = VectorApartir2Puntos(puntos[1],puntos[2])
    vector3 = VectorApartir2Puntos(puntos[2],puntos[0])

    print AnguloVector(vector1,vector2)
    print AnguloVector(vector2,vector3)
    print AnguloVector(vector1,vector3)
    print puntos

#funcion para llenar aleatoriamente una matriz , con numeros en un rango del -1-9
def LLenarMatrizAleatoria(columna,fila,matriz):
    con = 0
    while con <fila:
        f=[]
        con2 = 0
        while con2 < columna:
            valor = random.randrange(9)
            f.append(valor)
            con2+=1
        con+=1
        matriz.append(f)
    return matriz
        

#Funcion para obtener la matriz opuesta de una matriz
def MatrizOpuesta(matriz):
    aux = len(matriz)
    aux2 = len(matriz[0])
    for fila in range(aux):
        for col in range(aux2):
            matriz [fila][col] = -1 * matriz[fila][col]
    return matriz

#Funcion para obtener la matriz transpuesta de una matriz
def MatrizTrasnspuesta (matriz1):
    matrizAux=[]
    LLenarMatrizAleatoria(nf,nc,matrizAux)
    aux2 = len(matrizAux[0])
    aux = len(matrizAux)
    for fila in range(aux):
        for col in range(aux2):
            matrizAux [fila][col] = matriz1 [col][fila]
    return matrizAux

#Funcion para sumar dos matrices
def SumarDosMatriz (matriz1, matriz2):
    if( len(matriz1)==len(matriz2)): #si se tienen las mismas filas 
        if (len(matriz1[0]) == len(matriz2[0])): # si se tienen las mismas columnas 
            matrizAux=[]    #se crea una matriz auxiliar
            aux = len (matriz1) #auxiliares para recorrer las matrices
            aux2 = len (matriz1[0])
            LLenarMatrizAleatoria(nc,nf,matrizAux) #se llena la matriz auxiliar de manera aleatoria pero con igual numer de filas y columnas que las matrices a sumar 
            for fila in range (aux):
                for col in range (aux2):
                    matrizAux [fila][col] = matriz1 [fila][col] + matriz2 [fila][col] 
            return matrizAux
        else:
            return 0; #sino tienen las mismas columnas
    else:
        return 1; #sino tienen las mismas filas

#Fucion para sumas filas determinadas en una matriz
def sumaFilas (matriz,fila1,fila2,NumfilaR):
    PFila = matriz[fila1] #Se asigna la primera que se desea sumar, en base al atributo fila 1
    SFila = matriz[fila2] #Se asigna la segunda fila que se desea sumar
    aux = len (matriz[0]) #variable auxiliar , que contiene el numero de columnas de la matriz
    filaR = []  #la fila resultalnte se declara vacia
    for con in range(aux):
        filaR.append(0) #dependiendo de el numero de columnas se llena con ese mismo numero de 0 la lista con la fila resultante filaR[0,0,...]
    for fila in range(aux):
        filaR[fila] = PFila[fila] + SFila[fila] #la fila resultante es igual a la suma de la primera y segunda fila , en la posicion fila .
    matriz[NumfilaR] = filaR #finalmente se agrega la fila a la matriz , dependiendo del atributo NUmfilaR ,  que me dice que fila sera modificada
    return matriz

#Retorno un numero de fla determinada de una matriz
def FilaDeMatriz (matriz,num_fila):
    if num_fila-1 >= 0 and num_fila-1 < len(matriz):
        return matriz[num_fila-1]
    else:
        return 0

#Retorna una columna Determinad de una matriz
def ColumnaDeMatriz(matriz,num_columna):
    numeros = []
    if num_columna-1 >= 0 and num_columna-1 < len(matriz[0]):
        aux = len(matriz)
        aux2 = len(matriz[0])
        for fila in range(aux):
            for col in range(aux2):
                numero = matriz[fila][num_columna-1]
            numeros.append(numero)
        return numeros
    else:
        return 0

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

#Funcion para calcular el radio , de las coordenadas polares 
def CalcularRadioPolares(Vector):
    R = math.sqrt(pow(Vector[0],2)+pow(Vector[1],2))
    return R

#funcion para calcular el angulo de las coordenadas polares 
def AnguloPolarVector(Vector):
    y = math.radians(Vector[1])
    x = math.radians(Vector[0])
    return math.degrees(math.atan2(y,x))

#funcion que dado un vector , me calcula una recta que pasa a 45 grados de el , con ayuda de coordenadas polares 
def RectaVector(Vector):
    R = CalcularRadioPolares(Vector) # Se calcula el radio (coordenas polares) del vector
    angulo = AnguloPolarVector(Vector) # se calcula el angulo (coordenadas polares) del vector

    anguloRecta = angulo + 45 # se calcula el angulo que tendra la recta (sera 45 grados mayor al angulo del vector previamente calculado)

    x = R * math.cos(math.radians(anguloRecta)) # se obtiene la corrdenada x cartesiana de la recta (sera el mismo radio o puede ser cualquiera, lo que importa es el angulo)
    y = R * math.sin(math.radians(anguloRecta)) # se ontiene la coordenada y al igual que la coordenada x

    punto = (x,y) # creo el punto con las coordendas , este sera un punto de la recta 
    return punto # retorno el punto 
    
#Funcion Para Graficar R = 2 - 2sen(angulo) -> cardioide
def GraficarPolar ():
    ListaPuntos = []
    angulo = 0 #Angulo varia de 0 a 360 grados
    while(angulo <= 360): 
        rAngle = angulo
        Angle=math.radians(rAngle) #se pasa el angulo a radianes 
        R = 2 - 2*math.sin(rAngle) #se calcula R
        x = (60*R)*math.cos(angulo) # se alla componente x en cooredeandas cartesianas , (se multiplica por 60 para que sea mas grande)
        y = (60*R)*math.sin(angulo) # se alla componente y en cooredeandas cartesianas , (se multiplica por 60 para que sea mas grande)
        punto = (x,y) #se crean un punto con cada componente
        angulo += 1 # se incrementa el angulo
        ListaPuntos.append(punto) # se agrega el punto a una lista de puntos
    return ListaPuntos # se retorna la lista de puntos
