'''saludo =  "hola"
nombre = input('ingrese nombre')

print(saludo + nombre)

print (5 < 10)
print(2>20)
print(6<=6)
print(0==0)
'''
##si prom> 13 
	##entonces aprueba
##sino 
	##reprueba

nota1 = int(input("nota1"))
nota2 = int(input("nota2"))
nota3 = int(input("nota3"))
prom= (nota1+nota2+nota3)/3
print("el promedio es %f"%prom)

if(prom>13):	
 	print("aprueba")
else:
 	print("desaprueba")