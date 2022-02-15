class Fabrica:
  def __init__(self, tiempo, nombre, ruedas):  # funcion constructora
    self.tiempo = tiempo
    self.nombre = nombre
    self.ruedas = ruedas
    print('Se creo el auto ', self.nombre)
  

  def __del__(self):
    print('Se elimino el auto', self.nombre)
      

  # convertir un objeto a una cadena string
  def __str__(self):
    return "{} se fabrico con éxito en {} meses y tiene {} ruedas".format(self.nombre, self.tiempo, self.ruedas)


  def __len__(self):
    return self.tiempo  

a = Fabrica(10, 'Mazda', 4)


print(str(a))  # Mazda se fabrico con exito en 10 meses y tiene 4 ruedas

print(len(a))  # 10
