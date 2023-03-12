'''* El código define una clase llamada Fabrica que representa una fábrica de autos. 
* La clase tiene un método constructor (init) que recibe tres parámetros: el tiempo de fabricación, el nombre del auto y el número de ruedas. 
* El método constructor asigna estos parámetros a los atributos de la instancia (self) e imprime un mensaje indicando que se creó el auto.
* La clase también tiene un método destructor (del) que se ejecuta cuando se elimina la instancia y que imprime un mensaje indicando que se eliminó el auto. 
* Además, la clase tiene dos métodos especiales (str y len) que definen cómo se representa la instancia como una cadena y cómo se obtiene su longitud. - El método str devuelve una cadena con el nombre, el tiempo y las ruedas del auto, mientras que el método len devuelve el tiempo de fabricación. 
* El código crea una instancia de la clase Fabrica con los valores 10, ‘Mazda’ y 4 para los parámetros del constructor y la asigna a la variable a. 
Luego imprime la representación en cadena de "a" usando la función str() y la longitud de "a" usando la función len().'''


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

print(f'Se creo en {len(a)} meses')  # 10

