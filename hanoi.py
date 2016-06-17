def hanoi(nDiscos,origen,auxiliar,destino,profundidad):
	nMoves=1;
	if(nDiscos==1):
		print("| "*profundidad+"Mueve un disco de {} a {}".format(origen,destino))
	else:
		nMoves=nMoves+hanoi(nDiscos-1,origen,destino,auxiliar,profundidad+1)
		print("| "*profundidad+"Mueve un disco de {} a {}".format(origen,destino))
		nMoves=nMoves+hanoi(nDiscos-1,auxiliar,origen,destino,profundidad+1)
	return nMoves
	


nMoves=hanoi(5,0,1,2,0);
print("La partida se ha completado en {} movimientos.".format(nMoves))

