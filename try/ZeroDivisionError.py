while True:
  try:
    num = int(input('Ingresa un numero: '))
    resultado = 100 / num
    print(f'100 / entre {num} es: {resultado}\n')
    break
  except ZeroDivisionError:
    print('No se puede dividir entre cero\n')
