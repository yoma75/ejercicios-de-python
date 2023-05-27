def opbasicas(a,b,c):

	suma = a+b+c
	resta = a-b-c
	multi = a*b*c
	divis = a/b/c

	return f'Totales: suma: {suma}, resta: {resta}, Multiplicacion: {multi}, División: {round(divis,2)}'


final=opbasicas(12,7,9)
final2=opbasicas(14,2,-3)

print(final)
# Totales: suma: 28, resta: -4, Multiplicacion: 756, División: 0.19

print(final2)
# Totales: suma: 13, resta: 15, Multiplicacion: -84, División: -2.33
