# getattr: obtiene el valor del atributo especificado

class Person:
  name = "Fredy"
  age = 47
  country = "Colombia"

print(getattr(Person, 'country'))  # Colombia
