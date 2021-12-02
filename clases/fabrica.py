# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica:
  def __init__(self, llantas, color, precio):
    self.llantas = llantas
    self.color = color
    self.precio = precio
  

class Moto(Fabrica):
  def datos(self):
    print(f'Llantas MOTO: {self.llantas}')
    print(f'Color MOTO: {self.color}')
    print(f'Precio MOTO: {self.precio}')
  

class Carro(Fabrica):
  def datos(self):
    print(f'\nLlantas CARRO: {self.llantas}')
    print(f'Color CARRO: {self.color}')
    print(f'Valor CARRO: {self.precio}')
    

moto = Moto(2, 'Negro', 4000)
moto.datos()

carro = Carro(4, 'Azul', 5000)
carro.datos()
