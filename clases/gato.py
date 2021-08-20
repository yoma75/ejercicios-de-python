class Gato:
  # atributo estático: no necesita un objeto para poderlo obtener, estará presente en todos los objetos que instancie
  especie = 'mamifero'  

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    self.alimentos = []

  def verEtapaDeVida(self):
    if self.edad <= 1:
      print(self.nombre, 'es adulto')
    else:
      print(self.nombre, 'es cachorro')
  
  def esAlimentoFavorito(self, alimento):
    return alimento in self.alimentos


p = Gato('Michin', 1)
p.alimentos = ['leche', 'galletas', 'arroz']
print(p.verEtapaDeVida())  # Michin es adulto
print(p.esAlimentoFavorito('leche'))  # True
print(p.especie)  # mamifero

h = Gato('Pelusa', 2)
h.alimentos = ['pan', 'pescado']
print(h.verEtapaDeVida())  # Pelusa es cachorro
print(h.esAlimentoFavorito('leche'))  # False
print(h.especie)  # mamifero

print(Gato.especie)  # mamifero
