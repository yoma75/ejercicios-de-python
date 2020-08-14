# Obtener una palabra a la inversa:

cadena = input('Escriba la palabra a invertir: '.upper())
print()

for i in range(len(cadena)-1,-1,-1):      
    print(cadena[::-1])


