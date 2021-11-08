class Profesion:
  def __init__(self, nombre):
    self.nombre = nombre
    self.materias = {}  # diccionario
  
  # Creamos un nuevo método para agregar datos al 'diccionario materias'
  def agregarMateria(self, materia, codigo):
    self.materias[codigo] = materia # [clave] = valor


class Materia:
  def __init__(self, nombre, profesor, fecha):
    self.nombre = nombre
    self.profesor = profesor
    # No puede ser anterior a 2006
    self.fechaInicioDictado = fecha  
  
  # A partir de los atributos se crean propiedades que son las que definen a un objeto:
  @property  # decorator
  def fechaInicioDictado(self):
    print('prueba')
    return self._fechaInicioDictado
  
  # Setter, tiene el mismo nombre del atributo al igual que la property
  @fechaInicioDictado.setter
  def _fechaInicioDictado(self, fecha):
    if fecha < 2006:
      # Si la fecha es menor a 2006 dejar 2006, si es mayor deja la fecha actual
      self._fechaInicioDictado = 2006
    else:
      self._fechaInicioDictado = fecha


# instancia 
ing = Profesion('Ingenieria de Sistemas')
algebra = Materia('Algebra', 'Ricardo Quintero', 2010)
fisica = Materia('Fisica', 'Margarita Gómez', 2006)
quimica = Materia('Quimica', 'Lorena Ríos', 2003)      
print(algebra.profesor)  # Ricardo Quintero
print(algebra.fechaInicioDictado())


# Agregar las materias para la profesion de ingenieria de sistemas dentro de la tupla [Materias] linea 4 se cambia corchetes
# ing.materias.append((134, algebra))
# ing.materias.append((412, fisica))
# print(len(ing.materias))  # 2 elementos


# Agregar las materias y su codigo al 'diccionario materias', método creado linea 7
ing.agregarMateria(algebra, 134)
print(ing.materias)  # {134: <__main__.Materia object at 0x01BA3D48>}

