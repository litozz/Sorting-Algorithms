#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def burbuja(m):
	for i in xrange(len(m)):
		for j in xrange(i+1,len(m)):
			if(m[i]>m[j]):
				aux=m[i]
				m[i]=m[j]
				m[j]=aux
	return m


#Esta es la parte magica del quickSort: Buscar el pivote, dejar los menores que el pivote a la izquierda y los mayores a la derecha.
#Insisto que el pivoteo solo deja a izquierda y derecha los menores y mayores respectivamente. No tiene por qué dejar el vector ordenado.
def pivoteoLineal(v,izquierda,derecha):
	pivote=v[(izquierda+derecha)/2]#Se calcula ¡¡SOLO EL VALOR!! (no su posición) del pivote en base a las posiciones derecha e izquierda
	print("El pivote es: {} y está en la posición: {}".format(pivote,(izquierda+derecha)/2))
	while(izquierda < derecha):#Mientras que los punteros izquierda (principio) y derecha (final) no se crucen:
		while(v[izquierda]<pivote):#Buscamos el siguiente elemento MAYOR que el pivote desde la izquierda
			izquierda=izquierda+1
		while(v[derecha]>pivote):#Buscamos el siguiente elemento MENOR que el pivote desde la derecha
			derecha=derecha-1
		#Una vez hemos encontrado elementos que cumplan las restricciones anteriores procedemos a intercambiarlos (un swap de toda la vida)
		#Fíjate que si el vector está ordenado (alguien nos trolea), izquierda y derecha podrían cruzarse, 
		#por lo que hay que comprobar de nuevo si izquierda y derecha siguen siendo iguales. 
		if(izquierda<derecha):
			aux=v[izquierda]
			v[izquierda]=v[derecha]
			v[derecha]=aux
	return v



#DESCOMENTA LOS PRINT SI QUIERES SABER QUE ES LO QUE VA PASANDO ;), TEN EN CUENTA SI LO HACES PERDERÁS EFICIENCIA AL PROBARLO SERIAMENTE.
def quickSort(v,izquierda,derecha,prof):
	if(len(v)<=1): #Si la longitud del vector es menor que uno, ya esta ordenado, se retorna el mismo vector tal cual está
		#print ("\t"*prof+"V: {}".format(v))
		return v
	if(len(v)==2): #Si la longitud es dos, hay que mirar si es necesario un intercambio (un swap de toda la vida)
		if(v[0]>v[1]):
			aux=v[0]
			v[0]=v[1]
			v[1]=aux
		#print ("\t"*prof+"V: {}".format(v))
		return v
	else:
		#print ("\t"*prof+"V: {}".format(v))
		######################  EL TRUCO DEL ALMENDRUCO: PIVOTAR EL VECTOR  ######################
		pos_pivote=(izquierda+derecha)/2#Calculamos la posicion del pivote (Si los elementos se repiten, hará falta.)
		pivote=v[(izquierda+derecha)/2] #Se calcula ¡¡SOLO EL VALOR!! (no su posición) del pivote en base a las posiciones derecha e izquierda
		while(izquierda < derecha): #Mientras que los punteros izquierda (principio) y derecha (final) no se crucen:
			while(v[izquierda]<pivote): #Buscamos el siguiente elemento MAYOR que el pivote desde la izquierda
				izquierda=izquierda+1
			while(v[derecha]>pivote): #Buscamos el siguiente elemento MENOR que el pivote desde la derecha
				derecha=derecha-1
			#Una vez hemos encontrado elementos que cumplan las restricciones anteriores procedemos a intercambiarlos (un swap de toda la vida)
			#Fíjate que si el vector está ordenado (alguien nos trolea), izquierda y derecha podrían cruzarse, 
			#por lo que hay que comprobar de nuevo si izquierda y derecha siguen siendo iguales. 
			if(izquierda<derecha):
				if(izquierda==pos_pivote): #El pivote se va a mover a la posicion derecha
					pos_pivote=derecha
				elif(derecha==pos_pivote): #El pivote se va a mover a la posicion izquierda
					pos_pivote=izquierda
				aux=v[izquierda]
				v[izquierda]=v[derecha]
				v[derecha]=aux
				izquierda=izquierda+1 #Aumentamos izquierda o decrementamos derecha arbitrariamente, hay que avanzar una de las posiciones para evitar cuelgues
		##########################################################################################
