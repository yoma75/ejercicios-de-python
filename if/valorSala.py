# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
#  El programa debe preguntar al usuario:
#  la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.


edad = int(input('Que edad tienes: '))

if edad < 4:
    print('Puedes entrar gratis por ser menor de 4 años')
elif edad >= 4 and edad <=18:
    print('Debes de pagar 5 euros por estar entre los 4 y 18 años de edad')
else:
    print('Debes de pagar 10 euros, por ser mayor de 18 años')



