'''keys: genera una lista de las claves del diccionario:'''
# clave:valor
# keys:value

colores = { 
  "amarillo":"yellow", 
  "azul":"blue", 
  "verde":"green" 
}

print(colores.keys())  # dict_keys(['amarillo', 'azul', 'verde'])


for key in colores.keys():
  print(f'{key}: {colores[key]}')

# amarillo: yellow
# azul: blue
# verde: green