#############################################################################################################################################
#	Un poco de álgebra para saber cuántos elementos hay en un intervalo:																	#
#																																			#
#	Si yo tengo un vector v[0:(izquierda+derecha)/2]: 																						#
#	eso quiere decir que va desde la posicion 0 hasta la posición ((izquierda+derecha)/2)-1 (La parte derecha del intervalo es exclusive)	#
#	Las leyes del álgebra nos dicen que en un intervalo [a,b] hay:																			#
#		b-a + 1 -> Si a y b están inclusive																									#
#		b-a - 1 -> Si a y b están exclusive																									#
#	En el intervalo [50-60] hay 60-50+1 = 11 números si ambos están incluidos: 	50,51,52,53,54,55,56,57,58,59,60 							#
#																				1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11							#
#	Entonces si nostros tenemos algo así: 																									#
#		v[0:(izquierda+derecha)/2], el intervalo será: [0,((izquierda+derecha)/2)-1],														#
#		de donde extraeremos que la cantidad de elementos que contiene ese vector es: ((izquierda+derecha)/2)-1 - 0 + 1 					#
#		es decir, su len(v)=((izquierda+derecha)/2)-1 - 0 + 1=((izquierda+derecha)/2), 														#
#		¡¡¡¡¡PERO OJO!!!!! dado que ese es su len(v), el último elemento (izquierda) será len(v)-1, es decir: ((izquierda+derecha)/2)-1 	#
#																																			#
#	Esto viene a cuenta del tercer parámetro de quickSort() ya que el segundo siempre será 0 (si queremos ordenar todo el vector)			#
#############################################################################################################################################
		#Ahora procedemos a trocear el vector en dos partes: lo que está a la izquierda del pivote y 
		#lo que está a la derecha del mismo SIN INCLUIRLO!!
		v_izq=quickSort(v[0:pos_pivote],0,pos_pivote-1,prof+1) #Ordeno la parte izquierda de forma independiente
		v_der=quickSort(v[pos_pivote+1:len(v)],0,len(v)-pos_pivote-3,prof+1) #Ordeno la parte derecha de forma independiente
		#(Le pongo -1+1 para que se entienda cómo he calculado el intervalo con la regla de arriba)
		lpivote=[pivote] #Añado el pivote a un vector para poder concatenarlo (capricho de Python)
		return v_izq+lpivote+v_der #El resultado será la concatenacion de la parte izquierda (menores que el pivote) ordenada,
		#el pivote entre ambas partes y la parte derecha (mayores que el pivote) ordenada




def mergeSort(v,izquierda,derecha,prof):	
	if(len(v)<=1): #Si la longitud del vector es menor que uno, ya esta ordenado, se retorna el mismo vector tal cual está
		#print ("\t"*prof+"V: {}".format(v))
		return v
	if(len(v)==2): #Si la longitud es dos, hay que mirar si es necesario un intercambio (un swap de toda la vida)
		if(v[0]>v[1]):
			aux=v[0]
			v[0]=v[1]
			v[1]=aux
		#print ("\t"*prof+"V: {}".format(v))
		return v
	else:
		medio=(izquierda+derecha)/2 #Calculamos el punto por donde partir
		v_izq=mergeSort(v[0:medio],0,medio-1,prof+1) #Hacemos mergeSort sobre el vector que contiene la parte izquierda SIN el elemento medio
		v_der=mergeSort(v[medio:len(v)],0,(len(v)-medio)-1,prof+1) #Hacemos mergeSort sobre el vector que contiene la parte derecha CON el elemento medio

		punt_v_izq=0 #Este indice recorrerá la parte izquierda ordenada
		punt_v_der=0 #Este indice recorrerá la parte derecha ordenada

		v=[] #V queda vacía.

		while(punt_v_izq<len(v_izq) and punt_v_der<len(v_der)): #Mientras que ambos indices no hayan llegado al final de su vector
			if(v_izq[punt_v_izq]<v_der[punt_v_der]): #Vemos si el elemento actual del vector izquierdo es el más pequeño
				v.append(v_izq[punt_v_izq]) #Lo añadimos al vector solucion
				punt_v_izq=punt_v_izq+1 #Avanzamos el indice de la parte izquierda
			else: #En caso de que el actual izquierdo no sea el más pequeño:
				v.append(v_der[punt_v_der]) #Añadimos el actual de la parte derecha
				punt_v_der=punt_v_der+1 #Avanzamos el puntero de la parte derecha

		#En este punto, van a sobrar elementos en el vector de la izquierda o en el de la derecha
		if(punt_v_izq<len(v_izq)): #Vemos si sobran en la izquierda
			while(punt_v_izq<len(v_izq)): #Recorremos todos los que falten
				v.append(v_izq[punt_v_izq]) #Los metemos todos
				punt_v_izq=punt_v_izq+1 #Avanzamos el puntero en cada iteracion
		elif(punt_v_der<len(v_der)): #Hacemos lo mismo en caso de que donde haya sobrado haya sido en la derecha. Son casos excluyentes.
			while(punt_v_der<len(v_der)):
				v.append(v_der[punt_v_der])
				punt_v_der=punt_v_der+1

		return v #Retornamos la solución
		
		







#PUEDES PROBAR SI QUIERES INDEPENDIENTEMENTE LA PARTE DE PIVOTAR, SI TE FIJAS, EL CÓDIGO DONDE PONE EL TRUCO DEL ALMENDRUCO, ES EL MISMO
#QUE LA FUNCIÓN PIVOTEOLINEAL(), 


if (__name__=="__main__"):
	#m=[5,89,35,14,24,15,37,13,20,7,70]
	CUANTOS=1000000
	m=[]
	for i in range(CUANTOS):
		m.append(i+1)
	random.shuffle(m)
	#m=burbuja(m) #--> No obtiene respuesta en 10 minutos para 1000000 elementos; 10.6 segundos para 10000 elementos 
	m=quickSort(m,0,len(m)-1,0) #--> 6.2 segundos con 1000000 elementos
	#m=mergeSort(m,0,len(m)-1,0) # --> 8 segundos con 1000000 elementos
