# hasattr: comprueba si en la clase Person contiene la propiedad asignada

class Person:
  name = "Fredy"
  age = 47
  country = "Colombia"

print(hasattr(Person, 'age'))  # True
print(hasattr(Person, 'hobby'))  # False
