# pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que 'riman'. Si coinciden sólo las dos últimas tiene que decir que 'riman un poco' y si no, que 'no riman'.

palabra1 = input('Escriba una palabra: '.upper())
palabra2 = input('Escriba otra palabra: '.upper())

if (palabra1[-3] == palabra2[-3]):
  print(f'La palabra "{palabra1}" y la palabra "{palabra2}"... Si riman\n')
elif (palabra1[-2] == palabra2[-2]):
  print(f'La palabra "{palabra1}" y la palabra "{palabra2}"... riman un poco\n')
else:
  print(f'La palabra "{palabra1}" y la palabra "{palabra2}"... no riman\n')

