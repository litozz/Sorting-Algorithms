def max(a,b):
	if(a>b):
		return a 
	else: 
		return b
def potencia (a,b):
	if(b==0):
		return 1
	elif(b==1):
		return a
	else:
		return a*potencia(a,b-1)

class NumeroLargo(object):
	def convertirAVector(self,numeroL):
		num=[]
		aux=-1
		while(numeroL>9):
			aux=numeroL%10
			num.insert(0,aux);
			numeroL=int(numeroL/10)
		num.insert(0,numeroL)
		return num

	def __init__(self,numeroL):
		if(type(numeroL)==list):
			self.n=numeroL
		else:
			self.n=self.convertirAVector(numeroL)

	def __str__(self):
		cad=""
		for i in range(len(self.n)):
			cad=cad+str(self.n[i])
		return cad
	
	def digitos(self):
		if(type(self.n)==list):
			return len(self.n)
		else:
			return len(convertirAVector(self.n))
	
	def ultimos(self,cuantos):
		#if(type(self.n)!=list):
		#	self.n=self.convertirAVector(self.n)
		#return self.n[len(self.n)-cuantos:len(self.n)]
		if(type(self.n)==list):
			self.n=int(self.__str__())
		return int(self.n % potencia(10, cuantos));
	
	def primeros(self,cuantos):
		#if(type(self.n)!=list):
		#	self.n=self.convertirAVector(self.n)
		#return self.n[0:cuantos]
		if(type(self.n)==list):
			self.n=int(self.__str__())
		return int(self.n/potencia(10, cuantos));
	
	def mitad(self):
		if(type(self.n)!=list):
			self.n=self.convertirAVector(self.n)
		if(len(self.n)%2==0):
			return self.primeros(len(self.n)%2)
		else:
			return self.primeros(len(self.n)%2-1)

	def return_as_integer(self):
		return int(self.__str__())

	def sumar(self,otronumero):
		return self.return_as_integer()+otronumero.return_as_integer()



def multiplica(u,v):
	dig1=0
	dig2=0
	
	numDigitos = max(u.digitos(), v.digitos())
	
	if (numDigitos <= 1): 
		return u.return_as_integer()*v.return_as_integer()
	
	numDigitos = int((numDigitos / 2) + (numDigitos % 2))
	print("---------------------------------------------------")
	w = NumeroLargo(u.primeros(numDigitos)).return_as_integer()
	print("w vale: {}".format(w))
	x = NumeroLargo(u.ultimos(numDigitos)).return_as_integer()
	print("x vale: {}".format(x))
	y = NumeroLargo(v.primeros(numDigitos)).return_as_integer()
	print("y vale: {}".format(y))
	z = NumeroLargo(v.ultimos(numDigitos)).return_as_integer()
	print("z vale: {}".format(z))
	print("---------------------------------------------------")
	p=w*y;
	q=x*z;
	wMasx = NumeroLargo(w + x)
	zMasy = NumeroLargo(z + y)
	
	r=multiplica(wMasx, zMasy)
	
	return potencia(10, 2*numDigitos)*p+potencia(10, numDigitos)*(r-p-q)+q;


primernum=NumeroLargo(61231564582745274581)

segunnum=NumeroLargo(4650274)

print (multiplica(primernum,segunnum));


