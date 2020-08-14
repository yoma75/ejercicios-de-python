# Programa en el cual se ingresen 2 números y luego realice las siguientes operaciones: 
# a) Si los números son iguales restarlos 
# b) Si los números son diferentes sumarlos


def numeros(a,b):
    if a == b:
        return a - b
    else:
        return a + b

print('Los numeros son iguales se restan: {}'.format(numeros(23,23)))
print('Los numeros son diferentes se suman: {}'.format(numeros(45,67)))

