# Crear una Jerarquía de Herencia Básica

# Persona <- Estudiante, quiere decir que estudiante hereda de persona

class Persona:
    def __init__(self, documento, nombre, correo):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo
    
# La clase estudiante hereda de persona
# super() permite invocar un método de una clase padre desde una clase hija.
class Estudiante(Persona):
    def __init__(self, documento, nombre, correo, carnet, carrera):
            super().__init__(documento, nombre, correo)
            self.carnet = carnet
            self.carrera = carrera
    
fredy = Estudiante('43567867', 'Fredy', 'micorreo@yahoo.es', '0345', 'Ingeniero')
print(isinstance(fredy, Estudiante))
print(isinstance(fredy, Persona))

#  isinstance(objeto, nombre de la clase) Devuelve si un objeto es una instancia de una clase o de una subclase de la misma.


