# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
  def datosPersonales(self, nombre, nota):  # inicializar sus atributos
    self.nombre = nombre
    self.nota = nota
  
  def imprimir(self):
    print(f'NOMBRE: {self.nombre}\nNOTA: {self.nota}')
  
  def resultadoNota(self):
    if self.nota < 5:
      print('Has reprobado\n')
    else:
      print('Has aprobado\n')


# Esta clase no tiene metodo __init__ por tal motivo mandamos los datos al metodo datosPersonales, porque el ejercicio no pide constructor

alumno1 = Alumno()
alumno1.datosPersonales('Carlos', 3)

alumno2 = Alumno()
alumno2.datosPersonales('Maria', 9)

alumno1.imprimir()  # NOMBRE: Carlos
                    # NOTA: 3

alumno1.resultadoNota()  # Has reprobado

alumno2.imprimir()  # NOMBRE: Maria
                    # NOTA: 9

alumno2.resultadoNota()  # Has aprobado

