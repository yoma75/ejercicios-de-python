class Fabrica:
  def __init__(self, tiempo, nombre, ruedas):  # funcion constructora
    self.tiempo = tiempo
    self.nombre = nombre
    self.ruedas = ruedas
    print('Se creo el auto', self.nombre)

  def __str__(self):
    return "{} {}".format(self.nombre, self.tiempo)


class Listado:

  autos = []

  def __init__(self, autos=[]):  # constructor __init__
    self.autos = autos
  
  def fabricar(self, x):
    self.autos.append(x)
  
  def visualizar(self):
    for x in self.autos:
      print(x)


# ---------------- Creación de objetos: -------------------

r = Fabrica(10, 'Renault', 5)
print(r)  # Se creo el auto Renault


lista = Listado([r])
lista.visualizar()  # Renault 10 


lista.fabricar(Fabrica(15, 'Audi', 5))  # Se creo el auto Audi
lista.visualizar()  # Audi 15 
