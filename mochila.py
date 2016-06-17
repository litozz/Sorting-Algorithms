#!/usr/bin/env python
# -*- coding: utf-8 -*-
#José Carlos Martínez Velázquez - Algorítmica - 2ºGII(C)
#Conjunto de peso elementos PE={P1,P2,P3,...,Pn}				
#Conjunto de beneficios de elementos BE={B1,B2,B3,...,Bn}

#|PE|=|BE|

#Conjunto de mochilas CM={M1,M2,...,Mm}
#Conjunto de capacidades de mochilas CapM={C1,C2,...,Cm}

#|CM|=|CapM|

#m no necesariamente igual n

def max(a,b):
	if(a>b):
		return a
	else:
		return b


def pintarMatriz(m):
	for i in range(len(m)):
		print(str(m[i])),
	print("")

def interpretarResultado(resultado,pesos,beneficios):#Esta funcion interpreta un vector que contendrá los objetos que se han ido cogiendo y el beneficio obtenido
	elementos=resultado[0:len(resultado)-1]
	beneficio=resultado[len(resultado)-1]
	peso_total=0
	print("La forma optima de llenado es:")
	for i in range(len(elementos)):
		print("\t* Meter el elemento con peso {} y beneficio {}".format(pesos[elementos[i]],beneficios[elementos[i]]))
		peso_total=peso_total+pesos[elementos[i]]
	print("Con un beneficio de {} y un peso total de {}".format(beneficio,peso_total))


def mochila(pesos, beneficios, capacidad):#La funcion que calcula la forma optima de coger elementos con Prog. Dinámica.
	matriz=[[-1 for j in range(capacidad + 1)] for i in range(len(pesos) + 1)]
	print ("Pesos de los objetos: \t\t\t\t"+str(pesos))
	print ("Beneficios de los objetos: \t\t\t"+str(beneficios))
	print ("Capacidad maxima de la mochila: \t"+str(capacidad))
	#######################  APLICACION DE LAS NORMAS DE LA ECUACION DE RECURRENCIA  #######################
	for i in range(len(pesos)+1):
		for j in range(capacidad+1):
			if (i==0 or j==0):#No hay mochilas o no hay objetos
				matriz[i][j]=0
			elif(pesos[i-1]>j):#El peso del objeto a introducir es mayor que el que queda
				matriz[i][j]=matriz[i-1][j]
			elif(pesos[i-1]<=j):#El objeto se puede introducir
				matriz[i][j]=max(matriz[i-1][j], matriz[i-1][j-pesos[i-1]]+beneficios[i-1])
	#####################  FIN APLICACION DE LAS NORMAS DE LA ECUACION DE RECURRENCIA  #####################
	pintarMatriz(matriz)			
	

	i=len(pesos)
	j=capacidad
	cogidos=[]
	#######################  RESCATE DE LOS OBJETOS QUE FUERON COGIDOS TIRANDO DE LA ECUACION DE RECURRENCIA  #######################
	while(matriz[i][j]!=0):
		if(matriz[i][j]==matriz[i-1][j]):#El objeto no se introdujo
			i=i-1
		elif(matriz[i][j]==matriz[i-1][j-pesos[i-1]]+beneficios[i-1]):#El objeto se introdujo
			j=j-pesos[i-1]
			i=i-1
			cogidos.append(i)#Tengo que coger pesos[i] porque acabo de reducir i en 1 elemento
	cogidos.append(matriz[len(pesos)][capacidad])#Añado el beneficio máximo por política propia para interpretar el resultado con una funcion
	#############################################  FIN RESCATE DE LOS OBJETOS COGIDOS  #############################################
	interpretarResultado(cogidos,pesos,beneficios)


if __name__=="__main__":#Algunos main para probar el algoritmo
	#pesos=[3,5,7]
	#beneficios=[4,5,6]
	#capacidad=8

	#pesos=[4,12,22,8]
	#beneficios=[7,3,10,4]
	#capacidad=24	

	#pesos=[4,6,3,5]
	#beneficios=[4,4,4,4]
	#capacidad=12

	#pesos=[5,3,7,10]
	#beneficios=[4,2,5,7]
	#capacidad=12

	#pesos=[9,6,5]
	#beneficios=[38,40,24]
	#capacidad=15

	#[Brassard,Bratley pág 300]:
	pesos=[1,2,5,6,7]
	beneficios=[1,6,18,22,28]
	capacidad=11

	

	mochila(pesos,beneficios,capacidad)