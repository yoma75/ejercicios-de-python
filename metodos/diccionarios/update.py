# update: actualiza el diccionario con las llaves y valores dados

numeros1 = {'one':1, 'two':2, 'three':3}
numeros2 = {'ten':10, 'twenty':20, 'thirty':30}

print(numeros1)  # {'one': 1, 'two': 2, 'three': 3}

numeros1.update(numeros2)
print(numeros1)  # {'one': 1, 'two': 2, 'three': 3, 'ten': 10, 'twenty': 20, 'thirty': 30}


# --------------- ejemplo 2 -------------------------
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})
print(car)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}
