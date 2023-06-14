# delattr: elimina el atributo o propiedad asignado de una clase

class Person:
  name = "Fredy"
  age = 47
  country = "Colombia"

delattr(Person, 'age')
