'''La secuencia de Fibonacci es una serie de números donde cada número es la suma de los dos números anteriores en la serie. La serie comienza con 0 y 1, y luego cada número subsiguiente se calcula como la suma de los dos números anteriores.'''


def fibonacci(n):

  # Verificar si el número es menor o igual a 0
  if n <= 0:
    print("El número de términos debe ser mayor que 0.")

  # Si el número 1, imprima el primer número en la secuencia
  elif n == 1:
    return 0
  
  # Si el número es 2, imprima los primeros dos números en la secuencia
  elif n == 2:
    return 1
  
  # Si el número es mayor que 2, calcula la secuencia de Fibonacci
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Imprimir los primeros 10 números
for i in range(1, 11):
    print(fibonacci(i))


'''El código define la función "fibonacci(n)" que toma un número llamado "n" como entrada. Este número le dice a la función cuántos números de Fibonacci queremos que genere.
Después de eso, el código verifica si el número que hemos ingresado es mayor que cero (si no es así, nos dice que necesitamos ingresar un número mayor que cero). 
Si el número es igual a 1, la función devuelve 0 (que es el primer número de Fibonacci). 
Si el número es igual a 2, la función devuelve 1 (que es el segundo número de Fibonacci). 
Si el número es mayor que 2, la función usa un proceso llamado "recursividad" para calcular los números subsiguientes en la serie de Fibonacci.
Finalmente, el código usa un bucle "for" para imprimir los primeros 10 números en la serie de Fibonacci.'''
