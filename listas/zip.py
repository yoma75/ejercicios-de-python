# zip(): sirve para iterar sobre 2 secuencias simultaneamente con el ciclo for

numeros = [1, 2, 3, 4]
letras = ['a', 'b', 'c', 'd']

for x, y in zip(numeros, letras):
  print(x, y)  # 1 a
               # 2 b
               # 3 c
               # 4 d
