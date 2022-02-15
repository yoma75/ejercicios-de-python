class Nacionalidad:
  def __init__(self, nombre, pais):
    self.nombre = nombre
    self.pais = pais
  
  def presentacion(self, presento):
    return (f'Mi nombre es {presento.nombre} soy de {presento.pais}')


mexico = Nacionalidad('Laura', 'Mexico')
colombia = Nacionalidad('Jose', 'Colombia')

print(mexico.presentacion(mexico))  # Mi nombre es Laura soy de Mexico
print(f'{colombia.presentacion(colombia)}\n')  # Mi nombre es Jose soy de Colombia
