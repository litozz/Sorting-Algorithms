def potenciaDV(base, exponente):
	if(exponente==0):
		return 1
	if(exponente<2):
		x=base
		for i in range(exponente-1):
			x=x*x
		return x
	else :
		x=potenciaDV( potenciaDV(base,int(exponente/2)) , 2 )
		if(exponente%2!=0):
			x=x*base
		return x


print (potenciaDV(2,5000))