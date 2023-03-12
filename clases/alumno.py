# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
  def datosPersonales(self, nombre, nota):  # inicializar sus atributos
    self.nombre = nombre
    self.nota = nota
  
  # imprime los atributos
  def imprimir(self):
    print(f'NOMBRE: {self.nombre}\nNOTA: {self.nota}')
  
  # Mostrar el mensaje con el resultado de la nota
  def resultadoNota(self):
    if self.nota < 5:
      print(f'{self.nombre}, has reprobado\n')
    else:
      print(f'Felicitaciones {self.nombre}, has aprobado\n')


# Esta clase no tiene método __init__ por tal motivo mandamos los datos al método datosPersonales, porque el ejercicio no pide constructor

alumno1 = Alumno()
alumno1.datosPersonales('Carlos', 3)

alumno2 = Alumno()
alumno2.datosPersonales('Maria', 9)


# LLamar a los metodos:
alumno1.imprimir()  # NOMBRE: Carlos
                    # NOTA: 3

alumno1.resultadoNota()  # Has reprobado

alumno2.imprimir()  # NOMBRE: Maria
                    # NOTA: 9

alumno2.resultadoNota()  # Has aprobado
