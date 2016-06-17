def factible(objetos,i,solucion,capacidad):
	return objeto[i]<=capacidad
		


def mochila(objetos,capacidad):
	nivel=0
	solucion=[-1 for x in range(len(objetos))]

	while(nivel<len(objetos)):
		solucion[nivel]=solucion[nivel]+1
		if(Factible(objetos,nivel,solucion,capacidad)):
			









objetos=[(1,1),(2,6),(5,18),(6,22),(7,28)]
capacidad=11

mochila(objetos,capacidad)