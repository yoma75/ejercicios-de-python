# POLIMORFISMO:

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


class Auto(Fabrica):
  pass


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


class Accesorios(Fabrica):
  autor = ''
  fabricante = ''

  def __str__(self):
      return """
        MARCA:\t\t{}
        NOMBRE ACC:\t{}
        PRECIO:\t\t{}
        DESCRIPCION:\t{}
        AUTOR:\t\t{}
        FABRICANTE:\t{}""".format(self.marca, self.nombre, self.precio, self.descripcion, self.autor, 
                                  self.fabricante)


a = Auto('Ford', 'Ranger', 7000, 'Camioneta')

deportivo = Deportivo('Audi', 'Esencial', 25456000, 'Confort')
deportivo.ruedas = 3
deportivo.distribuidor = 'El autico'

accesorios = Accesorios('Fiat', 'luces de neon', 5000, 'Iluminan mejor')
accesorios.autor = 'Vos'
accesorios.fabricante = 'Yo'

fabrica = [accesorios, deportivo]
fabrica.append(a)


for x in fabrica:
  print(x,'\n')  # MARCA:          Fiat
                 # NOMBRE:         luces de neon
                 # PRECIO:         259740
                 # DESCRIPCION:    Iluminan mejor
                 # AUTOR:          Vos
                 # FABRICANTE:     Yo

                 # MARCA:          Audi
                 # NOMBRE:         Esencial
                 # PRECIO:         25456000
                 # DESCRIPCION:    Confort
                 # RUEDAS:         3
                 # DISTRIBUIDOR:   El autico

                 # MARCA:            Ford
                 # NOMBRE:           Ranger
                 # PRECIO:           65258000
                 # DESCRIPCION:      Camioneta

for x in fabrica:
  print(x.marca, x.precio)  # Fiat 259740
                            # Audi 25456000
                            # Ford 65258000

# Muestra ERROR porque el atributo 'autor' no esta en el objeto Deportivo
# for x in fabrica:
#   print(x.autor)


for x in fabrica:
  if(isinstance(x, Auto)):
    print(x.marca, x.nombre)  # Ford Ranger
  elif(isinstance(x, Deportivo)):
    print(x.marca, x.nombre, x.ruedas)  # Audi Esencial 3
  elif(isinstance(x, Accesorios)):
    print(x.marca, x.nombre, x.fabricante)  # Fiat luces de neon Yo


def Descuento_auto(t, descuento):
  t.precio = t.precio - (t.precio / 100 * descuento)

Descuento_auto(accesorios, 10)
print(accesorios.precio)  # 4500.0


import copy

copia_deportivo = copy.copy(accesorios)
print(copia_deportivo)  # MARCA:          Fiat
                        # NOMBRE ACC:     luces de neon
                        # PRECIO:         4500.0
                        # DESCRIPCION:    Iluminan mejor
                        # AUTOR:          Vos
                        # FABRICANTE:     Yo

descuento = 10

a.precio = a.precio - (a.precio / 100 * descuento)
print(a.precio)  # 6300.0

