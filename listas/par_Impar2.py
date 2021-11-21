lista = []


def pedir():
  i = 0
  while i < 5:
    num = int (input('Ingrese un número: '))
    lista.append(num)
    i += 1

def numeros():
  lista.sort()
  pares = []
  impares = []
  for i in lista:
    if i % 2 == 0:
      pares.append(i)
    else:
      impares.append(i)
  
  print(f'\nPares: {pares}')
  print(f'Impares: {impares}\n')

pedir()
numeros()

