# Pide al usuario un número entero (por ejemplo, 58) y responde todos los múltiplos de 7 que haya entre el número 1 y ese número (incluido).

num = int(input('\nDigite un número: '.upper()))  # 58

print(f'Los múltiplos de 7 hasta el número {num} son: ')  # Los múltiplos de 7 hasta el número 58 son:

for x in range(1, num + 1):
  if (x % 7 == 0):
    print(x, end=' ')  # 7 14 21 28 35 42 49 56

    