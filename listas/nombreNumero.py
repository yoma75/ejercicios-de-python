from math import floor


p = input('\nDigite su primer nombre: ').lower()
nombre = list(p)
print(nombre)

agregar_numero = list()

# recorrer lista 'nombre' y adicionar numero
for i in nombre:
  if ((i == 'a') or (i == 'j') or (i == 'r')):
    agregar_numero.append(1)
  elif ((i == 'b') or (i == 'k') or (i == 's')):
    agregar_numero.append(2)
  elif ((i == 'c') or (i == 'l') or (i == 't')):
    agregar_numero.append(3)
  elif ((i == 'd') or (i == 'm') or (i == 'u')):
    agregar_numero.append(4)
  elif ((i == 'e') or (i == 'n') or (i == 'v')):
    agregar_numero.append(5)
  elif ((i == 'f') or (i == 'ñ') or (i == 'w')):
    agregar_numero.append(6)
  elif ((i == 'g') or (i == 'o') or (i == 'x')):
    agregar_numero.append(7)
  elif ((i == 'h') or (i == 'p') or (i == 'y')):
    agregar_numero.append(8)
  elif ((i == 'i') or (i == 'q') or (i == 'z')):
    agregar_numero.append(9)

print(agregar_numero)
n = sum(agregar_numero)
print(f'La suma del nombre es: {n}\n')  

# suma = 0
# while n > 0:
#   suma = suma + n % 10
#   n = n / 10

# redondea numero hacia abajo
# print(f'Numero final: {floor(suma)}')
