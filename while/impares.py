# Crea un bucle while que cuente de 0 a 10, e imprima números impares

x = 1

while x < 11:
  if x % 2 != 0:
    print(x, end=', ')  # 1, 3, 5, 7, 9,
  x += 1
