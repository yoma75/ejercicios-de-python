# Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga "Hola...". Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por "Soy un Pulpo". Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mensaje como parametro


class Marino:
  def hablar(self):
    print('Hola...')
  

class Pulpo(Marino):
  def hablar(self):
    print('Soy un pulpo')


class Foca(Marino):
  def hablar(self, mensaje):
    self.mensaje = mensaje
    print(self.mensaje)


marino = Marino()
marino.hablar()  # Hola...

pulpo = Pulpo()
pulpo.hablar()  # Soy un pulpo

foca = Foca()
foca.hablar('Hola, soy la foca')  # Hola, soy la foca


''' Explicacion con IA Bing: esto parece ser un código de Python que muestra el concepto de la herencia y el polimorfismo . La herencia es la capacidad de una clase para heredar los atributos y métodos de otra clase . El polimorfismo es la capacidad de un objeto para cambiar su comportamiento según el contexto o el tipo de clase al que pertenece .

En este caso, la clase Marino es la clase base o padre, y las clases Pulpo y Foca son las clases derivadas o hijas. Estas clases heredan el método hablar() de la clase Marino, pero lo sobrescriben con su propia definición. Esto hace que cada objeto creado a partir de estas clases tenga un comportamiento diferente al llamar al método hablar(). Por ejemplo, el objeto pulpo dice ‘Soy un pulpo’, mientras que el objeto foca dice lo que se le pasa como argumento.'''
