class Primera:
  def __init__(self):
    print('Yo soy la primera clase')
  
  def primerita(self):
    return 'Este es le metodo heredado de PRIMERA'
    

class Segunda:
  def __init__(self):
    print('Yo soy la segunda clase')
  
  def secundita(self):
    return 'Este es le metodo heredado de SEGUNDA'


class Tercera(Segunda, Primera):
  def tercerita(self):
    return 'Este es le metodo heredado de TERCERA'


herencia_multiple = Tercera()
print(herencia_multiple)

print(herencia_multiple.primerita())  # Este es le metodo heredado de PRIMERA
print(herencia_multiple.secundita())  # Este es le metodo heredado de SEGUNDA
print(herencia_multiple.tercerita())  # Este es le metodo heredado de TERCERA

