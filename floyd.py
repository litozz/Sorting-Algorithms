#!/usr/bin/python
import random
import sys
#print "unString {}".format(random.randrange(1,10+1))


def min(a,b):
	_min=0
	if(b<a): 
		_min=b
	else: 
		_min=a
	return _min

def imprimirMatriz(ady,fil,col):
	for i in xrange(fil):
		for j in xrange(col):
			print ady[i][j],
		print ""

def recuperarDestino(origen,destino,costes,vertices,solucion):
	if(vertices[origen][destino]!=-1):
		recuperarDestino(origen,vertices[origen][destino],costes,vertices,solucion)
		recuperarDestino(vertices[origen][destino],destino,costes,vertices,solucion)
	else:
		solucion.append(destino)
	return solucion


simetrico=raw_input("Tu grafo es bidireccional? (No dirigido): ")
numNodos=input("Dime cuantos nodos tiene tu grafo: ")

#adyacencia = [[random.randrange(1,10) for x in range(NC)] for x in range(NF)]
adyacencia = [[-1 for x in range(numNodos)] for x in range(numNodos)];
vertices = [[-1 for x in range(numNodos)] for x in range(numNodos)];

#ASIGNACION DE LONGITUDES
for i in xrange(numNodos):
	for j in xrange(numNodos):
		if(i!=j):
			correcto=False
			while(not correcto):
				if(adyacencia[i][j]<0):
					camino=raw_input("Longitud del camino de {} a {}: ".format(i,j))
					if ( camino=="i" ):
						adyacencia[i][j]=sys.maxint #asigno
						#adyacencia[i][j]=float("inf") 
						if(simetrico=="S" or simetrico=="s"):
							adyacencia[j][i]=sys.maxint
							#adyacencia[i][j]=float("inf")
						correcto=True
					else:
						try:
							adyacencia[i][j]=int(camino)
							if(simetrico=="S" or simetrico=="s"):
								adyacencia[j][i]=int(camino)
							correcto=True
						except ValueError:
							print ("Por favor, introduce un valor entero o bien 'i' (infinito)")
							correcto=False
				else:
					correcto=True
		else:
			adyacencia[i][j]=0
		
#MATRIZ DE ADYACENCIA COMPLETADA

imprimirMatriz(adyacencia,numNodos,numNodos)

for iteracion in range(numNodos):
	for i in xrange(numNodos):
 		for j in xrange(numNodos):
 			if( (i!=iteracion and j!=iteracion) and i!=j ):
 				if( min(adyacencia[i][j] , adyacencia[i][iteracion]+adyacencia[iteracion][j]) == (adyacencia[i][iteracion]+adyacencia[iteracion][j]) ):
 					adyacencia[i][j]=(adyacencia[i][iteracion]+adyacencia[iteracion][j])
 					vertices[i][j]=iteracion;

print "Tras los calculos: "
imprimirMatriz(adyacencia,numNodos,numNodos)
print ""
imprimirMatriz(vertices,numNodos,numNodos)

consultar=True
while(consultar):
	origen=input("Dime un origen: ")
	destino=input("Dime un destino: ")
	if(adyacencia[origen][destino]==sys.maxint):
		print "No se puede recorrer este camino."
	else:
		sol=[]
		sol.append(origen)
		sol=recuperarDestino(origen,destino,adyacencia,vertices,sol);
		print "Los nodos a recorrer son: ",sol," con coste: ",adyacencia[origen][destino]
	continuar=raw_input("Desea consultar otro camino? (S/N): ")
	if (continuar == "s" or continuar=="S"):
		consultar=True
	else:
		consultar=False