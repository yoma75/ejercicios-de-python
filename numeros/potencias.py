# Programa que permita obtener el cubo, la cuarta y la quinta potencia de N números ingresados por el usuario. 

print()
numero = int(input('Ingrese un numero: '))

cubo = numero**3
cuarta = pow(numero, 4)
quinta = pow(numero, 5)
   
print()
print(f'La tercera potencia de {numero} es: {cubo}')
print(f'La cuarta potencia de {numero} es: {cuarta}')
print(f'La quinta potencia de {numero} es: {quinta}')

