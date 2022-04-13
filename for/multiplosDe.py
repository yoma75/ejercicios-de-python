# Pide al usuario un número entero (por ejemplo, 58) y responde todos los múltiplos de 7 que haya entre el número 1 y ese número (incluido).

num = int(input('\nDigite un número: '.upper()))

print(f'Los múltiplos de 7 hasta el número {num} son: ')

for x in range(1, num + 1):
  if (x % 7 == 0):
    print(x)