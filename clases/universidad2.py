# Crear un programa con tres clases, Universidad con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
# El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

class Universidad:
  def __init__(self, nombre):
    self.nombre = nombre
        

class Carrera:
  def __init__(self, especialidad):
    self.especialidad = especialidad
        

class Estudiante:
  def __init__(self, nombre, edad, carrera, universidad):
    self.nombre = nombre
    self.edad = edad
    self.carrera = carrera
    self.universidad = universidad


universidad = Universidad("Universidad Nacional")
carrera = Carrera("Ingeniería de Sistemas")
persona = Estudiante("Juan Perez", 20, carrera, universidad)

print("Especialidad: " + persona.carrera.especialidad)  # Especialidad: Ingeniería de Sistemas
print("Edad: " + str(persona.edad))  # Edad: 20
print("Nombre: " + persona.nombre)  # Nombre: Juan Perez
print("Universidad: " + persona.universidad.nombre)  # Universidad: Universidad Nacional


'''Explicación del código:

* Primero se define la clase Universidad con un atributo 'nombre
* Luego se define la clase Carrera con un atributo 'especialidad
* Por último, se define la clase Estudiante con atributos 'nombrecarrera (objeto de la clase Carrera) y 'universidaduniversidad (objeto de la clase Universidad).
* Se crea un objeto 'universidad
* Se crea un objeto 'carrera de la clase Carrera con la especialidad del estudiante.
* Finalmente, se crea un objeto '
* Se imprimen los datos del estudiante con los atributos correspondientes de las clases.'''

