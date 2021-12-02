# Crear un programa con tres clases, Universidad con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
# El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

class Universidad:
  def __init__(self, nombreUniv):
    self.nombreUniv = nombreUniv


class Carrera:
  def carrera(self, especialidad):
    self.especialidad = especialidad
  

class Estudiante(Universidad, Carrera):
  def datos(self, nombreEst, edad):
    self.nombreEst = nombreEst
    self.edad = edad

    print(f'\nMi nombre es {self.nombreEst} tengo {self.edad} años, mi especialidad es: {self.especialidad} y estudio en la universidad {self.nombreUniv}\n')
    # Mi nombre es Fredy tengo 46 años, mi especialidad es: Ingenieria de Software y estudio en la universidad El Bosque


persona = Estudiante('El Bosque')
persona.carrera('Ingenieria de Software')
persona.datos('Fredy', 46)

