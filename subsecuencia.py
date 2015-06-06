#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def quickSort(v):
	if(len(v)<=1):
		return v
	elif(len(v)==2):
		if(v[0]>v[1]):
			aux=v[0]
			v[0]=v[1]
			v[1]=aux
		return v
	else:
		izquierda=0
		derecha=len(v)-1
		pos_pivote=(izquierda+derecha)/2
		pivote=v[pos_pivote]

		while(izquierda<derecha):	
			while(v[izquierda]<pivote):
				izquierda=izquierda+1
			while(v[derecha]>pivote):
				derecha=derecha-1
			if(izquierda<derecha):
				if(izquierda==pos_pivote):
					pos_pivote=derecha
				elif(derecha==pos_pivote):
					pos_pivote=izquierda
				aux=v[izquierda]
				v[izquierda]=v[derecha]
				v[derecha]=aux
				izquierda=izquierda+1 #Debo incrementar uno arbitrariamente
		v_pivote=[pivote]
		v_izq=quickSort(v[0:pos_pivote])
		v_der=quickSort(v[pos_pivote+1:len(v)])
		return v_izq+v_pivote+v_der

def subSecuenciaConsecutivaMasLarga(v,prof):
	v=quickSort(v)
	izquierda=0
	derecha=len(v)-1
	pos_pivote=((izquierda+derecha)/2)
	print("\t"*prof+"la posicion del pivote es: {} y el vector es: {}".format(pos_pivote,v))
	if(pos_pivote>=0):
		pivote=v[pos_pivote]

	if(len(v)<=1):
		return v
	elif(len(v)==2):
		if(v[1]==v[0]+1):
			return v
		else:
			if(v[0]+1==pivote or v[0]-1==pivote):
				return [v[0]]
			else:
				return [v[1]]
	else:
		pos_pivote_izquierda=pos_pivote
		pos_pivote_derecha=pos_pivote+1

		v_izq=v[0:pos_pivote_izquierda]
		v_der=v[pos_pivote_derecha:len(v)]
		v_pivote=[pivote]

		###### CALCULO DE UNA SECUENCIA MAXIMA PROVISIONAL ALREDEDOR DEL PIVOTE ######
		if(v_izq[len(v_izq)-1]+1 == pivote ):
			pos_pivote_izquierda=pos_pivote_izquierda-1
			if(pivote + 1 == v_der[0]):
				v_pivote=[v_izq[len(v_izq)-1]]+v_pivote+[v_der[0]]
				pos_pivote_derecha=pos_pivote_derecha+1
			else:
				v_pivote=[v_izq[len(v_izq)-1]]+v_pivote
		elif( pivote+1 == v_der[0] ):
			v_pivote=v_pivote+[v_der[0]]
			pos_pivote_derecha=pos_pivote_derecha+1
		elif( v_izq[len(v_izq)-1]+1 == v_der[0] ):
			v_pivote=[v_izq[len(v_izq)-1]]+[v_der[0]]
			pos_pivote_izquierda=pos_pivote_izquierda-1
			pos_pivote_derecha=pos_pivote_derecha+1
		
		###### EL PIVOTE AHORA PUEDE TENER MAS DE UN ELEMENTO ######
		print ("\t"*prof+"Provisional: {}".format(v_pivote))
		
		
		v_izq=v[0:pos_pivote_izquierda]
		sec_izq=subSecuenciaConsecutivaMasLarga(v_izq,prof+1)
		v_der=v[pos_pivote_derecha:len(v)]
		sec_der=subSecuenciaConsecutivaMasLarga(v_der,prof+1)
		print("\t"*prof+"La subsecuencia izquierda tiene {} elementos, y es: {}.".format(len(sec_izq),sec_izq))
		print("\t"*prof+"La subsecuencia derecha tiene {} elementos, y es: {}.".format(len(sec_der),sec_der))
		
		sml=[]

		if(len(sec_izq)==0):
			if(len(sec_der)>len(v_pivote)):
				sml=sec_der
			else:
				sml=v_pivote
		elif(len(sec_der)==0):
			if(len(sec_izq)>len(v_pivote)):
				sml=sec_izq
			else:
				sml=v_pivote
		else:
			if( sec_izq[len(sec_izq)-1]+1 == v_pivote[0] ):
				if(v_pivote[len(v_pivote)-1] + 1 == sec_der[0]):
					sml=sec_izq+v_pivote+sec_der
				else:
					sml=sec_izq+v_pivote
			elif( v_pivote[len(v_pivote)-1] + 1 == sec_der[0]):
				sml=v_pivote+sec_der
			elif( sec_izq[len(sec_izq)-1]+1 == sec_der[0] ):
				sml=sec_izq+sec_der
			
			elif( len(sec_izq) > len(sec_der) ):
				if(len(sec_izq)>len(v_pivote)):
					sml=sec_izq
				else:
					sml=v_pivote
			else:
				if(len(sec_der)>len(v_pivote)):
					sml=sec_der
				else:
					sml=v_pivote
		return sml




if (__name__=="__main__"):
	CUANTOS=100
	m=[]
	for i in range(CUANTOS):
		m.append(random.randrange(200))
	m=subSecuenciaConsecutivaMasLarga(m,0)
	print m