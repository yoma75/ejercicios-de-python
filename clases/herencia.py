# la Super Clase va de la linea 4 a la 16
# la SUBCLASE hereda la super clase, lineas de la 20 a la 24

class Fabrica:
  def __init__(self,marca,nombre,precio,descripcion):
    self.marca = marca
    self.nombre = nombre
    self.precio = precio
    self.descripcion = descripcion
  
  def __str__(self):
    return """
      MARCA:\t\t{}
      NOMBRE:\t\t{}
      PRECIO:\t\t{}
      DESCRIPCION:\t{}""".format(self.marca, self.nombre, self.precio, self.descripcion)
      

# ---------- Subclase, hereda la superclase Fabrica ------------
class Auto(Fabrica):
  pass

z = Auto('Ford', 'Ranger', 100.000, 'camioneta')
print(z)  # MARCA:        Ford
          # NOMBRE:       Ranger
          # PRECIO:       100.0
          # DESCRIPCION:  camioneta


# ---------- Subclase, hereda la superclase Fabrica ------------
class Deportivo(Fabrica):
  ruedas = ''
  distribuidor = ''

  def __str__(self):
      return """
        MARCA:\t\t{}
        NOMBRE:\t\t{}
        PRECIO:\t\t{}
        DESCRIPCION:\t{}
        RUEDAS:\t\t{}
        DISTRIBUIDOR:\t{}""".format(self.marca, self.nombre, self.precio, self.descripcion, self.ruedas, 
                                    self.distribuidor)
      
x = Deportivo('audi', 'essencial', 250.000, 'el mejor')
x.ruedas = 4
x.distribuidor = 'El autico'
print(x)  # MARCA:          audi
          # NOMBRE:         essencial
          # PRECIO:         250.0
          # DESCRIPCION:    el mejor
          # RUEDAS:         4
          # DISTRIBUIDOR:   El autico

