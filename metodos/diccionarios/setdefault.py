# setdefault: devuelve el valor del elemento con la clave especificada

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model")
print(x)  # Mustang


# Si la clave no existe, inserta la clave, con el valor especificado
car.setdefault("puertas", 5)
print(car)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'puertas': 5}

