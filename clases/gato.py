class Gato:
  # atributo estático: no necesita un objeto para poderlo obtener, estará presente en todos los objetos que instancie
  especie = 'mamifero'  

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    self.alimentos = []

  def verEtapaDeVida(self):
    if self.edad <= 1:
      print(self.nombre, 'es cachorro')
    else:
      print(self.nombre, 'es adulto')
  
  def esAlimentoFavorito(self, alimento):
    return alimento in self.alimentos


p = Gato('Michin', 1)
p.alimentos = ['leche', 'galletas', 'arroz']
print(p.verEtapaDeVida())  # Michin es cachorro
print(p.esAlimentoFavorito('leche'))  # True
print(p.especie)  # mamifero

h = Gato('Pelusa', 2)
h.alimentos = ['pan', 'pescado']
print(h.verEtapaDeVida())  # Pelusa es adulto
print(h.esAlimentoFavorito('leche'))  # False
print(h.especie)  # mamifero

print(Gato.especie)  # mamifero



'''Explicacion con IA Bing: has escrito un código en Python para definir una clase llamada Gato que hereda de la clase Animal. La clase Gato tiene un atributo de clase especie que vale ‘mamifero’ y cuatro atributos de instancia: nombre, edad, alimentos y sonido. También tiene tres métodos: init, verEtapaDeVida y esAlimentoFavorito. El método init asigna los valores de los parámetros nombre y edad a los atributos de instancia correspondientes e inicializa la lista de alimentos vacía. El método verEtapaDeVida imprime si el gato es cachorro o adulto según su edad. El método esAlimentoFavorito devuelve True si el alimento pasado como argumento está en la lista de alimentos del gato y False en caso contrario.

Has creado dos objetos de la clase Gato: p y h. Cada uno tiene su propio nombre, edad y lista de alimentos. Luego has llamado a los métodos verEtapaDeVida y esAlimentoFavorito para cada objeto y has impreso el valor del atributo especie tanto para los objetos como para la clase.'''
