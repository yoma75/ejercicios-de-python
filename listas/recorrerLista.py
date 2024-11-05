# Recorrer los elementos de la lista uno por uno
animals = ['ballena', 'gato', 'caballo']
for x in animals:
  print(x)

print('-------------------------------------------------------')


# Imprima todos los elementos haciendo referencia a su número de índice:
profesiones = ['ingeniero', 'chef', 'medico', 'arquitecto', 'arqueologo']
for x in range(len(profesiones)):
  print(profesiones[x])

print('-------------------------------------------------------')


# Con WHILE
planetas = ['mercurio', 'venus', 'tierra', 'marte', 'jupiter', 'saturno', 'urano', 'neptuno']
i = 0
while i < len(planetas):
  print(planetas[i])
  i += 1

print('-------------------------------------------------------')


# Mediante la COMPRENSION DE LISTAS
alfanum = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
[print(x) for x in alfanum]

