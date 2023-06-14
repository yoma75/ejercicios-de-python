# setattr: cambia el valor del atributo especificado
# setattr(object, attribute, value)

class Person:
  name = "Fredy"
  age = 47
  country = "Colombia"

print(Person.age)  # 47

setattr(Person, 'age', 56)
print(Person.age)  # 56
