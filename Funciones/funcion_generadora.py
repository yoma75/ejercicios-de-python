# FUNCION GENERADORA: es aquella que genera valores sobre la marcha

# Cuando el intérprete Python encuentra una función que incluye un yield (o varios), entiende que al llamar esta función no obtendremos un valor devuelto con un return, sino que obtendremos un generador (generator).

def pares(maximo):
  for numero in range(maximo):
    if(numero % 2 == 0):
      yield numero

maximo = int(input('Digite un numerito: '))
for numero in pares(maximo):
  print(numero)


