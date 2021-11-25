class Fabrica:
  def __init__(self, tiempo, nombre, ruedas):  # funcion constructora
    self.tiempo = tiempo
    self.nombre = nombre
    self.ruedas = ruedas
    print('Se creo el auto', self.nombre)

  def __str__(self):
    return "{} {} meses".format(self.nombre, self.tiempo)


class Listado:

  autos = []

  def __init__(self, autos=[]):  # constructor __init__
    self.autos = autos
  
  def fabricar(self, x):
    self.autos.append(x)
  
  def visualizar(self):
    for x in self.autos:
      print(x)


a = Fabrica(10, 'Renault', 5)
print(a)


m = Listado([a])
m.visualizar()
print(m)

