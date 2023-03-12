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


''' Definir tres clases: Primera, Segunda y Tercera. La clase Tercera hereda de las clases Segunda y Primera, lo que se llama herencia múltiple. Cada clase tiene un método init que imprime un mensaje y otro método que devuelve una cadena. La clase Tercera también tiene un método propio llamado tercerita.

Has creado un objeto de la clase Tercera llamado herencia_multiple y has impreso su representación. Luego has llamado a los métodos primerita, secundita y tercerita para el objeto y los has impreso.'''