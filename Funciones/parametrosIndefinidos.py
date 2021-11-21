# * el asterisco: significa que los parametros son indefinidos

def lista(*valores):
  for x in valores:
    print(x, end=' ')  # 95 159 Hola 287

lista(95, 159, 'Hola', 287)

