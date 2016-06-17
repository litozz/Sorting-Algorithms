def Fibonacci(n):#Utilizamos la política de ignorar el término 0, pues el primer término de Fibonacci es 1.
	if(n==0):
		return 0
	if(n==1):
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

def FibonacciPD(n):#Utilizamos la política de ignorar el término 0, pues el primer término de Fibonacci es 1.
	if(n>=2):
		numeros=[-1 for i in range(n+1)]
	else:
		numeros=[-1 for i in range(2)]
	numeros[0]=0
	numeros[1]=1
	if(n==0):
		return numeros[0]
	elif(n==1):
		return numeros[1]
	else:
		for i in range(2,n+1):
			numeros[i]=numeros[i-1]+numeros[i-2]
	return numeros[n]



#Vamos a demostrar los beneficios de la programación dinámica:: 
#print(Fibonacci(35)) -> 9.7 segundos
print(FibonacciPD(50000)) #-> 0.7 segundos