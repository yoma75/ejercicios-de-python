'''
Digamos que tiene una definición de función que toma un argumento, y ese argumento se multiplicará con un número desconocido:
'''

def myfunc(num):
  return lambda e : e * num

variable = myfunc(2)

print(variable(11))  # 22
print(variable(62))  # 124
print(variable(459))  # 918
