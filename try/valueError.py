while True:
  try:
    edad = int(input('Digite su edad: '))
    print(f'{edad} años\n')
    break
  except ValueError:
    print('Has colocado un valor erroneo\n')

