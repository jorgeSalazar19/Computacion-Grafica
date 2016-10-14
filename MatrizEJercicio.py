##Mostrar la matriz opuesta de una matriz
import random

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
			matrizAux=[]	#se crea una matriz auxiliar
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
	filaR = []	#la fila resultalnte se declara vacia
	for con in range(aux):
		filaR.append(0)	#dependiendo de el numero de columnas se llena con ese mismo numero de 0 la lista con la fila resultante filaR[0,0,...]
	for fila in range(aux):
		filaR[fila] = PFila[fila] + SFila[fila] #la fila resultante es igual a la suma de la primera y segunda fila , en la posicion fila .
	matriz[NumfilaR] = filaR #finalmente se agrega la fila a la matriz , dependiendo del atributo NUmfilaR ,  que me dice que fila sera modificada
	return matriz

	

nc = 3
nf = 3
matriz1 =[]
matriz2 =[]


for fila in LLenarMatrizAleatoria(nc,nf,matriz1):
	print fila
print  "\n"

columna = ColumnaDeMatriz(matriz1,0)
if columna != 0:
	for cont in range(len(columna)):
		print "[",columna[cont],"]"
else:
	print "columna Fuera De Rango"

fila = FilaDeMatriz(matriz1,3)
if fila != 0:
	print fila
else:
	print "Fila Fuera De Rango"


#for fila in LLenarMatrizAleatoria(nc,nf,matriz2):
#	print fila 
#print  "\n"

#if(SumarDosMatriz(matriz1,matriz2) == 0):
#	print "Las Matrices no poseen las mismas columnas"
#else:
#	if(SumarDosMatriz(matriz1,matriz2) == 1):
#		print "Las Matrices no poseen las mismas filas"		
#	else:
#		for fila in SumarDosMatriz(matriz1,matriz2):
#				print fila

#for fila in sumaFilas(matriz1,1,2,2):
#	print fila
#print  "\n"

#for fila in MatrizTrasnspuesta(matriz1):
#	print fila
#print  "\n"




