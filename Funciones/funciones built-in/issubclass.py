# issubclass: comprueba si un objeto es una subclase de otro objeto
# issubclass(object, subclass)

# Comprueba si la clase 'Persona' es una subclase de 'miEdad'
class miEdad:
  age = 36

class Persona(miEdad):
  name = "John"
  age = miEdad

x = issubclass(Persona, miEdad)
print(x)  # true
