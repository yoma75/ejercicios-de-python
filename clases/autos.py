class Fabrica:
  def __init__(self, tiempo, nombre, ruedas):  # funcion constructora
    self.tiempo = tiempo
    self.nombre = nombre
    self.ruedas = ruedas
    print('Se creo el auto ', self.nombre)
  
  def __del__(self):
    print('Se elimino el auto', self.nombre)
      

  def __str__(self):
    return "{} se fabrico con exito en {} meses y tiene ruedas {}".format(self.nombre, self.tiempo, self.ruedas)


a = Fabrica(10, 'Mazda', 5)

print(str(a))
