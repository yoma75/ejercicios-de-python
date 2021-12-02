# Escribir una clase que se llame Areas(). A partir de un constructor se deben pasar los valores de Base y Altura. Luego, se debe calcular area de un cuadrado, triangulo y pentagono

class Areas:
  def __init__(self):
    self.base = int(input('\nDigite la base: '))
    self.altura = int(input('Digite la altura: '))
  

  def area_cuadrado(self):
    self.cuadrado = self.base * self.altura
    print(f'\nEl area del cuadrado es de: {self.cuadrado} cm')
  

  def area_triangulo(self):
    self.triangulo = (self.base * self.altura) / 2
    print(f'El area del triangulo es de: {self.triangulo} cm\n')


  def area_pentagono(self):
    pass


area = Areas()

area.area_cuadrado()
area.area_triangulo()
