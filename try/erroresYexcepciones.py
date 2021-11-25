# finally: se ejecuta alla o no alla error

while True:
  try:
    edad = int(input('Ingrese su edad: '))
    print(f'Tu edad es: {edad}')
    break
  except:
    print('Ingreso un valor erroneo\n')
  finally:
    print('La ejecucion ha terminado')

