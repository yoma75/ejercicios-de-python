# Programa que permita calcular el 30% es el 0,3 el 60% y el 90% de un número cualquiera

numero = float(input('Digita una cantidad para ver sus porcentajes: '))

a = (numero * 30)/100
b = (numero * 60)/100
c = (numero * 90)/100

print('Al 30 por ciento es de: {r:1.2f}'.format(r=a))
print('Al 60 por ciento es de: {r:1.2f}'.format(r=b))
print('Al 90 por ciento es de: {r:1.2f}'.format(r=c))

