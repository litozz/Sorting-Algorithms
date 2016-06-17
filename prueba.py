def valorar(jugador, jugadorContrario, tablero, rows, cols, direccion, cantidadYo, candtidadContrario):
	for i in range(rows):
		for j in range(cols):
			if (direccion=-1): #ABAJO
				if(tablero[i][j]==jugador)
					if(tablero[i+1][j]==jugador)
						cantidadYo++
						valorar(jugador,jugadorContrario,tablero,rows-1,cols,direccion,cantidadYo,cantidadContrario)
				else if(tablero[i][j]==jugadorContrario)
						cantidadContrario++
						valorar(jugador,jugadorContrario,tablero,rows-1,cols,direccion,cantidadYo,cantidadContrario)
			else if (direccion=0): # DIAGONAL
			
			else #DERECHA


tablero=[[-1 for x in range(7)] for x in range(7)];
