import math

def ESParalelo (valor1, valor2):

	valorTolP = valor1 + (valor1 * 0.05)
	valorTolN = valor1 - (valor1 * 0.05)

	if (valor2 >= valorTolN and valor2 <= valorTolP):
		return 1
	else:
		return 0



print "Recta 1","\n"
A= int (raw_input("Digite La componente A de la recta: "))
B= int (raw_input("Digite La componente B de la recta: "))
C= int (raw_input("Digite La componente C de la recta: "))

print "Recta 2","\n"
A1= int (raw_input("Digite La componente A de la recta: "))
B2= int (raw_input("Digite La componente B de la recta: "))
C3= int (raw_input("Digite La componente C de la recta: "))

valor = B/B2
valor2= A/A1


if (ESParalelo(valor,valor2)):
	print "Son paralelas con una tolerancia del 5%"

else:
	print "No son Paralelas"