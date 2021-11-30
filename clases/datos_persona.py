# Crear una Clase para representar los Datos de una Persona

class Persona:
    def __init__(self, nombre, edad, correo): # Constructor o inicializar clase
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def __str__(self):
        return 'Nombre: {}\nEdad: {}\nCorreo: {}'.format(self.nombre, self.edad, self.correo)

# Crear una instancia
fredy = Persona('Fredy', '33', 'micorreo@gmail.com')
Karol = Persona('Karol', '23', 'karol@yahoo.es')

print(fredy)  # Nombre: Fredy
              # Edad: 33
              # Correo: micorreo@gmail.com

print(f'\n{Karol.nombre}')  # Karol
