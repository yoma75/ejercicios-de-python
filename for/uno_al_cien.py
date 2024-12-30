# Usar el while para mostrar los numeros impares del 1 al 100:

i = 1

while(i <= 100):
    print(i)
    i += 2

print('-----------------------------------------')


# con un for seria:
for x in range(1,101,2):
    print(x)

'''El bucle for se inicia con la palabra clave for, seguida por el nombre de una variable (en este caso, x) y la palabra clave in.
range(1,101,2) se utiliza para crear un rango de números que comienza en 1 y termina en 101 (pero sin incluir el 101) en incrementos de 2. Es decir, los valores del rango son 1, 3, 5, 7, 9, 11, ..., 97, 99.
En cada iteración del bucle, la variable x se establece en el siguiente valor en el rango (1 en la primera iteración, 3 en la segunda iteración, 5 en la tercera iteración, y así sucesivamente).
Dentro del bucle, la función print() se utiliza para imprimir el valor actual de la variable x en la pantalla.
Entonces, el resultado de este código será imprimir los números impares del 1 al 99, ya que estamos saltando de dos en dos con el argumento 2 en la función range().'''

print('-----------------------------------------')

# Si es para numeros pares debe comenzar en 2 y termina en 101 e incrementa de 2 en 2:
for y in range(2,101,2):
    print(y)
