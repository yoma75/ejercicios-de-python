# Definir una funcion max() que tome como argumento tres numeros y devuelva el mayor de ellos:

def max_de_tres(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print('El numero mayor es: {}'.format(n1))
    elif n2 > n1 and n2 > n3:
        print('El numero mayor es: {}'.format(n2))
    elif n3 > n1 and n3 > n2:
        print('El numero mayor es: {}'.format(n3))
    else:
        print('Son iguales')

max_de_tres(23,43,54)
max_de_tres(145,34,7)
max_de_tres(5,10,1)
max_de_tres(3,3,4)
max_de_tres(4,4,4)

