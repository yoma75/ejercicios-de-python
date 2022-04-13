# Pide al usuario 10 números y luego muestra los que son pares.

pares = []

for x in range(1, 11):
  numeros = int(input(f'{x}. Digita un número: '))
  pares.append(numeros)

for n in pares:
  if (n % 2 == 0):
    print(n, end=', ')