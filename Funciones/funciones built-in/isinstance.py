# isinstance: comprueba si el valor asignado corresponde al tipo de dato

print(isinstance(5, int))  # True
print(isinstance(7.3, int))  # False
print(isinstance(7.3, float))  # True
print(isinstance('Hola', str))  # True
print(isinstance(True, bool))  # True


# Comprueba si 'y' es una instancia de Persona
class Persona:
  name = "John"

y = Persona()
x = isinstance(y, Persona)
print(x)  # True
