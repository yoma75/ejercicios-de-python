# Crear un programa con tres clases, Universidad con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
# El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

# CREADO CON: Bard Google

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante:
    def __init__(self, nombre, edad, universidad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.universidad = universidad
        self.carrera = carrera

persona = Estudiante("Juan Pérez", 21, "Universidad de Chile", "Ingeniería Civil")

print(f'Estudiante: {persona.nombre}, edad: {persona.edad}, {persona.universidad}, {persona.carrera}')
# Estudiante: Juan Pérez, edad: 21, Universidad de Chile, Ingeniería Civil
