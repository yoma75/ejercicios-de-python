# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno


'''Define el nombre de la clase Fabrica con la palabra reservada class, seguida de dos puntos. Dentro de la clase, define el método especial __init__ para asignar valores a los atributos llantas, color y precio cuando se crea un objeto de la clase.'''

class Fabrica:
  def __init__(self, llantas, color, precio):
    self.llantas = llantas
    self.color = color
    self.precio = precio


'''Define el nombre de la clase Moto con la palabra reservada class, seguida del nombre de la clase Fabrica entre paréntesis. Esto indica que la clase Moto hereda de la clase Fabrica. 
Dentro de la clase Moto, define el método especial __init__ para asignar valores a los atributos llantas, color y precio usando el método super() para invocar al método __init__ de la clase Fabrica. También puedes definir otros atributos o métodos específicos para la clase Moto.'''

class Moto(Fabrica):
  def __init__(self, llantas, color, precio):
    super().__init__(llantas, color, precio)
    self.tipo = "Moto"

  def mostrar_tipo(self):
    print(f"\nEste es un transporte tipo {self.tipo}.")


'''Define el nombre de la clase Carro con la palabra reservada class, seguida del nombre de la clase Fabrica entre paréntesis. Esto indica que la clase Carro hereda de la clase Fabrica. Dentro de la clase Carro, define el método especial __init__ para asignar valores a los atributos llantas, color y precio usando el método super() para invocar al método __init__ de la clase Fabrica. También puedes definir otros atributos o métodos específicos para la clase Carro.'''

class Carro(Fabrica):
  def __init__(self, llantas, color ,precio):
    super().__init__(llantas,color ,precio)
    self.tipo = "Carro"

  def mostrar_tipo(self):
    print(f"Este es un transporte tipo {self.tipo}.")


'''Para crear objetos para cada clase y mostrar por pantalla los atributos de cada uno , puedes usar el operador punto (.) después del nombre del objeto'''

m1 = Moto(2,"Rojo",1000)
c1 = Carro(4,"Azul",2000)

print(f"La moto tiene {m1.llantas} llantas.")
print(f"El carro tiene {c1.llantas} llantas.")
print(f"\nLa moto es de color {m1.color}.")
print(f"El carro es de color {c1.color}.")
print(f"\nLa moto cuesta {m1.precio} dólares.")
print(f"El carro cuesta {c1.precio} dólares.")

m1.mostrar_tipo()
c1.mostrar_tipo()
